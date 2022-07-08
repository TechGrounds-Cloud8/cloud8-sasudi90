from aws_cdk import (
    # Duration,
    Stack,
    aws_ec2 as ec2,
)
from constructs import Construct


instanceName1="webserver"
instanceName2="managementserver"
instanceType= "t2.micro"
amiName="amzn2-ami-hvm-2.0.20200520.1-x86_64-gp2"

class Ec2InstanceStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here
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

        # create a new security group
        app_prod_SG = ec2.SecurityGroup(
            self,
            "sec-group-allow-ssh",
            vpc=vpc1,
            allow_all_outbound=True,
        )

        # add a new ingress rule to allow port 22 to internal hosts
        app_prod_SG.add_ingress_rule(
            peer=ec2.Peer.ipv4('10.10.10.0/24'),
            description="Allow SSH connection", 
            connection=ec2.Port.tcp(22)
        )

        instance_web = ec2.Instance(
            self,
            "web instance",
            instance_name=instanceName1,
            instance_type=ec2.InstanceType(instanceType),
            machine_image=ec2.MachineImage().lookup(name=amiName),
            security_group=app_prod_SG,
            vpc=vpc1
        )
        
        instance_mngmt= ec2.Instance(
            self,
            "mngmnt instance",
            instance_name=instanceName2,
            instance_type=ec2.InstanceType(instanceType),
            machine_image=ec2.MachineImage().lookup(name=amiName),
            vpc=vpc2
        )

        cfn_vPCPeering_connection = ec2.CfnVPCPeeringConnection(self, "PeerConnection",
        peer_vpc_id="vpc2",
        vpc_id="vpc1",
        )
