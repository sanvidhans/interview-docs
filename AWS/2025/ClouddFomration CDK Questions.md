## ✅ AWS CloudFormation & CDK Interview Questions


#### 🔹 CloudFormation Basics

1. **What is AWS CloudFormation?**
   A fully managed IaC (Infrastructure as Code) service that lets you model, provision, and manage AWS and third‑party resources by writing declarative templates. It automates provisioning, updates, and deletion of entire environments in a safe, repeatable way.
---
2. **What are the main benefits of using CloudFormation?**

   * **Repeatability & Consistency:** Spin up identical environments (dev/test/prod) from the same template.
   * **Version Control:** Store templates in Git to track changes.
   * **Change Management:** Preview changes with ChangeSets before applying.
   * **Drift Detection:** Identify out–of–band changes.
   * **Automation & Orchestration:** Manage dependencies and parallel resource provisioning.
---
3. **What are stacks and how do they work in CloudFormation?**
   A *stack* is a running instance of a template. When you create a stack, CloudFormation provisions resources defined in the template. You update or delete the stack to modify or tear down all associated resources as a single unit.

---
4. **What is a CloudFormation template?**
   A text file (YAML or JSON) that declaratively defines AWS resources, their properties, and relationships. It can include parameters, mappings, conditions, transforms, resources, and outputs.

---

5. **What formats are supported for templates?**

   * **YAML:** Preferable for readability and support of comments.
   * **JSON:** Legacy format, more verbose, but fully supported.
---

6. **What is the difference between a template and a stack?**

   * **Template:** A declarative blueprint.
   * **Stack:** A live collection of AWS resources provisioned from that blueprint.
---

7. **What is a stack set in CloudFormation?**
   A StackSet lets you deploy a single template across multiple AWS accounts and Regions in one operation. You define an administration account and grant permission to target accounts.
---

8. **How does CloudFormation handle resource creation order?**
   It uses *implicit* and *explicit* dependencies:

   * **Implicit:** Based on references (e.g. if Resource A references Resource B, B is created first).
   * **Explicit:** The `DependsOn` attribute forces order when references alone aren’t sufficient.

---

9. **What is a nested stack and when should you use it?**
   A nested stack is a child stack defined via the `AWS::CloudFormation::Stack` resource inside a parent template. Use it to modularize large templates, share common patterns, or break up logical components (networking, compute, security) for reuse and maintainability.
---

10. **What is drift detection in CloudFormation?**
    Drift detection compares the actual, live configuration of stack resources against the template’s declared configuration. It reports which resources have drifted (i.e., been changed outside of CloudFormation) so you can remediate or update your templates.

---

#### 🔹 Template Components

11. **What are the main sections of a CloudFormation template?**

    * **AWSTemplateFormatVersion (optional):** Template version.
    * **Description (optional):** Human‑readable summary.
    * **Metadata (optional):** Arbitrary JSON/YAML data.
    * **Parameters:** User inputs at stack creation.
    * **Mappings:** Static, fixed key–value lookup tables.
    * **Conditions:** Logical rules to control resource creation.
    * **Transform:** Macro declarations (e.g., `AWS::Serverless-2016-10-31`).
    * **Resources (required):** The AWS entities to provision.
    * **Outputs (optional):** Return values after provisioning.

12. **What are parameters in a CloudFormation template?**
    Placeholders for values you supply at stack creation time. They enable templates to be customized without editing the template itself (e.g., instance type, CIDR block, AMI ID).

13. **What are resources in a CloudFormation template?**
    The core section where you declare every AWS service object (EC2 instances, VPCs, S3 buckets, IAM roles, etc.). Each resource has a logical name and a type (e.g., `AWS::EC2::Instance`) plus a set of properties.

14. **How do you define outputs in CloudFormation?**
    Under the `Outputs` section, you give each output a name, a value (which can use intrinsic functions or references), and an optional description and export name. Outputs let you share values (like VPC IDs) with other stacks or simply display them post‑deployment.

15. **What are mappings and conditions in templates?**

    * **Mappings:** Static lookup tables mapping keys to values (e.g., region → AMI ID).
    * **Conditions:** Boolean expressions (using `Fn::If`, `Fn::Equals`, etc.) that control whether resources or outputs are created or assigned.

16. **What is a transform in CloudFormation?**
    A directive that instructs CloudFormation to process the template with a macro. The most common is the AWS SAM transform (`AWS::Serverless-2016-10-31`), which expands SAM shorthand into full resource definitions.

17. **How do you use AWS::Include and AWS::Serverless macros?**

    * **`AWS::Include`:** Embeds external snippets stored in S3 into your template (via a `Fn::Transform`). Useful for sharing common parameter or mapping fragments.
    * **SAM (`AWS::Serverless`) macro:** Allows use of higher‑level resources (like `AWS::Serverless::Function`, `AWS::Serverless::Api`) that the SAM macro expands into standard CloudFormation resources.

