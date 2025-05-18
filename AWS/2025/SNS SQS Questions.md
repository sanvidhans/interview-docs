## ✅ **AWS SNS & SQS Interview Questions**

#### 🔹 Basics & Fundamentals

1. **What is Amazon SNS?**
   A fully managed pub/sub messaging service that decouples microservices, distributed systems, and serverless applications. Publishers send messages to topics; SNS broadcasts them to all subscribed endpoints.

2. **What are the key use cases of SNS?**

   * **Fan‑out:** Distribute updates to multiple systems (e.g., push notifications, downstream processing).
   * **Application alerts:** System health alerts via SMS, email, or mobile push.
   * **Workflow triggering:** Invoke Lambda functions or send to SQS to kick off asynchronous workflows.

3. **What types of subscribers can SNS support?**
   HTTP/HTTPS endpoints, email (raw or JSON), SMS, mobile push (APNS, FCM), Lambda functions, SQS queues, and EventBridge buses.

4. **What is the difference between a topic and a subscription in SNS?**

   * **Topic:** Logical access point and communication channel for messages.
   * **Subscription:** An endpoint (with a protocol) registered to receive messages published to that topic.

5. **What are SNS message filtering policies?**
   JSON policies you attach to subscriptions that inspect message attributes and deliver only those messages matching the filter criteria, reducing unnecessary downstream processing.

6. **How does SNS handle fan‑out messaging?**
   When you publish to a topic, SNS concurrently pushes the message to every confirmed subscription endpoint, scaling automatically to support very high throughput.

7. **What is the format of an SNS message payload?**
   By default, SNS wraps your message in a JSON envelope with metadata (TopicArn, MessageId, Timestamp, etc.). You can enable **raw message delivery** to send just the original payload.

8. **Can SNS deliver messages to encrypted endpoints?**
   Yes—if the subscriber is an SQS queue or Lambda function with a KMS‑encrypted policy, SNS will deliver messages encrypted at rest (via SSE) where supported.

9. **What delivery protocols does SNS support?**
   HTTP, HTTPS, Email/Email‑JSON, SMS, Application (mobile push), Lambda, SQS, and EventBridge.

10. **What are the limits for message size and throughput in SNS?**

    * **Message size:** Up to 256 KB per published message.
    * **Throughput:** Virtually unlimited; per‑topic and per‑account quotas can be increased via AWS Support.

---

#### 🔹 Architecture & Integration

11. **How do you implement pub/sub architecture using SNS?**

    1. Create an SNS topic.
    2. Subscribe endpoints (Lambda, SQS, HTTP, etc.).
    3. Publishers send messages to the topic; SNS routes to all subscribers, decoupling producers from consumers.

12. **How do you trigger a Lambda function from an SNS topic?**
    Subscribe the Lambda’s ARN to the topic. SNS will invoke the function synchronously with the message envelope whenever a new message is published.

13. **How do you set up an SQS queue as an SNS subscriber?**

    1. Create or identify the SQS queue.
    2. Subscribe the queue’s ARN to the SNS topic.
    3. Update the queue’s access policy to allow SNS to send messages to it.

14. **How do you use message filtering in SNS subscriptions?**
    When subscribing, define a FilterPolicy JSON document mapping message attribute names to allowed values. SNS evaluates each published message’s attributes and delivers only matching messages to that subscription.

15. **How does SNS handle message ordering and delivery attempts?**

    * **Ordering:** SNS does not guarantee ordering across standard topics (use FIFO topics for ordering).
    * **Retries:** SNS retries failed deliveries up to several times with exponential backoff. For HTTP/HTTPS endpoints, it retries over several minutes before marking failure.

16. **What is the difference between raw message delivery and structured message delivery?**

    * **Structured (default):** SNS wraps payload in a JSON envelope with metadata.
    * **Raw:** SNS sends only the original message body, without additional metadata.

17. **What happens if an endpoint (e.g., HTTP) fails to receive an SNS message?**
    SNS retries according to its retry policy. If delivery continues to fail, and you’ve configured a dead‑letter queue (DLQ) on the subscription, the message is sent there for later inspection.

18. **How can SNS integrate with EventBridge?**
    You can configure an SNS topic as an EventBridge rule target. Conversely, EventBridge can forward matching events to an SNS topic for broader fan‑out, bridging custom and AWS service events.

19. **How do you secure SNS topics using IAM policies?**

    * **Resource‑based policies** on the topic control which principals can publish or subscribe.
    * Use condition keys (e.g., `aws:SourceAccount`, `aws:SourceArn`) to restrict access.
    * Enforce encryption at rest with a KMS key and restrict decrypt permissions.

