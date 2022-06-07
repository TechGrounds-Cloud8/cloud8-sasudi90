# [Shared Responsibility Model]
Study the AWS Shared Responsibility Model 

## Key terminology
- **Shared Responsibility Model**: This model defines what you as a customer of AWS and AWS itself are responsible for when it comes to security and compliance/ 
- **inherited controls**: controls which a customer fully inherits from AWS 
- **shared controls**: controls which apply to both the infrastructure layer and customer layers, but in separate contexts. AWS provides the requirements for infratsructure and customer provides their own control implementation within their use of AWS
  - patch and configuration management: AWS is responsible for patching, fixing flaws and maintaining of infrastructure (devices). Customer must patch their guest OS, apps and configure their own guest OS, databases and applications. 
- **customer specific**: Controls which are solely the responsibility of the customer based on the application they are deploying within AWS services. 
  - Service and Communications Protection or Zone Security which may require a customer to route or zone data within specific security environments.

## Exercise
Study the AWS Shared Responsibility Model

### Sources
[Shared responsibility model ](https://aws.amazon.com/compliance/shared-responsibility-model/)

### Overcome challenges
- Looked up the model 

### Results
- AWS is responsible for (security OF the cloud) protecting infrastructure that runs all the AWS Cloud services
  - hardware, software, networking and facilities that run AWS Cloud services
- Customer is reponsible for (security IN the cloud)
  - For EC2 this includes network level security (NACLs, security groups), operating system patches and updates, IAM user access management, and client and server-side data encryption.

![](../../00_includes/AWS/AWS-09/Shared_Responsibility_Model_V2.59d1eccec334b366627e9295b304202faf7b899b.jpg)