## ✅ AWS ECS (Elastic Container Service) Interview Questions

#### 🔹 Core Concepts

1. **What is Amazon ECS?**
   Amazon Elastic Container Service (ECS) is a fully managed container orchestration service that lets you run, stop, and manage Docker containers at scale. It handles scheduling, cluster management, service discovery, load balancing integration, and integrates with IAM, CloudWatch, and other AWS services.
---
2. **What is the difference between ECS and EKS?**

   * **ECS:** AWS‑managed scheduler and control plane specific to Docker containers. No cluster control plane to manage, simpler setup, AWS‑native APIs.
   * **EKS:** AWS‑managed Kubernetes control plane. Provides upstream Kubernetes API compatibility and ecosystem. You manage Kubernetes constructs (Pods, Services, Deployments).
---
3. **What is the difference between EC2 launch type and Fargate?**

   * **EC2 launch type:** You provision and manage the underlying EC2 instances in your ECS cluster. You choose instance types, AMIs, and scale the host fleet.
   * **Fargate launch type:** Serverless containers. AWS provisions and scales compute resources for you; you pay per vCPU and memory used by tasks.
---
4. **What are task definitions in ECS?**
   A task definition is a declarative JSON object that describes how to run one or more containers together (a “task”). It specifies container images, CPU/memory requirements, networking mode, environment variables, IAM role, volumes, port mappings, and logging configuration.
---
5. **What is a service in ECS?**
   An ECS service ensures that a specified number of task instances (based on a task definition) are continuously running and healthy. Services integrate with load balancers, support blue/green and rolling updates, and optionally auto‑scale tasks.
---
6. **What is a task placement strategy?**
   It defines how ECS places tasks across container instances in a cluster. Common strategies include:

   * **spread:** Evenly distribute tasks across Availability Zones or instance attributes.
   * **binpack:** Pack tasks onto the fewest instances by CPU or memory, optimizing resource usage.
   * **random:** Place tasks randomly.
     You can combine this with placement constraints to control instance attributes.
---
7. **How does ECS manage container health checks?**

   * **Docker health checks:** Defined in the container image or task definition; ECS monitors the container’s HEALTH status.
   * **Load balancer health checks:** When you attach a service to an ALB or NLB, the load balancer probes container ports and reports unhealthy targets back to ECS, which can replace failed tasks.
---
8. **What are ECS clusters?**
   A cluster is a logical grouping of container instances (EC2) or Fargate capacity where you run your tasks and services. You can have multiple clusters per account/region to isolate workloads or environments.
---
9. **What is a container instance?**
   In the EC2 launch type, a container instance is an EC2 instance that has the ECS agent installed and registered with a cluster. It provides CPU and memory resources for running tasks.
---
10. **What is the ECS agent?**
    The ECS agent is software that runs on each EC2 container instance. It polls the ECS control plane for tasks to launch, reports resource utilization and health status, and manages the Docker daemon to start and stop containers.

---

#### 🔹 Scaling & Networking

11. **How do you scale ECS tasks?**

    * **Manual:** Update the desired count on the service.
    * **Auto Scaling:**

      * **Service Auto Scaling:** Based on CloudWatch metrics (CPU, memory, custom), scale in/out the desired count.
      * **Cluster Auto Scaling (EC2):** Automatically adjusts the EC2 instance fleet via the ECS Cluster Auto Scaling feature or EC2 Auto Scaling Groups.
---
12. **How do you secure ECS tasks with IAM roles?**

    * **Task IAM Role:** Attach an IAM role to the task definition. Containers in that task assume the role to call AWS APIs with least privilege.
    * **Instance IAM Role:** For EC2 launch type, the instance profile grants the ECS agent permissions; tasks should not rely on instance role, but use task roles instead.
---
13. **How does ECS integrate with ALB?**

    * You configure the service with a load balancer definition: target group ARN and container details.
    * ECS registers and deregisters task IPs/ports with the ALB target group.
    * You can use path‑ or host‑based routing for microservices behind the same ALB.
---
14. **How do you monitor ECS services and tasks?**

    * **CloudWatch Metrics:** Built‑in metrics for CPU, memory, running tasks, service deployments, etc.
    * **CloudWatch Logs:** Configure awslogs or FireLens to collect container stdout/stderr.
    * **Events & Alarms:** Set alarms on metrics, use EventBridge rules to react to service or task state changes.
    * **Container Insights:** For detailed performance data and visualizations.
---
15. **How do you use ECS with EFS or S3?**

    * **EFS:** In your task definition, define a volume of type `efsVolumeConfiguration` and mount it into containers for shared, persistent storage across tasks.
    * **S3:** Containers interact with S3 via the AWS SDK or CLI. Use pre‑signed URLs for uploads/downloads. To inject buckets or credentials as environment variables, reference parameters or secrets in the task definition.
