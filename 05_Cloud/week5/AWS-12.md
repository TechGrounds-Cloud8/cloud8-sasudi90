# [Well architected Framework]
AWS Well-Architected helps cloud architects build secure, high-performing, resilient, and efficient infrastructure for a variety of applications and workloads. Built around six pillars—operational excellence, security, reliability, performance efficiency, cost optimization, and sustainability—AWS Well-Architected provides a consistent approach for customers and partners to evaluate architectures and implement scalable designs.

## Key terminology
- **Cost optimization**: The cost optimization pillar focuses on avoiding unnecessary costs. Key topics include understanding spending over time and controlling fund allocation, selecting resources of the right type and quantity, and scaling to meet business needs without overspending.
    - implement Cloud Financial Management
    - adopt a consumption model
    - measure overall efficiency
    - stop spending money on heavy lifting as hardware for infrastructure
    - understand your costs; analyze and attribute expenditure


- **Reliability**: The reliability pillar focuses on workloads performing their intended functions and how to recover quickly from failure to meet demands. Key topics include distributed system design, recovery planning, and adapting to changing requirements. 
    - automate recovery from failure
    - scale horizontally to increase aggregate workload availability -> Replace one large resource with multiple small resources to reduce the impact of a single failure on the overall workload. Distribute requests across multiple, smaller resources to ensure that they don’t share a common point of failure.
    - stop guessing capacity
    - manage change in automation that can be tracked and reviewed


- **Operational Excellence**: The operational excellence pillar focuses on running and monitoring systems, and continually improving processes and procedures. Key topics include automating changes, responding to events, and defining standards to manage daily operations.
    - operations as code (don't jump in manually)
    - frequent, small, reversible code
    - refine operations procedures
    - anticipate failure!!!
- **Performance efficiency**: The performance efficiency pillar focuses on the efficient use of computing resources to meet requirements, and how to maintain efficiency as demand changes and technologies evolve.
    -  Democratize advanced technologies: Make advanced technology implementation easier for your team by delegating complex tasks to your cloud vendor. Rather than asking your IT team to learn about hosting and running a new technology, consider consuming the technology as a service.
    -  go global in minutes (deploy workload in multiple regions around the world for lower latency and better experience)
    -  user serverless architecture
    -  experiment more often with newly consumed technologies/services offered.
    -  consider mechanical sympathy: Use the technology approach that aligns best with your goals
- **Security**: The security pillar focuses on protecting information and systems. Key topics include confidentiality and integrity of data, managing user permissions, and establishing controls to detect security events.
    - implement strong identity foundation; principle of least privilege
    - enable traceabilty; make use of metric monitoring and alerts to enhance automation processes
    - apply security at all layers
    - automate security best practices
    - protect data in transit and in rest; encryption, tokenaziation, acces control
    - keep people away from data
    - prepare for security events; incident management and investigation policy and processes. Run incident response simulations and use tools with automation to increase speed for detection, investigation and recovery.
- **Sustainability**: The sustainability pillar focuses on minimizing the environmental impacts of running cloud workloads. Key topics include a shared responsibility model for sustainability, understanding impact, and maximizing utilization to minimize required resources and reduce downstream impacts. AWS is responsible for optimizing the sustainability of the cloud – delivering efficient, shared infrastructure, water stewardship, and sourcing renewable power. Customers are responsible for sustainability in the cloud – optimizing workloads and resource utilization, and minimizing the total resources required to be deployed for your workloads.
  - Understand your impact: Measure the impact of your cloud workload and model the future impact of your workload. Include all sources of impact, including impacts resulting from customer use of your products, and impacts resulting from their eventual decommissioning and retirement. Compare the productive output with the total impact of your cloud workloads by reviewing the resources and emissions required per unit of work. Use this data to establish key performance indicators (KPIs), evaluate ways to improve productivity while reducing impact, and estimate the impact of proposed changes over time.

  -  Establish sustainability goals: For each cloud workload, establish long-term sustainability goals such as reducing the compute and storage resources required per transaction. Model the return on investment of sustainability improvements for existing workloads, and give owners the resources they need to invest in sustainability goals. Plan for growth, and architect your workloads so that growth results in reduced impact intensity measured against an appropriate unit, such as per user or per transaction. Goals help you support the wider sustainability goals of your business or organization, identify regressions, and prioritize areas of potential improvement.

  - Maximize utilization: Right-size workloads and implement efficient design to ensure high utilization and maximize the energy efficiency of the underlying hardware. Two hosts running at 30% utilization are less efficient than one host running at 60% due to baseline power consumption per host. At the same time, eliminate or minimize idle resources, processing, and storage to reduce the total energy required to power your workload.

  - Anticipate and adopt new, more efficient hardware and software offerings: Support the upstream improvements your partners and suppliers make to help you reduce the impact of your cloud workloads. Continually monitor and evaluate new, more efficient hardware and software offerings. Design for flexibility to allow for the rapid adoption of new efficient technologies.

  - Use managed services: Sharing services across a broad customer base helps maximize resource utilization, which reduces the amount of infrastructure needed to support cloud workloads. For example, customers can share the impact of common data center components like power and networking by migrating workloads to the AWS Cloud and adopting managed services, such as AWS Fargate for serverless containers, where AWS operates at scale and is responsible for their efficient operation. Use managed services that can help minimize your impact, such as automatically moving infrequently accessed data to cold storage with Amazon S3 Lifecycle configurations or Amazon EC2 Auto Scaling to adjust capacity to meet demand.

  - Reduce the downstream impact of your cloud workloads: Reduce the amount of energy or resources required to use your services. Reduce or eliminate the need for customers to upgrade their devices to use your services. Test using device farms to understand expected impact and test with customers to understand the actual impact from using your services.


## Exercise
Study the Well Architected Framework

### Sources
- [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected/?wa-lens-whitepapers.sort-by=item.additionalFields.sortDate&wa-lens-whitepapers.sort-order=desc&awsm.page-wa-lens-whitepapers=1)

### Overcome challenges
- Looked up key terminology.


### Results
- See key terminology. 
- Note to self: UNDERSTAND BUSINESS OBJECTIVES and big focus on security  and sustainability (costs, environment) --> consume technology, automate, monitor, review, repeat 
