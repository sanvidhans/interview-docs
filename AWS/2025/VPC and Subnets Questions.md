## ✅ AWS VPC & Subnets Interview Questions

#### 🔹 VPC Fundamentals

1. **What is an Amazon VPC?**
   A Virtual Private Cloud (VPC) is an isolated virtual network in AWS where you launch AWS resources in a logically separate section of the AWS Cloud. You control IP ranges, subnets, routing, and security.

2. **What are the components of a VPC?**

   * **Subnets:** Segments within AZs.
   * **Route Tables:** Control traffic routing.
   * **Internet Gateway (IGW):** Enables Internet access.
   * **NAT Gateway/Instance:** Allows outbound Internet from private subnets.
   * **Security Groups & NACLs:** Stateful and stateless firewalls.
   * **DHCP Options Sets:** DNS and NTP settings.
   * **VPC Peering / Transit Gateway:** Connect VPCs.

3. **What is the default VPC and how does it differ from a custom VPC?**
   AWS creates a default VPC in each region with a default subnet in each AZ, default security group, and IGW attached. You can launch instances with public IPs immediately. A custom VPC starts empty; you must configure subnets, routing, and gateways.

4. **How do you create a custom VPC?**
   Via Console/CLI/SDK:

   ```bash
   aws ec2 create-vpc --cidr-block 10.0.0.0/16
   ```

   Then create subnets, attach an IGW, configure route tables, and security.

5. **What is CIDR and how do you assign CIDR blocks to a VPC?**
   Classless Inter‑Domain Routing (CIDR) notation defines IP ranges (e.g., `10.0.0.0/16`). When creating a VPC, you specify one primary CIDR block; you can later add secondary CIDRs (up to five) to expand the network.

6. **What is the maximum and minimum size of a VPC?**

   * **Minimum:** `/28` (16 IPs) CIDR block.
   * **Maximum:** `/16` (65,536 IPs) per CIDR block, up to five CIDR blocks per VPC.

7. **Can a VPC span multiple Availability Zones?**
   Yes. A VPC is regional; its CIDR block applies across all AZs in that region. You create subnets within each AZ to place resources.

8. **Can a VPC span multiple regions?**
   No. A VPC is confined to one AWS region. For cross‑region networking, use VPC peering or Transit Gateway with inter‑region peering.

9. **How do you delete a default VPC?**
   You cannot delete the AWS‑provided default VPC, but you can delete subnets, IGW, and recreations aren’t allowed. Instead, create and use a custom VPC as your default.

10. **What are the limitations of a VPC?**

    * Maximum of 5 VPCs per region (adjustable).
    * Maximum subnets per VPC: 200 (adjustable).
    * Route tables, NAT gateways, IGWs have quotas.
    * Secondary CIDR blocks limited to five per VPC.

---

#### 🔹 Subnets

11. **What is a subnet in a VPC?**
    A subnet is a range of IP addresses in your VPC, isolated within a single Availability Zone. Resources launched into a subnet inherit its routing and security.

12. **What is the difference between a public and private subnet?**

    * **Public subnet:** Has a route to an Internet Gateway; instances can have public IPs and receive inbound Internet traffic.
    * **Private subnet:** No direct route to an IGW; instances cannot be reached from the Internet but can access outbound via a NAT.

13. **How do you create a subnet within a VPC?**
    Via Console/CLI:

    ```bash
    aws ec2 create-subnet --vpc-id vpc-12345 --cidr-block 10.0.1.0/24 --availability-zone us-east-1a
    ```

14. **How do subnets relate to Availability Zones?**
    Each subnet resides in a single AZ. For high availability, you create one subnet per AZ for each tier (public/private).

15. **What is the smallest subnet you can create in AWS?**
    A `/28` CIDR block, which provides 16 IP addresses (11 available to resources after AWS reserves five addresses).

16. **Can a subnet span multiple Availability Zones?**
    No. A subnet is AZ‑specific. To cover multiple AZs, create separate subnets in each AZ.

17. **What happens if two subnets overlap in CIDR range?**
    AWS prevents creation of subnets whose CIDR ranges overlap with any existing subnets’ ranges in the same VPC.

18. **How do you move a resource between subnets?**
    Most resources (e.g., ENIs, RDS instances) don’t support in‑place moves. You generally:

    1. Launch a new resource in the target subnet.
    2. Migrate data or attach existing ENI.
    3. Decommission the old resource.