18. **What is an intrinsic function in CloudFormation?**
    Built‑in functions (prefixed `Fn::` or short YAML form) that let you reference parameters, other resources, perform string substitutions, joins, selects, and more at template parse time (e.g., `Fn::Join`, `Fn::GetAtt`, `Ref`).

19. **How do you use `Fn::GetAtt` and `Fn::Sub`?**

    * **`Fn::GetAtt`:** Retrieves an attribute value from a resource (`Fn::GetAtt: [MyBucket, Arn]`).
    * **`Fn::Sub`:** Performs string interpolation, substituting `${LogicalName}` or `${AWS::Region}` syntax into a string (e.g., `"arn:aws:s3:::${MyBucket}"`).

20. **How do you define dependencies between resources?**

    * **Implicit** via references (`Ref` or `Fn::GetAtt`).
    * **Explicit** with the `DependsOn` attribute when you need to guarantee ordering but there’s no direct reference.

---

#### 🔹 Stack Operations

21. **How do you create and update stacks?**

    * **Console / CLI / SDK:**

      * **Create:** `aws cloudformation create-stack --stack-name MyStack --template-body file://template.yaml [--parameters …]`
      * **Update:** `aws cloudformation update-stack --stack-name MyStack --template-body file://template.yaml [--parameters …]`
    * **Infrastructure as Code:** embed these commands in CI/CD pipelines (e.g. CodePipeline, GitHub Actions).
    * **CDK:** `cdk deploy MyStack` (synthesizes & applies changes).

22. **What is a change set in CloudFormation?**
    A Change Set is a preview of proposed modifications to a stack. When you submit changes (new template or parameter overrides), CloudFormation generates a Change Set listing each resource it will add, modify, or remove—letting you inspect and confirm before execution.

23. **How does CloudFormation handle failed stack creation?**
    By default, CloudFormation performs an automatic rollback: any resources that were successfully created before the failure are deleted, and the stack ends up in the `ROLLBACK_COMPLETE` state. You can disable automatic rollback to inspect partially created resources.

24. **How do you rollback a failed stack update?**

    * **Automatic rollback:** on update failure, CloudFormation reverts to the last known good state.
    * **Manual:** if automatic rollback is disabled, use

      ```
      aws cloudformation continue-update-rollback --stack-name MyStack
      ```

      to resume rollback and clean up.

25. **What are stack policies and how are they used?**
    A Stack Policy is a JSON document attached to a stack that restricts what updates can occur on specified resources. You “lock down” critical resources (e.g., databases) by denying `Update` operations on their logical IDs, preventing accidental replacement or deletion during updates.

26. **What is the difference between Replace and Update in CloudFormation?**

    * **Update (in-place):** modifies properties of existing resources without replacement.
    * **Replace:** for certain property or type changes, CloudFormation must delete the old resource and create a new one. You’ll see “Replacement” in the Change Set and possibly a resource-swapping process.

27. **What happens when you delete a stack?**
    CloudFormation deletes every resource defined in the stack (in dependency order) and then removes the stack record. Any resources created outside the stack (or with `Retain` DeletionPolicy) remain untouched.

28. **How do you automate CloudFormation deployments?**

    * **CI/CD pipelines:** AWS CodePipeline + CodeBuild, Jenkins, GitHub Actions
    * **Automated CLI/SDK calls:** `create-stack` / `update-stack` or CloudFormation Change Sets in scripts
    * **CDK Pipelines:** high‑level construct that integrates with CodePipeline for automatic whenever you push commits

29. **What is termination protection in CloudFormation?**
    A safety feature you enable on a stack to prevent accidental deletion. Any `delete-stack` call fails until you explicitly disable termination protection.

30. **How do you validate a CloudFormation template before deployment?**

    * **AWS CLI:** `aws cloudformation validate-template --template-body file://template.yaml`
    * **cfn-lint:** a community tool that checks for syntax errors, best practices, and unsupported features.
    * **Dry‑run Changeset:** create a Change Set without executing it to surface errors in resource definitions or parameters.

---

## AWS CDK (Cloud Development Kit)

31. **What is AWS CDK?**
    The AWS Cloud Development Kit is an open‑source framework that enables you to define cloud infrastructure using familiar programming languages. Your code compiles (“synthesizes”) into standard CloudFormation templates.

32. **How does CDK differ from CloudFormation?**

    * **Imperative / Typed code:** use variables, loops, conditionals, and IDE tooling.
    * **Higher‑level abstractions:** constructs that encapsulate complex patterns.
    * **Synth step:** CDK code → synthesized CFN template → deployed by CloudFormation.

