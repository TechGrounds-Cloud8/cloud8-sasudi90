
# README TechGrounds Project 1.0

This is guide will ease your way into the delivered Infrastructure as Code (IaC). It contains the prerequisites to start with the AWS CDK and how to deploy and adjust the IaC.

# Prerequisites

- [NodeJS](https://cdkworkshop.com/15-prerequisites/300-nodejs.html)
- [Python 3](https://www.python.org/)
  - Note: Add Python 3.x to PATH checkbox on the first screen of the Python installer wizard.
- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html)
- [AWS Account and User](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html)
- [AWS CDK Toolkit](https://cdkworkshop.com/15-prerequisites/500-toolkit.html)

## Set up your CDK

Create a virtualenv:

```
python -m venv .venv
```

After the init process completes and the virtualenv is created, you can use the following
step to activate your virtualenv.

```
source .venv/bin/activate
```

If you are a Windows platform, you would activate the virtualenv like this:

```
% .venv\Scripts\activate.bat
```

Once the virtualenv is activated, you can install the required dependencies.

```
pip install -r requirements.txt
```

# Adjust the IaC before deploying

1. Edit the IP adress variable to the administrators home IP adress in the top of the `ec2_instance_stack.py` file.
2. Create a key pair. Follow these [instructions](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/create-key-pairs.html). Name the key par 'project_key_pair' and carefully store your `project_key_pair.pem` file.
   - It's possible to adjust the name of the key pair, just edit the variable below th IP adress variable in the `ec2_instance_stack.py` file.
3. The IaC is now ready to be deployed by using the following command:

    ```
    cdk deploy
    ```

# Connecting through RDP to Admin Server

1. Go to the AWS Managements Console and go to the service 'Ec2'. Look for your running 'admin server' instance and click on 'Connect'.
2. Navigate to the tab 'RDP Client' and click on 'Download remote desktop file'.
3. To log in to the instance a password is needed. Click on 'Get password' and locate the key pair which was made before. Decrypt the password and use it to log in as Administrator on the Windows Server.

# Connecting through SSH to Web Server via Admin Server

Navigate to the directory the key pair is stored and start the SSH agent in Git Bash from there.

```
ssh-agent bash
```

Add the key pair to the agent. Edit the key pair name if it has been named differently.

```
ssh-add project_key_pair.pem
```

SSH to your Admin server's public IP. Add the -A -J to enable forwarding of the connection to the webserver.

```
ssh -A -J Administrator@<admin.server.public.ip>  ec2-user@<web.server.private.ip>
```

A password is now being asked to enter the Admin Server as user Administrator. Password can be acquired as explained in step 3 of 'Connecting through RDP to Admin Server'.

# Edit website content

When the website needs to be updated the `demo.zip` can be overwritten in the `postdeploymentscripts` directory. Just replace this ZIP file without adjusting the name.

# Clean up
After testing destroy the stack by using:
``` 
$ cdk destroy
```
