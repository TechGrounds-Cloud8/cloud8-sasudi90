# [Global Infrastructure]
Study AWS Global infrastructure and its components. 

## Key terminology 
- **AWS availabilty zone**: data center living within a 'region', consist of one or more discrete data centers.  84 Availability Zones.  Each zone in a region has redundant and separate power, networking and connectivity to reduce the likelihood of two zones failing simultaneously. A common misconception is that a single zone equals a single data center. In fact, each zone is backed by one or more physical data centers, with the largest backed by five. While a single availability zone can span multiple data centers, no two zones share a data center. Abstracting things further, to distribute resources evenly across the zones in a given region, Amazon independently maps zones to identifiers for each account. In AZ’s, customers are able to operate production applications and databases that are more fault tolerant, scalable, and highly available than you would see from a single data center. 
- **Regions**: geographical location with multiple Availablity Zones, 26 regions. Every region is physically isolated from and independent of every other region in terms of location, power, water supply, etc. This level of isolation is critical for workloads with compliance and data sovereignty requirements where guarantees must be made that user data does not leave a particular geographic region.
- **Edge location**: AWS data centers designed to deliver services with the lowest latency possible, closer to users than Regions or Availablity Zones, responses are fast.
- **IAM**: Identity and Access Management. With IAM, you can manage AWS permissions for workforce users and workloads.  You can specify who can access which services and resources, and under which conditions.
- **RDS**: relational database service;  is a collection of managed services that makes it simple to set up, operate, and scale databases in the cloud.
- **latency**: is a measurement of a round-trip between two systems such as how long it takes data to make its way between two

When you launch an instance, you select a Region and a virtual private cloud (VPC), and then you can either select a subnet from one of the Availability Zones or let us choose one for you. If you distribute your instances across multiple Availability Zones and one instance fails, you can design your application so that an instance in another Availability Zone can handle requests. 

Keep in account when choosing a Region:
- Compliance. If your workload contains data that is bound by local regulations, then selecting the Region that complies with the regulation overrides other evaluation factors. This applies to workloads that are bound by data residency laws where choosing an AWS Region located in that country is mandatory.
- Latency. A major factor to consider for user experience is latency. Reduced network latency can make substantial impact on enhancing the user experience. Choosing an AWS Region with close proximity to your user base location can achieve lower network latency. It can also increase communication quality, given that network packets have fewer exchange points to travel through.
- Cost. AWS services are priced differently from one Region to another. Some Regions have lower cost than others, which can result in a cost reduction for the same deployment.
- Services and features. Newer services and features are deployed to Regions gradually. Although all AWS Regions have the same service level agreement (SLA), some larger Regions are usually first to offer newer services, features, and software releases. Smaller Regions may not get these services or features in time for you to use them to support your workload.

## Exercise
1. What is an AWS Availability Zone?
2. What is a Region?
3. What is an Edge Location?
4. Why would you choose one region over another? (e.g. eu-central-1 (Frankfurt) over us-west-2 (Oregon))

### Sources
- [Global infrastructure](https://docs.aws.amazon.com/whitepapers/latest/aws-overview/global-infrastructure.html)
- [Using regions and availablity zones](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html#concepts-regions)
- [Considering Region](https://aws.amazon.com/blogs/architecture/what-to-consider-when-selecting-a-region-for-your-workloads/)

### Overcome challenges
- Looked up key terminology

### Results
1. Availability Zones are distinct locations within an AWS Region that are engineered to be isolated from failures in other Availability Zones. They provide inexpensive, low-latency network connectivity to other Availability Zones in the same AWS Region.
2. Each Region is a separate geographic area. Availability Zones are multiple, isolated locations within each Region.
3.  An edge location is a very closest point to the user using the AWS service that contains a small setup instead of the server and is responsible to deliver a static content as a quick respose to the user request.
4.  Choosing an AWS Region closer nearby the user base location could provide lower network latency  and increase communication quality. Also check the costs of different Regions, they could differ substantially.  
