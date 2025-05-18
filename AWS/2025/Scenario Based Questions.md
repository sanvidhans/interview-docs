## ✅ Scenario-Based & Advanced

66. **How do you route requests from API Gateway to different services based on the path?**

* **HTTP REST APIs:** Define multiple resources and methods in API Gateway (e.g., `/users`, `/orders`). For each resource/method, configure an integration to the appropriate backend (Lambda, HTTP endpoint, VPC Link).
* **HTTP APIs:** Create multiple routes (e.g., `GET /users`, `POST /orders`) and attach them to distinct integrations.
* **Path parameters & catch‑all:** Use `{proxy+}` to capture dynamic segments, then inspect `event.path` in a single Lambda “router” or use mapping templates to forward to different downstream services.

67. **How would you design a container‑based microservice architecture using ECS and ALB?**

68. **Cluster per environment:** Create separate ECS clusters for dev, stage, prod.

69. **Task definitions:** One per microservice, specifying CPU/memory, IAM task role, container image, port mappings, and health checks.

70. **Services:** Deploy each task definition as an ECS Service with desired count and auto‑scaling policies.

71. **ALB:**

    * Create one ALB per cluster.
    * Define listeners (e.g., 80/443) and listener rules with host‑ or path‑based routing to target groups for each service.

72. **Security:** Place services in private subnets; ALB in public subnets. Use security groups to restrict traffic.

73. **Service discovery:** Optionally use AWS Cloud Map for internal service discovery, or rely on ALB DNS.

74. **How do you connect an ECS service to an RDS database securely?**

* **VPC placement:** Run ECS tasks in the same VPC/subnets as the RDS instance (prefer private subnets).
* **Security groups:**

  1. Attach a security group to ECS tasks that allows outbound to the database port.
  2. Attach a security group to RDS that permits inbound from the ECS task SG only.
* **Credentials:** Store DB credentials in Secrets Manager and grant the ECS task role permission to retrieve them.
* **IAM authentication:** If using MySQL/PostgreSQL, you can enable IAM DB Authentication to eliminate static passwords.

69. **How do you perform zero‑downtime deployment with ECS?**

* **Blue/Green with CodeDeploy:** Integrate ECS with AWS CodeDeploy’s ECS deployment controller. CodeDeploy sets up a new task set, shifts traffic gradually via the ALB, monitors health, then decommissions the old set.
* **Rolling updates (default):** Configure your ECS Service’s deployment configuration (minimum healthy percent, maximum percent) so that new tasks spin up before old ones terminate, keeping capacity constant. Monitor health checks to ensure no traffic to unhealthy tasks.

70. **What would you do if an RDS Read Replica is lagging behind the primary?**

* **Investigate load:** Check replica’s CPU, I/O, and network metrics to see if it’s under‑resourced.
* **Scale vertically:** Increase instance class or IOPS if it’s resource‑starved.
* **Optimize writes:** Reduce write volume or batch writes on the primary if possible.
* **Parameter tuning:** Ensure replication parameters (e.g., `max_standby_streaming_delay`) aren’t delaying apply.
* **Network latency:** If cross‑AZ or cross‑region, consider moving the replica closer or using Aurora Global Database for minimal lag.

71. **How would you set up a public‑facing API with private backend services using API Gateway and VPC Links?**

72. **Create a Network Load Balancer** in front of your private services running on ECS/EKS or EC2.

73. **Configure a VPC Link** in API Gateway (REST or HTTP API) pointing to that NLB.

74. **Define API routes** that integrate via the VPC Link to target your NLB’s listener and target group.

75. **Security:** Use private subnets and security groups so only the NLB and API Gateway (via ENIs) can reach the services.

76. **Authorizers & throttling:** Enforce auth (Cognito or Lambda authorizer) and usage plans at the API layer.

77. **How do you automate the provisioning of ECS, RDS, and API Gateway using CloudFormation or Terraform?**

* **CloudFormation:** Write a template defining `AWS::ECS::Cluster`, `AWS::ECS::TaskDefinition`, `AWS::ECS::Service`, `AWS::RDS::DBInstance` or `DBCluster`, and `AWS::ApiGateway::*` resources. Use `DependsOn` or intrinsic references to wire them together.
* **Terraform:** Define `aws_ecs_cluster`, `aws_ecs_task_definition`, `aws_ecs_service`, `aws_db_instance` or `aws_rds_cluster`, and `aws_api_gateway_*` resources in HCL. Use module composition for reuse and workspaces or separate state files for environments.

73. **How would you debug a failed health check in ECS?**

74. **Check container logs:** CloudWatch Logs or logging driver for stdout/stderr errors.

75. **Verify target group health:** In the EC2 console under Load Balancing → Target Groups, inspect unhealthy targets and reason codes.

76. **Test container endpoints directly:** `curl` the container’s health endpoint inside the VPC via an EC2 bastion host.

77. **Inspect task definition:** Ensure the `healthCheck` configuration (interval, path, port) matches what the container serves.

78. **Resource limits:** Confirm CPU/memory aren’t starved, causing the container to not respond.

79. **What is the best way to migrate from EC2‑based ECS to Fargate?**

* **Update task definitions:** Change the `requiresCompatibilities` field from EC2 to FARGATE, specify `networkMode: awsvpc`, and remove host‑port mappings.
* **Define subnets & security groups:** Fargate tasks require `awsvpc` networking, so ensure your cluster has private subnets with NAT or VPC endpoints.
* **Review IAM:** Ensure the task execution role is configured for Fargate.
* **Deploy side by side:** Launch new Fargate services alongside EC2 ones, shift traffic via ALB rules, then decommission EC2 services once stable.

75. **How would you monitor and alert on database connection spikes in RDS?**

* **CloudWatch Metrics:** Use the `DatabaseConnections` metric to track active connections.
* **Enhanced Monitoring:** For OS‑level session details if needed.
* **Alarms:** Create a CloudWatch alarm on `DatabaseConnections` exceeding a threshold for a sustained period, triggering SNS notifications.
* **Dashboard:** Build a CloudWatch dashboard combining connection count, CPU, and replica lag to correlate spikes with load patterns.


