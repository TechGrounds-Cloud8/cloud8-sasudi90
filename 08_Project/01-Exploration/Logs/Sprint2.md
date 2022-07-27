# Log [11-7-2022]

## One Sentence summary of the day

Read better even if it's dry.

## Challenges

- creating a bucket attached to an instance was no problem
- I thought s3deploy. was meant to be used for hosting a website only! Didn't read good enough AND I was working in the wrong dir....

## Solutions
1.
1. ```#create s3 bucket
        bucket = s3.Bucket(
            self, 
            "postdeploybucketau",
            bucket_name="postdeploybucketau",
            removal_policy=aws_cdk.RemovalPolicy.DESTROY,
            auto_delete_objects=True,
        )```

2. ```#put the scripts in dir postdeploymentscripts into s3 bucket
        s3deploy.BucketDeployment(
            self,
            "postdeploytest",
            sources=[s3deploy.Source.asset('./postdeploymentscripts')],
            destination_bucket=bucket,
        )```

# Log [12-7-2022]

## One Sentence summary of the day

Tired.

## Challenges

- create ACL for webserver (allow HTTP and HTTP)
- get the S3 bucket file and run it

## Solutions

- created a part of the NACL, but cant get onto webserver is NACL are made. Something with ports
- user data is not read from the s3 bucket; permissions?
  
____

# Log [13-7-2022]

## One Sentence summary of the day

Fruitful, gave the web instance permission to read the s3 Bucket

## Challenges

- read the S3 bucket file wityh de post deployment scripts

## Solutions

- This is put in the attributes a the web instance  

  ```
  role=iam.Role(
                self, 
                "WebServerRole",
                assumed_by=iam.ServicePrincipal("ec2.amazonaws.com"),
                description="Webserver role",
            )
- ```bucket.grant_read(instance_web)```
  
____

# Log [14-7-2022]

## One Sentence summary of the day

Yeah, this one felt like giving birth.

## Challenges

- How to make an SSH connection from home to admin server
- How to make a SSH connection from admin server to webserver

## Solutions

- create a key pair specifically for this project
- open bash and run ssh-agent bash
- run ssh-add "keyname.pem"
- run ssh -A (this enables forwarding!!!!) ec2-user@mnmgt_server_public_IP
  - this connection brings u to the admin server
- run ssh ec2-user@webserver_PRIVATE_IP
- aaaannnnddddd there u go.
-PUT THIS IN USER INSTRUCTION
Source: <https://stackoverflow.com/questions/12257968/how-to-forward-local-keypair-in-a-ssh-session>

__

# Log [15-7-2022]

## One Sentence summary of the day

Jokes on me, I needed to add route tables for the vpc's.

## Challenges

- Need to give the 2 subnets in a both vpc's a peer route, but couldn't get the subnet ID's (tokens)
- Steakholder told me he wanted to have a Windows server running on the admin server.

## Solutions

- cFnRoute something, token was not found
