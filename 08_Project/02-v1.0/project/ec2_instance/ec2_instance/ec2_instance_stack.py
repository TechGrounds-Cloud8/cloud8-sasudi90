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


instanceName1="webserver"
instanceName2="managementserver"
instanceType= "t2.micro"
amiName="amzn2-ami-hvm-2.0.20200520.1-x86_64-gp2"

with open("./postdeploymentscripts/user_data_web.sh", encoding="utf-8") as f:
    user_data = f.read()

class Ec2InstanceStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        #################################
        ############# VPC's #############
        #################################

        vpc1 = ec2.Vpc(self, "Application Production Server",
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
        
        vpc2 = ec2.Vpc(self, "Management Production Server",
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
        ######### SG wWebserver #########
        #################################

        app_prod_SG = ec2.SecurityGroup(
            self,
            "SG_allow_HTTP_HTTPS",
            vpc=vpc1,
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

        #################################
        ###### Webserver Instance #######
        #################################

        instance_web = ec2.Instance(
            self,
            "web instance_web",
            instance_name=instanceName1,
            instance_type=ec2.InstanceType(instanceType),
            machine_image=ec2.MachineImage().lookup(name=amiName),
            security_group=app_prod_SG,
            user_data=ec2.UserData.custom(user_data),
            vpc=vpc1
        )
        
        #################################
        ######## NACL Webserver #########
        #################################

        network_acl = ec2.NetworkAcl(
            self,
            "Web_NACL",
            vpc=vpc1,
            subnet_selection=ec2.SubnetSelection(
                subnet_type=ec2.SubnetType.PUBLIC
            )
        )      

        network_acl.add_entry(
            id="Inbound: HTTP from anywhere",
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number=100,
            traffic=ec2.AclTraffic.tcp_port(80),
            direction=ec2.TrafficDirection.INGRESS,
            rule_action=ec2.Action.ALLOW
        )

        network_acl.add_entry(
            "Outbound: HTTP to anywhere",
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number=100,
            traffic=ec2.AclTraffic.tcp_port(80),
            direction=ec2.TrafficDirection.EGRESS,
            rule_action=ec2.Action.ALLOW
        )

        network_acl.add_entry(
            "Inbound: HTTPS from anywhere",
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number=110,
            traffic=ec2.AclTraffic.tcp_port(443),
            direction=ec2.TrafficDirection.INGRESS,
            rule_action=ec2.Action.ALLOW
        )

        network_acl.add_entry(
            "Outbound: HTTPS to anywhere",
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number=110,
            traffic=ec2.AclTraffic.tcp_port(443),
            direction=ec2.TrafficDirection.EGRESS,
            rule_action=ec2.Action.ALLOW
        )

        network_acl.add_entry(
            "Inbound: Ephemeral ports",
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number=140,
            traffic=ec2.AclTraffic.tcp_port_range(1024, 65535),
            direction=ec2.TrafficDirection.INGRESS,
            rule_action=ec2.Action.ALLOW
        )

        network_acl.add_entry(
            "Outbound: Ephemeral ports to anywhere",
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number=140,
            traffic=ec2.AclTraffic.tcp_port_range(1024, 65535),
            direction=ec2.TrafficDirection.EGRESS,
            rule_action=ec2.Action.ALLOW
        )

        #################################
        ####### Management server #######
        #################################

        instance_mngmt= ec2.Instance(
            self,
            "mngmnt instance_web",
            instance_name=instanceName2,
            instance_type=ec2.InstanceType(instanceType),
            machine_image=ec2.MachineImage().lookup(name=amiName),
            vpc=vpc2
        )

        #################################
        ########## VPC Peering ##########
        #################################

        #create vpc peering
        cfn_vPCPeering_connection = ec2.CfnVPCPeeringConnection(
            self, 
            "PeerConnection",
            peer_vpc_id=vpc2.vpc_id,
            vpc_id=vpc1.vpc_id,
        )

        #################################
        ########### S3 Bucket ###########
        #################################

        bucket = s3.Bucket(
            self, 
            "postdeploybucketau",
            bucket_name="postdeploybucketau",
            removal_policy=aws_cdk.RemovalPolicy.DESTROY,
            auto_delete_objects=True,
        )

        #put the scripts in dir postdeploymentscripts into s3 bucket
        s3deploy.BucketDeployment(
            self,
            "postdeploytest",
            sources=[s3deploy.Source.asset('./postdeploymentscripts')],
            destination_bucket=bucket,
        )
        
        """instance_web_user_data=ec2.UserData.add_s3_download_command(
            self,
            bucket="postdeploybucketau", 
            bucket_key="user_data_web.sh",         
        )

        user_data=instance_web.user_data.add_execute_file_command(file=instance_web_user_data)"""