from re import sub
import aws_cdk
from constructs import Construct
from aws_cdk import (
    CfnOutput,
    Duration,
    RemovalPolicy,
    Stack,
    aws_ec2 as ec2,
    aws_s3 as s3,
    aws_s3_deployment as s3deploy,
    aws_s3_assets as Asset,
    aws_iam as iam,
    aws_backup as backup,
    aws_events as event,
)

my_ip="24.132.91.9/32"


class Ec2InstanceStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        #################################
        ############# VPC's #############
        #################################

        vpc_web = ec2.Vpc(self, "Application Production Server",
        cidr="10.10.10.0/24",
        max_azs=2,
        nat_gateways=0,
        subnet_configuration = [
            ec2.SubnetConfiguration(
                name="app-prd-vpc",
                subnet_type=ec2.SubnetType.PUBLIC,
                cidr_mask=26
            )]
        )
        
        vpc_admin = ec2.Vpc(self, "Management Production Server",
        cidr="10.20.20.0/24",
        max_azs=2,
        nat_gateways=0,
        subnet_configuration = [
            ec2.SubnetConfiguration(
                name="management-prd-vpc",
                subnet_type=ec2.SubnetType.PUBLIC,
                cidr_mask=26
            )]
        )

        #################################
        ######### SG Webserver #########
        #################################

        app_prod_SG = ec2.SecurityGroup(
            self,
            "SG_allow_HTTP_HTTPS_SSH",
            vpc=vpc_web,
            allow_all_outbound=True,
        )

        #APP_PROD_SG: add a new ingress rules to allow port 80 and 443
        app_prod_SG.add_ingress_rule(
            peer=ec2.Peer.any_ipv4(),
            description="Allow HTTP", 
            connection=ec2.Port.tcp(80)
        )

        app_prod_SG.add_ingress_rule(
            peer=ec2.Peer.any_ipv4(),
            description="Allow HTTPS", 
            connection=ec2.Port.tcp(443)
        )

        app_prod_SG.add_ingress_rule(
            peer=ec2.Peer.any_ipv4(),
            description="Allow SSH", 
            connection=ec2.Port.tcp(22)
        )

        app_prod_SG.add_ingress_rule(
            peer=ec2.Peer.any_ipv4(),
            description="Allow RDP", 
            connection=ec2.Port.tcp(3389)
        )


        #################################
        ###### Webserver Instance #######
        #################################

        instance_web = ec2.Instance(
            self,
            "web instance_web",
            instance_name="webserver",
            instance_type=ec2.InstanceType("t3.nano"),
            machine_image=ec2.MachineImage.latest_amazon_linux(
                generation=ec2.AmazonLinuxGeneration.AMAZON_LINUX_2),
            security_group=app_prod_SG,
            key_name="project_key_pair",
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
            vpc=vpc_web,
        )

        #################################
        ######## NACL Webserver #########
        #################################

        web_nacl = ec2.NetworkAcl(
            self,
            "Web_NACL",
            vpc=vpc_web,
            subnet_selection=ec2.SubnetSelection(
                subnet_type=ec2.SubnetType.PUBLIC
            )
        )      

        web_nacl.add_entry(
            id="Inbound: HTTP from anywhere",
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number=100,
            traffic=ec2.AclTraffic.tcp_port(80),
            direction=ec2.TrafficDirection.INGRESS,
            rule_action=ec2.Action.ALLOW
        )

        web_nacl.add_entry(
            "Outbound: HTTP to anywhere",
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number=100,
            traffic=ec2.AclTraffic.tcp_port(80),
            direction=ec2.TrafficDirection.EGRESS,
            rule_action=ec2.Action.ALLOW
        )

        web_nacl.add_entry(
            "Inbound: HTTPS from anywhere",
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number=110,
            traffic=ec2.AclTraffic.tcp_port(443),
            direction=ec2.TrafficDirection.INGRESS,
            rule_action=ec2.Action.ALLOW
        )

        web_nacl.add_entry(
            "Outbound: HTTPS to anywhere",
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number=110,
            traffic=ec2.AclTraffic.tcp_port(443),
            direction=ec2.TrafficDirection.EGRESS,
            rule_action=ec2.Action.ALLOW
        )

        web_nacl.add_entry(
            "Inbound: Ephemeral ports from anywhere",
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number=140,
            traffic=ec2.AclTraffic.tcp_port_range(1024, 65535),
            direction=ec2.TrafficDirection.INGRESS,
            rule_action=ec2.Action.ALLOW
        )

        web_nacl.add_entry(
            "Outbound: Ephemeral ports to anywhere",
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number=140,
            traffic=ec2.AclTraffic.tcp_port_range(1024, 65535),
            direction=ec2.TrafficDirection.EGRESS,
            rule_action=ec2.Action.ALLOW
        )

        web_nacl.add_entry(
            id="Inbound: SSH from anywhere",
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number=150,
            traffic=ec2.AclTraffic.tcp_port(22),
            direction=ec2.TrafficDirection.INGRESS,
            rule_action=ec2.Action.ALLOW
        )

        web_nacl.add_entry(
            id="Outbound: SSH to anywhere",
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number=150,
            traffic=ec2.AclTraffic.tcp_port(22),
            direction=ec2.TrafficDirection.EGRESS,
            rule_action=ec2.Action.ALLOW
        )
        
        web_nacl.add_entry(
            id="Inbound: RDP from anywhere",
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number=160,
            traffic=ec2.AclTraffic.tcp_port(3389),
            direction=ec2.TrafficDirection.INGRESS,
            rule_action=ec2.Action.ALLOW
        )

        #################################
        ######### SG MNMGTserver #########
        #################################

        admin_SG = ec2.SecurityGroup(
            self,
            "SG_allow_SSH",
            vpc=vpc_admin,
            allow_all_outbound=True,
        )

        admin_SG.add_ingress_rule(
            peer=ec2.Peer.ipv4(my_ip),
            description="Allow SSH", 
            connection=ec2.Port.tcp(22)
        )

        admin_SG.add_ingress_rule(
            peer=ec2.Peer.ipv4(my_ip),
            description="Allow RDP",
            connection=ec2.Port.tcp(3389)
        )

        admin_SG.add_ingress_rule(
            peer=ec2.Peer.any_ipv4(),
            description="Allow HTTP", 
            connection=ec2.Port.tcp(80)
        )

        admin_SG.add_ingress_rule(
            peer=ec2.Peer.any_ipv4(),
            description="Allow HTTPS", 
            connection=ec2.Port.tcp(443)
        )

        #################################
        ####### Admin Instance #######
        #################################

        instance_admin= ec2.Instance(
            self,
            "admin instance",
            instance_name="adminserver",
            instance_type=ec2.InstanceType("t2.nano"),
            machine_image=ec2.MachineImage.latest_windows(ec2.WindowsVersion.WINDOWS_SERVER_2019_ENGLISH_FULL_BASE),
            security_group=admin_SG,
            key_name="project_key_pair",
            block_devices=[ec2.BlockDevice(
                device_name="/dev/sda1",
                volume=ec2.BlockDeviceVolume.ebs(
                    volume_size=30,
                    encrypted=True,
                    delete_on_termination=True)
            )],
            vpc=vpc_admin
        )

        #################################
        ######## NACL Adminserver #######
        #################################

        admin_nacl=ec2.NetworkAcl(
            self,
            "Admin_NACL",
            vpc=vpc_admin,
            subnet_selection=ec2.SubnetSelection(
                subnet_type=ec2.SubnetType.PUBLIC
            )
        )      

        admin_nacl.add_entry(
            id="Inbound: SSH from my IP",
            cidr=ec2.AclCidr.ipv4(my_ip),
            rule_number=200,
            traffic=ec2.AclTraffic.tcp_port(22),
            direction=ec2.TrafficDirection.INGRESS,
            rule_action=ec2.Action.ALLOW
        )

        admin_nacl.add_entry(
            id="Outbound: SSH to anywhere",
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number=200,
            traffic=ec2.AclTraffic.tcp_port(22),
            direction=ec2.TrafficDirection.EGRESS,
            rule_action=ec2.Action.ALLOW
        )

        admin_nacl.add_entry(
            "Inbound: Ephemeral ports from anywhere",
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number=210,
            traffic=ec2.AclTraffic.tcp_port_range(1024, 65535),
            direction=ec2.TrafficDirection.INGRESS,
            rule_action=ec2.Action.ALLOW
        )

        admin_nacl.add_entry(
            "Outbound: Ephemeral ports to anywhere",
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number=210,
            traffic=ec2.AclTraffic.tcp_port_range(1024, 65535),
            direction=ec2.TrafficDirection.EGRESS,
            rule_action=ec2.Action.ALLOW
        )

        admin_nacl.add_entry(
            "Inbound: RDP from anywhere",
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number=230,
            traffic=ec2.AclTraffic.tcp_port(3389),
            direction=ec2.TrafficDirection.INGRESS,
            rule_action=ec2.Action.ALLOW
        )

        admin_nacl.add_entry(
            "Outbound: RDP to anywhere",
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number=230,
            traffic=ec2.AclTraffic.tcp_port(3389),
            direction=ec2.TrafficDirection.EGRESS,
            rule_action=ec2.Action.ALLOW
        )

        admin_nacl.add_entry(
            "Inbound: HTTP from anywhere",
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number=250,
            traffic=ec2.AclTraffic.tcp_port(80),
            direction=ec2.TrafficDirection.INGRESS,
            rule_action=ec2.Action.ALLOW
        )

        admin_nacl.add_entry(
            "Outbound: HTTP to anywhere",
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number=250,
            traffic=ec2.AclTraffic.tcp_port(80),
            direction=ec2.TrafficDirection.EGRESS,
            rule_action=ec2.Action.ALLOW
        )

        admin_nacl.add_entry(
            "Inbound: HTTPS from anywhere",
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number=270,
            traffic=ec2.AclTraffic.tcp_port(443),
            direction=ec2.TrafficDirection.INGRESS,
            rule_action=ec2.Action.ALLOW
        )

        admin_nacl.add_entry(
            "Outbound: HTTPS to anywhere",
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number=270,
            traffic=ec2.AclTraffic.tcp_port(443),
            direction=ec2.TrafficDirection.EGRESS,
            rule_action=ec2.Action.ALLOW
        )


        #################################
        ########## VPC Peering ##########
        #################################

        vPCPeering_connection = ec2.CfnVPCPeeringConnection(
            self, 
            "PeerConnection",
            peer_vpc_id=vpc_admin.vpc_id,
            vpc_id=vpc_web.vpc_id,
        )

        for subnet in vpc_web.public_subnets:
            ec2.CfnRoute(
                self,
                id=f"${subnet.node.id}-PeerRoute",
                route_table_id=subnet.route_table.route_table_id,
                destination_cidr_block="10.20.20.0/24",
                vpc_peering_connection_id=vPCPeering_connection.ref,
            )

        for subnet in vpc_admin.public_subnets:
            ec2.CfnRoute(
                self,
                id=f"${subnet.node.id}-PeerRoute", 
                route_table_id=subnet.route_table.route_table_id,
                destination_cidr_block="10.10.10.0/24",
                vpc_peering_connection_id=vPCPeering_connection.ref,
            )

        #################################
        ########### S3 Bucket ###########
        #################################

        bucket = s3.Bucket(
            self, 
            "postdeploybucketau",
            bucket_name="postdeploybucketau",
            removal_policy=aws_cdk.RemovalPolicy.DESTROY,
            encryption=s3.BucketEncryption.S3_MANAGED,
            enforce_ssl=True,
            auto_delete_objects=True,
        )

        #put the scripts in dir postdeploymentscripts into s3 bucket
        postdeploytest = s3deploy.BucketDeployment(
            self,
            "postdeploytest",
            sources=[s3deploy.Source.asset('./postdeploymentscripts')],
            destination_bucket=bucket,
        )
        
        instance_web_user_data=instance_web.user_data.add_s3_download_command(
            bucket=bucket, 
            bucket_key="user_data_web.sh",         
        )

        instance_web.user_data.add_execute_file_command(file_path=instance_web_user_data)

        instance_web.user_data.add_s3_download_command(
            bucket=bucket, 
            bucket_key="demo.zip",
            local_file="/tmp/demo.zip",         
        )

        #-R recursive, give 775 permission to everything under var dir
        instance_web.user_data.add_commands("chmod 775 -R /var/www/html/")
        #destination
        instance_web.user_data.add_commands("unzip /tmp/demo.zip -d /var/www/html/")

        bucket.grant_read(instance_web)

        #################################
        ########### AWS Backup ##########
        #################################

        #nodig -> vault, plan , rule, selection

        back_up_vault = backup.BackupVault(
            self, "backup_vault",
            backup_vault_name="backup_vault",
            removal_policy=aws_cdk.RemovalPolicy.DESTROY
        )

        backup_plan=backup.BackupPlan(
            self, 
            "backup_webserver",
            backup_plan_name="backup_webserver",
            backup_vault=back_up_vault,        
        )

        #werkt niet, zoek uit waar je recovery points kunt deleten
        backup_plan.apply_removal_policy(RemovalPolicy.DESTROY)

        backup_plan.add_rule(
            rule=backup.BackupPlanRule(
                rule_name="daily_backup_webserver",
                delete_after=Duration.days(7),
                enable_continuous_backup=True,
                schedule_expression=event.Schedule.cron(
                    minute="0",
                    hour="11",
                )
            )
        )

        backup_plan.add_selection(
            id="backup_web_selection",
            backup_selection_name="backup_web_selection",
            resources=[
                backup.BackupResource.from_ec2_instance(instance_web)
            ]
        )