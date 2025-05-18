## ✅ **AWS Lambda & Serverless Architecture Interview Questions**

### 🔹 Fundamentals of AWS Lambda

1. **What is AWS Lambda?**
   AWS Lambda is a serverless compute service that runs your code in response to events and automatically manages the underlying compute resources. You upload functions (code + configuration), and Lambda handles scaling, patching, and high availability.

2. **What are the key benefits of using AWS Lambda?**

   * **No server management:** AWS handles infrastructure.
   * **Automatic scaling:** Concurrency scales with load, down to zero when idle.
   * **Pay-per-use:** You’re billed only for execution time (GB‑seconds) and invocation count.
   * **Integrated ecosystem:** Natively integrates with 200+ AWS services and custom event sources.

3. **How does Lambda pricing work?**

   * **Compute charges:** Billed per 1 ms of execution time, rounded up, based on the memory size you allocate (128 MB to 10 240 MB).
   * **Request charges:** \$0.20 per 1 M requests.
   * **Provisioned concurrency (optional):** You pay for the amount of concurrency you reserve plus execution.

4. **What is a cold start in AWS Lambda?**
   A cold start occurs when Lambda needs to provision a new execution environment to run your function—fetching code, initializing the runtime, and running initialization code. This adds latency (typically tens to hundreds of milliseconds).

5. **How is AWS Lambda different from EC2 or containers?**

   * **Lambda:** Event‑driven, ephemeral, no servers to manage, scales to zero.
   * **EC2/Containers:** You provision and manage servers/instances, pay for uptime regardless of utilization, handle capacity planning and patching.

6. **What is the maximum timeout for a Lambda function?**
   The maximum invocation timeout is **15 minutes** (900 seconds).

7. **What are the memory and runtime limits of a Lambda function?**

   * **Memory:** 128 MB to 10 240 MB, in 1 MB increments.
   * **Ephemeral storage (/tmp):** Up to 10 GB.
   * **Package size:** ZIP deployment up to 50 MB (compressed), 250 MB uncompressed including layers.
   * **Code execution runtime:** Up to 15 minutes per invocation.

