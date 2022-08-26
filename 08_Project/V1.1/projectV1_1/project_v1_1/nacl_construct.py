from aws_cdk import(
    aws_ec2 as ec2,
)

from constructs import Construct

my_ip="24.132.91.9/32"

class NACL_construct(Construct):

    def __init__(self, scope: Construct, id: str, vpc_web, vpc_admin, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        #################################
        ##### NACL Webserver Public #####
        #################################

        self.web_nacl_public = ec2.NetworkAcl(
            self,
            "Web_NACL_PUBLIC",
            vpc=vpc_web,
            subnet_selection=ec2.SubnetSelection(
                subnet_type=ec2.SubnetType.PUBLIC
            )
        )      

        self.web_nacl_public.add_entry(
            id="Inbound: HTTP from anywhere",
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number=100,
            traffic=ec2.AclTraffic.tcp_port(80),
            direction=ec2.TrafficDirection.INGRESS,
            rule_action=ec2.Action.ALLOW
        )

        self.web_nacl_public.add_entry(
            "Outbound: HTTP to anywhere",
            cidr=ec2.AclCidr.ipv4(vpc_web.vpc_cidr_block),
            rule_number=100,
            traffic=ec2.AclTraffic.tcp_port(80),
            direction=ec2.TrafficDirection.EGRESS,
            rule_action=ec2.Action.ALLOW
        )

        self.web_nacl_public.add_entry(
            "Inbound: HTTPS from anywhere",
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number=120,
            traffic=ec2.AclTraffic.tcp_port(443),
            direction=ec2.TrafficDirection.INGRESS,
            rule_action=ec2.Action.ALLOW
        )

        self.web_nacl_public.add_entry(
            "Outbound: HTTPS to anywhere",
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number=120,
            traffic=ec2.AclTraffic.tcp_port(443),
            direction=ec2.TrafficDirection.EGRESS,
            rule_action=ec2.Action.ALLOW
        )

        self.web_nacl_public.add_entry(
            "Inbound: Ephemeral ports from anywhere",
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number=140,
            traffic=ec2.AclTraffic.tcp_port_range(1024, 65535),
            direction=ec2.TrafficDirection.INGRESS,
            rule_action=ec2.Action.ALLOW
        )

        self.web_nacl_public.add_entry(
            "Outbound: Ephemeral ports to anywhere",
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number=140,
            traffic=ec2.AclTraffic.tcp_port_range(1024, 65535),
            direction=ec2.TrafficDirection.EGRESS,
            rule_action=ec2.Action.ALLOW
        )

        self.web_nacl_public.add_entry(
            id="Inbound: SSH from anywhere",
            cidr=ec2.AclCidr.ipv4(vpc_web.vpc_cidr_block),
            rule_number=160,
            traffic=ec2.AclTraffic.tcp_port(22),
            direction=ec2.TrafficDirection.INGRESS,
            rule_action=ec2.Action.ALLOW
        )

        self.web_nacl_public.add_entry(
            id="Outbound: SSH to anywhere",
            cidr=ec2.AclCidr.ipv4(vpc_web.vpc_cidr_block),
            rule_number=160,
            traffic=ec2.AclTraffic.tcp_port(22),
            direction=ec2.TrafficDirection.EGRESS,
            rule_action=ec2.Action.ALLOW
        )

        #################################
        #### NACL Webserver Private #####
        #################################

        self.web_nacl_private = ec2.NetworkAcl(
            self,
            "Web_NACL_PRIVATE",
            vpc=vpc_web,
            subnet_selection=ec2.SubnetSelection(
                subnet_type=ec2.SubnetType.PRIVATE_ISOLATED
            )
        )  
        
        self.web_nacl_private.add_entry(
            id="Inbound: HTTP allow",
            cidr=ec2.AclCidr.ipv4(vpc_web.vpc_cidr_block),
            rule_number=100,
            traffic=ec2.AclTraffic.tcp_port(80),
            direction=ec2.TrafficDirection.INGRESS,
            rule_action=ec2.Action.ALLOW
        )

        self.web_nacl_private.add_entry(
            id="Outbound: HTTP allow",
            cidr=ec2.AclCidr.ipv4(vpc_web.vpc_cidr_block),
            rule_number=100,
            traffic=ec2.AclTraffic.tcp_port(80),
            direction=ec2.TrafficDirection.EGRESS,
            rule_action=ec2.Action.ALLOW
        )

        self.web_nacl_private.add_entry(
            "Inbound: HTTPS allow",
            cidr=ec2.AclCidr.ipv4(vpc_web.vpc_cidr_block),
            rule_number=120,
            traffic=ec2.AclTraffic.tcp_port(443),
            direction=ec2.TrafficDirection.INGRESS,
            rule_action=ec2.Action.ALLOW
        )

        self.web_nacl_private.add_entry(
            "Outbound: HTTPS allow",
            cidr=ec2.AclCidr.ipv4(vpc_web.vpc_cidr_block),
            rule_number=120,
            traffic=ec2.AclTraffic.tcp_port(443),
            direction=ec2.TrafficDirection.EGRESS,
            rule_action=ec2.Action.ALLOW
        )

        self.web_nacl_private.add_entry(
            "Inbound: Ephemeral ports allow",
            cidr=ec2.AclCidr.ipv4(vpc_web.vpc_cidr_block),
            rule_number=140,
            traffic=ec2.AclTraffic.tcp_port_range(1024, 65535),
            direction=ec2.TrafficDirection.INGRESS,
            rule_action=ec2.Action.ALLOW
        )

        self.web_nacl_private.add_entry(
            "Outbound: Ephemeral ports allow",
            cidr=ec2.AclCidr.ipv4(vpc_web.vpc_cidr_block),
            rule_number=140,
            traffic=ec2.AclTraffic.tcp_port_range(1024, 65535),
            direction=ec2.TrafficDirection.EGRESS,
            rule_action=ec2.Action.ALLOW
        )

        self.web_nacl_private.add_entry(
            id="Inbound: SSH allow",
            cidr=ec2.AclCidr.ipv4(vpc_web.vpc_cidr_block),
            rule_number=160,
            traffic=ec2.AclTraffic.tcp_port(22),
            direction=ec2.TrafficDirection.INGRESS,
            rule_action=ec2.Action.ALLOW
        )

        self.web_nacl_private.add_entry(
            id="Outbound: SSH allow",
            cidr=ec2.AclCidr.ipv4(vpc_web.vpc_cidr_block),
            rule_number=160,
            traffic=ec2.AclTraffic.tcp_port(22),
            direction=ec2.TrafficDirection.EGRESS,
            rule_action=ec2.Action.ALLOW
        )

        #################################
        ######## NACL Adminserver #######
        #################################

        self.admin_nacl=ec2.NetworkAcl(
            self,
            "Admin_NACL",
            vpc=vpc_admin,
            subnet_selection=ec2.SubnetSelection(
                subnet_type=ec2.SubnetType.PUBLIC
            )
        )      

        self.admin_nacl.add_entry(
            id="Inbound: SSH from my IP",
            cidr=ec2.AclCidr.ipv4(my_ip),
            rule_number=200,
            traffic=ec2.AclTraffic.tcp_port(22),
            direction=ec2.TrafficDirection.INGRESS,
            rule_action=ec2.Action.ALLOW
        )

        self.admin_nacl.add_entry(
            id="Outbound: SSH to anywhere",
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number=200,
            traffic=ec2.AclTraffic.tcp_port(22),
            direction=ec2.TrafficDirection.EGRESS,
            rule_action=ec2.Action.ALLOW
        )

        self.admin_nacl.add_entry(
            "Inbound: Ephemeral ports from anywhere",
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number=210,
            traffic=ec2.AclTraffic.tcp_port_range(1024, 65535),
            direction=ec2.TrafficDirection.INGRESS,
            rule_action=ec2.Action.ALLOW
        )

        self.admin_nacl.add_entry(
            "Outbound: Ephemeral ports to anywhere",
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number=210,
            traffic=ec2.AclTraffic.tcp_port_range(1024, 65535),
            direction=ec2.TrafficDirection.EGRESS,
            rule_action=ec2.Action.ALLOW
        )

        self.admin_nacl.add_entry(
            "Inbound: RDP from my IP",
            cidr=ec2.AclCidr.ipv4(my_ip),
            rule_number=230,
            traffic=ec2.AclTraffic.tcp_port(3389),
            direction=ec2.TrafficDirection.INGRESS,
            rule_action=ec2.Action.ALLOW
        )

        self.admin_nacl.add_entry(
            "Outbound: RDP to anywhere",
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number=230,
            traffic=ec2.AclTraffic.tcp_port(3389),
            direction=ec2.TrafficDirection.EGRESS,
            rule_action=ec2.Action.ALLOW
        )

        self.admin_nacl.add_entry(
            "Inbound: HTTP from anywhere",
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number=250,
            traffic=ec2.AclTraffic.tcp_port(80),
            direction=ec2.TrafficDirection.INGRESS,
            rule_action=ec2.Action.ALLOW
        )

        self.admin_nacl.add_entry(
            "Outbound: HTTP to anywhere",
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number=250,
            traffic=ec2.AclTraffic.tcp_port(80),
            direction=ec2.TrafficDirection.EGRESS,
            rule_action=ec2.Action.ALLOW
        )

        self.admin_nacl.add_entry(
            "Inbound: HTTPS from anywhere",
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number=270,
            traffic=ec2.AclTraffic.tcp_port(443),
            direction=ec2.TrafficDirection.INGRESS,
            rule_action=ec2.Action.ALLOW
        )

        self.admin_nacl.add_entry(
            "Outbound: HTTPS to anywhere",
            cidr=ec2.AclCidr.any_ipv4(),
            rule_number=270,
            traffic=ec2.AclTraffic.tcp_port(443),
            direction=ec2.TrafficDirection.EGRESS,
            rule_action=ec2.Action.ALLOW
        )