19. **How does a subnet determine public vs private classification?**
    By its associated route table: if a route table has a 0.0.0.0/0 route pointing to an IGW, the subnet is public; otherwise it’s private.

20. **How do you enable Internet access for a subnet?**

    1. Attach an Internet Gateway to the VPC.
    2. Add a default route (`0.0.0.0/0`) in the subnet’s route table pointing to the IGW.
    3. Ensure instances have public IPs or Elastic IPs, and security groups/NACLs allow traffic.

---

**Pro Tips:**

* Emphasize high‑availability patterns: one public/private subnet per AZ.
* Highlight security: least‑privilege SGs, segregate workloads.
* Know default quotas and how to request increases.

Good luck with your VPC interview preparation!


Here’s a detailed, professional set of answers to **AWS VPC Routing, Connectivity, and Security interview questions** — ideal for an architecture or lead role:

---

### 🔹 **Routing & Connectivity**

**21. What is a route table in AWS VPC?**
A route table contains rules (routes) that determine where network traffic is directed. Each subnet in a VPC must be associated with a route table. Routes can point to local VPC, IGW, NAT Gateway, VGW, or Transit Gateway.

---

**22. How does routing work between subnets?**
Routing within the same VPC is automatic and handled by the `local` route, which is present in all route tables. No additional configuration is needed for internal VPC communication.

---

**23. How do you configure a route to the internet?**

* Attach an **Internet Gateway** to the VPC.
* Add a `0.0.0.0/0` route in the subnet’s route table pointing to the IGW.
* Assign public or Elastic IPs to instances.
* Ensure security group/NACL rules allow traffic.

---

**24. What is an Internet Gateway (IGW)?**
A horizontally scaled, redundant VPC component that allows communication between your VPC and the public Internet. One IGW per VPC.

---

**25. What is a NAT Gateway and how does it work?**
A **NAT Gateway** enables instances in a **private subnet** to initiate outbound Internet requests (e.g., updates, API calls), but prevents unsolicited inbound traffic. It must be placed in a **public subnet** with a route in the private subnet pointing to it.

---

**26. What is the difference between a NAT instance and a NAT Gateway?**

| Feature     | NAT Gateway           | NAT Instance              |
| ----------- | --------------------- | ------------------------- |
| Scalability | Managed & auto‑scales | Manual (EC2 size matters) |
| HA          | Multi-AZ (if setup)   | Needs custom HA setup     |
| Maintenance | Managed by AWS        | User-managed              |
| Throughput  | Up to 100 Gbps        | Limited by instance type  |

Use **NAT Gateway** unless you need custom routing logic or very low cost.

---

**27. What is a Virtual Private Gateway (VGW)?**
A component on the AWS side of a **VPN connection**. It enables your VPC to connect securely to your on-premises network over IPSec VPN or via AWS Direct Connect.

---

**28. What is a Customer Gateway (CGW)?**
A **representation of your on-premises VPN device** in AWS. It is used when establishing a site-to-site VPN connection from your network to a VPC.

---

**29. How do you configure a VPN connection in a VPC?**

1. Create a **Customer Gateway** (with your on-prem public IP & ASN).
2. Create a **Virtual Private Gateway** and attach it to your VPC.
3. Create a **VPN Connection** between CGW and VGW.
4. Update your on-prem device with the configuration (AWS provides downloadable config).

---

**30. What is a Transit Gateway and when would you use it?**
An AWS service to **connect multiple VPCs and on-prem networks** using a **hub-and-spoke** model. It's scalable, simplifies routing, and supports up to 5,000 VPCs.
**Use cases:** multi-account architectures, large enterprise networks, hybrid connectivity.

---

### 🔹 **Security in VPC**

**31. What are security groups?**
Virtual firewalls attached to EC2 instances or ENIs. They are **stateful**, meaning return traffic is automatically allowed. Security groups operate at the instance level.

---

**32. What are network ACLs (NACLs)?**
Optional stateless firewalls applied at the subnet level. You define **allow/deny rules** for inbound and outbound traffic based on IPs and ports. Each rule is evaluated in number order.

---

**33. What is the difference between a security group and a NACL?**

| Feature          | Security Group            | NACL                      |
| ---------------- | ------------------------- | ------------------------- |
| Scope            | Instance level            | Subnet level              |
| Stateful         | Yes                       | No                        |
| Rules            | Only allow                | Allow and deny            |
| Rule evaluation  | All rules evaluated       | In order (numbered)       |
| Default behavior | All denied unless allowed | All allowed unless denied |

