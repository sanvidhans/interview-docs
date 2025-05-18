## ✅ AWS S3 (Simple Storage Service) Interview Questions

#### 🔹 S3 Basics & Concepts

1. **What is Amazon S3?**
   Amazon Simple Storage Service (S3) is an object storage service that offers industry‑leading scalability, data availability, security, and performance. You can store and retrieve any amount of data—from anywhere on the web—using a simple web services interface.

2. **What is an S3 bucket?**
   A bucket is a logical container in S3 that holds objects (files and metadata). Every object lives in exactly one bucket, and bucket names are globally unique across AWS.

3. **How is data organized in S3?**
   Data is stored as *objects* in buckets. Each object consists of a key (its name), a value (the data), and metadata. You can emulate folders by using prefixes and the “/” delimiter in object keys.

4. **What are S3 object keys?**
   The object key is the unique identifier for an object within a bucket—essentially its full “path.” For example, `images/2025/05/photo.jpg` is a key with two prefixes (`images`, `2025/05`) and the object name.

5. **What is the maximum object size you can upload to S3?**

   * **Single PUT:** up to 5 GB per call.
   * **Multipart upload:** up to 5 TB per object.

6. **What storage classes does S3 support?**

   * **Standard:** General‑purpose, frequently accessed.
   * **Intelligent‑Tiering:** Auto‑moves objects between two tiers based on access patterns.
   * **Standard‑IA (Infrequent Access):** Lower cost for less‑frequently accessed data, retrieval fees apply.
   * **One Zone‑IA:** Like Standard‑IA but stored in a single AZ.
   * **Glacier Instant, Flexible, Deep Archive:** For long‑term archival with varying retrieval times.
   * **Reduced Redundancy (legacy):** Lower durability; rarely used today.

7. **What is the default storage class for S3?**
   **Standard** storage class is the default for all new objects unless you specify otherwise.

8. **How do you upload large files to S3?**
   Use the **Multipart Upload** API or SDK support: split the file into parts (5 MB–5 GB each), upload parts in parallel, then complete the upload to assemble the object. This improves throughput, resiliency, and allows retrying individual parts.

9. **What are multipart uploads?**
   A mechanism to upload a single object as a set of parts. You initiate a multipart upload, upload each part independently, and then complete the upload. If any part fails, you can retry just that part.

10. **How do you delete an S3 object?**

    * **Single delete:** `DELETE /bucket-name/object-key` via API/SDK/console.
    * **Bulk delete:** Use the `DeleteObjects` API with up to 1,000 keys per request.
    * **Versioned buckets:** Deleting adds a delete marker; previous versions remain until explicitly removed.

---

#### 🔹 Bucket Configuration & Management

11. **How do you create and name an S3 bucket?**

    * **Console/CLI/API:** `aws s3api create-bucket --bucket my-unique-bucket-name --region us-east-1` (add `--create-bucket-configuration LocationConstraint=…` outside `us-east-1`).
    * Choose a globally unique, DNS‑compliant name.

12. **What are the naming rules for S3 buckets?**

    * 3–63 characters, lowercase letters, numbers, hyphens.
    * Must start and end with a letter or number.
    * No underscores, uppercase, or adjacent periods.
    * Cannot look like an IP address (e.g., 192.168.5.4).

13. **What is versioning in S3 and how does it work?**
    Versioning keeps multiple variants of an object in the same bucket. When enabled, each PUT or DELETE creates a new version ID. You can retrieve, restore, or permanently delete specific versions.

14. **How do you enable versioning on an S3 bucket?**

    * **Console:** Bucket → Properties → Versioning → Enable.
    * **CLI:**

      ```bash
      aws s3api put-bucket-versioning \
        --bucket my-bucket \
        --versioning-configuration Status=Enabled
      ```

15. **What happens when you delete a versioned object?**
    A *delete marker* is added as the current version, making the object appear deleted. Older versions remain and can be restored by removing the delete marker or retrieving a specific version ID.

16. **What is the lifecycle configuration in S3?**
    Rules that manage object transitions and expirations. You can automatically:

    * **Transition** objects to cheaper storage classes after a set number of days.
    * **Expire** objects or non-current versions after a retention period.
    * **Abort** incomplete multipart uploads after a specified number of days.

17. **How do you transition data between storage classes?**
    Define a lifecycle rule with a `Transition` action specifying the target storage class (e.g., Standard → Standard‑IA after 30 days, then to Glacier after 90).

