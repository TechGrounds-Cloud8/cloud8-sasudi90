from aws_cdk import (
    Stack,
    aws_ec2 as ec2,
    aws_iam as iam,
    aws_backup as backup,
)

from constructs import Construct
from project_v1_1.s3_construct import S3_construct
from project_v1_1.sg_construct import SG_admin_construct
from project_v1_1.sg_construct import SG_web_construct
from project_v1_1.nacl_construct import NACL_construct
from project_v1_1.backup_construct import Backup_construct
from project_v1_1.vpc_construct import web_vpc_construct, admin_vpc_construct

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

        ######### Admin Instance ########

        sg_admin=SG_admin_construct(self, "admin-sg",
            vpc=vpc_admin.vpc,
        )

        instance_admin= ec2.Instance(
            self,
            "admin instance",
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
                destination_cidr_block="10.20.20.0/24",
                vpc_peering_connection_id=vPCPeering_connection.ref,
            )

        for subnet in vpc_admin.vpc.public_subnets:
            ec2.CfnRoute(
                self,
                id=f"${subnet.node.id}-PeerRoute", 
                route_table_id=subnet.route_table.route_table_id,
                destination_cidr_block="10.10.10.0/24",
                vpc_peering_connection_id=vPCPeering_connection.ref,
            )

        ########### NACLS ###########


        nacl=NACL_construct(self, "NACLS web and admin",
            vpc_web=vpc_web.vpc,
            vpc_admin=vpc_admin.vpc,
            )


        ########### S3 Bucket ###########

        bucket=S3_construct(self, "PostDeploymentScripts", 
        )

        instance_web_user_data=instance_web.user_data.add_s3_download_command(
            bucket=bucket.pdsbucket, 
            bucket_key="user_data_web.sh",         
        )

        instance_web.user_data.add_execute_file_command(file_path=instance_web_user_data)

        instance_web.user_data.add_s3_download_command(
            bucket=bucket.pdsbucket, 
            bucket_key="web_content.zip",
            local_file="/tmp/web_content.zip",         
        )

        instance_web.user_data.add_commands("chmod 775 -R /var/www/html/")
        instance_web.user_data.add_commands("unzip /tmp/web_content.zip -d /var/www/html/")

        bucket.pdsbucket.grant_read(instance_web)

        ############# Backup #################

        daily_backup_dps=Backup_construct(self, "backup_plan",)

        daily_backup_dps.backup_plan.add_selection(
            id="backup_web_selection",
            backup_selection_name="backup_web_selection",
            resources=[
                backup.BackupResource.from_ec2_instance(instance_web)
            ]
        )

