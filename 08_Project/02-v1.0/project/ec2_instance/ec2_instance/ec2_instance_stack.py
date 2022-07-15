import aws_cdk
from constructs import Construct
from aws_cdk import (
    CfnOutput,
    Stack,
    aws_ec2 as ec2,
    aws_s3 as s3,
    aws_s3_deployment as s3deploy,
    aws_s3_assets as Asset
)

"""with open("./postdeploymentscripts/user_data_web.sh", encoding="utf-8") as f:
    user_data = f.read()"""

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

        # APP_PROD_SG: add a new ingress rules to allow port 80 and 443
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

        #################################
        ###### Webserver Instance #######
        #################################

        instance_web = ec2.Instance(
            self,
            "web instance_web",
            instance_name="webserver",
            instance_type=ec2.InstanceType("t3a.nano"),
            machine_image=ec2.MachineImage().lookup(name="amzn2-ami-kernel-5.10-hvm-2.0.20220606.1-x86_64-gp2"),
            security_group=app_prod_SG,
            key_name="project_key_pair",
            #user_data=ec2.UserData.custom(user_data),
            vpc=vpc_web
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
            peer=ec2.Peer.any_ipv4(),
            description="Allow SSH", 
            connection=ec2.Port.tcp(22)
        )
        #################################
        ####### Admin Instance #######
        #################################

        instance_mngmt= ec2.Instance(
            self,
            "admin instance",
            instance_name="adminserver",
            instance_type=ec2.InstanceType("t3a.nano"),
            machine_image=ec2.MachineImage().lookup(name="amzn2-ami-kernel-5.10-hvm-2.0.20220606.1-x86_64-gp2"),
            security_group=admin_SG,
            key_name="project_key_pair",
            vpc=vpc_admin
        )

        #################################
        ######## NACL Webserver #########
        #################################

        # network_acl_admin = ec2.NetworkAcl(
        #     self,
        #     "Admin_NACL",
        #     vpc=vpc_web,
        #     subnet_selection=ec2.SubnetSelection(
        #         subnet_type=ec2.SubnetType.PUBLIC
        #     )
        # )      

        # network_acl_admin.add_entry(
        #     id="Inbound: SSH from anywhere",
        #     cidr=ec2.AclCidr.any_ipv4(),
        #     rule_number=100,
        #     traffic=ec2.AclTraffic.tcp_port(22),
        #     direction=ec2.TrafficDirection.INGRESS,
        #     rule_action=ec2.Action.ALLOW
        # )

        # network_acl_admin.add_entry(
        #     "Inbound: Ephemeral ports from anywhere",
        #     cidr=ec2.AclCidr.any_ipv4(),
        #     rule_number=140,
        #     traffic=ec2.AclTraffic.tcp_port_range(1024, 65535),
        #     direction=ec2.TrafficDirection.INGRESS,
        #     rule_action=ec2.Action.ALLOW
        # )

        # network_acl_admin.add_entry(
        #     "Outbound: Ephemeral ports to anywhere",
        #     cidr=ec2.AclCidr.any_ipv4(),
        #     rule_number=140,
        #     traffic=ec2.AclTraffic.tcp_port_range(1024, 65535),
        #     direction=ec2.TrafficDirection.EGRESS,
        #     rule_action=ec2.Action.ALLOW
        # )

        #################################
        ########## VPC Peering ##########
        #################################

        vPCPeering_connection = ec2.CfnVPCPeeringConnection(
            self, 
            "PeerConnection",
            peer_vpc_id=vpc_admin.vpc_id,
            vpc_id=vpc_web.vpc_id,
        )
        
        # for subnet in vpc_web.public_subnets:
        #     ec2.CfnRoute(
        #         self,
        #         id=f"{subnet.subnet_id}", 
        #         route_table_id=subnet.route_table.route_table_id,
        #         destination_cidr_block="10.20.20.0/24",
        #         vpc_peering_connection_id=vPCPeering_connection.ref,
        #         )

        # for subnet in vpc_admin.public_subnets:
        #     ec2.CfnRoute(
        #         self,
        #         id=f"{subnet.subnet_id}",
        #         route_table_id=subnet.route_table.route_table_id,
        #         destination_cidr_block="10.10.10.0/24",
        #         vpc_peering_connection_id=vPCPeering_connection.ref,
        #         )

        #################################
        ########### S3 Bucket ###########
        #################################

        bucket = s3.Bucket(
            self, 
            "postdeploybucketau",
            bucket_name="postdeploybucketau",
            removal_policy=aws_cdk.RemovalPolicy.DESTROY,
            encryption=s3.BucketEncryption.S3_MANAGED,
            auto_delete_objects=True,
            public_read_access=False,
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