20. **Can you use SNS to send cross‑region notifications?**
    SNS topics are regional. For cross‑region distribution, you can create topics in multiple regions and use either:

    * **Cross‑account/region subscriptions:** Subscribe an endpoint in another region directly.
    * **Message replication:** Publish to one topic, then forward via Lambda or EventBridge to topics in other regions.

---

**Pro Tips:**

* Demonstrate how you’ve used filtering policies to optimize downstream workloads.
* Discuss trade‑offs between SNS standard vs. FIFO topics for ordering and deduplication.
* Highlight best practices for monitoring (CloudWatch metrics, DLQs) and securing topics (least‑privilege policies, encryption).


#### 🔹 Basics & Concepts

21. **What is Amazon SQS?**
    Amazon Simple Queue Service (SQS) is a fully managed message queuing service for decoupling and scaling microservices, distributed systems, and serverless applications. Producers enqueue messages; consumers poll and process them asynchronously.

22. **What is the difference between Standard and FIFO queues?**

    * **Standard Queues:**

      * At‑least‑once delivery (occasionally duplicates)
      * Best‑effort ordering (not guaranteed)
      * Virtually unlimited throughput
    * **FIFO Queues:**

      * Exactly‑once processing (deduplicated)
      * First‑in, first‑out ordering guaranteed
      * Limited throughput (up to 3,000 messages/sec with batching)

23. **What is message visibility timeout?**
    The period after a consumer retrieves a message during which it remains “invisible” to other consumers. If the consumer doesn’t delete it before timeout, the message becomes visible again for reprocessing.

24. **How does long polling work in SQS?**
    Consumers specify a **WaitTimeSeconds** (up to 20 s) when calling `ReceiveMessage`. Long polling holds the connection open until a message arrives or the timeout elapses, reducing empty responses and API costs.

25. **What is the maximum retention period of SQS messages?**
    Messages can be retained for **1 minute to 14 days**. Default is 4 days.

26. **What is the maximum size of an SQS message?**

    * **Standard payload:** Up to 256 KB per message body.
    * **Extended payload:** Up to 2 GB when using SQS Extended Client Library with S3 for large‑payload offloading.

27. **How does deduplication work in FIFO queues?**

    * **Content‑based deduplication:** AWS computes a SHA‑256 hash of the message body to detect duplicates within the 5‑minute deduplication interval.
    * **Explicit deduplication ID:** Producer provides a `MessageDeduplicationId`. Messages with the same ID in the interval are treated as duplicates and only one is delivered.

28. **What is a dead‑letter queue (DLQ) and how is it used?**
    A DLQ is a secondary queue where messages that can’t be processed successfully (after a configured maximum receive count) are moved. This isolates “poison pill” messages for analysis or manual handling without blocking the main queue.

29. **What is message delay in SQS?**
    A per‑message or per‑queue setting that delays visibility of new messages by up to 15 minutes. Use it to postpone processing of time‑sensitive tasks.

30. **Can SQS guarantee exactly‑once delivery?**

    * **Standard Queues:** At‑least‑once (duplicates possible).
    * **FIFO Queues:** Exactly‑once (with deduplication), provided no consumer errors and within the deduplication window.

---

#### 🔹 Usage & Integration

31. **How does Lambda poll and process messages from SQS?**
    Lambda uses an **event source mapping** to poll the queue. When messages arrive, Lambda invokes your function with a batch of records. Successful execution deletes the messages; failures trigger retries or DLQ routing.

32. **How do you configure batch size and concurrency for SQS‑Lambda integration?**

    * **Batch size:** Set `MaximumBatchingWindowInSeconds` and `BatchSize` in the event source mapping (default batch size = 10).
    * **Concurrency:** Control with reserved concurrency on the function or set `ParallelizationFactor` (up to 10) to allow multiple batches per shard for FIFO queues.

33. **How do you use SQS in a decoupled microservice architecture?**

    * **Producer Microservice:** Push events/messages to an SQS queue.
    * **Consumer Microservice:** Poll the queue and process messages independently, retrying or sending failures to a DLQ.
    * **Benefits:** Resilience (backpressure handling), scaling consumers independently, and loose coupling between services.

34. **How does SQS work with AWS Step Functions?**
    You can use the **Task** state with the `arn:aws:states:::sqs:sendMessage` integration to enqueue messages, or use a **Wait** state to poll for messages. Step Functions can orchestrate complex workflows that include queue‑based tasks.

