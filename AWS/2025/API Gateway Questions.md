## ✅ AWS API Gateway Interview Questions

#### 🔹 Fundamentals

1. **What is Amazon API Gateway?**
   Amazon API Gateway is a fully managed service for creating, publishing, securing, monitoring, and maintaining RESTful, HTTP, and WebSocket APIs at any scale. You define API operations (resources and methods), integrate them with backend endpoints (Lambda functions, HTTP services, other AWS services), and API Gateway handles request routing, authorization, throttling, monitoring, and versioning.

---

2. **What are the use cases for API Gateway?**

   * **Serverless backends:** Expose Lambda‑driven business logic over HTTP/S.
   * **Microservices front door:** Provide a unified façade for multiple microservices, hiding internal complexity.
   * **WebSocket APIs:** Build real‑time two‑way communication (chat apps, streaming dashboards).
   * **Third‑party integrations:** Proxy or transform external REST/HTTP APIs.
   * **SDK generation & throttling:** Automatically generate client SDKs (JavaScript, iOS, Android) and enforce usage plans for partners.

---

3. **What protocols are supported by API Gateway?**

   * **REST APIs:** Full OpenAPI/Swagger support, resource‑based URL paths.
   * **HTTP APIs:** Lower‑cost, lower‑latency option for standard HTTP routes (RESTful style).
   * **WebSocket APIs:** Persistent connections for two‑way, real‑time communication.

---

4. **Difference between HTTP API and REST API in API Gateway:**

   | Feature        | HTTP API                                | REST API                                                                                                    |
   | -------------- | --------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
   | Latency & Cost | Lower latency, lower cost               | Higher feature set, slightly higher cost                                                                    |
   | Features       | JWT/OIDC auth, CORS, route selection    | API keys, usage plans, request validation, Swagger import/export, AWS integration mappings, WAF integration |
   | Customizations | Limited mapping templates               | Full Velocity templates, response mapping, stage variables                                                  |
   | Ideal for      | Simple proxying & JWT‑secured endpoints | Complex API management needs                                                                                |

---

5. **What are integration types in API Gateway?**

   * **AWS Integration:** Direct integration with AWS service actions (e.g., invoke DynamoDB, SQS).
   * **Lambda Integration:** Invoke a Lambda function; choose “proxy” for minimal mapping or “custom” for request/response mapping.
   * **HTTP Integration:** Forward to any HTTP endpoint (public or private via VPC Link).
   * **Mock Integration:** Return a pre‑configured response without connecting to a backend (useful for tests or early Smithy stages).

---

6. **How does API Gateway route requests to Lambda, HTTP, or AWS services?**
   You configure for each resource‑method pair an **Integration Request** specifying:

   1. **Integration type** (AWS, Lambda, HTTP, Mock)
   2. **Endpoint URI** or AWS action
   3. **Mapping templates** (to transform incoming JSON/XML into the backend’s expected format)
      When a client calls the API, API Gateway matches the path+method, applies any request mappings, and dispatches to the configured integration.

---

7. **What is the purpose of a usage plan?**
   A usage plan links one or more API Stages to API keys. It defines:

   * **Request quotas** (e.g., 10 M requests per month)
   * **Rate limits** (e.g., 100 RPS burst, 50 steady RPS)
     Usage plans enable you to monetize, meter, and throttle partner API access.

---

8. **How do you configure throttling and rate limiting?**

   * **Account-level limits:** AWS sets default regional limits (e.g., 10,000 RPS).
   * **Stage-level throttling:** On each deployment stage, set a **Rate** (steady state RPS) and a **Burst** (peak concurrent requests).
   * **Usage plan throttling:** Per API key, override stage defaults with more granular rules.
     Configuration is in the API Gateway console under **Stages → Throttling** or **Usage Plans → Throttling**.

---

