## ✅ AWS Load Balancing Interview Questions


#### 🔹 Types and Concepts

1. **What is Elastic Load Balancing (ELB)?**
   ELB is a fully managed service that automatically distributes incoming application traffic across multiple targets (EC2 instances, containers, IP addresses, and Lambda functions) in one or more Availability Zones. It improves fault tolerance by detecting unhealthy targets and rerouting traffic.

2. **What are the types of ELBs (ALB, NLB, CLB)?**

   * **Application Load Balancer (ALB):** Layer 7, content‑based routing (HTTP/HTTPS), WebSocket support, host‑ and path‑based routing, native WAF integration.
   * **Network Load Balancer (NLB):** Layer 4, ultra‑high performance, TLS passthrough/termination, static IP, preserves source IP, ideal for TCP/UDP workloads.
   * **Classic Load Balancer (CLB):** Legacy Layer 4/7 load balancer; limited feature set. Superseded by ALB/NLB.

3. **What is the difference between ALB and NLB?**

   | Feature                | ALB                               | NLB                                       |
   | ---------------------- | --------------------------------- | ----------------------------------------- |
   | OSI Layer              | Layer 7 (HTTP/HTTPS)              | Layer 4 (TCP/UDP/TLS)                     |
   | Routing                | Host‑ and path‑based, header/host | IP and port‑level, no content‑based logic |
   | Performance            | Moderate (optimized for HTTP)     | Very high throughput & low latency        |
   | IP Addressing          | No static IP (uses DNS)           | Static IP per AZ, Elastic IP support      |
   | Source IP Preservation | No (client IP in headers)         | Yes                                       |
   | TLS Termination        | Yes                               | Yes (TLS passthrough or termination)      |

4. **When would you choose ALB over NLB?**

   * You need advanced HTTP features: route based on URL path, host, headers, or query strings.
   * You want integrated WAF, WebSocket support, or HTTP/2.
   * You run microservices or containerized apps that require content‑aware routing.

5. **What is a target group?**
   A target group is a set of endpoints (EC2 instances, IP addresses, Lambda functions) to which the load balancer routes traffic. You configure health checks, protocol/port, and stickiness per target group, and then associate target groups with listener rules.

6. **How does health check work in ELB?**
   For each target group, ELB periodically sends requests (HTTP(s), TCP, or gRPC) to each registered target’s health‑check path/port. If a target fails the configured threshold of consecutive checks, it’s marked unhealthy and removed from rotation until it passes again.

7. **What is sticky session and when is it used?**
   Sticky sessions (session affinity) bind a user’s session to a specific target to maintain session state (e.g., in‑memory shopping cart). ALB uses application‑controlled cookies or load‑balancer‑generated cookies; NLB does not support stickiness.

8. **What is path‑based and host‑based routing in ALB?**

   * **Path‑based routing:** Direct traffic to different target groups based on URL path patterns (e.g., `/api/*` → API service, `/static/*` → CDN).
   * **Host‑based routing:** Route requests based on the HTTP Host header (e.g., `api.example.com` vs. `app.example.com`) to different target groups.

9. **Can an ELB distribute traffic across multiple regions?**
   No—each ELB is regional. For multi‑region failover or load balancing, you use Route 53 with latency‑ or geoproximity‑based routing, combined with health checks, to direct traffic to ELBs in different regions.

10. **How do you configure SSL termination in ALB?**

    1. **Provision or import** an SSL/TLS certificate in ACM (must be in the same region as the ALB).
    2. **Create an HTTPS listener** on port 443 and select the ACM certificate.
    3. **Define listener rules** mapping to target groups. Optionally enable HTTP to HTTPS redirection.

---

#### 🔹 Performance & Monitoring

11. **How does ELB scale under high load?**
    ELB is a managed, horizontally scalable service. It automatically provisions capacity across multiple Availability Zones to handle spikes. For NLB, it uses pre‑provisioned scaling “cold starts” to accommodate sudden traffic increases without disruption.

12. **How do you troubleshoot 504 errors in ELB?**

    * **Check backend health:** Ensure targets are healthy and responding within the idle timeout.
    * **Idle timeout:** Increase the load balancer’s idle timeout (default 60 s) if upstream responses take longer.
    * **Security groups/NACLs:** Verify that network rules allow traffic on required ports.
    * **Application logs:** Inspect application server logs for slow queries or errors.

13. **What are connection draining and deregistration delay?**

    * **Deregistration delay (target group setting):** When a target is deregistered, ELB stops sending new requests but lets in‑flight requests complete within the delay period (default 300 s).
    * **Connection draining (older CLB term):** Same concept for Classic Load Balancer—gracefully remove targets without dropping active connections.

14. **How do you enable access logs for ELB?**

    * In the ELB console or via CLI, enable access logging on your load balancer.
    * Specify an S3 bucket and optional prefix for log storage.
    * ELB writes detailed request logs (client IP, request path, backend response) every 5 minutes.

15. **What metrics are available in CloudWatch for ELB?**

    * **RequestCount / ActiveFlowCount:** Number of requests or active connections.
    * **HealthyHostCount / UnHealthyHostCount:** Target health status.
    * **Latency / TargetResponseTime:** Time from request to response.
    * **HTTPCode\_ELB\_4XX/5XX and HTTPCode\_Target\_4XX/5XX:** Error rates at load balancer and target.
    * **NewConnectionCount (NLB) / SurgeQueueLength (ALB):** Load and queuing indicators.