18. **What are object tags in S3?**
    Key‑value pairs you can assign to objects (up to 10 tags per object). Tags help with lifecycle rules, cost allocation, and access control via tag‑based IAM policies.

19. **How does S3 Object Lock work?**
    Object Lock prevents object version deletion or modification for a defined retention period. Two modes:

    * **Governance:** Certain users can override retention.
    * **Compliance:** Immutable—no one (even root) can delete or modify until the retention period expires.

20. **What is S3 Batch Operations?**
    A managed feature to perform large‑scale batch operations on billions of objects. You define a job (via CSV manifest) and choose an action: Object copy, ACL changes, tagging, Glacier restore, or Lambda invocation per object. Batch jobs run reliably and track progress in CloudWatch.

---

#### 🔹 Security & Access Control

21. **How do you secure data in S3?**

    * **Encryption at rest:** Enable SSE‑S3, SSE‑KMS, or client‑side encryption.
    * **Encryption in transit:** Enforce SSL/TLS for all requests.
    * **Access policies:** Use IAM policies, bucket policies, and ACLs with least‑privilege.
    * **Block public access:** Enable Block Public Access account‑ or bucket‑wide.
    * **VPC Endpoints:** Use S3 VPC endpoints to keep traffic off the public internet.

22. **What is an S3 bucket policy?**
    A resource‑based IAM policy attached directly to a bucket that defines who (principals) can perform which actions (`s3:GetObject`, `s3:PutObject`, etc.) on that bucket’s objects under specified conditions.

23. **What is the difference between a bucket policy and IAM policy?**

    * **Bucket policy:** Resource‑based, attached to the bucket, controls access for any principal (including cross‑account).
    * **IAM policy:** Identity‑based, attached to users/groups/roles, controls what principal can do across all resources.

24. **How do you make a bucket public?**

    1. Disable Block Public Access on the bucket.
    2. Attach a bucket policy allowing `s3:GetObject` to `"Principal": "*"`.
    3. Optionally enable static website hosting to serve objects via HTTP.

25. **What are S3 Access Control Lists (ACLs)?**
    Legacy, coarse‑grained grants at the bucket or object level. ACLs let you grant read/write permissions to AWS accounts or predefined groups (e.g., “AllUsers”), but are superseded by bucket policies for most use cases.

26. **What is S3 Block Public Access and why is it important?**
    A set of account‑ or bucket‑level settings that override any ACLs or bucket policies to prevent public access. It’s a safeguard against accidental exposure of sensitive data.

27. **What is encryption at rest and in transit?**

    * **At rest:** Data stored on disk is encrypted.
    * **In transit:** Data moving between client and S3 (or internal AWS) is encrypted via TLS to prevent eavesdropping.

28. **What types of server‑side encryption are available in S3?**

    * **SSE‑S3:** S3‑managed keys (`AES‑256`).
    * **SSE‑KMS:** KMS‑managed keys with auditability, IAM and KMS key policies.
    * **SSE‑C:** Customer‑provided keys—customers supply and manage encryption keys.

29. **How do you use SSE‑S3, SSE‑KMS, and SSE‑C?**

    * **SSE‑S3:** Set `x‑amz‑server‑side‑encryption: AES256` header on PUT.
    * **SSE‑KMS:** Specify `x‑amz‑server‑side‑encryption: aws:kms` and `x‑amz‑server‑side‑encryption‑aws‑kms‑key‑id`.
    * **SSE‑C:** Provide `x‑amz‑server‑side‑encryption‑customer‑algorithm` and customer key headers; S3 does not store the key.

30. **How can you audit access to S3 buckets?**

    * **CloudTrail Data Events:** Log object‑level API calls (`GetObject`, `PutObject`).
    * **Server Access Logging:** Deliver logs of requests to a target bucket.
    * **S3 Storage Lens & CloudWatch:** Monitor usage and activity trends.

---

#### 🔹 Data Management & Performance

31. **What is S3 Transfer Acceleration?**
    A feature that speeds up uploads and downloads by routing traffic over AWS’s optimized network via edge locations. You enable it per bucket and use a special endpoint (`bucketname.transfer.accelerate.amazonaws.com`).

32. **What is S3 Select and when should you use it?**
    S3 Select lets you retrieve subsets of object data (e.g., CSV, JSON) using SQL expressions. Use it to reduce data transfer and processing when you need only part of a large object.

