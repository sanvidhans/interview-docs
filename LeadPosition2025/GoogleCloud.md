### GCP Interview Questions (Production Focus & Lead Level)

#### Compute Services

* **Compute Engine (GCE - VMs):**
    * **Brief:** Provides highly customizable virtual machines (VMs) for running workloads. Offers fine-grained control over instance types, OS, storage, and networking.
    * **Use Case:** When you need full control over the server environment, custom OS, or specific hardware configurations (e.g., GPU instances).
    * **Lead Focus:** Understanding instance families (N, E, C, M), autoscaling groups, managed instance groups (MIGs) for high availability and self-healing.

* **Kubernetes Engine (GKE - deep dive into architecture, deployments, services, ingress, scaling):**
    * **Brief:** Managed Kubernetes service. Abstracts away the complexity of managing a Kubernetes control plane.
    * **Architecture:** Master nodes (control plane) are managed by Google; Worker nodes run your Pods.
    * **Deployments:** Declarative way to manage application lifecycle, ensuring a desired number of Pod replicas.
    * **Services:** Abstraction for networking within the cluster, allowing Pods to communicate.
    * **Ingress:** Manages external access to services in the cluster, providing HTTP/HTTPS routing.
    * **Scaling:** Horizontal Pod Autoscaler (HPA) for Pods, Cluster Autoscaler (CA) for nodes. GKE Autopilot simplifies node management further.
    * **Lead Focus:** Node pools, GKE networking models (VPC-native), best practices for production deployments, managing secrets, Istio/service mesh concepts.

* **Cloud Run (serverless containers):**
    * **Brief:** Fully managed serverless platform for deploying containerized applications. Scales automatically from zero to thousands of instances based on traffic.
    * **Use Case:** Ideal for stateless web services, APIs, or event-driven applications where you pay only for actual request processing time.
    * **Lead Focus:** Concurrency settings, cold starts, managing environment variables, integrating with Pub/Sub or other event sources.

* **Cloud Functions (FaaS):**
    * **Brief:** Serverless, event-driven compute service for running small pieces of code (functions) in response to events (e.g., HTTP requests, database changes, Pub/Sub messages).
    * **Use Case:** Micro-tasks, event handlers, webhook processors.
    * **Lead Focus:** Cold starts, triggers (HTTP, Cloud Storage, Pub/Sub, Firestore), environment variables, connecting to VPC networks.

* **App Engine (PaaS):**
    * **Brief:** Fully managed platform-as-a-service (PaaS) for developing and hosting web applications. Offers standard (constrained environment) and flexible (containerized) environments.
    * **Use Case:** Web applications that need quick deployment and automatic scaling without managing underlying infrastructure.
    * **Lead Focus:** Environment choice (Standard vs. Flexible), scaling mechanisms, deployment strategy, integration with other GCP services.

#### Storage

* **Cloud Storage (object storage, different storage classes):**
    * **Brief:** Scalable, durable object storage. Ideal for unstructured data like images, videos, backups, data lakes.
    * **Storage Classes:**
        * **Standard:** High availability, frequent access (e.g., live content).
        * **Nearline:** Accessed less than once a month (e.g., backups).
        * **Coldline:** Accessed less than once a quarter (e.g., disaster recovery).
        * **Archive:** Long-term archival, accessed less than once a year (e.g., regulatory compliance).
    * **Lead Focus:** Lifecycle management (moving objects between classes), multi-regional vs. regional buckets, strong consistency, security (IAM, signed URLs).

* **Cloud SQL (managed relational DBs):**
    * **Brief:** Fully managed relational database service for MySQL, PostgreSQL, and SQL Server. Handles patching, backups, replication, and scaling.
    * **Use Case:** Traditional relational workloads, transactional applications.
    * **Lead Focus:** High availability (failover replicas), read replicas, connection management, scaling options (vertical/horizontal read replicas), private IP connectivity.

* **Cloud Spanner (horizontally scalable relational DB):**
    * **Brief:** Horizontally scalable, globally distributed, and strongly consistent relational database service. Offers unlimited scale with transactional consistency.
    * **Use Case:** Mission-critical applications requiring extreme scalability, high availability, and strong consistency globally.
    * **Lead Focus:** When to choose Spanner over Cloud SQL, cost implications, designing for global consistency.

