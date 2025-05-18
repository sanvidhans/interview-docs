## ✅ AWS RDS (Relational Database Service) Interview Questions

#### 🔹 Basics & Configuration

1. **What is Amazon RDS?**
   Amazon Relational Database Service (RDS) is a fully managed service that makes it easy to set up, operate, and scale relational databases in the cloud. It automates time‑consuming administration tasks such as provisioning, patching, backup, recovery, failure detection, and repair.

2. **What database engines are supported by RDS?**

   * **Amazon Aurora** (MySQL‑ and PostgreSQL‑compatible)
   * **MySQL**
   * **PostgreSQL**
   * **MariaDB**
   * **Oracle**
   * **SQL Server**

3. **What is Multi‑AZ deployment?**
   Multi‑AZ deploys a synchronous standby replica in a different Availability Zone. All writes are synchronously replicated to the standby. In case of primary failure, Amazon RDS automatically fails over to the standby, minimizing downtime and data loss.

4. **What is a Read Replica and how is it different from Multi‑AZ?**
   A Read Replica is an asynchronously replicated copy of the primary database used to offload read traffic or for reporting, analytics, and geo‑scale. Unlike Multi‑AZ (which is for high availability and automatic failover), Read Replicas are meant for read scaling and must be promoted manually if you want to use them as a writable primary.

5. **What is the backup retention period?**
   You can configure automatic backups to be retained for 0–35 days. When set to 0, automatic backups are disabled. Longer retention increases storage costs but allows point‑in‑time recovery further back into history.

6. **How do you enable automatic backups in RDS?**
   When creating or modifying an instance, enable **Backup retention** by setting the retention period to 1–35 days. Amazon RDS will take daily snapshots during the preferred backup window and store transaction logs for PITR.

7. **How do you scale RDS vertically and horizontally?**

   * **Vertical scaling:** Modify the instance class to a larger VM size (more CPU, memory) or increase storage size/IOPS. Requires a reboot during a maintenance window.
   * **Horizontal scaling:**

     * **Read Replicas:** Add replicas to handle read‑heavy workloads.
     * **Aurora Auto Scaling:** For Aurora clusters, add or remove Aurora Replicas automatically.

8. **What is the difference between RDS and Aurora?**

   * **Aurora:** AWS‑designed, distributed storage across three AZs by default, up to 15 low‑latency replicas, continuous backup to S3, faster (often 2× MySQL, 3× PostgreSQL), serverless options, global database.
   * **RDS engines:** Traditional single‑AZ or Multi‑AZ deployments, fewer replica options, storage limited to a single AZ (backed to S3), and no built‑in serverless.

9. **What are parameter groups and option groups?**

   * **Parameter group:** A collection of engine configuration values (e.g., `max_connections`, `innodb_buffer_pool_size`) that apply to instances. You can create custom groups to tweak engine behavior.
   * **Option group:** A set of additional features or “options” (e.g., Oracle APEX, SQL Server Audit, TDE encryption) that you can enable on an RDS instance.

10. **What are RDS storage types (gp2, io1, etc)?**

    * **General Purpose SSD (gp2/gp3):** Cost‑effective, burstable performance suitable for most workloads. gp3 lets you provision IOPS independently.
    * **Provisioned IOPS SSD (io1/io2):** High‑performance SSD with guaranteed IOPS for I/O‑intensive workloads.
    * **Magnetic (standard):** Legacy HDD storage for infrequently accessed data (least expensive, slowest).

---

#### 🔹 Security & Monitoring

11. **How do you secure an RDS instance?**

    * **VPC placement:** Deploy the instance in a private subnet.
    * **Security groups:** Restrict inbound access to only necessary sources and ports.
    * **IAM authentication:** Use IAM DB authentication for supported engines.
    * **Encryption:** Enable encryption at rest (KMS) and in transit (SSL/TLS).
    * **Network ACLs and VPC endpoints:** Use VPC endpoints for S3 export/import to avoid traversing the public internet.

12. **What is encryption at rest and in transit in RDS?**

    * **At rest:** Data and automated backups, snapshots, and replicas are encrypted using a customer‑managed or AWS‑managed KMS key.
    * **In transit:** Enforce SSL/TLS connections between your application and the database to protect data over the network.

13. **How does RDS integrate with IAM?**

    * **IAM Database Authentication:** Supported for MySQL and PostgreSQL — allows authentication using IAM tokens instead of static passwords.
    * **IAM policies:** Control who can call RDS APIs (create, modify, delete).
    * **Enhanced monitoring:** IAM roles grant RDS permission to write metrics to CloudWatch Logs.

14. **What is enhanced monitoring in RDS?**
    Enhanced Monitoring provides real‑time metrics for the operating system (CPU, memory, file system, disk I/O) at 1‑second granularity. Metrics are delivered to CloudWatch Logs for deeper visibility than standard CloudWatch metrics.

15. **How do you audit RDS activity?**

    * **Database engine logs:** Enable general, slow query, and error logs and export them to CloudWatch Logs or S3.
    * **CloudTrail:** Records all RDS API calls (who, when, what).
    * **Performance Insights:** Provides SQL-level performance metrics and query analytics.
    * **Database audit features:** Use native engine auditing (e.g., Oracle AUDIT, PostgreSQL pgAudit) for fine‑grained activity logging.

---