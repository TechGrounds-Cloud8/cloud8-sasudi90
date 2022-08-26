
from aws_cdk import (
    aws_ec2 as ec2,
)

from constructs import Construct

my_ip="24.132.91.9/32"

class SG_admin_construct(Construct):

    def __init__(self, scope: Construct, id: str, vpc, **kwargs):
        super().__init__(scope, id, **kwargs)

        #################################
        ######### SG MNMGTserver ########
        #################################

        self.admin_SG = ec2.SecurityGroup(
            self,
            "Admin_SG",
            vpc=vpc,
            allow_all_outbound=True,
        )

        self.admin_SG.add_ingress_rule(
            peer=ec2.Peer.ipv4(my_ip),
            description="Allow SSH", 
            connection=ec2.Port.tcp(22)
        )

        self.admin_SG.add_ingress_rule(
            peer=ec2.Peer.ipv4(my_ip),
            description="Allow RDP",
            connection=ec2.Port.tcp(3389)
        )

        self.admin_SG.add_ingress_rule(
            peer=ec2.Peer.any_ipv4(),
            description="Allow HTTP", 
            connection=ec2.Port.tcp(80)
        )

        self.admin_SG.add_ingress_rule(
            peer=ec2.Peer.any_ipv4(),
            description="Allow HTTPS", 
            connection=ec2.Port.tcp(443)
        )

class SG_web_construct(Construct):
        
    def __init__(self, scope: Construct, id: str, vpc, **kwargs):
        super().__init__(scope, id, **kwargs)

        self.web_SG = ec2.SecurityGroup(
            self,
            "WEB_SG",
            vpc=vpc,
            allow_all_outbound=True,
        )

        self.web_SG.connections.allow_from(ec2.Peer.ipv4("10.20.20.0/24"), ec2.Port.tcp(22))