35. **How do you handle poison pill messages in SQS?**

    * Configure a **maxReceiveCount** so that after N failed processing attempts, the message moves to a DLQ.
    * Monitor the DLQ, inspect the poison message, fix the issue or manually reprocess after remediation.

36. **How does visibility timeout affect message reprocessing?**
    If a consumer fails to delete a message before the visibility timeout expires, the message becomes visible again and another consumer can reprocess it. You can extend visibility (via `ChangeMessageVisibility`) to allow more processing time.

37. **How can you purge an SQS queue?**
    Use the **PurgeQueue** API (`aws sqs purge-queue --queue-url <url>`) to delete all messages in the queue. Note: Purge can only be called once every 60 seconds per queue.

38. **How do you scale SQS consumers for high‑volume workloads?**

    * Increase the number of consumers (Lambda concurrency or EC2/Container consumers).
    * Use **long polling** to maximize receive efficiency.
    * For FIFO queues, adjust `ParallelizationFactor` to process multiple batches across multiple shards.

39. **How do you securely interact with SQS using IAM roles and policies?**

    * Grant least‑privilege permissions (`sqs:SendMessage`, `sqs:ReceiveMessage`, `sqs:DeleteMessage`) to your producers and consumers via IAM roles.
    * Use resource ARNs and condition keys (`aws:SourceVpce`, `aws:SourceIp`) to restrict access further.

40. **What happens if Lambda times out while processing an SQS message?**

    * The message remains un‑deleted, and after the visibility timeout, becomes visible again for retry.
    * Lambda retry behavior combined with the queue’s retry settings determine how many times the message is retried before it moves to the DLQ.

---

## 🔄 SNS vs. SQS (Comparison & Architecture)

#### Differences & Use Cases

41. **What is the difference between SNS and SQS?**

* **SNS (Pub/Sub):** Push‑based, broadcasts messages to multiple subscribers (fan‑out), real‑time delivery.
* **SQS (Queue):** Pull‑based, stores messages durably until consumers poll and delete them; point‑to‑point processing.

42. **When would you choose SNS over SQS, and vice versa?**

* **SNS:** When you need to broadcast events to many subscribers (e.g., push notifications, fan‑out to multiple services).
* **SQS:** When you need guaranteed, decoupled, asynchronous point‑to‑point processing with durability (e.g., background job queue).

43. **Can you use SNS and SQS together? Explain a real‑world use case.**
    Yes. **Fan‑out pattern**: Publish to an SNS topic, subscribe multiple SQS queues—one per downstream service. Each service processes messages at its own pace. Use case: Order placement publishes an “OrderCreated” event; billing, inventory, and shipping services each consume from dedicated SQS queues.

44. **How does the message delivery mechanism differ between SNS and SQS?**

* **SNS:** Pushes messages to subscribers (HTTP, SQS, Lambda) immediately, retries on failure with backoff.
* **SQS:** Messages sit in a queue; consumers poll (`ReceiveMessage`), then explicitly delete after processing. Retries happen when visibility timeout expires.

45. **How do you ensure reliable delivery using SNS → SQS → Lambda?**

46. **SNS → SQS:** Use DLQs on the subscription for undeliverable messages.

47. **SQS → Lambda:** Configure a DLQ on the Lambda event source mapping.

48. **Visibility timeout & retries:** Tune visibility timeout greater than Lambda timeout.

49. **Monitoring:** Alarms on DLQs and error metrics.

50. **How do you handle message retries in SNS and SQS?**

* **SNS:** Retries based on protocol (HTTP backoff, SMS retries). Configure DLQs on subscriptions for failures.
* **SQS:** Visibility timeout causes message to reappear if not deleted. Configure maxReceiveCount on consumer to move poisoned messages to a DLQ.

47. **What are the scaling capabilities of SNS vs. SQS?**

* **SNS:** Virtually unlimited throughput; automatically scales to millions of publishes per second.
* **SQS Standard:** Virtually unlimited throughput; Standard queues handle nearly unlimited transactions.
* **SQS FIFO:** Limited to 3,000 TPS with batching; ordering and deduplication guarantees.

48. **How do you secure message publishing and consumption in SNS and SQS?**

* **IAM policies:** Identity‑based and resource‑based policies grant least privilege.
* **Encryption:**

  * SNS: SSE‑KMS for topic messages.
  * SQS: SSE‑KMS for queue storage.