8. **What languages are supported by AWS Lambda?**
   Officially supported runtimes: Node.js, Python, Java, Go, Ruby, .NET (C#), and Custom Runtimes via the Lambda Runtime API (any language).

9. **How do you monitor a Lambda function's performance?**

   * **CloudWatch Metrics:** Invocations, duration, errors, throttles, iterator age (for streams).
   * **CloudWatch Logs:** Enable detailed logging in your code.
   * **X‑Ray Tracing:** For end‑to‑end distributed tracing and performance analysis.
   * **Lambda Insights:** Deep insights into memory, CPU, and resource usage.

10. **What is the difference between synchronous and asynchronous invocation in Lambda?**

    * **Synchronous:** Caller waits for the function to complete and receives the response or error immediately (e.g., API Gateway trigger).
    * **Asynchronous:** AWS queues the event and returns a 202 status immediately; Lambda retries on failure (up to two retries) or sends failures to a Dead Letter Queue or on‑failure destination.

---

### 🔹 Design & Implementation

11. **How do you trigger a Lambda function?**
    Lambda can be triggered by: API Gateway, S3 events, DynamoDB Streams, Kinesis Data Streams, SQS, CloudWatch Events (EventBridge), Step Functions, Cognito, Alexa Skills, and custom applications via the SDK.

12. **What are Lambda event sources?**

    * **Push model (asynchronous):** Services push events to Lambda (e.g., S3, SNS, EventBridge).
    * **Pull model (streams):** Lambda polls streams or queues (e.g., Kinesis, DynamoDB Streams, SQS FIFO).

13. **How do you pass data to a Lambda function?**
    The invoking service serializes event data into a JSON payload, which is provided to your handler as the `event` parameter. You can also pass custom input via the SDK or Step Functions.

14. **What is the execution role for a Lambda function?**
    An IAM role that Lambda assumes when executing your code. It grants permissions your function needs (e.g., DynamoDB read/write, S3 access). Always follow least‑privilege—grant only required actions.

15. **How do you deploy a Lambda function?**

    * **Console:** ZIP or inline editor upload.
    * **CLI:** `aws lambda update-function-code --function-name MyFunc --zip-file fileb://func.zip`.
    * **IaC:** CloudFormation, SAM (`sam deploy`), Serverless Framework, or CDK (`cdk deploy`).
    * **CI/CD:** Integrate with CodePipeline/CodeBuild or GitHub Actions for automated packaging and deployment.

16. **What are Lambda layers and why are they used?**
    Layers are ZIP archives containing libraries, runtime dependencies, or custom runtimes that you can attach to multiple functions. They help share common code (e.g., utility modules) while keeping deployment packages small.

17. **How do you manage dependencies in a Lambda function?**

    * **Package dependencies** in your deployment bundle (e.g., `node_modules`, `vendor` directories).
    * **Use layers** for shared libraries.
    * **Container images:** Build a Docker image including OS libraries and dependencies, up to 10 GB.

18. **What are environment variables in Lambda and how are they used?**
    Key‑value pairs you configure on your function for configuration settings (DB endpoints, feature flags). They’re encrypted at rest (optionally with KMS) and injected into the runtime as environment variables.

19. **How do you version and alias Lambda functions?**

    * **Publish a version:** `aws lambda publish-version --function-name MyFunc`. This creates an immutable snapshot.
    * **Aliases:** Named pointers to versions (e.g., `dev`, `prod`). You can shift traffic gradually between versions by changing alias routing configuration (traffic splitting).

20. **How do you test Lambda functions locally?**

    * **AWS SAM CLI:** `sam local invoke` with event payloads.
    * **Serverless Framework:** `sls invoke local`.
    * **Docker containers:** Use the AWS Lambda container image for local testing.
    * **Unit tests:** Mock AWS services via libraries (e.g., moto for Python, aws-sdk-mock for Node.js).

---

### 🔹 Integration with Other AWS Services

21. **How does Lambda work with API Gateway?**
    API Gateway acts as a “front door” for HTTP(S) requests. You:

    1. Define REST or HTTP API routes in API Gateway.
    2. Configure each route’s integration to invoke a specific Lambda function (synchronous).
    3. API Gateway transforms incoming requests into the `event` payload for your handler.
    4. Your function returns a JSON response, which API Gateway serializes into HTTP responses (status code, headers, body).

22. **How do you use Lambda with S3?**
    Configure an S3 bucket notification to invoke Lambda on object-level events (PUT, POST, DELETE). S3 pushes an event record containing bucket name, object key, size, etc. Your function can process or transform the file (e.g., generate thumbnails, index metadata).

23. **How do you trigger Lambda using CloudWatch Events?**

    * **EventBridge rule** (formerly CloudWatch Events): define a schedule (cron/rate) or pattern (e.g., EC2 state changes).
    * Set the rule’s target to your Lambda function.
    * When the rule matches, EventBridge invokes the function with the event payload.

24. **Can a Lambda function be triggered by DynamoDB Streams?**
    Yes. Configure your DynamoDB table to enable Streams. Then, in the Lambda console (or via IaC), add a DynamoDB stream event source mapping. Lambda will poll the stream and invoke your function with batches of record modifications (INSERT, MODIFY, REMOVE).

25. **How do you use Lambda to process messages from an SQS queue?**
    Create an SQS queue, then configure a Lambda event source mapping for that queue. Lambda will invoke your function with batches of messages, handling visibility timeouts and batch sizes. On success, messages are deleted; on failure, messages retry or go to a DLQ.

26. **What is the role of EventBridge with Lambda?**
    EventBridge provides a flexible event bus for decoupled, event-driven architectures. You can publish custom events or use AWS service events. EventBridge rules filter and route events to targets, including Lambda functions, enabling fan‑out and complex routing logic without polling.

27. **How does Lambda integrate with Step Functions?**
    Step Functions orchestrate multiple steps (tasks) in a workflow using state machines. Lambda functions are a primary task type. You:

    * Define a state machine JSON/YAML with `Task` states invoking specific Lambdas.
    * Step Functions manage retries, parallelism, error handling, and pass outputs from one function to the next.

28. **How do you use Lambda to update an RDS or Aurora database?**

    * **VPC connectivity:** Place your function in the same VPC/subnets as the database.
    * **Credential management:** Retrieve DB credentials securely (Secrets Manager or SSM Parameter Store) within the function.
    * Use your language’s database client (e.g., `pg` for PostgreSQL) to open a connection, execute SQL queries, and close connections (or use a connection pooler like RDS Proxy).

29. **How do you connect Lambda to a VPC and why?**
    Assign your function to one or more VPC subnets and security groups. This enables access to resources inside private networks (e.g., RDS, ElastiCache) and ensures network isolation. Note: VPC cold‑starts can be higher due to ENI initialization.

30. **How does Lambda work with Cognito?**

    * **Pre/Post Authentication Triggers:** Run custom logic during sign‑in or sign‑up flows.
    * **User Pool Triggers:** Validate or modify attributes, send custom messages (e.g., SMS), or auto‑confirm users.
    * **Authorizers:** Use Cognito User Pool JWT tokens with API Gateway to authorize Lambda‑backed APIs.

---

### 🔹 Security

31. **How do you secure a Lambda function?**

    * **Least‑privilege IAM role:** Grant only required permissions to the function’s execution role.
    * **VPC placement:** Restrict network access via security groups.
    * **Encrypt environment variables:** Use KMS–encrypted variables for secrets.
    * **Function policies:** Use resource‑based policies to restrict which principals can invoke your function.

32. **What IAM permissions are required for Lambda to access other AWS services?**
    The function’s execution role needs specific action permissions. For example, to read from S3 and write to DynamoDB:

    ```json
    {
      "Effect": "Allow",
      "Action": [
        "s3:GetObject",
        "dynamodb:PutItem",
        "dynamodb:GetItem"
      ],
      "Resource": [
        "arn:aws:s3:::my-bucket/*",
        "arn:aws:dynamodb:us-east-1:123456789012:table/my-table"
      ]
    }
    ```

33. **How do you use AWS Secrets Manager or SSM Parameter Store in Lambda?**

    * **Grant permissions** (`secretsmanager:GetSecretValue`, or `ssm:GetParameter`).
    * **Fetch at runtime** using the AWS SDK in your handler’s initialization code.
    * **Cache** the secret outside the handler if multiple invocations share the same environment to minimize API calls.

34. **How do you protect sensitive environment variables?**

    * In the Lambda console or IaC, mark variables as **“Encrypt environment variables”** (KMS).
    * Use a dedicated KMS key with a restrictive key policy.
    * Avoid logging environment variables or spilling them into error messages.

35. **What is the principle of least privilege in Lambda?**
    Grant only the minimal set of permissions that your function needs to perform its work. Avoid umbrella policies (e.g., `*`), regularly audit roles, and rotate secrets to reduce blast radius.

---

### 🔹 Best Practices

36. **What are the best practices for managing cold starts?**

    * **Provisioned Concurrency:** Keep a pool of pre‑initialized environments.
    * **Keep initialization code minimal:** Defer heavy imports or SDK clients until inside the handler.
    * **Use lighter runtimes:** Choose Node.js, Python, or Go over heavier languages.

37. **How do you structure a monolithic vs micro Lambda application?**

    * **Monolithic:** One Lambda with multiple handlers or a router (e.g., using Express in Node.js). Simpler deployments but larger deployment package.
    * **Micro:** One function per responsibility. Smaller packages, independent scaling, isolated failures, but more operational artifacts to manage.

38. **What are best practices for error handling in Lambda?**

    * **Graceful retries:** For idempotent operations, let AWS retry asynchronously.
    * **Dead Letter Queues (DLQ):** Configure SQS/SNS DLQs for asynchronous invocations.
    * **Catch exceptions:** Return structured errors to synchronous callers; log stack traces to CloudWatch Logs.
    * **Use Try/Catch/Fallback:** Provide fallback logic or safe defaults.

39. **How do you log and trace Lambda invocations?**

    * **CloudWatch Logs:** Use structured (JSON) logging for easier querying.
    * **AWS X‑Ray:** Enable active tracing to capture end‑to‑end request flows across services.
    * **Correlation IDs:** Pass a request ID or custom trace ID through events and logs.

40. **How do you handle retries in asynchronous invocations?**

    * AWS automatically retries twice on failures, with delays.
    * **Customize retry behavior:** Use Function Dead Letter Queues or Destination Configurations (Successful/Failed destinations) to route events to SQS, SNS, or another Lambda for manual processing.

41. **How do you ensure idempotency in Lambda executions?**

    * **Idempotency tokens:** Pass a unique token in the event and store processed tokens (e.g., in DynamoDB) to skip duplicates.
    * **De-duplication at source:** Use SQS FIFO queues with deduplication IDs.
    * **Stateless design:** Design handlers so reprocessing the same event has no side effects.

42. **What is the recommended way to handle large dependencies in Lambda?**

    * **Lambda Layers:** Package shared libraries in layers to avoid exceeding deployment size limits.
    * **Container images:** Bundle up to 10 GB of dependencies in a Docker image stored in ECR.
    * **Tree‑shaking & bundling:** Use tools like Webpack or esbuild to include only needed code.

43. **How do you use Lambda Destinations?**
    Configure `onSuccess` and `onFailure` destinations (SNS, SQS, EventBridge, or another Lambda). After an asynchronous invocation, Lambda publishes the full event and response or error to the specified destination, enabling decoupled post‑processing or alerting.

---

Here are professional, interview‑ready answers for AWS Lambda observability and broader serverless architecture concepts. Tailor your examples to your experience and the role’s focus.

---

### 🔹 Observability & Monitoring

44. **How do you monitor a Lambda function using CloudWatch?**

* **Metrics Dashboard:** In the CloudWatch console, view built‑in metrics for your Lambda function.
* **Alarms:** Create alarms on error count, duration, throttle count, or iterator age.
* **Custom Metrics:** Publish business or application metrics from your function via the CloudWatch SDK.

45. **What metrics are emitted by AWS Lambda?**

* **Invocations:** Number of times your function is invoked.
* **Duration:** Execution time in milliseconds.
* **Errors:** Count of failed invocations.
* **Throttles:** Number of invocation requests rejected due to concurrency limits.
* **IteratorAge:** Age of the last record for stream‑based invocations (Kinesis/DynamoDB).
* **ConcurrentExecutions & UnreservedConcurrentExecutions:** Current concurrency usage and available capacity.

46. **How do you use AWS X‑Ray with Lambda?**

* **Enable Tracing:** Turn on active tracing in function configuration.
* **Instrument Code:** Import the X‑Ray SDK in supported languages to add custom annotations and subsegments.
* **View Traces:** In the X‑Ray console, analyze the service map, latency breakdowns, and error hotspots.

47. **How do you capture logs for a Lambda function?**

* **CloudWatch Logs:** Lambda automatically streams `stdout`/`stderr` to CloudWatch Logs under the `/aws/lambda/<function‑name>` group.
* **Structured Logging:** Use JSON or key‑value pairs for easy parsing.
* **Log Retention & Insights:** Set retention policies and query logs with CloudWatch Logs Insights.

48. **How do you detect and handle function timeouts?**

* **Detect:** CloudWatch metric “Duration” will hit the configured timeout, and a “Task timed out” error appears in logs.
* **Handle:**

  1. Increase the timeout if the workload legitimately needs more time.
  2. Break the task into smaller, stateful steps using Step Functions.
  3. Use idempotent retries or DLQs to capture timed‑out events for later processing.

---

### 🔹 Serverless Architecture Concepts

49. **What is serverless architecture?**
    A model where the cloud provider fully manages compute resources—provisioning, scaling, and maintenance—so developers focus solely on application code and business logic. Billing is granular (per execution or resource use).

50. **What are the advantages and disadvantages of serverless?**

* **Advantages:**

  * No server management or patching
  * Automatic, granular scaling
  * Cost‑efficient pay‑per‑use
  * Rapid development with managed integrations
* **Disadvantages:**

  * Cold‑start latency
  * Limited execution duration and resources
  * Vendor lock‑in
  * More complex local testing and debugging

51. **What is the difference between serverless and container‑based microservices?**

* **Serverless:** Event‑driven, ephemeral functions with per‑invocation billing, no OS or container management.
* **Containers:** Long‑running processes you package into images, deployed on orchestrators (ECS/EKS), with more control over runtime but more operational overhead.

52. **When should you NOT use serverless architecture?**

* Low‑latency, high‑throughput workloads where cold starts are unacceptable.
* Long‑running processes that exceed 15 minutes.
* Applications requiring consistent, dedicated compute (e.g., HPC or real‑time gaming servers).
* Strict compliance requiring full control over the OS or network stack.

53. **How do you design a scalable serverless application?**

* **Event‑driven patterns:** Use queues, streams, and pub/sub to decouple components.
* **Stateless functions:** Store state externally (DynamoDB, S3).
* **Granular functions:** One responsibility per function for independent scaling.
* **Caching and batching:** Use API Gateway caching, DynamoDB DAX, or batch jobs for peak loads.

54. **What is the role of API Gateway in a serverless app?**

* Acts as the secure, scalable HTTP(S) front door.
* Handles request validation, throttling, authorization (Cognito/IAM/Lambda authorizers), and transforms.
* Integrates natively with Lambda and other AWS services.

55. **How does a serverless architecture impact CI/CD?**

* **Infrastructure as Code:** Templates (SAM, CDK) or serverless frameworks define resources.
* **Automated Tests:** Include unit tests for functions and integration tests against deployed stacks.
* **Blue/Green or Canary Deployments:** Use deployment preferences in SAM or traffic‑shifting aliases to minimize risk.
* **Artifact Management:** Package each function or service as a separate deployable unit.

56. **What is the Serverless Application Model (SAM)?**
    An open‑source framework on top of CloudFormation that provides shorthand syntax for defining serverless resources (`AWS::Serverless::Function`, `Api`, `SimpleTable`), plus a CLI for local testing (`sam local`), debugging, and guided deployments.

57. **What are CloudFormation and SAM/Serverless Framework differences?**

* **CloudFormation:** General-purpose IaC with full AWS coverage, but verbose for serverless patterns.
* **SAM:** Extension of CFN with serverless-specific abstractions, CLI tooling for local emulation.
* **Serverless Framework:** Third-party, multi-cloud framework using YAML, with plugins and community extensions—less native than SAM but more flexible across providers.

58. **What is the Serverless Framework and why is it popular?**
    A community-driven, multi-cloud framework that uses a simple YAML syntax to declare functions, events, and resources. It’s popular for its plugin ecosystem, provider-agnostic design, and powerful CLI for deploying and managing serverless apps.

59. **How do you use Terraform to manage Lambda infrastructure?**

* Define AWS Lambda resources (`aws_lambda_function`, `aws_lambda_layer_version`) and triggers (`aws_lambda_event_source_mapping`, `aws_api_gateway_integration`) in Terraform HCL.
* Manage versions, aliases, IAM roles, and environment variables declaratively alongside other cloud resources.
* Use workspaces or directory structures to separate environments.

60. **How do you test serverless applications?**

* **Unit Tests:** Mock AWS services (moto for Python, aws-sdk-mock for Node.js).
* **Local Emulation:** SAM CLI (`sam local invoke`), Serverless Offline plugin.
* **Integration Tests:** Deploy to a test environment and run end‑to‑end tests against real services.
* **Contract Tests:** Validate event schemas and API contracts before deployment.


---

Here are professional, interview‑ready answers for scenario‑based serverless questions 61–70. Tailor them with examples from your own experience.

---

### 🔹 Real‑World Scenario‑Based Questions

61. **How would you build a serverless file processing pipeline with S3 and Lambda?**

    1. Configure an S3 bucket with an **ObjectCreated** event notification to invoke a Lambda function.
    2. In the Lambda handler, fetch the uploaded file via the S3 SDK, process or transform it (e.g., image thumbnail generation, CSV parsing), and write results to another S3 bucket or downstream store (DynamoDB, RDS).
    3. Use SNS or EventBridge to notify downstream systems of completion or errors.
    4. Secure the pipeline by granting the Lambda execution role least‑privilege S3 permissions and enabling encryption at rest.

62. **How do you design a serverless REST API?**

    1. **API Gateway** as the HTTP front door, defining resources and methods.
    2. Integrate routes to individual **Lambda** functions (one per CRUD operation) for clear separation of concerns.
    3. Use **Cognito** or Lambda authorizers for authentication/authorization.
    4. Model data in **DynamoDB** (for scale) or RDS (for relational needs).
    5. Implement **input validation** (request models) in API Gateway or in-Lambda.
    6. Enable **CORS**, **throttling**, and **stages** (dev/prod) with usage plans.

63. **How would you build a cron‑like job using Lambda?**

    1. Create an **EventBridge (CloudWatch Events)** rule with a **cron** or **rate** expression (e.g., `cron(0 6 * * ? *)` for daily runs).
    2. Set the rule’s target to a Lambda function that contains the scheduled job logic.
    3. Use environment variables or parameters to configure schedules or payloads.
    4. Monitor failures with CloudWatch Alarms and capture failed events with a DLQ or Lambda Destination.

64. **How do you batch process events from DynamoDB Streams using Lambda?**

    1. Enable **DynamoDB Streams** on the table with an appropriate view type (NEW\_IMAGE/OLD\_IMAGE).
    2. Configure a **Lambda event source mapping** with batch size (e.g., 100), parallelization factor, and retry behavior.
    3. In the handler, loop through the batch of records, process each change (INSERT/MODIFY/REMOVE), and checkpoint automatically on success.
    4. Handle partial failures by throwing an error to retry or route to a DLQ for manual inspection.

65. **How would you migrate a monolith to a serverless architecture?**

    1. **Assess & modularize:** Identify modules or domains (authentication, billing, reporting).
    2. **Extract APIs:** Move a single module at a time behind API Gateway + Lambda.
    3. **Data layer refactor:** Migrate storage to DynamoDB, S3, or partition an RDS database per service.
    4. **Messaging:** Introduce EventBridge or SQS for inter‑module communication.
    5. **Iterate:** Test each cut‑over, monitor performance and cost, and refactor the next module.

66. **How do you design a serverless pub/sub architecture?**

    1. Use **SNS** topics for fan‑out of events.
    2. Subscribe **Lambda** functions, SQS queues, or HTTP endpoints as subscribers.
    3. For durable retries, front each Lambda with an SQS DLQ or use a subscription filter policy.
    4. Secure topics with IAM policies, VPC endpoints, and encryption.
    5. Monitor delivery success/failure metrics and set alarms on `NumberOfNotificationsFailed`.

67. **How do you implement authentication and authorization in a serverless app?**

    * **Authentication:** Use **Amazon Cognito User Pools** for user sign‑up/sign‑in and JWT issuance.
    * **API Authorization:** Configure a **Cognito authorizer** or **Lambda authorizer** in API Gateway to validate JWTs.
    * **Fine‑grained access:** Leverage IAM roles with context-based policies (e.g., `cognito:username`) or embed user claims to enforce resource‑level permissions in your Lambda code.

68. **How do you implement blue/green deployment for Lambda?**

    1. Publish a new **version** of your Lambda function.
    2. Create or update an **alias** (e.g., `prod`) that initially points to the old version.
    3. Use **traffic shifting** on the alias to gradually route a percentage (e.g., 10%, 50%) of requests to the new version.
    4. Monitor errors and latency; if stable, shift 100% traffic and optionally delete the old version.

69. **How do you debug performance issues in Lambda?**

    1. Enable **X‑Ray** tracing and analyze the service map for latency hotspots.
    2. Review **CloudWatch Logs** for function duration, memory usage, and error stack traces.
    3. Check **configuration** (memory size, timeout) and use increased memory to improve CPU and network throughput.
    4. Profile initialization code by logging timestamps around imports or heavy operations.
    5. If VPC‑related latency, use **Hyperplane ENIs** or lighter VPC configurations.

70. **How do you manage secrets and credentials in a production Lambda function?**

    1. Store secrets in **AWS Secrets Manager** or **SSM Parameter Store** (SecureString).
    2. Grant the function’s execution role **least‑privilege** access to retrieve only the necessary secrets.
    3. Retrieve secrets at cold‑start and cache the results in memory to minimize API calls.
    4. Rotate secrets automatically via Secrets Manager and handle rotation logic in Lambda or via built‑in rotation functions.
    5. Encrypt any sensitive environment variables with a dedicated **KMS key** and restrict decryption to the function’s role.