33. **What languages are supported by AWS CDK?**
    TypeScript, JavaScript, Python, Java, C#, and (as of CDK v2) Go.

34. **What is a CDK App, Stack, and Construct?**

    * **App:** the root CLI entry point that synthesizes one or more Stacks.
    * **Stack:** a unit of deployment (maps 1:1 to a CloudFormation stack).
    * **Construct:** a reusable building block; can be:

      * **L1 (Cfn…)** – low‑level CFN resource
      * **L2** – richer, AWS‑idiomatic abstractions
      * **L3 (Patterns)** – opinionated, multi‑resource architectures

35. **How does CDK synthesize to CloudFormation?**
    When you run `cdk synth` (or `cdk deploy`), the CDK runtime walks the construct tree, emits a CloudAssembly (JSON assets + metadata), and writes out a CloudFormation template under the `cdk.out` directory.

36. **What are L1, L2, and L3 constructs in CDK?**

    * **L1:** Direct, one‑to‑one representations of CFN resources (`CfnBucket`, etc.).
    * **L2:** Higher‑level wrappers with sensible defaults and rich APIs (e.g., `Bucket`).
    * **L3 (Patterns):** Prebuilt architectural patterns (e.g., `ApplicationLoadBalancedFargateService`) that wire together multiple L2s.

37. **What is the purpose of `cdk.json`?**
    It’s the CDK project configuration file. It defines:

    * **Entry point** (e.g., `app` script)
    * **Context values** (environment lookups, feature flags)
    * **CLI defaults** (region, account)

38. **How do you define environment‑specific resources in CDK?**

    * **Per‑Stack `env` property:** supply `{ account, region }` when instantiating a Stack.
    * **Context + Conditions:** read `app.node.tryGetContext('env')` and apply `if` logic.
    * **Multiple stacks:** each targeting different accounts/regions with configuration passed as parameters or context.

39. **What is the CDK context and how is it used?**
    A key–value store (in `cdk.json` or passed via `--context`/`-c`) for lookups (e.g., VPC IDs), feature toggles, or environment metadata. The CDK runtime uses context to cache AWS lookups and drive conditional logic.

40. **What is CDK bootstrap and why is it required?**
    CDK Bootstrap provisions the resources CloudFormation needs to deploy assets (an S3 bucket for Lambda code, an ECR repo for Docker images, IAM roles). You run `cdk bootstrap` once per environment (account/region) before deploying any stack that uses assets.


---

#### 🔹 CDK Deployment & Operations

41. **How do you deploy a CDK stack?**
    Run `cdk deploy [StackName]`. CDK synthesizes the CloudFormation template, uploads any assets (Lambda code, Docker images) to the bootstrap bucket, and invokes CloudFormation to create/update the stack.

42. **How do you destroy a CDK stack?**
    Use `cdk destroy [StackName]`. CDK will call CloudFormation’s `DeleteStack` API to tear down all resources, respecting any `RemovalPolicy` you’ve set (e.g., `RETAIN` vs. `DESTROY`).

43. **What is `cdk diff` and how is it useful?**
    `cdk diff [StackName]` compares your current CDK code’s synthesized template against the deployed stack’s live template. It highlights which resources will be added, changed, or removed—helpful for catching unintended changes before deploying.

44. **How do you share and reuse CDK constructs?**

* **Local libraries:** Extract common constructs into separate packages (e.g., an internal `@myorg/cdk-constructs` repo).
* **Publish to NPM/PyPI:** Version and distribute your constructs as modules, so other teams can import them.
* **CDK Patterns:** Contribute or use community patterns (e.g., AWS Solutions Constructs).

45. **How do you use environment variables with CDK?**
    Read from `process.env` (Node) or `os.environ` (Python) in your CDK app. You can also pass context via `cdk.json` or the CLI (`-c key=value`) and read with `app.node.tryGetContext('key')`.

46. **How do you import existing resources into CDK?**
    Use the static “from” methods on L2 constructs (e.g., `Bucket.fromBucketName()`, `Vpc.fromLookup()`) or L1 constructs with `CfnResource` and explicit ARN/ID properties. This lets CDK reference resources you didn’t create in code.

47. **Difference between CDK’s `addDependency` and CloudFormation `DependsOn`:**

* **`addDependency`** (Construct level): Enforces a creation order between two CDK stacks or constructs.
* **`DependsOn`** (Resource level): A CloudFormation resource property that ensures one logical resource isn’t created until another is fully provisioned.

48. **How do you manage secrets and parameters securely in CDK?**

* **Secrets Manager / Parameter Store:** Use `Secret.fromSecretNameV2()` or `StringParameter.fromStringParameterName()` to reference secrets at deploy time.
* **Context exclusion:** Don’t hard‑code secrets in code or `cdk.json`.
* **KMS encryption:** For any parameters you must store, enable encryption.

