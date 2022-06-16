## AWS resources
- **AWS Codebuild**: fully managed continuous integration service that compiles source code, runs tests, and produces software packages that are ready to deploy

- **AWS SMS**: AWS Server Migration Service is used for migration of virtual machines.
  
- **AWS DMS**: AWS Database Migration Service is used for migration of databases.

- **AWS Mobile Hub**: This service is used for building, testing, and monitoring mobile applications that make use of one or more AWS services

- **VPC flow logs**:  VPC Flow Logs are used to capture network traffic information
  
### Management tools

- **AWS Systems Manager**: AWS Systems Manager is an AWS service that provides visibility and control of infrastructure on AWS.

AWS Systems Manager provides a unified interface through which you can view operational data from multiple AWS services.

- **AWS OPSWorks**: AWS OpsWorks is a configuration management service that provides managed instances of these two open-source tools (Chef and Puppet).

With OpsWorks AWS manage and automate how your infrastructure configured, deployed, and managed.

- **AWS Personal Health Dashboard**: provides alerts and remediation guidance when AWS is experiencing events that may impact you. While the Service Health Dashboard displays the general status of AWS services, Personal Health Dashboard gives you a personalized view into the performance and availability of the AWS services underlying your AWS resources

- **AWS Trusted Advisor**: AWS Trusted Advisor checks security groups for rules that allow unrestricted access (0.0.0.0/0) to specific ports. Unrestricted access increases opportunities for malicious activity (hacking, denial-of-service attacks, loss of data). 

- **Personal Health Dashboard vs Service Health Dashboard**: 
AWS Personal Health Dashboard provides alerts and remediation guidance when AWS is experiencing events that may impact you. While the Service Health Dashboard displays the general status of AWS services, Personal Health Dashboard gives you a personalized view into the performance and availability of the AWS services underlying your AWS resources.

- **AWS VPN**: AWS Virtual Private Network solutions establish secure connections between your on-premises networks, remote offices, client devices, and the AWS global network.
  
### Compute
- **AWS Elastic Beanstalk**: denk aan Casper's voorbeeld met zn Netflix replica
  
- **AWS Lightsail**: great for users who do not have deep AWS technical expertise as it makes it very easy to provision compute services: provides preconfigured virtual private servers (instances) that include everything required to deploy and application or create a database

### Storage
- **AWS Storage gateway**: hybrid cloud storage service that gives you on-premises access to virtually unlimited cloud storage. Customers use Storage Gateway to simplify storage management and reduce costs for key hybrid cloud storage use cases.
  
- **AWS DataSync**: AWS DataSync is an online data transfer service that simplifies, automates, and accelerates copying large amounts of data between on-premises storage systems and AWS Storage services, as well as between AWS Storage services.
  - DataSync vs  Storage Gateway:
    - ![](/00_includes/EP/exam2/datasyncVSstorageGateway.png)
  
- **S3 storage classes**:
  - S3 Standard (durable, immediately available, frequently accessed).
  - S3 Intelligent-Tiering (automatically moves data to the most cost-effective tier).
  - S3 Standard-IA (durable, immediately available, infrequently accessed).
  - S3 One Zone-IA (lower cost for infrequently accessed data with less resilience).
  - S3 Glacier Instant Retrieval (data that is rarely accessed and requires retrieval in milliseconds).
  - S3 Glacier Flexible Retrieval (archived data, retrieval times in minutes or hours).
  - S3 Glacier Deep Archive (lowest cost storage class for long term retention).
  - ![](../../00_includes/EP/exam2/s3%20storage%20classes.png)

- **AWS Snowball**: AWS Snowball is a method of transferring the data using a physical device. A Snowball Edge device can hold up to 80 TB so a single device can be used. This transfer method completely avoids the slow and unreliable internet connection:
    - AWS Snowball:	Bulk data transfer, edge storage, and edge compute
    - AWS Snowmobile: A literal shipping container full of storage (up to 100PB) and a truck to transport it
    - AWS Snowcone: The smallest device in the range that is best suited for outside the data center