* **Firestore/Datastore (NoSQL):**
    * **Brief:** Scalable, flexible NoSQL document databases. Firestore is newer, provides real-time updates and stronger consistency guarantees. Datastore is the older version, good for large-scale, non-relational data.
    * **Use Case:** Mobile/web apps with real-time data needs, user profiles, catalogs.
    * **Lead Focus:** Data modeling for NoSQL, denormalization, handling eventual consistency (Datastore), real-time listeners (Firestore).

#### Networking

* **VPC (Virtual Private Cloud):**
    * **Brief:** A global, software-defined network that provides networking functionality for your GCP resources. It's the logical isolation for your cloud resources.
    * **Lead Focus:** Global reach (subnets in different regions but in the same VPC), network peering, Shared VPC for large organizations.

* **Subnets:**
    * **Brief:** Logical divisions within a VPC, defined by an IP address range. Resources are launched into specific subnets.
    * **Lead Focus:** Regional scope of subnets, private IP allocation, designing subnet CIDR ranges.

* **Load Balancers (various types):**
    * **Brief:** Distribute incoming traffic across multiple instances to ensure high availability and scalability.
    * **Types:**
        * **External HTTP(S) Load Balancer:** Global, for web traffic, supports advanced routing, CDN.
        * **Internal HTTP(S) Load Balancer:** Regional, for internal service-to-service communication.
        * **TCP/UDP Proxy Load Balancer:** Global, for non-HTTP(S) protocols.
        * **Network Load Balancer:** Regional, pass-through, for extreme performance for non-HTTP(S) protocols.
    * **Lead Focus:** Choosing the right load balancer for the workload, global vs. regional, health checks, session affinity.

* **Cloud DNS:**
    * **Brief:** High-performance, global DNS service that provides authoritative DNS lookup for your domains.
    * **Lead Focus:** Managing public and private DNS zones, integration with GKE, DNSSEC.

* **Cloud CDN:**
    * **Brief:** Content Delivery Network that caches content closer to your users globally, reducing latency and origin server load.
    * **Lead Focus:** Cache invalidation strategies, integration with HTTP(S) Load Balancer.

#### IAM and Security Best Practices

* **Identity and Access Management (IAM):**
    * **Brief:** Controls who (identities) can do what (roles) on which resources. Granular permissions are key.
    * **Roles:** Predefined (Owner, Editor, Viewer), Primitive (Legacy), Custom.
    * **Policies:** Collections of bindings (identity, role, resource) applied to resources.
    * **Service Accounts:** Identities used by applications or VMs to interact with GCP services securely.
    * **Best Practices (Least Privilege):** Grant only the necessary permissions for a task, no more. Use service accounts for applications, not user credentials. Regularly review and audit policies.
    * **Lead Focus:** Designing IAM policies, security for service accounts, role-based access control (RBAC) in GKE, separation of duties.

* **VPC Service Controls:**
    * **Brief:** Creates a "security perimeter" around sensitive GCP services and resources to prevent data exfiltration. It defines a boundary that data cannot cross.
    * **Lead Focus:** Protecting sensitive data, preventing unauthorized access from outside the perimeter, use cases for highly regulated environments.

* **Key Management Service (KMS):**
    * **Brief:** Managed service for creating, managing, and using cryptographic keys. Integrates with many GCP services for encryption at rest.
    * **Lead Focus:** Data encryption strategies (customer-managed encryption keys - CMEK, customer-supplied encryption keys - CSEK), key rotation, access control for keys.

#### Monitoring and Logging

* **Cloud Monitoring (metrics, dashboards, alerting):**
    * **Brief:** Collects metrics, events, and metadata from GCP resources, applications, and custom sources.
    * **Metrics:** Predefined metrics for all GCP services.
    * **Dashboards:** Customizable visualizations of metrics.
    * **Alerting:** Define conditions to trigger notifications (e.g., email, PagerDuty) when metrics cross thresholds.
    * **Lead Focus:** Defining SLOs/SLIs, creating effective dashboards, designing alerting strategies, custom metrics.