49. **How do you debug CDK apps?**

* **Verbose logging:** Run with `CDK_DEBUG=1` or `--verbose`.
* **Inspect synth output:** Check the CloudFormation template under `cdk.out`.
* **Unit tests for constructs:** Validate your construct logic before synth.
* **Breakpoints/IDE:** In TypeScript/Python, set breakpoints in your app code and run `cdk synth` within the debugger.

50. **How do you write unit tests for CDK stacks?**

* **Assertion libraries:** Use `@aws-cdk/assert` (v1) or `assertions` module (v2) in Jest (JavaScript/TypeScript) or pytest (Python).
* **Snapshot tests:** Compare synthesized templates against stored snapshots.
* **Resource‑level assertions:** Verify that a given resource exists with specific properties, e.g.:

  ```ts
  const template = Template.fromStack(stack);
  template.hasResourceProperties('AWS::S3::Bucket', { VersioningConfiguration: { Status: 'Enabled' } });
  ```

---

#### 🔹 Real‑World Scenarios

51. **When would you choose CDK over plain CloudFormation?**

* Your team prefers familiar programming languages with loops, conditionals, and abstractions.
* You need to share and version‑control reusable patterns (construct libraries).
* You want richer IDE support (autocomplete, type safety).

52. **How do you manage multi‑account infrastructure using CDK or StackSets?**

* **CDK Pipelines:** Define multiple deployment stages targeting different accounts/regions.
* **Bootstrap per environment:** Run `cdk bootstrap` in each account/region.
* **AWS Organizations & StackSets:** For uniform deployments (e.g., guardrails), use CloudFormation StackSets with service-managed permissions.

53. **How do you implement CI/CD for CloudFormation/CDK templates?**

* **CodeCommit/GitHub → CodePipeline/GitHub Actions:** Trigger on pull requests or merges.
* **Lint & Unit Tests:** cfn-lint, CDK assertions.
* **Synth & ChangeSet Approval:** `cdk synth` + `cdk diff` in build stage; manual approval for prod.
* **Deploy Stage:** `cdk deploy` (or CLI/SDK’s `create-change-set` → `execute-change-set`).

54. **How would you organize a large infrastructure project in CDK?**

* **Mono‑repo vs. multi‑repo:** Group by domain or team.
* **Layered constructs:** Core (networking/security), services (compute/storage), app stacks.
* **Construct libraries:** Shared patterns and utilities extracted into versioned packages.
* **Well‑defined boundaries:** One stack per logical domain (e.g., VPC, Security, Services).

55. **How do you handle cross‑stack references in CloudFormation and CDK?**

* **CloudFormation:** `Fn::ImportValue`/`Export` outputs from one stack and `Fn::ImportValue` in another.
* **CDK:** Use L1 exports or pass references directly between stacks in the same app (`new OtherStack(scope, 'Other', { vpc: vpcStack.vpc })`). CDK will automatically create exports/imports under the hood.

56. **How do you manage IAM roles and policies across stacks?**

* Define a dedicated “IAM” stack or module with roles and managed policies.
* Export ARNs/Names via outputs and import into service stacks.
* Use CDK’s `Role.fromRoleArn()` to reference existing roles, then attach policies as needed.

57. **How do you manage multiple environments (dev/stage/prod) in CDK?**

* **Context-based configs:** Use `cdk.json` contexts like `"env": "prod"`, then branch in code.
* **Separate stacks:** Instantiate stacks per environment with different parameters.
* **Pipeline stages:** CDK Pipelines can deploy stack variants to each environment sequentially.

58. **How would you migrate an existing CloudFormation template to CDK?**

59. **Import with `cdk import`** (experimental) or

60. **Manually rewrite:** Read the CFN template, instantiate corresponding L2 constructs in code.

61. **Verify with `cdk diff`** against the live stack to ensure parity.

62. **Deploy under CDK control** with `cdk deploy`.

63. **What tools can be used to lint or validate templates and CDK code?**

* **cfn-lint** for CloudFormation YAML/JSON.
* **AWS Config Rules** for drift and best practices.
* **cdk-nag** for CDK apps (enforces security/best‑practice rules).
* **IDE linters:** ESLint (TypeScript), pylint/flake8 (Python).

60. **How do you handle rollback and failure recovery in large CloudFormation/CDK deployments?**

* **Enable ChangeSets:** Review and approve before deployment.
* **Automatic rollback:** Let CloudFormation roll back on failures, or disable for investigation.
* **Stack policies & termination protection:** Prevent unintended deletions.
* **Idempotent operations:** Write Lambda-backed custom resources to handle retries.
* **Monitoring & alerts:** Use CloudWatch Events to detect failures and trigger notifications or automated remediation (e.g., rollback or retry jobs).



