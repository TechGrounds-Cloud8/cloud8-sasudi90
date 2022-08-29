# Design documentation

## VPC

- 2 VPC's
  - 10.10.10.0/24
  - 10.20.20.0/24
- each VPC should have at least 1 public subnet
  - each subnet must be in a different Availablity Zone
- they should have a peering connection
- subnets must have a firewall (NACL's)

## EC2 Instances and Security Groups

- 2 instances for 2 vpc's with different purposes
  - an instance for Web Server VPC
    - must not have public IP
    - must be accessible from Admin Server only by SSH: port 22
    - use proxy between between the Web Server and Public Internet
  - an instance for Admin Server VPC
    - must have internet connection to download OPENSSH: ports 80 and 443
    - SSH connection must ONLY be accessible from administrators home IP adress
    - allow RDP connection from admin's home IP: port 3389
  - both VM's must be encrypted
- Web Server must run 'User Data' to automatically install 'Apache'
- Admin Server must run 'Custom Data' to automatically run 'OPENSSH'
- Admin Server runs on Windows
- Auto Scaling Group uses a **template** of the Web Server
  - minimal capacity is 1
  - maximum capacity is 3
- Auto Scaling Group has a health check interval of 30 seconds

## NACLS

- One of the requirements was to have a firewall on subnet level. As Security Group rules are allowing all outbound and NACL's don't, the outbound rules of the NACLS have to be specified as well.  
  - As the default setting in a NACL is 'deny all outbound', this has to be adjusted. So open the needed ports on the outbound as well. As TCP works with the three way handshake, ephemeral ports has to allowed to the in- and outbound rules.

## Storage

- An encrypted S3 bucket is where the post deployment scripts must be stored
  - Contains: User Data, Custom Data and a ZIP-file containing the website.

## Backup

- daily backup after production hours, in this case set at 3 AM
- must be stored for 7 days

### Assumptions

- Region is 'europe-central'
- VPC's in same region
- Use the most facile/inexpensive instance type as possible
- Second public subnet is not in use nor needed in the Admin Server
- Use Launch Template for auto scaling group

### Suggestions
- May be better practice in future to use a custom AMI instead of a Launch Template