* **Cloud Logging (logs, log sinks, exports):**
    * **Brief:** Centralized logging service for collecting, storing, analyzing, and exporting logs from GCP resources and applications.
    * **Logs:** Structured logging is preferred (JSON).
    * **Log Sinks:** Route logs to destinations like Cloud Storage, BigQuery, Pub/Sub for further analysis or archiving.
    * **Lead Focus:** Structured logging best practices, log parsing, exporting logs for long-term retention or SIEM integration, log-based metrics.

* **Cloud Trace:**
    * **Brief:** Distributed tracing system that collects latency data from applications and visualizes call flows between services.
    * **Lead Focus:** Identifying performance bottlenecks in microservice architectures, understanding request propagation.

* **Cloud Debugger:**
    * **Brief:** Allows you to inspect the state of a running application in production without stopping or slowing it down.
    * **Lead Focus:** Non-intrusive debugging, diagnosing elusive bugs, using snapshots and logpoints.

#### CI/CD & IaC

* **Cloud Build:**
    * **Brief:** A serverless CI/CD platform that executes your builds on GCP infrastructure. Supports various source repositories (GitHub, Cloud Source Repositories).
    * **Use Case:** Building, testing, and deploying container images or applications.
    * **Lead Focus:** Build steps, triggers, integrating with GCR (Google Container Registry), orchestrating multi-stage builds.

* **Cloud Deploy:**
    * **Brief:** Fully managed continuous delivery service that automates deployments to GKE, Cloud Run, and App Engine. Supports progressive delivery (e.g., canary deployments).
    * **Lead Focus:** Release automation, managing deployment pipelines across environments, rollbacks.

* **Integrating with GKE for CI/CD pipelines:**
    * **Brief:** Cloud Build can build Docker images, push them to GCR, and then update GKE deployments using `kubectl` commands or Cloud Deploy to trigger new rollouts.
    * **Lead Focus:** Blue/Green deployments, canary deployments, automating rollbacks, managing Kubernetes manifests, GitOps principles.

* **Infrastructure as Code (IaC) with Terraform or Deployment Manager:**
    * **Brief:** Managing and provisioning infrastructure through code instead of manual configuration.
    * **Terraform:** Open-source, cloud-agnostic tool (HashiCorp) for provisioning and managing infrastructure. Declarative syntax.
    * **Deployment Manager:** GCP's native IaC service, uses YAML or Python to define resources.
    * **Lead Focus:** Benefits (reproducibility, version control, auditability), state management (Terraform state files), module creation, team collaboration with IaC.

#### Cost Optimization Strategies

* **Strategies for reducing GCP costs:**
    * **Right-sizing:** Choose the smallest instance types or service tiers that meet performance requirements.
    * **Autoscaling:** Scale resources up/down automatically based on demand.
    * **Spot VMs / Preemptible VMs:** Use for fault-tolerant, batch, or non-critical workloads for significant cost savings.
    * **Committed Use Discounts (CUDs):**
        * **Brief:** Commit to a certain level of resource usage (e.g., vCPUs, memory for VMs) for 1 or 3 years in exchange for significant discounts.
        * **Lead Focus:** Strategic long-term planning, identifying stable workloads for CUDs, analyzing cost data.
    * **Storage Class Optimization:** Use appropriate Cloud Storage classes based on access frequency.
    * **Serverless First:** Prefer Cloud Functions/Cloud Run where possible as you only pay for execution.
    * **Network Egress Optimization:** Minimize data transfer costs, especially cross-region or to the internet.
    * **Deleting Unused Resources:** Regularly audit and remove unneeded VMs, disks, unattached IPs, etc.

#### Architecture & Best Practices

* **Designing highly available, scalable, and fault-tolerant applications on GCP:**
    * **High Availability (HA):** Deploy across multiple regions/zones, use managed services with built-in HA (Cloud SQL HA, GKE), load balancers, auto-healing.
    * **Scalability:** Use autoscaling for compute (MIGs, HPA), serverless platforms (Cloud Run, Cloud Functions), horizontally scalable databases (Spanner, Firestore), message queues (Pub/Sub).
    * **Fault Tolerance:** Design for failure, implement retries with exponential backoff, circuit breakers, distributed tracing, robust error handling, disaster recovery.
    * **Lead Focus:** N+1 redundancy, active-active vs. active-passive, regional vs. multi-regional deployments, single points of failure analysis.