---

**34. Can you attach multiple security groups to a single instance?**
Yes, an EC2 instance can have **up to 5 security groups** (default limit). Rules from all attached groups are aggregated.

---

**35. What is the default behavior of a security group?**

* **Inbound:** All denied by default.
* **Outbound:** All allowed by default.
  You must explicitly allow inbound traffic.

---

**36. How do you block a specific IP in a security group?**
You **can’t deny traffic** in a security group — only **allow rules** are supported.
To block traffic from a specific IP:

* Use a **NACL** with a deny rule.
* Or use **WAF** / **NLB Listener Rules** / **Firewall Manager**.

---

**37. How do NACLs work with subnets?**
Each subnet is associated with a single NACL. All traffic entering/leaving the subnet is evaluated against NACL rules. You can use numbered rules for prioritization.

---

**38. What is the default behavior of a NACL?**

* **Default NACL:** Allows all inbound and outbound traffic.
* **Custom NACL:** Denies all traffic until rules are defined.
  Rules are **stateless**, so return traffic must be explicitly allowed.

---

**39. How do you audit VPC traffic?**

* **VPC Flow Logs**: Monitor and capture IP traffic going to/from network interfaces.
* Integrate with **CloudWatch Logs** or **S3** for storage.
* Use **AWS Config** for tracking changes to security groups, NACLs, etc.

---

**40. What are VPC Flow Logs and how are they used?**
VPC Flow Logs capture metadata about traffic going to/from network interfaces (source/destination IP, ports, protocol, action, result).
**Use cases:**

* Diagnose connectivity issues.
* Monitor for unusual traffic (e.g., exfiltration).
* Feed to SIEM tools for analysis.

---

Let me know if you'd like scenario-based VPC design questions, diagrams, or cheat sheets.


Here are concise, interview-ready responses for questions 41–60:

---

#### 🔹 VPC Peering & Hybrid Networks

**41. What is VPC peering?**
A VPC peering connection is a networking connection between two VPCs that enables routing of traffic between them using private IPv4 or IPv6 addresses, as if they’re within the same network.

**42. How do you configure VPC peering?**

1. **Requester**: Create a peering request in the AWS console/CLI, specifying your VPC and the peer VPC (ID and account).
2. **Accepter**: In the peer account (if different), accept the request.
3. **Route tables**: In each VPC’s route table, add a route pointing the peer’s CIDR to the peering connection.
4. **Security**: Update security groups and network ACLs to allow desired traffic.

**43. Can you peer VPCs across regions?**
Yes. AWS supports **Inter-Region VPC Peering**, allowing you to peer VPCs in different regions. It incurs additional data-transfer charges and slightly higher latency.

**44. What are the limitations of VPC peering?**

* **No transitive routing**: Peered VPCs cannot forward traffic to a third VPC.
* **Overlapping CIDRs**: CIDR blocks must not overlap.
* **Limited max peers**: Default quota is 125 peering connections per VPC.
* **Region-based**: Separate peering per region (unless using Transit Gateway).

**45. What is the difference between VPC peering and Transit Gateway?**

| Feature      | VPC Peering                       | Transit Gateway                              |
| ------------ | --------------------------------- | -------------------------------------------- |
| Architecture | Point-to-point between two VPCs   | Hub-and-spoke connecting many VPCs & on-prem |
| Transitive   | No                                | Yes                                          |
| Scalability  | Quota-based, manual for each pair | More scalable; central management            |
| Cost         | Pay per data transfer             | Per-hour + per-GB attachment charges         |

**46. How do you share a VPC across AWS accounts?**
Use **AWS Resource Access Manager (RAM)** to share subnet resources (or route tables) from a “network” account with other accounts. The other accounts can then launch resources into those shared subnets.

**47. How do you connect your on-premise network to a VPC?**

* **Site-to-Site VPN**: Over the internet using IPSec tunnels.
* **AWS Direct Connect**: Private, dedicated network link to an AWS Direct Connect location.
* Optionally, combine both for redundancy.

**48. What is AWS Direct Connect and how is it different from a VPN?**

* **Direct Connect**: Dedicated physical connection between on-prem and AWS, lower latency, consistent throughput, no internet.
* **VPN**: IPSec over public internet, easier to set up, encrypted, but more variable latency and throughput.

**49. How do you enable private connectivity between services across accounts?**

