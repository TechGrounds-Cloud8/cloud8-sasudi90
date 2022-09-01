from aws_cdk import (
    CfnOutput,
    Stack,
    aws_ec2 as ec2,
    aws_iam as iam,
    aws_backup as backup,
    aws_autoscaling as autoscaling,
    Duration,
)

from constructs import Construct
from project_v1_1.s3_construct import S3_construct
from project_v1_1.sg_construct import SG_admin_construct
from project_v1_1.sg_construct import SG_web_construct
from project_v1_1.nacl_construct import NACL_construct
from project_v1_1.backup_construct import Backup_construct
from project_v1_1.vpc_construct import web_vpc_construct, admin_vpc_construct
from project_v1_1.webtemplate_construct import webtemplate_construct
from project_v1_1.elb_construct import elb_construct

key_pair_name="project_key_pair"

class ProjectV11Stack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        ############# VPC's #############

        vpc_web=web_vpc_construct(self, "web-vpc")
        vpc_admin=admin_vpc_construct(self, "admin-vpc")

        ###### Webserver Instance #######

        sg_web=SG_web_construct(self,"web-sg",
            vpc=vpc_web.vpc,
            )

        instance_web = ec2.Instance(
            self,
            "web_instance",
            instance_name="webserver",
            instance_type=ec2.InstanceType("t3.nano"),
            machine_image=ec2.MachineImage.latest_amazon_linux(
                generation=ec2.AmazonLinuxGeneration.AMAZON_LINUX_2),
            security_group=sg_web.web_SG,
            key_name=key_pair_name,
            role=iam.Role(
                self, 
                "WebServerRole",
                assumed_by=iam.ServicePrincipal("ec2.amazonaws.com"),
                description="Webserver role",
            ),
            block_devices=[ec2.BlockDevice(
                device_name="/dev/xvda",
                volume=ec2.BlockDeviceVolume.ebs(
                    volume_size=8,
                    encrypted=True,
                    delete_on_termination=True)
            )],
            vpc=vpc_web.vpc,
        )

        ############  Launch Template  ################
        
        web_template=webtemplate_construct(self, "ASG-web-template",
            security_group=sg_web.web_SG,
            key_name=key_pair_name,
        )

        ############### Auto Scaling Group ################

        asg_web=autoscaling.AutoScalingGroup(self, "ASG",
            vpc=vpc_web.vpc,
            launch_template=web_template.template,
            max_capacity=3,
            vpc_subnets=ec2.SubnetSelection(
                subnet_type=ec2.SubnetType.PUBLIC,
            ),
        )

        asg_web.scale_on_cpu_utilization("Scaling due CPU utilization",
            target_utilization_percent=80,
        )
        
        ######### Admin Instance ########

        sg_admin=SG_admin_construct(self, "admin-sg",
            vpc=vpc_admin.vpc,
        )

        instance_admin= ec2.Instance(
            self,
            "admin_instance",
            instance_name="adminserver",
            instance_type=ec2.InstanceType("t2.nano"),
            machine_image=ec2.MachineImage.latest_windows(ec2.WindowsVersion.WINDOWS_SERVER_2019_ENGLISH_FULL_BASE),
            security_group=sg_admin.admin_SG,
            key_name=key_pair_name,
            block_devices=[ec2.BlockDevice(
                device_name="/dev/sda1",
                volume=ec2.BlockDeviceVolume.ebs(
                    volume_size=30,
                    encrypted=True,
                    delete_on_termination=True)
            )],
            vpc=vpc_admin.vpc
        )

        ############### User Data Admin Server #################
        
        instance_admin.user_data.for_windows()
        
        instance_admin.add_user_data(
            "Add-WindowsCapability -Online -Name OpenSSH.Server~~~~0.0.1.0",
            "Start-Service sshd",
            "Set-Service -Name sshd -StartupType 'Automatic'",
            "New-NetFirewallRule -Name sshd -DisplayName 'Allow SSH' -Enabled True -Direction Inbound -Protocol TCP -Action Allow -LocalPort 22",
        )


        ########## VPC Peering ##########

        vPCPeering_connection = ec2.CfnVPCPeeringConnection(
            self, 
            "PeerConnection",
            peer_vpc_id=vpc_admin.vpc.vpc_id,
            vpc_id=vpc_web.vpc.vpc_id,
        )

        for subnet in vpc_web.vpc.public_subnets:
            ec2.CfnRoute(
                self,
                id=f"${subnet.node.id}-PeerRoute",
                route_table_id=subnet.route_table.route_table_id,
                destination_cidr_block="10.20.20.0/26",
                vpc_peering_connection_id=vPCPeering_connection.ref,
            )

        for subnet in vpc_web.vpc.private_subnets:
            ec2.CfnRoute(
                self,
                id=f"${subnet.node.id}-PeerRoute",
                route_table_id=subnet.route_table.route_table_id,
                destination_cidr_block="10.20.20.0/26",
                vpc_peering_connection_id=vPCPeering_connection.ref,
            )

        for subnet in vpc_admin.vpc.public_subnets:
            ec2.CfnRoute(
                self,
                id=f"${subnet.node.id}-PeerRoute", 
                route_table_id=subnet.route_table.route_table_id,
                destination_cidr_block="10.10.10.0/26",
                vpc_peering_connection_id=vPCPeering_connection.ref,
            )

        ########### NACLS ###########

        nacl=NACL_construct(self, "NACLS web and admin",
            vpc_web=vpc_web.vpc,
            vpc_admin=vpc_admin.vpc,
            )

        ########### S3 Bucket ###########

        bucket=S3_construct(self, "PostDeploymentScripts",)

        ########### User Data Web Server ###########

        instance_web_user_data=instance_web.user_data.add_s3_download_command(
            bucket=bucket.pdsbucket, 
            bucket_key="userdataweb.sh",         
        )

        instance_web.user_data.add_execute_file_command(file_path=instance_web_user_data)

        instance_web.user_data.add_s3_download_command(
            bucket=bucket.pdsbucket, 
            bucket_key="webcontent.zip",
            local_file="/tmp/webcontent.zip",         
        )

        instance_web.user_data.add_commands("chmod 775 -R /var/www/html/")
        instance_web.user_data.add_commands("unzip /tmp/webcontent.zip -d /var/www/html/")
        
        bucket.pdsbucket.grant_read(instance_web)

        ################# User Data Web-Template ###############

        asg_web_user_data=asg_web.user_data.add_s3_download_command(
            bucket=bucket.pdsbucket,
            bucket_key="userdataweb.sh",
        )

        asg_web.user_data.add_execute_file_command(file_path=asg_web_user_data)

        asg_web.user_data.add_s3_download_command(
            bucket=bucket.pdsbucket, 
            bucket_key="webcontent.zip",
            local_file="/tmp/webcontent.zip",         
        )

        asg_web.user_data.add_commands("sudo chmod 775 -R /var/www/html/")
        asg_web.user_data.add_commands("unzip /tmp/webcontent.zip -d /var/www/html/")

        bucket.pdsbucket.grant_read(asg_web)
        
        # ############# Backup #################

        daily_backup_dps=Backup_construct(self, "backup_plan",)

        daily_backup_dps.backup_plan.add_selection(
            id="backup_web_selection",
            backup_selection_name="backup_web_selection",
            resources=[
                backup.BackupResource.from_ec2_instance(instance_web)
            ]
        )

        alb=elb_construct(
            self, "web_server_alb",
            vpc=vpc_web.vpc,
            asg=asg_web,
        )

        asg_web.scale_on_request_count("Target on request number",
            target_requests_per_minute=256)

        CfnOutput(self, "albDNS",
            value= alb.alb.load_balancer_dns_name)

    
        