* **Disaster recovery strategies:**
    * **Brief:** Plans and procedures to recover from major outages (e.g., regional failure).
    * **RTO (Recovery Time Objective):** Maximum acceptable downtime.
    * **RPO (Recovery Point Objective):** Maximum acceptable data loss.
    * **Strategies:** Cross-regional backups (Cloud Storage), multi-regional deployments (GKE, Spanner), regularly testing DR plans.
    * **Lead Focus:** Defining RTO/RPO, implementing recovery processes, backup/restore strategies, data replication.

* **Understanding different architectural patterns (microservices, monoliths):**
    * **Monoliths:** (Covered above) Discuss when they are appropriate (small, simple apps, early stage startups).
    * **Microservices:** (Covered above) Discuss when they are appropriate (complex, large-scale, high-growth apps).
    * **Lead Focus:** Understanding the trade-offs of each, guiding the team on architectural choices, patterns like API Gateway, messaging queues, service discovery in a microservices context.

#### Troubleshooting

* **Diagnosing common issues in GCP environments (networking, compute, database):**
    * **Networking:** Firewall rules, VPC peering issues, load balancer misconfigurations, DNS resolution problems, routing issues.
    * **Compute:** High CPU/memory usage, unhealthy instances in MIGs, container crashes in GKE/Cloud Run, cold starts in serverless.
    * **Database:** Slow queries, connection pooling issues, deadlocks, disk I/O bottlenecks, replication lags.
    * **Lead Focus:** Systematic troubleshooting approach (divide and conquer), using GCP's monitoring tools, understanding network flows.

* **Using GCP tools for troubleshooting:**
    * **Cloud Logging:** For application and infrastructure logs.
    * **Cloud Monitoring:** For metrics, dashboards, and alerts.
    * **Cloud Trace:** For distributed request tracing across services.
    * **Cloud Debugger:** For inspecting live code in production.
    * **Network Intelligence Center:** For network insights, firewall insights, connectivity tests.
    * **Cloud Shell/`gcloud` CLI:** For quick command-line diagnostics.
    * **GKE Dashboard/kubectl:** For Kubernetes-specific issues.

* **Scenario-based questions: Expect questions like "How would you deploy a highly available Golang application on GCP?" or "Design a real-time data processing pipeline using GCP services."**
    * **Deploying a Highly Available Golang App on GCP:**
        1.  **Containerize:** Dockerize the Golang app.
        2.  **GKE:** Deploy to GKE across multiple availability zones (regional cluster).
        3.  **Deployment:** Use Kubernetes Deployment with multiple replicas.
        4.  **Scaling:** HPA for Pods, Cluster Autoscaler for nodes.
        5.  **Load Balancer:** External HTTP(S) Load Balancer in front of GKE (Ingress).
        6.  **Database:** Cloud SQL with HA (failover replica) or Cloud Spanner for global scale.
        7.  **CI/CD:** Cloud Build to build/deploy, Cloud Deploy for staged rollouts.
        8.  **Monitoring:** Cloud Monitoring for app/GKE metrics, Cloud Logging for logs.
        9.  **Secrets:** Kubernetes Secrets or Secret Manager.
        10. **Networking:** Private IP for inter-service communication.
        11. **Code:** Ensure statelessness in the Golang app.

    * **Design a Real-time Data Processing Pipeline using GCP services:**
        1.  **Ingestion:** Cloud Pub/Sub (for high-throughput, low-latency message ingestion).
        2.  **Processing (Stream):** Dataflow (for managed Apache Beam pipelines, scales automatically), or GKE/Cloud Run (for custom processing logic in containers).
        3.  **Storage (Hot Path):** BigQuery (for analytics, data warehousing), Firestore (for real-time dashboards), or Cloud Memorystore (Redis) for caching.
        4.  **Storage (Cold Path/Archive):** Cloud Storage (for raw data lake, backups).
        5.  **Monitoring:** Cloud Monitoring and Cloud Logging throughout the pipeline.
        6.  **Visualization:** Looker Studio (formerly Data Studio) or Looker.
        7.  **Data Transformation (Batch):** Dataflow or Dataproc for batch ETL.

Good luck!