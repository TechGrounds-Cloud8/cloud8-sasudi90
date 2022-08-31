from aws_cdk import(
    aws_ec2 as ec2,
)

from constructs import Construct

class web_vpc_construct(Construct):

    def __init__(self, scope: Construct, id: str, **kwargs):
        super().__init__(scope, id)

        self.vpc= ec2.Vpc(self, "Web Server",
        cidr="10.10.10.0/24",
        max_azs=3,
        nat_gateways=0,
        subnet_configuration=[
            ec2.SubnetConfiguration(
                name="web-public-subnet",
                subnet_type=ec2.SubnetType.PUBLIC,
                cidr_mask=26,
            ),
            ec2.SubnetConfiguration(
                name="web-private-subnet",
                subnet_type=ec2.SubnetType.PRIVATE_ISOLATED,
                cidr_mask=26,
            ),],
        )

class admin_vpc_construct(Construct):        
    
    def __init__(self, scope: Construct, id: str, **kwargs):
        super().__init__(scope, id)

        self.vpc= ec2.Vpc(self, "Admin Server",
        cidr="10.20.20.0/24",
        max_azs=1,
        nat_gateways=0,
        subnet_configuration = [
            ec2.SubnetConfiguration(
                name="admin-vpc",
                subnet_type=ec2.SubnetType.PUBLIC,
                cidr_mask=26
            )]
        )

