# Log [7-7-2022]

## One Sentence summary of the day

Feeling overwhelmed as I dont know where to start.

## Challenges

- did not know how to configure subnets for the VPC's

## Solutions

- subnet_configuration
  - use subnet_configuration LOL
- vpc connection peering
  - in CLI --> aws ec2 create-vpc-peering-connection --vpc-id vpc-01e285bca01181fee --peer-vpc-id vpc-004a8c73e12fa5cae
  - in CLI -->    aws ec2 accept-vpc-peering-connection --vpc-peering-connection-id pcx-0249466999f689be7
__- this was not the way!

# Log [8-7-2022]

## One Sentence summary of the day

Very challenging

## Challenges

- VPC peering with CfnVPCPeeringConnection
- how to get vpc_id as return value
- get user data working in .sh file in cdk, couldnt be read by pythong chrmap error
- open webserver

## Solutions

- get vpc_id by seeing vpc1 as an object
- user data  --> encoding=
- open port 80 by using
  - instance_web.connections.allow_from_any_ipv4(
            ec2.Port.tcp(80)
        )

        CfnOutput(self, "Output",
            value=instance_web.instance_public_ip)
