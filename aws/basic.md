## Basic AWS Questions:

### 1. **What is AWS?**
**Answer:**
Amazon Web Services (AWS) is a cloud computing platform provided by Amazon that offers a suite of cloud services. These services include computing power, storage, databases, machine learning, analytics, content delivery, and more. AWS allows businesses to access and use these services on a pay-as-you-go basis, eliminating the need for upfront infrastructure investments.

### 2. **Explain the core components of AWS.**
**Answer:**
- **Compute Services:**
  - **EC2 (Elastic Compute Cloud):** Provides resizable compute capacity in the cloud.
  - **Lambda:** Allows serverless computing by running code in response to events.

- **Storage Services:**
  - **S3 (Simple Storage Service):** Object storage for the web.
  - **EBS (Elastic Block Store):** Persistent block-level storage volumes for EC2 instances.

- **Database Services:**
  - **RDS (Relational Database Service):** Managed relational database service.
  - **DynamoDB:** Fully managed NoSQL database.

- **Networking Services:**
  - **VPC (Virtual Private Cloud):** Isolated virtual network in the AWS cloud.
  - **Route 53:** Scalable domain name system (DNS) web service.

### 3. **What is the difference between EC2 and Lambda?**
**Answer:**
- **EC2 (Elastic Compute Cloud):**
  - Provides virtual servers that can be configured and managed.
  - Suitable for traditional applications and workloads.
  - Requires manual scaling.

- **Lambda:**
  - Allows serverless computing with automatic scaling.
  - Executes code in response to events without managing servers.
  - Ideal for event-driven, short-duration tasks.

### 4. **Explain Elastic Load Balancing (ELB) in AWS.**
**Answer:**
Elastic Load Balancing automatically distributes incoming application traffic across multiple targets, such as EC2 instances, containers, and IP addresses, in one or more Availability Zones. ELB increases the availability and fault tolerance of applications.

There are two types of ELB:
- **Application Load Balancer (ALB):** Operates at the application layer and allows routing decisions based on content.
- **Network Load Balancer (NLB):** Operates at the transport layer and is suitable for handling TCP/UDP traffic.

### 5. **What is Amazon S3?**
**Answer:**
Amazon S3 (Simple Storage Service) is an object storage service that offers scalable and durable storage. It is designed to store and retrieve any amount of data from anywhere on the web. S3 provides a simple web interface to manage and configure storage, making it suitable for a wide range of use cases, including data backup, archiving, and application data storage.

### 6. **Explain the concept of AWS Lambda.**
**Answer:**
AWS Lambda is a serverless computing service that allows developers to run code in response to events without provisioning or managing servers. Developers can upload their code, and Lambda automatically scales and manages the compute resources. Lambda supports multiple programming languages, and pricing is based on the actual compute time consumed by the code.

### 7. **What is AWS VPC?**
**Answer:**
Amazon Virtual Private Cloud (VPC) is a logically isolated section of the AWS Cloud where you can launch AWS resources. It allows you to define a virtual network topology, including subnets, route tables, and security groups. VPC provides control over the networking environment, including IP address ranges, subnets, and configuration of route tables and network gateways.

### 8. **Explain the purpose of Amazon RDS.**
**Answer:**
Amazon RDS (Relational Database Service) is a fully managed relational database service that makes it easy to set up, operate, and scale a relational database in the cloud. RDS supports various database engines such as MySQL, PostgreSQL, Oracle, SQL Server, and MariaDB. It handles routine database tasks, such as patch management, backups, and automatic failover, allowing users to focus on their applications.

### 9. **What is Amazon Route 53?**
**Answer:**
Amazon Route 53 is a scalable domain name system (DNS) web service designed to route end-user requests to globally distributed endpoints. It can be used to register domain names, route traffic to resources like EC2 instances or load balancers, and configure health checks for routing decisions.

### 10. **How can you ensure the security of data stored in Amazon S3?**
**Answer:**
To ensure the security of data stored in Amazon S3:
- **Use Access Control Lists (ACLs) and Bucket Policies:** Define who can access the data and what permissions they have.
- **Enable Versioning:** Keep multiple versions of an object, allowing recovery from accidental deletion.
- **Use Encryption:** Enable server-side encryption to protect data at rest.
- **Implement MFA (Multi-Factor Authentication) Delete:** Require additional authentication for sensitive operations like object deletion.