### Security
- **AWS Secrets Manager**:AWS Secrets Manager is a secrets management service that helps you protect access to your applications, services, and IT resources. This service enables you to easily rotate, manage, and retrieve database credentials, API keys, and other secrets throughout their lifecycle. Using Secrets Manager, you can secure and manage secrets used to access resources in the AWS Cloud, on third-party services, and on-premises.
  
- **AWS Shield**: AWS Shield is a managed Distributed Denial of Service (DDoS) protection service. Safeguards web application running on AWS with always-on detection and automatic inline mitigations. Helps to minimize application downtime and latency. Two tiers – Standard and Advanced.

- **AWS WAF**: AWS WAF is a web application firewall that protects against common exploits that could compromise application availability, compromise security or consume excessive resources.

- **AWS KMS**: (KMS) gives you centralized control over the encryption keys used to protect your data. You can create, import, rotate, disable, delete, define usage policies for, and audit the use of encryption keys used to encrypt your data.
  
- **Amazon CloudHSM**: CloudHSM is a service that is used to securely store and manage encryption keys. Cloud-based hardware security module (HSM) that enables you to easily generate and use your own encryption keys on the AWS Cloud

### Analytics
- **AWS Kinesis**: Amazon Kinesis makes it easy to collect, process, and analyze real-time, streaming data so you can get timely insights and react quickly to new information.
  - Kinesis Video Streams: makes it easy to securely stream video from connected devices to AWS for analytics, machine learning (ML), and other processing.
  - Kinesis Data Streams: enables you to build custom applications that process or analyze streaming data for specialized needs.
  - Kinesis Data Firehose: is the easiest way to load streaming data into data stores and analytics tools. Captures, transforms, and loads streaming data.
  - Kinesis Data Analytics: is the easiest way to process and analyze real-time, streaming data.Can use standard SQL queries to process Kinesis data streams.

  
- **AWS QuickSight**: cloud-native, serverless, business intelligence service

- **AWS Athena**: Athena is a serverless, interactive query service to query data and analyze big data in Amazon S3 using standard SQL
  
- **AWS Glue**:  serverless data integration service that makes it easy to discover, prepare, and combine data for analytics, machine learning, and application development. AWS Glue is an Extract, Transform, and Load (ETL) service. You can use AWS Glue with data sources on Amazon S3, RedShift and other databases. Use AWS Glue to discover properties of data, transform it, and prepare it for analytics.

- **Amazon EMR**: Amazon Elastic Map Reduce (EMR) is a web service that enables businesses, researchers, data analysts, and developers to easily and cost-effectively process vast amounts of data. EMR utilizes a hosted Hadoop framework running on Amazon EC2 and Amazon S3. Most commonly used for log analysis, financial analysis, or extract, translate and loading (ETL) activities.

## parts of AWS resources
- **EC2 auto scaling**: 
    - Application Load Balancer (ALB) – layer 7 load balancer that routes connections based on the content of the request.
    - Network Load Balancer (NLB) – layer 4 load balancer that routes connections based on IP protocol data.
      - Classic Load Balancer (CLB) – this is the oldest of the three and provides basic load balancing at both layer 4 and layer 7 (not on the exam anymore).
      - Gateway Load Balancer (GLB) – distributes connections to virtual appliances and scales them up or down (not on the exam).
- **Amazon S3 select**: This service enables applications to retrieve only a subset of data from an object by using simple SQL expressions.

- **Soc 1**
- **SOC 2**
- **HIPAA**
- **ISO 27001**
- **ITIL processes**
- **ITSM tools**: IT Service Management (ITSM) tools such as the ServiceNow platform

Beste practice remarks: 

1. AWS recommends that you create individual IAM users rather than sharing IAM user accounts.

For extra security, AWS recommends that you require multi-factor authentication (MFA) for all users in your account. For privileged IAM users who are allowed to access sensitive resources or API operations, AWS recommend using U2F or hardware MFA devices.