* **VPC endpoints:** Use AWS PrivateLink endpoints (`com.amazonaws.region.sqs` / `sns`) to avoid public internet.
* **Access policies & subscription filters:** Restrict publishers/subscribers by account or principal.

49. **How does message ordering work in SNS vs. SQS FIFO?**

* **SNS:** No ordering guarantee on standard topics; ordering only in FIFO topics (feature added).
* **SQS FIFO:** Delivers messages in the same order within a message group; deduplication prevents duplicates.

50. **What is the latency comparison between SNS and SQS?**

* **SNS:** Millisecond‑level push latency to subscribers.
* **SQS:** Poll‑based; latency depends on poll frequency and long‑poll duration (can be under 100 ms with long polling).

---

## 📘 Bonus: Scenario‑Based Questions

51. **Design a decoupled microservice system using SNS and SQS.**

52. Use SNS for domain events (e.g., `UserRegistered`).

53. Subscribe per‑service SQS queues (email service, analytics service).

54. Each microservice polls its queue, processes independently, and deletes messages.

55. Monitor DLQs and set alarms for failed processing.

56. **You’re seeing duplicate Lambda invocations from SQS — how do you fix it?**

* Ensure **idempotency** in your function (use dedupe keys in DynamoDB).
* Increase **visibility timeout** so Lambda has enough time to process before message reappears.
* Check for errors in the function causing premature exit without deleting the message.

53. **How would you ensure exactly‑once processing using SQS FIFO and Lambda?**

* Use an SQS FIFO queue with **MessageGroupId** to preserve order.
* Provide **MessageDeduplicationId** to eliminate duplicates within the dedupe window.
* Implement idempotent processing in Lambda to handle rare edge cases.

54. **How would you handle failure retries for SNS‑delivered messages?**

* Configure a DLQ (SQS) on the SNS subscription.
* Monitor the DLQ and set up an alert.
* Optionally, use a Lambda to reprocess or notify engineers of DLQ messages.

55. **A service is overloaded by burst messages from SNS → SQS → Lambda. What’s your fix?**

* **Buffering:** Increase SQS visibility timeout and batch size to process more per invocation.
* **Throttle:** Use reserved concurrency on Lambda to smooth processing.
* **Scale consumers:** Add more parallel consumers or increase Lambda concurrency.
* **Decompose burst:** Implement a Step Functions workflow to throttle downstream calls.

56. **How do you monitor and alert for failed message deliveries in SNS and SQS?**

* **SNS:** Monitor `NumberOfNotificationsFailed` and `NumberOfSMSFailed` CloudWatch metrics; set alarms. Use subscription DLQs.
* **SQS:** Monitor `ApproximateNumberOfMessagesVisible` for growing queues, `ApproximateNumberOfMessagesNotVisible` for in‑flight; set alarms on DLQ queue depth.

57. **How do you handle message replay in SQS?**

* Retain messages in a **replay** queue (a FIFO or Standard queue) by copy.
* Replay by re‑publishing messages to the original queue or triggering a Lambda that reprocesses the replay queue.

58. **What are some ways to reduce cost in a high‑throughput SQS + Lambda system?**

* **Batching:** Increase `batchSize` to process multiple messages per invocation.
* **Long polling:** Reduce empty receives.
* **Use reserved concurrency:** Prevent uncontrolled Lambda scaling.
* **Monitor and right‑size:** Adjust memory allocation to balance duration and cost.

59. **How do you ensure delivery to multiple microservices using SNS?**

* Subscribe each microservice’s endpoint (SQS queue or Lambda) to the SNS topic.
* Use **FilterPolicies** to send only relevant messages to each microservice.
* Monitor `NumberOfNotificationsDelivered` per subscription.

60. **Explain the end‑to‑end architecture for an event‑driven system using SNS, SQS, and Lambda.**
61. **Publishers** send events to an SNS topic.
62. **SNS** fans out to multiple SQS queues (one per consumer service).
63. **Lambda event source mappings** poll each queue and invoke the corresponding function.
64. **Functions** process messages, write results to databases or downstream services, and delete messages upon success.
65. **DLQs** capture unprocessable messages; CloudWatch metrics and alarms monitor queue depth, processing errors, and Lambda failures.
66. **IAM roles**, **encryption**, and **VPC endpoints** secure the entire pipeline.

---

**Pro Tips:**

* Emphasize **decoupling**, **resilience**, and **scalability** in your designs.
* Always discuss **error handling**, **monitoring**, and **security** aspects.
* Use **diagrams** to clarify event flows in whiteboard or virtual interviews.


