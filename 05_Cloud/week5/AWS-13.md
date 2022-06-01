# [File, AppServices, CDN, DNS & Database]


## Key terminology
- CDN: A content delivery network refers to a geographically distributed group of servers which work together to provide fast delivery of Internet content. A CDN allows for the quick transfer of assets needed for loading Internet content.
-  EFS: Amazon Elastic File System (Amazon EFS) automatically grows and shrinks as you add and remove files with no need for management or provisioning.
- RDS: Amazon Relational Database Service (RDS) is a collection of managed services that makes it simple to set up, operate, and scale databases in the cloud. Choose from seven popular engines
- Aurora: Amazon Aurora is a relational database management system (RDBMS) built for the cloud with full MySQL and PostgreSQL compatibility. 


## Exercise
Study:
- Elastic Beanstalk
- Cloudfront 
- Route 53

### Sources
- [CDN](https://www.cloudflare.com/learning/cdn/what-is-a-cdn/)
- [RDS](https://aws.amazon.com/rds/)
- [Aurora](https://aws.amazon.com/rds/aurora/)
- [Elastic Beanstalk](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/Welcome.html)
- [Alternatives to EB](https://www.g2.com/products/aws-elastic-beanstalk/competitors/alternatives)
- [AWS CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Introduction.html)
- [Alternatives to Cloudfront](https://stackshare.io/amazon-cloudfront/alternatives)
- [Route53](https://aws.amazon.com/route53/)
- [Alternatives to Route53](https://www.g2.com/products/amazon-route-53/competitors/alternatives)

### Overcome challenges
- Looked up the key terminology and AWS services
- Did not really know where to start with practical due to the new way of getting assignments which is to enhance the self-learning ability. 
<br>
<br> 

# Results
## Elastic Beanstalk
- Utility: Elastic Beanstalk is a platform within AWS that is used for deploying and scaling web applications. In simple terms this platform as a service (PaaS) takes your application code and deploys it while provisioning the supporting architecture and compute resources required for your code to run. Elastic Beanstalk also fully manages the patching and security updates for those provisioned resources. 
- Replacement in classical setting: Elastic Beanstalk provisions and operates the infrastructure and manages the application stack (platform) for you, so you don't have to spend the time or develop the expertise. It will also keep the underlying platform running your application up-to-date with the latest patches and updates.
- How to combine with other services:
  - CloudFront
  - Logging Elastic Beanstalk API calls with AWS CloudTrail
  - CloudWatch
  - CloudWatch Logs
  - EventBridge
  - Finding and tracking Elastic Beanstalk resources with AWS Config
  - DynamoDB
  - ElastiCache
  - Amazon Elastic File System
  - AWS Identity and Access Management
  - Amazon RDS
  - Amazon S3
  - Amazon VPC
<br>
<br>To use Elastic Beanstalk, you create an application, upload an application version in the form of an application source bundle (for example, a Java .war file) to Elastic Beanstalk, and then provide some information about the application. Elastic Beanstalk automatically launches an environment and creates and configures the AWS resources needed to run your code. After your environment is launched, you can then manage your environment and deploy new application versions. The following diagram illustrates the workflow of Elastic Beanstalk.
- Differences with similar services: 
    -  Google App Engine.
    -  Salesforce Heroku.
    -  Azure Web Apps.
    -  Azure App Service.
    -  Cloud Foundry.
    -  Dokku.
    -  Salesforce Platform.
    -  Plesk.

## CloudFront (CDN)
- Utility: Amazon CloudFront is a web service that speeds up distribution of your static and    dynamic web content, such as .html, .css, .js, and image files, to your users. CloudFront delivers your content through a worldwide network of data centers called edge locations. When a user requests content that you're serving with CloudFront, the request is routed to the edge location that provides the lowest latency (time delay), so that content is delivered with the best possible performance.

    If the content is already in the edge location with the lowest latency, CloudFront delivers it immediately.

    If the content is not in that edge location, CloudFront retrieves it from an origin that you've defined—such as an Amazon S3 bucket, a MediaPackage channel, or an HTTP server (for example, a web server) that you have identified as the source for the definitive version of your content.
- Replacement in classical setting: This used to be done manually, now it's just easier because of automated processes. 
- How to combine with other services:
  <br>CloudFront works seamlessly with any AWS origin, such as Amazon S3, Amazon EC2, Elastic Load Balancing, or with any custom HTTP origin. You can customize your content delivery through CloudFront using the secure and programmable edge computing features CloudFront Functions and AWS Lambda@Edge.
- Differences with similar services:
    -   CloudFlare. 
    -   Google Cloud Storage.
    -   Fastly. 
    -   MaxCDN. 
    -   Amazon S3. 
    -   Azure CDN. 
    -   Incapsula.


- Utility: Amazon Route 53 is a scalable and highly available DNS service that translates human readable website names into the numeric IP address location of the target website host or a private VPC or application endpoint.
  
  - ROUTE 53 HOSTED ZONES
    A hosted zone is a collection of DNS information. These records describe how you want to route traffic for the nominated domain and it’s subdomains.

    A hosted zone has the same name as the primary domain and can be either a public or private hosted zone.

    A public hosted zone describes how you want to route traffic for the domain in the public internet while a private hosted zone defines how you want to route traffic in a private AWS VPC.
- Replacement in classical setting: regular DNS server
- How to combine with other services:
  - Amazon Route 53 integrates with AWS Identity and Access Management (IAM), a service that lets your organization do the following:

    -  Create users and groups under your organization's AWS account
    -  Easily share your AWS account resources among the users in the account
    -  Assign unique security credentials to each user
    -  Granularly control user access to services and resources
- Differences with similar services:
    -   Cloudflare DNS.
    -   Google Cloud DNS.
    -   Azure DNS.
    -   GoDaddy Premium DNS.
    -   DNSMadeEasy.
    -   ClouDNS.
    -   UltraDNS.
    -   DNSimple.
  
# EFS - lab
1. Made security group with solely access with SSH; called it EFS group
2. Create 1 EFS with SG EFS group 
3. Create 2 instances with connection to concerning EFS WITH SAME SG.
4. Connect to 1 instance with SSH via PowerShell, navigate to /dev/, mkdir efs for mount point.
5. Mount efs and check with dh -f if successfull.
   ![](../../00_includes/AWS/AWS-13/mountline.png)
6. Create files in the mounted /efs/.
7. Doublecheck structure and logout. ![](/00_includes/AWS/AWS-13/EFS1.png)
8. Connect to other instance with SSH via PowerShell, navigate to /dev/, mkdir efs for mount point.
9.  Mount efs and check with dh -f if successfull.
10. Behold the files from the first instance in /efs/![](../../00_includes/AWS/AWS-13/EFS2.png)