* **Interface VPC Endpoints (AWS PrivateLink)**: Expose a service via a Network Load Balancer in the provider account; consumer creates an endpoint in their VPC that attaches ENIs to access it privately.
* **AWS RAM**: Share endpoint services or subnets directly.

**50. What is PrivateLink and how does it work?**
AWS PrivateLink lets you privately access services using **interface endpoints**. A service provider publishes an endpoint service backed by an NLB; consumers create endpoints that spin up ENIs in their subnets; traffic stays on the AWS network and never traverses the internet.

---

#### 🔹 Real-world & Scenario-Based Questions

**51. How do you design a secure multi-tier architecture using public/private subnets?**

* **Web tier**: Public subnets with IGW access; hosts load balancer or NAT.
* **App tier**: Private subnets, only accessible from web tier via security groups.
* **Data tier**: Private subnets with no outbound internet; database instances locked down via SGs and NACLs.
* Use NAT gateways in private-tier subnets if the app tier requires outbound internet (e.g., for updates).

**52. How would you allow internet access for only some EC2 instances in a private subnet?**

* **Separate route tables**: Create two private subnets. One’s route table points to a NAT Gateway (thus internet-capable); the other’s does not. Place only the chosen instances in the NAT-enabled subnet.
* Additionally, use security groups to further restrict outbound traffic.

**53. How would you restrict access to a database only from specific subnets?**

* **Security groups**: Set the DB’s SG to allow ingress only from the CIDR blocks of your application subnets (or from the SG attached to app instances).
* **Network ACLs**: As a second layer, configure NACLs on the DB subnet to allow only those source CIDRs.

**54. How do you route traffic between VPCs without exposing to the internet?**

* **VPC Peering** or **Transit Gateway**: Add routes in each VPC’s route table pointing at the peering connection or TGW attachment.
* Ensure SGs and NACLs permit the inter-VPC CIDR ranges. No IGW involvement needed.

**55. What are the best practices for subnet sizing and IP planning?**

* **Power-of-two** blocks (e.g., /24, /26) for simplicity.
* Reserve at least 5 IPs per subnet (AWS consumes some).
* Allocate per-AZ subnets to ensure high availability.
* Leave future growth headroom; avoid too-tight CIDRs.
* Document and map all CIDR usage in a centralized IPAM tool.

**56. How would you troubleshoot a connection timeout to an EC2 in a public subnet?**

1. **Check public IP**: Does the instance have a public IP or Elastic IP?
2. **Route table**: Does the subnet’s route table have 0.0.0.0/0 → IGW?
3. **Security group**: Ingress/egress rules allow your source/destination?
4. **Network ACLs**: Ensure they’re not blocking traffic.
5. **OS Firewall**: Instance-level (iptables, Windows Firewall) isn’t blocking.
6. **Instance status**: Verify the instance is healthy and application is listening.

**57. How do you scale NAT Gateway for high-throughput workloads?**

* **Per-AZ NAT Gateways**: Deploy one NAT Gateway per Availability Zone to distribute load and avoid cross-AZ data charges.
* **High throughput**: Each NAT Gateway supports bursts up to 10 Gbps. If more is needed, architect multiple smaller subnets with their own NATs or use a self-managed NAT instance cluster.

**58. How do you design VPCs for multi-account environments?**

* **Central network account**: Hosts shared services (Transit Gateway, Direct Connect).
* **Spoke accounts**: Own application VPCs that attach to the central hub via TGW or RAM-shared segments.
* Use AWS Organizations & Service Control Policies to enforce tagging, CIDR ranges, and guardrails.

**59. How do you migrate resources from one VPC to another?**

* **EC2**: Create AMIs, launch new instances in the target VPC; migrate data via rsync or DataSync.
* **RDS**: Take a snapshot, restore into the new VPC.
* **Elastic IPs / ENIs**: Reassociate after launch.
* **Elastic Load Balancers**: Recreate in target VPC and shift traffic via DNS or Route 53 weighted records.
* Plan cutover to minimize downtime (blue/green or canary).

**60. How would you monitor and alert on suspicious activity within a VPC?**

* **VPC Flow Logs**: Send to CloudWatch Logs or S3; use CloudWatch Log Insights to detect anomalies (e.g., spikes or blacklisted IPs).
* **AWS GuardDuty**: Continuously analyzes VPC Flow Logs, DNS logs, and CloudTrail for threats.
* **CloudWatch Alarms**: Trigger on unexpected metrics (e.g., unusually high connection count).
* **AWS Config & CloudTrail**: Alert on configuration changes (security group openings, route table edits).

