from aws_cdk import(
    aws_ec2 as ec2,
    aws_iam as iam,
)

from constructs import Construct

class webtemplate_construct(Construct):
    
    def __init__(self, scope: Construct, id: str, security_group, key_name, **kwargs):
        super().__init__(scope, id)

        self.template=ec2.LaunchTemplate(self, "web-template",
            instance_type=ec2.InstanceType("t3.nano"),
            machine_image=ec2.MachineImage.latest_amazon_linux(
                generation=ec2.AmazonLinuxGeneration.AMAZON_LINUX_2,
            ),
            security_group=security_group,
            key_name=key_name,
            role=iam.Role(
                self, 
                "WebTemplateRole",
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
            user_data=ec2.UserData.for_linux(),
        )