33. **How does S3 support static website hosting?**

    * Enable static website hosting on the bucket.
    * Specify an index document (e.g., `index.html`) and optional error document.
    * Configure bucket policy or ACLs to allow public `GetObject`.
    * Use the generated website endpoint (`http://bucket.s3-website-region.amazonaws.com`).

34. **What are pre‑signed URLs and how are they used?**
    URLs generated with temporary credentials that grant time‑limited access to S3 operations (GET, PUT). Useful for client‑side uploads/downloads without exposing AWS credentials or making buckets public.

35. **How do you optimize performance for frequently accessed data?**

    * **Prefix design:** Spread keys across multiple prefixes to improve request parallelism.
    * **S3 Intelligent‑Tiering:** Automatically optimize cost/performance.
    * **CloudFront CDN:** Cache objects at edge locations.
    * **Multipart downloads:** Use ranged GETs in parallel.

36. **How does S3 handle data consistency?**
    Since December 2020, S3 provides strong read-after-write consistency for PUTs and DELETEs of new or overwritten objects across all regions and storage classes.

37. **How do you copy data between buckets?**

    * **S3 Console or CLI:** `aws s3 cp s3://src-bucket/key s3://dest-bucket/key` or `aws s3 sync`.
    * **Cross‑region replication:** Configure replication rules (CRR) for automatic, asynchronous copying.

38. **What are replication rules in S3 (CRR & SRR)?**

    * **Cross‑Region Replication (CRR):** Asynchronously replicate objects to a bucket in a different region for compliance, lower latency, or disaster recovery.
    * **Same‑Region Replication (SRR):** Replicate objects within the same region for data‑locality or multi‑account data sharing.

39. **What is Intelligent‑Tiering in S3?**
    An automated storage class that moves objects between access tiers (frequent, infrequent, archive) based on changing access patterns, optimizing cost without performance impact.

40. **How do you monitor and analyze S3 usage?**

    * **S3 Storage Lens:** Provides organization‑wide metrics and dashboards for usage, activity, and cost.
    * **CloudWatch Metrics:** Track bucket‑level metrics like total bytes, number of objects, and request counts.
    * **CloudWatch Logs Insights:** Query server access logs for detailed access patterns.

---

#### 🔹 Monitoring & Troubleshooting

41. **What are S3 access logs?**
    Detailed records of requests made against your bucket, capturing requester, bucket name, request time, action, response status, and error codes. Useful for security audits, usage analysis, and troubleshooting.

42. **How do you enable logging for an S3 bucket?**
    In the S3 console (or via CLI), go to **Properties → Server access logging**, specify a target bucket (must reside in the same region) and optional prefix. Ensure the target bucket’s ACL grants write permission to the source bucket.

43. **What is AWS CloudTrail and how does it work with S3?**
    CloudTrail records API calls for AWS services as events. For S3, you can enable **Data Events** in CloudTrail to log object-level operations (`GetObject`, `PutObject`, `DeleteObject`), which are delivered to an S3 bucket or CloudWatch Logs for audit and forensic analysis.

44. **How do you troubleshoot 403 and 404 errors in S3?**

    * **403 (Access Denied):** Check bucket policies, IAM policies, ACLs, and Block Public Access settings. Ensure the principal has the correct `s3:GetObject` or `s3:ListBucket` permissions, and that any VPC endpoint policies allow access.
    * **404 (Not Found):** Verify the bucket name, object key spelling (keys are case‑sensitive), correct region, and that you’re not expecting a deleted version in a versioned bucket (delete markers may hide objects).

45. **What metrics are available in CloudWatch for S3?**

    * **BucketSizeBytes:** Total storage used.
    * **NumberOfObjects:** Count of objects.
    * **AllRequests, GetRequests, PutRequests, DeleteRequests, 4xxErrors, 5xxErrors:** Request counts and error rates.
    * **FirstByteLatency & TotalRequestLatency (Storage Lens advanced metrics):** Latency per request.

46. **How do you set up alarms for S3 activity?**
    In CloudWatch, create alarms on any S3 namespace metric (e.g., `4xxErrors`) or on custom metrics (like CloudTrail data event counts). Define threshold, evaluation period, and notification via SNS or other actions.

47. **What is S3 Storage Lens?**
    A built‑in dashboards service that provides organization‑wide visibility into object storage usage, activity metrics, and best‑practice recommendations. Includes both free and advanced metrics with analytics.

