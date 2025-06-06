## 2. Systems Design

**Q:** “Design a scalable, reliable file-upload system for large media files.”
**A (outline):**

1. **Clarify requirements**: max file size, throughput, latency, security (auth/ZTNA), sync vs async.
2. **High-level flow**:

   * Client uploads to S3 via presigned URLs
   * S3 triggers Lambda for virus scan → on success, sends metadata to SQS
   * Auto-scaled EC2/ECS/Fargate consumers read SQS, process video (transcode, thumbnail)
   * Store outputs in versioned S3, metadata in DynamoDB
3. **Reliability & scaling**:

   * Use SQS DLQ for failures, CloudWatch alarms, Lambda reserved concurrency limits
4. **Trade-offs**:

   * Preferring async for long-running tasks vs blocking clients
   * S3 eventual consistency nuances

---

## 3. Python Deep Dive

**Q:** “Explain how you’d architect a Python microservice for real-time analytics.”
**A (outline):**

* **Framework**: FastAPI for async endpoints
* **Messaging**: Kafka consumer → processes events, writes to PostgreSQL with SQLAlchemy
* **Concurrency**: asyncio + uvicorn workers; CPU-intensive tasks offloaded to Celery
* **Testing**: pytest with fixtures + mocking Kafka brokers
* **Deployment**: Docker + AWS SAM; CI/CD via GitLab with lint, unit, integration steps

---

## 4. Cloud Migration

**Q:** “How would you migrate an on-prem monolith to AWS with zero downtime?”
**A (outline):**

1. **Plan**: Break into strangler-pattern microservices; define service boundaries
2. **Database**: Use AWS DMS for continuous replication to RDS, cutover at low-traffic window
3. **Deploy**:

   * Blue/green via ALB target groups + Route 53 weighted routing
   * Canary releases with Lambda versions and aliases for new services
4. **Observability**: CloudWatch + X-Ray to compare performance pre/post

---

## 5. Networking Fundamentals

**Q:** “How do you design a VPC for multi-tier application with strict security?”
**A (outline):**

* **Subnets**: Public (ALB/LB), private (app), isolated (DB) across ≥2 AZs
* **Routing**: Internet Gateway for public; NAT Gateways for private outbound; no IGW for isolated
* **Security**:

  * SG1: ALB allows 80/443 from internet
  * SG2: App SG allows only SG1 on 80/443
  * SG3: DB SG allows only SG2 on 5432
* **NACLs**: Stateless deny all inbound except required, allow all outbound

---

## 6. Performance Troubleshooting

**Q:** “An API’s 95th­-percentile latency is 200 ms; target is < 50 ms. How do you investigate?”
**A (outline):**

1. **Metrics**: Check CloudWatch/RDS slow-query logs, Lambda duration
2. **Profiling**: Use X-Ray or APM to pinpoint hotspots
3. **Optimize**:

   * Add DB indexes, optimize queries
   * Introduce Redis cache for hot endpoints
   * Increase concurrency or instance size if CPU-bound

---

## 7. Leadership & PM (STAR)

**Q:** “Describe a time you rescued a failing project.”
**A (outline):**

* **Situation:** CI/CD builds failing daily, blocking releases
* **Task:** Restore build reliability and velocity
* **Action:**

  1. Introduced SonarQube gating to catch errors early
  2. Parallelized test suites in GitLab runners
  3. Automated rollback scripts for bad releases
* **Result:** Deployment failures dropped 80%, lead time cut from 4 h to 45 min

---

## 8. Team Mentoring

**Q:** “How do you onboard and upskill junior engineers?”
**A (outline):**

* Kick off with **pair-programming** sessions on live tickets
* Weekly **“brown-bag”** talks on AWS best practices and microservices design
* **Code-reviews** focused on teaching: explain pitfalls, encourage questions
* Establish a **runbook** for common tasks (deployments, rollbacks)

---

## 9. Behavioral Fit

**Q:** “Why Wipro, and what excites you about working here?”
**A (outline):**

* Mention Wipro’s **global enterprise** footprint and complex, varied projects
* Draw connection to your passion for **enterprise networking** and large-scale integrations
* Emphasize desire to grow into an **Architect** role and contribute to their **innovation culture**

---

## 10. Your Questions

**Q (to ask them):**

1. “What’s the biggest challenge your TA team is facing in the next quarter?”
2. “How do you measure success for an L1 Architect at Wipro?”
3. “What opportunities exist for cross-domain collaboration within Wipro’s global practice?”

---

❇️ **Tip:** For each answer, lead with the outcome/impact, then briefly describe **how** you achieved it, tying back to tools and metrics. Keep each response under \~2 minutes so you can cover multiple areas in 30 minutes. Good luck!