9. **What is a custom domain name in API Gateway?**
   A custom domain name (e.g., `api.example.com`) lets you present APIs under your corporate domain rather than the default `*.execute-api.amazonaws.com`. You:

   1. **Verify your certificate** in ACM (in us‑east‑1 for REST & HTTP APIs).
   2. **Associate** the custom domain to one or more API Gateway stages.
   3. **Point** your DNS (Route 53 or external) to the provided CloudFront distribution or API Gateway target.
---

10. **What is the maximum payload size in API Gateway?**

    * **REST APIs:** 10 MB request or response payload.
    * **HTTP APIs:** 2 MB request payload (response is also 2 MB).
      If you need larger payloads, use presigned S3 URLs or AWS App Runner.

---

#### 🔹 Security & Auth

11. **How do you secure an API with IAM, Lambda authorizers, or Cognito?**

    * **IAM roles & policies:** Use SigV4 on client calls; leverage IAM for fine‑grained access control.
    * **Lambda authorizer:** A custom Lambda (Token or Request type) that validates tokens or headers and returns an IAM policy.
    * **Amazon Cognito User Pools:** Use JWT tokens issued by User Pools; configure a Cognito authorizer in API Gateway to verify them automatically.

---

12. **What is a Lambda authorizer?**
    A Lambda authorizer is a custom authorization function you write. When a request arrives, API Gateway invokes your authorizer with the token or request context. Your function returns an IAM policy (Allow/Deny) and context data, and API Gateway enforces the policy before routing to the backend.

---

13. **How do you use API keys in API Gateway?**

    1. **Enable API Key Required** on selected methods.
    2. Create an **API Key** in the console (or via CLI).
    3. Associate the key with a **Usage Plan** that targets specific Stages.
    4. Clients send the key in the `x-api-key` header on each request.

---

14. **How do you configure CORS in API Gateway?**

    * **REST APIs:** Enable “Enable CORS” on individual methods or the entire resource; API Gateway adds an `OPTIONS` method, injects `Access-Control-Allow-Origin` headers, and configures mapping templates.
    * **HTTP APIs:** Under Settings → CORS, specify allowed origins, headers, methods, credentials. HTTP APIs auto‑generate the `OPTIONS` preflight responses.

---

15. **What is request validation?**
    Request validation ensures that incoming client data meets your schema before invoking the backend. You define:

    * **Models** (JSON schema for body).
    * **Required parameters** (query strings, headers, path).
      Enabling request validation rejects malformed requests (4XX) at the gateway, reducing malformed traffic to your services.

---

#### 🔹 Monitoring & Scaling

16. **How do you log API requests?**

    * **Execution logs:** Enable at the Stage level under **Logs/Tracing**; choose log level (INFO, ERROR) and include request/response data.
    * **Access logs:** Define a log format (JSON, CLF) and a destination CloudWatch Log group; API Gateway writes one line per request with client IP, latency, status, etc.

---

17. **How do you trace API execution with X‑Ray?**
    Enable **X‑Ray Tracing** on the API Stage. API Gateway emits trace segments to X‑Ray whenever it routes a request, including downstream calls to Lambda or HTTP integrations (if they’re also X‑Ray–instrumented).

---

18. **How does API Gateway scale under heavy traffic?**
    API Gateway is a fully managed, serverless service that auto‑scales horizontally. AWS maintains a fleet of stateless edge‑optimized proxies that route requests. You only need to ensure your backend (Lambda concurrency, HTTP endpoints) can scale accordingly.

---

19. **What is caching in API Gateway and how does it work?**
    You can enable response caching per Stage and per Method:

    * Allocate a **cache cluster** size (e.g., 0.5 GB–237 GB).
    * Specify **TTL** per route.
    * Cache key includes path, query strings, headers (configurable).
      When enabled, API Gateway returns cached responses directly, reducing backend load and latency.

---

20. **How do you handle versioning of APIs?**

    * **Stages:** Use separate Stages (e.g., `dev`, `test`, `prod`) for lifecycle management.
    * **Base Path Mappings:** Associate different custom domain base paths (e.g., `/v1`, `/v2`) to different API deployments.
    * **Stage Variables & Canary Releases:** Use stage variables for configuration overrides and gradual traffic shifting between versions.