48. **How do you check the replication status of an object?**

    * In the console, select the object and view the **Replication** tab to see status (`PENDING`, `COMPLETED`, `FAILED`).
    * Via CLI: `aws s3api head-object --bucket src --key key --query ReplicationStatus`.

49. **How do you troubleshoot a failed object upload?**

    * Check S3 access logs or CloudTrail to see the error code.
    * Ensure correct permissions (`s3:PutObject`) and that the bucket exists in that region.
    * For multipart uploads, list parts (`ListParts`) to see which part failed and retry it, or abort the upload if beyond retry.

50. **How do you monitor costs for S3 storage?**

    * **AWS Cost Explorer:** Filter by service “Amazon Simple Storage Service.”
    * **S3 Storage Lens advanced metrics:** Analyze storage cost by tags, bucket, or region.
    * **AWS Budgets:** Set up alerts for S3 spend thresholds.

---

#### 🔹 Real‑World Scenarios & Architecture

51. **How would you use S3 as a data lake?**

    * Organize raw, processed, and curated data into well‑defined prefixes (“zones”).
    * Enforce schema validation via Glue Crawlers, Athena, or Lake Formation.
    * Apply fine‑grained access control with Lake Formation permissions, IAM, and bucket policies.
    * Use lifecycle policies to transition older data to Glacier tiers.

52. **How do you serve private content from S3 using CloudFront?**

    * Configure a CloudFront distribution with the S3 bucket as origin.
    * Use an Origin Access Identity (OAI) or Origin Access Control (OAC) so CloudFront can fetch private content.
    * Restrict bucket policy to only allow that OAI/OAC.
    * Generate signed URLs or signed cookies for clients to access content.

53. **How would you protect S3 content from accidental deletion?**

    * **Enable versioning:** So delete markers hide but do not permanently remove objects.
    * **Enable Object Lock:** In Compliance or Governance mode to enforce immutable retention periods.
    * **Use MFA Delete:** Require MFA for version‑deletion operations.
    * **Implement IAM policies:** Deny `s3:DeleteObjectVersion` unless from a specific admin role.

54. **How would you secure an S3 bucket for a multi‑tenant application?**

    * Partition data by tenant using prefixes or separate buckets.
    * Use IAM policies or bucket policies with condition keys (`s3:prefix`) to restrict each tenant’s access to their own prefix.
    * Encrypt all data in transit and at rest.
    * Audit access with CloudTrail data events.

55. **How do you integrate S3 with Lambda for event‑driven processing?**

    * Enable S3 event notifications on `s3:ObjectCreated:*` (and others if needed).
    * Configure the notification to invoke a Lambda function.
    * In the function, parse the event, retrieve the object, and perform business logic (e.g., image processing, ETL).

56. **How would you migrate on‑premise files to S3 efficiently?**

    * **AWS CLI `sync`:** For smaller datasets over a stable connection.
    * **AWS DataSync:** For accelerated, managed transfer with scheduling, monitoring, and validation.
    * **AWS Snowball:** For petabyte‑scale migrations when limited network bandwidth.
    * Use parallel multipart uploads and pipeline the process.

57. **How do you manage S3 access across multiple AWS accounts?**

    * Use **bucket policies** granting cross‑account principals specific actions.
    * Leverage **AWS Organizations** SCPs to enforce organization-wide restrictions.
    * Use **IAM roles** with trust policies to allow users in one account to assume a role that grants S3 access in another.

58. **How do you deliver large media files efficiently using S3?**

    * Serve through **CloudFront CDN** to cache at edge locations, reducing latency.
    * Use **Range GETs** for partial content streaming.
    * Enable **Transfer Acceleration** for faster global uploads.
    * Optimize objects (compression, appropriate codecs).

59. **How would you set up cross‑region replication for compliance?**

    * Enable **versioning** on source and destination buckets.
    * Create a **replication rule** specifying prefix/tag filters, destination bucket (in another region), and an IAM role for replication.
    * Monitor via replication metrics and S3 Storage Lens.

60. **What are best practices for S3 bucket naming, security, and lifecycle management?**

    * **Naming:** Use clearly defined, DNS‑compliant names; include environment and region (e.g., `myapp-prod-us-east-1`).
    * **Security:** Enable Block Public Access, enforce encryption, use least‑privilege polices, audit with CloudTrail.
    * **Lifecycle:** Implement rules to transition objects to cheaper tiers and expire/delete outdated data. Tag objects for cost allocation and policy targeting.

---

