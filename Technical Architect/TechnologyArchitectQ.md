
## Technology Architect Role

#### 1. How do you design a scalable Python-based microservices architecture?

- A scalable Python microservices architecture involves modular services communication via APIs. 
- Use frameworks like Flask or FastAPI for lightweight services, with Django for complex ones. 
- Implement asynchronous processing with asyncio or libraries like Calery for task queues.
Deploy on containerized platforms like Kubernetes for orchestration and AWS ECS for scalability.
- Use message brokers(e.g., Kafka, RabbitMQ) for inter-service communication and PostgreSQL or DynamoDB for data storage.
- Ensure fault tolerance with circuit breakers (e.g., PyCircuitBreaker) and monitoring via Prometheus/Grafana. 
- I have designed such systems at DBS, Capgemini, handling high throughput payment API with AWS Lambda and SQS.

#### 2. How does Python's Global Interpreter Lock (GIL) impact performance in multi-threaded application?

- The GIL prevents multiple native threads from executing Python bytecode simulteneously, limiting true parallelism in CPU-bound tasks. 
- For I/O-bound tasks, `threading` works well due to GIL release during I/O operations.
- For CPU-bound tasks, use `multiprocessing` to bypass the GIL or leverage `NumPy` for C-based computations.
- In a last company, I used multiprocessing to parallelize data processing, improving throughput by 40%.

#### 2v2. How does Python's GIL affect enterprise application performance?

- The GIL limits multi-threaded CPU-bould tasks, 
- For I/O-bound tasks, I use `asyncio` for concurrency.
- For CPU-bound tasks, I leverage `multiprocessing`

#### 3. How would you optimize a Python application for high performance?
- Optimize by profiling with tools like `cProfile` or `Py-Spy` to identify bottlenecks. 
- Use efficient data structure (e.g., collections.deque for queues). 
- Implement caching with `Redis` or `functools.lru_cache`. 
- For compute-heavy tasks, use `Cython` or `NumPy` for faster execution. 
- Leverage asynchronous programming with `asyncio` for I/O-bound tasks.


#### 4. Explain how you would implement a REST API in Python with security best practices?
- Use FastAPI or Flask to build API. Implement authentication with OAuth2(using python-jose) or JWT.
- Use HTTPS for data encryption and pydantiic for input validation. 
- Apply rate limiting with slowapi to prevent abuse. 
- Secure endpoints with role-based access control (RBAC) via libraries like Flask-Security. 
- Log requests with structlog for auditing.
- In last projects I used OAUTH2 and JWT tokens, ensuring compliance with PCI DSS.


#### 5. How do you handle error management in large-scale Python application?

- Use structured exception handling with try-except blocks. 
- Define custom exceptions for specific error types (e.g., class PaymentError(Exception)).
- Log errors with logging or sentry-sdk for monitoring. 
- Implement retry mechanism with tenacity for transient failure (e.g. network issues). 
- In a microservices project, I used sentry-sdk to track errors and tenancity for retrying failed API calls, reducing downtime by 20%.


#### 6. How do you ensure code quality in a Python development team?
- Enforce coding standards with flake8 and pylint. Use black for consistent formating. 
- Implement unit tests with pytest and achieve >80% coverage.
- Conduct code reviews via GitHub/GitLab. 
- Integrate static analysis with SonarQube. 
- In my lead role at Hectronic and Capgemini, I set up CI/CD pipelines with GitLab and SonarQube, reducing bugs by 25%.


#### 7. What is the difference between Python's `asyncio` and `threading` for concurrency?
- `asyncio` uses an event loop for asynchronous, non-blocking I/O operations, ideal for I/O-bound tasks (e.g.,API calls). 
- `threading` creates OS threads but is limited by the GIL for CPU-bound tasks.
- Use `asyncio` for scalable network applications and `threading` for simpler I/O tasks. 
- I used `asyncio` in a real-time analytics system to handle 10000 concurrent requests efficiently.


#### 8. How would you integrate Python microservices with AWS services?
- Use `boto3` to interact with AWS services like S3, Lambda, or DynamoDB.
- Deploy microservices as Lambda functions for serverless architecture or on ECS/EKS for containerized workloads.
- Use SQS/SNS for messaginig and CloudWatch for monitoring.
- In current company, I integrated a Python and NodeJs microservices with Lambda and SQS, processing 1M events daily.

#### 9. How do you design a Python-based system for high availablity?
- Use dustrubuted architecture with load balancers (e.g., AWS ELB). 
- Deploy across multiple availablity zones.
- Implement health checks and auto-scaling with Kubernetes or AWS Auto Scaling. 
- Use redundant databases (e.g., PostgreSQL with read replicas).
- Using this setup we can achieve 99.9 % uptime.

#### 10. What are the benefits of using Python's pydantic in system design?
- `pydantic` enforeces type safety and data validation, reducing runtime errors. 
- Its ideal for API input/output validation in FastAPI or configuration management. 
- It supports JSON schema generation for documentation.


#### 11. How do you manage dependencies in a Python project?
- Use poetry or pipenv for dependency management and virtual environments. 
- PIN versions in requirements.txt for reproducibility. Scan for vulnerabilities with safety or dependabot.
- In a microservices, I used poetry to manage dependencies, ensuring consistent bbuilds across environments.


#### 12. How would you architect a real-time data processing system in Python?
- Use `Kafka` or `RabbitMQ` for event streaming, with Python consumers using `confluent-kafka` or `pika`.
- Process data with `pandas` or `PySpark` for large databases.
- Store results in `Redis` or `DynamoDB` for low-latency access. Deploy on AWS Lambda for scalability.


#### 13. How do you approach database migrations in Python applications?
- Use alembic for SQL databases or custom script for NoSQL. 
- Version migrations and test them in staging environments. Automate with CI/CD pipelines.
- In a project, I used alembic with PostgreSQL to manage schema changes, ensuring zero-downtime deployments.


#### 14. How do you mentor a team in adopting Python best practices?
- Conduct workshops on Pythonic code (e.g., PEP8). Share resources like pylint and pytest.
- Pair program to demonstrate best practices. 
- Set up templates for microservicees. 
- In current company I mentored a team of 5, improving code quality via regular reviews and training.


#### 15. How do you handle backward compatibility in Python APIs?
- Use versioning (e.g., /v1/endpoint) and deprecate old endpoints gradually.
- Validate inputs with pydantic to avoid breaking changes.
- Document APIs with OpenAPI/Swagger. 
- In a project, I maintained compatibility by versioning APIs and using feature flags, ensuring seamless client transactions.

#### 16. How would you gather requirements from IT manager to design an enterprise system?

- I would conduct structured meetings with the IT manager to understand business goals, scalability needs, and technical constraints.
- Using frameworks like MoSCoW prioritization, I'd categorize requirements into must-haves and nice-to-haves. 
- I would create use case diagrams and document functional/non-functional requirements using tools like Confluence.
- In a past projects, I collaborated with stakeholders to define requirements, aligning with business objectives and ensuring scalability.

#### 17. How do you decide whether to upgrade an existing system or build a new one?

- Evaluate the system's performance, scalability, and technical debt using metrics like latecy and error rates.
- Access compatibility with new requirements and cost of upgrades vs new development.
- In current company, I conducted a cost-benifit analysis and recommendeed a new golang and python based microservices architecture, reducing maintenance costs by 20%.

#### 18. How woud you desiign a Python-based enterprise system for Wipro?

- I would use FastAPI for RESTFul services, `pydantic` for data validation, and PostgreSQL for data persistence. 
- Deploy on AWS ECS for scalability, with SQS for async communication.
- Implement monitoring with Prometheus and logging with `structlog`. In a project at hectronic, I designed a Python microservices system handling 10000 transactions/second, ensuring high availability.

#### 19. How do you manange a project to implement a new system at Wirpo?

- Use Agile with sprints, tracked via Jira.
- Define milestones for design, development, and testing.
- Coordinate with developers, QA, and stakeholders via daily standups.
- At hectronic, I led 6-month project to deploy a NodeJs based transaction system, delivering on time using Agile and CI/CD with Gitlab.

#### 20. How do you collaborate with developers to define software needs for a system?

- Hold workshops to align technical requirements, using UML diagrams for clarity.
- Pair with developers to prototype solutions in Python. 
- In a microservices project. I worked with team of 5 to define API specs using OpenAPI, ensuring seamless integration.

#### 21. How would you troubleshoot a Python-based system issue at Wipro?

- Use logging (`sentry-sdk`) and monitoring (CloudWatch) to identified issues.
- Reproduce errors in a staging environments and analyze stack traces.

#### 22. How do you oversee system integration in a Python-based project?

- Ensure modular design with clear API contracts (e.g., REST with FastAPI)
- Use Kafka for event-driven integration and `boto3` for AWS services.
- Test integration with `pytest` and Postman.

#### 23. How do you measure the performance of a newly installed system?

- Define KPIs like latency, throughput, and error rates.
- Use tools like Prometheun for metrics and Locust for load testing. 
- In Python system deployment, I reduced API latency by 25% by optimizing database queries after performance testing.

#### 24. How would you train Wipro staff on new system procedures?

- Create documentation with step-by-step guides and conduct hands-on workshops.
- Use Jupyter notebooks for Python-based demos. 

#### 25. How do you provide post-installation feedback to Wipro's stakeholders?

- Prepare reports with performance metrics, user feedback, and recommendations.
- Present findings in stakeholder meetings.
- After deploying a Python API at current company, I shared a report with uptime and latency stats, leading to further optimizzation.

#### 26. How does Python's `asyncio` improve enterprise performance?

- `asyncio` enables non-blocking I/O, idedal for high-concurrency APIs.
- Using `aiohttp` and `asyncio`, I built a real-time analytics system in my previous company, handling 5000 requests/second with low latency.

#### 27. How do you ensure security in a Python-baed enterprise system?

- Implement OAuth2 with `python-jose`, validate inputs with `pydantic`, and use HTTPS.
- Apply rate limiting with `slowapi`. 
- Secure APIs with OAuth2 or JWT and RBAC, ensure compliance with security standards.

#### 28. How do you integrate Python application with enterprise networking systems?

- Use `boto3` for AWS networking (e.g., VPC, Route53).
- Implement gRPC for low-latency communication.
- Use AWS API Gateway to enable secure access across enterprise networks.

#### 29. How do you handle complex IT issue as a Technical Architect?

- Break down issues using root cause analysis. 
- Use tools like `sentry-sdk` for error tracking and `pdb` for debugging.

#### 30. How do you lead a team to deliver a Python-based system at Wipro?

- Set clear goals, assign roles based on strengths, and mentor via code reviews.
- Use Agile for collaboration.


#### 31. How do you manage memory in Python when working with large datasets?

- **Generators:**: Process data lazily to avoid everything into memory (e.g., `yield` for iteration)
- **Chunking:** Read data in smaller pieces (e.g., `pandas.read_csv(chanksize=1000)`)
- **Efficient Data Types:** Use `NumPy` array or `pandas` DataFrames instead of lists for better memory usage.
- **Garbage Collection:** Manually trigger `gc.collect()` to free unused memory.
- **Avoid Copies:** Use in-place operations to minimize overhead.


#### 32. What are decorators, and how have you used them?

- Decorators are functions that wrap other functions to modify their behaviour without altering their code.
- We can use them for logging and timing. For example,a timing decorator:
```python
import time

def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"{func.__name__} took {time.time() - start:.2f} seconds.")
        return result
    return wrapper

@timing_decorator
def slow_task():
    time.sleep(1)


slow_task() # Outputs: "slow_task took 1.00 seconds"
```

#### 33. What security risk should you watch for in Python application, and how do you address them?
- **Injection Attacks:** Preent with parameterized queries and input validation.
- **XSS/CSRF:** Escape outputs and use CSRF tokens
- **Insecure Dependencies:** Update packages regularly and scan with `pip-audit`
- **Data Exposure:** Store secrets in environment variables and encrypt sensitive data.

#### 34. How do you implement object-oriented principles in Python?
- **Encapsulation:** Use classes with private attributes (e.g., `_attribute`)
- **Inheritance:** Extend base classes.
- **Polymorphism:** Override methods in subclasses
- **Abstraction:** Use `ABC` for inheritances
```python
from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def area(self):
        return 3.14 * self.radius ** 2

```


## Coding Challenges

#### 1. Design Rate Limiter for an API
```python
from time import time
from collections import defaultdict
import threading

class RateLimiter:
    def __init__(self, limit=100, window=60):
        self.limit = limit
        self.window = window
        self.requests = defaultdict(list)
        self.lock = threading.Lock()
    
    def is_allowed(self, user_id: str) -> bool:
        with self.lock:
            current_time = time()
            # remove requests older than window
            self.requestsp[user_id] = [
                t for t in self.requests[user_id] if current_time - t < self.window
            ]
            if len(self.requests[user_id]) < self.limit:
                self.requests[user_id].append(current_time)
                return True
            return False


limiter = RateLimiter()
print(limiter.is_allowed("user1")) # True
```

#### 2. Implement a Task Queue with Priority
- Create priority queue for tasks with high, medium, and low prioties.
- Process tasks in order of priority
```python
from heapq import headpush, headpop
from enum import Enum

class Priority(Enum):
    HIGH = 1
    MEDIUM = 2
    LOW = 3

class TaskQueue:
    def __init__(self):
        self.queue = []

    def add_task(self, task: str, priority: Priority):
        heappush(self.queue, (priority.value, task))

    def get_task(self) -> str:
        if self.queue:
            return heappop(self.queue)[1]
        return None


queue = TaskQueue()
queue.add_task("Process payment", Priority.HIGH)
queue.add_task("Send Email", Priority.LOW)
print(queue.get_task()) # Process Payment
```

#### 3. Parse and Validate JSON Configuration
- Write a function to parse JSON configuration and validate it using `pydantic`
- The config should have a `name` (string) and `reties`(integer, 1-5)

```python
from pydantic import BaseModel, Field
import json

class Config(BaseModel):
    name: str
    reties: int = Field(..., ge=1, le=5)

def parse_config(config_str: str) -> Config:
    try:
        return Config(**json.loads(config_str))
    except Exception as e:
        raise ValueError(f"Invalid config : {e}")

config_json = '{"name": "service1", "retries": 3}'
config = parse_config(config_json)
print(config) # name='service1' reties=3
```

#### 4. Concurrent File Processing:
- Process multiple large files concurrently, counting words occurances. 
- Use `multiprocessing` to parallelize

```python
from multiprocessing import Pool
from collections import Counter

def count_words(file_path: str) -> Counter:
    with open(file_path, 'r') as f:
        return Counter(f.read().split())
    
def process_files(file_paths: list) -> Counter:
    with Pool() as pool:
        results = pool.map(count_words, file_paths)
    total = Counter()
    for result in results:
        total.update(result)
    return total


files = ["file1.txt", "file2.txt"]
word_counts = process_files(files)
print(word_counts)
```

#### 5. Implement a Simple Cache Decorator
- Write a decorator to cache function results with a TTL (time-to-live) of 60 seconds.
```python
from functools import wraps
from time import time
import pickle

def cache_with_ttl(ttl=60):
    def decorator(func):
        cache = {}

        @wraps(func)
        def wrapper(*args, **kwargs):
            key = pickle.dumps(args, kwargs)
            current_time = time()
            if key in cache and current_time - cache[key][1] < ttl:
                return cache[key][0]
            result = func(*args, **kwargs)
            cache[key] = (result, current_time)
            return result
        return wrapper
    return decorator



# Example usage
@cache_with_ttl(60)
def expensive_operation(x: int) -> int:
    return x * x

print(expensive_operation(5)) # Computes: 25
print(expensive_operation(5)) # Computes: 25
```

#### 6. Design a Configuration Loader for Enterprise Systems
- Write a Python function to load and validate a YAML configuration for a microservices system, ensuring required fields (`service_name`, `port`, `retries`) are present and valid.

```python
from pydantic import BaseModel, Field
from typing import Dict
import yaml

class ServiceConfig(BaseModel):
    service_name: str
    port: int = Field(..., ge=1024, le=65525)
    retries: int = Field(..., ge=1, le=5)

def load_config(config_path: str) -> Dict[str, ServiceConfig]:
    try:
        with open(config_path, 'r') as f:
            data = yaml.safe_load(f)
        return {k: ServiceConfig(**v) for k, v in data.items()}
    except Exception as e:
        raise ValueError(f"Config load failed: {e}")


# Example
config_yaml = """
auth_service:
    service_name: auth
    port: 8080
    retries: 3
payment_service:
    service_name: payment
    port: 8081
    retries: 2
"""

with open("config.yaml", "w") as f:
    f.write(config_yaml)
config = load_config("config.yaml")
print(config) 
```

#### 7. Implement Circuit Breaker for API Calls
- Create a circuit breaker in Python to handle API call failures, with a threshold of 5 failures before opening
```python
from enum import Enum
from time import time
import requests

class CircuitState(Enum):
    CLOSED = 1
    OPEN = 2
    HALF_OPEN = 3

class CircuitBreaker:
    def __init__(self, failure_threshold=5, timeout=30):
        self.failure_threshold = failure_threshold
        self.timeout = timeout
        self.state = CircuitState.CLOSED
        self.failures = 0
        self.last_failures = 0

    def call(self, url: str):
        if self.state === CircuitState.OPEN:
            if time() - self.last_failure < self.timeout:
                raise Exception("Circuit open")
            self.state = CircuitState.HALF_OPEN

        try:
            response = requests.get(url, timeout=5)
            self.failures = 0
            self.state = CircuitState.CLOSED
            return response
        except Exception:
            self.failures += 1
            self.last_failures = time()
            if self.failures >= self.failures_threshold:
                self.state = CircuitState.OPEN
            raise
        
breaker = CircuitBreaker()
try:
    breaker.call("https://api.example.com")
except Exception as e:
    print(f"Error: {e}")
```

#### 8. Process Large Database with Pagination
- Write a Python function to fetch and process paginated data from an API, aggregating results.
```python
import aiohttp
import asyncio
from typing import List

async def fetch_page(session, url: str, page: int) -> List[dict]:
    async with session.get(f"{url}?page={page}") as response:
        return await response.json()

async def process_paginated_data(base_url: str, max_pages: int = 10) -> List[dict]:
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_page(session, base_url, i) for i in range(1, max_page+1)]
        pages = await asyncio.gather(**tasks)
        return [item for page in pages for item in page]



async def main():
    data = await process_paginated_data("https://api.example.com/data")
    print(len(data))

asyncio.run(main())
```

#### 9. Build a Simple Task Scheduler
- Implement a scheduler to run tasks at specific intervals using Python
```python
import schedule
import time
from typing import Callable

class TaskScheduler:
    def __init__(self):
        self.jobs = []

    def schedule_task(self, task: Callable, interval_seconds: int):
        schedule.every(interval_seconds).seconds.do(task)
        self.jobs.append(task)
    
    def run(self):
        while True:
            schedule.run_pending()
            time.sleep(1)
    
def log_status():
    print("System health check completed")

scheduler = TaskScheduler()
scheduler.schedule_task(log_status, 60)
schedule.run()
```

#### 10. Async API Client for Data Fetching
- Write an async function to fetch data from multiple API endpoints concurrently
```python
import aiohttp
import asyncio

async def fetch_data(url: str) -> dict:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()

async def fetch_multiple(urls: list) -> list:
    return await asyncio.gather(*[fetch_data(url), for url in urls])


async def main():
    urls = ["https://api.exaple.com", "https://api.example2.com"]
    results await fetch_multiple(urls)
    print(results)

```

#### 11. Reverse string

- Input: "hello"
- Output: "olleh"
```python
def reverse_string(s):
    return s[::-1]


def revers_string_recursive(s):
    result = ""
    for char in s:
        result = char + result
    return result


print(reverse_string("hello") # olleh
```

#### 11. Reverse Integer
```python
def reverse_integer(number):
    reversed_num = int(str(abs(number))[::-1])
    return -reversed_num if n < 0 else reversed_num

def reverse_integer_normal(number):
    reversed_num = 0
    is_negative = n < 0

    while n > 0:
        reversed_num = reversed_num * 10 + num % 10
        n = n // 10
    
    return -reversed_num if is_negative else reversed_num

```

#### 13. Is Prime number
```python
def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    
    return True

print(is_prime(12)) # False
print(is_prime(5)) # True
print(is_prime(7)) # True
```

#### 14. Factorial of Number

```python
def factorial(n):
    if n==0 or n==1:
        return 1
    
    return n * factorial(n-1)

print(factorial(3)) # 6
```


#### 15. Fibonacci Series
```python

def fibonacci_series(n):
    fib_series = [0, 1]

    while len(fib_series) < n:
        fib_series.append(fib_series[-1] + fib_series[-2])
    
    return fib_reries


print(fibonacci_series(10))

```

#### 16. Check Palindrome
- Input: "radar"
- Output: True
```python
def is_palindrome(s):
    return s == s[::-1]

print(is_palindrome("radar")) # True
```

#### 17. Count Vowels and Consonants
- Input: "hello"
- Output: 2,3
```python
def count_vowels_consonants(s):
    vowels = "aeiouAEIOU"
    v_count = sum(1 for char in s if char in vowels)
    c_count = sum(1 for char in s if char.isalpha() and char not in vowels)
    return v_count, c_count


print(count_vowels_consonants("hello")) # (2,3)
```

#### 18. Anagram Check

- Input: s1 = "listen", s2 = "silent"
- Ouput: True

```python

def are_anagrams(s1, s2):
    return sorted(s1) == sorted(s2)

print(are_anagrams("listen", "silent")) # True
```

#### 19. Firt Non-Repeating Character
- Input: "swiss"
- Output: "w"

```python
from collections import Counter
def first_non_repeating_char(s):
    count = Counter(s)
    for char in s:
        if count[char] == 1:
            return char
    return None

print(first_non_repeating_char("swiss")) # "w"
```

#### 20. Longest Substring Without Repeating Characters
- Input: "abcabcbb"
- Output: 3 # abc
```python
def length_longest_substring(s):
    seen = []
    start = max_length = 0
    for end, char in enumerate(s):
        if char in seen and seen[char] >= start:
            start = seen[char] + 1
        else:
            max_length = max(max_length, end - start + 1)
        seen[char] = end
    return max_length

print(length_longest_substring("abcabcbb")) # 3
```

#### 21. String Compression
- Input: "aabcccccaaa"
- Output: a2b1c5a3

```python
def compress_string(s):
    res = []
    count = 1
    for i in range(1, len(s)+1):
        if i < len(s) and s[i] == s[i-1]:
            count += 1
        else:
            res.append(s[i-1] + str(count))
            count = 1
    comp = ''.join(res)
    return comp if len(comp) < len(s) else s

```

#### 22. Implement substring search strStr()
- Input: heystack = "hello", needle = "ll"
- Output: 2
```python
def strStr(haystack, needle):
    if not needle:
        return 0
    
    for i in range(len(haystack) - len(needle) + 1):
        if haystack[i:i+len(needle)] == needle:
            return i
    return -1

print(strStr("hello", "ll"))
```

#### 23. Longest Palindromic Substring

- Input: "babad"
- Output: "bab" # or "aba"
```python
def longest_palindrome(s):
    def expand_around_center(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1: right]
    longest = ""
    for i in range(len(s)):
        p1 = expand_around_center(i, i)
        p2 = expand_around_center(i, i + 1)
        longest = p1 if len(p1) > len(longest) else longest
        longest = p1 if len(p2) > len(longest) else longest
    return longest

print(longest_palindrome("babad"))
```

#### 24. Wildcard String Matching
- Input: a = "adceb", p = "*a*b"
- Output: True
```python
import re
def wildcard_match(pattern, text):
    pattern = pattern.replace("*", ".*").replace("?", ".")
    return bool(re.fullmatch(pattern, text))

print(wildcard_match("a*c", "abc")) # True
```

#### 25. Minimum Window Substring
- Given two strings `s` and `t`, return the smallest substring of `s` that contains all characters of `t` (including duplicate)
- Input: s="ADOBECODEBANC", t="ABC"
- Output: "BANC"
```python

```

#### 26. Decode String
- Decode an encoded string with counts and brackets, e.g., "3[a2[c]]" -> "accaccacc"
- Input: "3[a]2[bc]"
- Output: "aaabcbc"
```python
def decode_string(s):
    stack = []
    num = 0
    current = ""
    for char in s:
        if char.isdigit():
            num = num * 10 + int(char)
        elif char == "[":
            stack.append((current, num))
            current, num = "", 0
        elif char == "]":
            prev_str, times = stack.pop()
            current = prev_str + current * times
        else:
            current += char
    return current

print(decode_string("3[a]2[bc]"))

```

#### 27. Character Frequency Count
- Input: "aaabbccdde"
- Output: {'a':3, 'b':2, 'c':2, 'd': }
```python
from collections import Counter
def char_frequency(s):
    return dict(Counter(s))

print(char_frequency("aaabbccdde"))
```


#### 28. Most Frequent Character
- Input: "successes"
- Output: "s"
```python
from collections import Counter
def most_frequent_char(s):
    count = Counter(s)
    return max(count, key=count.get)

print(most_frequent_char("successes")) # s

```



#### 29. Group Character By Frequency
- Input: "banana"
- Output: {1: ['b'], 2: ['n'], 3: ['a']}
```python
from collections import Counter, defaultdict
def group_by_frequency(s):
    count = Counter(s)
    freq_dict = defaultdict(list)
    for char, freq in count.items():
        freq_dict[freq].append(char)
    return dict(freq_dict)

print(group_by_frequency("banana"))
```

#### 30. Remove duplicate characters
- Input: "programming"
- Output: "progamin"
```python
def remove_duplicates(s):
    return ''.join(set(s))

print(remove_duplicates("aabbccdde"))
```


#### 31. Group Similar Characters Together
- Input: "programming"
- Output: "rrggmmpoain"
```python
def group_similar_chars(s):
    return "".join(sorted(s))

print(group_similar_chars("programming"))
```

#### 32. Shift letter by K
- Input: "abc", k=2
- Output: "cde"
```python
def shift_letters(s, k):
    return "".join(chr((ord(c)- ord("a") + k) % 26 + ord("a")) if c.isalpha() else c for c in s)

print(shift_letters("abc", 2))
```

#### 33. Is a subsequence?
- Input: s="abc", t="ahbgdc"
- Output: True
```python
def is_subsequence(s, t):
    iter_t = iter(t)
    return all(c in iter_t for c in s)

print(is_subsequence("abc", "ahbgdc"))
```


#### 34. Check Balance Parantheses
- Input: "(a+b)*(c)"
- Output: True
```python
def is_balanced(s):
    stack = []
    pairs = {')':'(', '}': '{', "]": "["}

    for char in s:
        if char in pairs.values():
            stack.append(char)
        elif char in pairs:
            if not stack or stack.pop() != pairs[char]:
                return False
    return len(stack) == 0

print(is_balanced("(a + b) * (c)"))
```


#### 35. Validate IPv4 address
- Input: "192.168.0.1"
- Output: True
```python
def is_valid_ipv4(ip):
    parts = ip.split(".")
    if len(parts) != 4:
        return False
    
    for part in parts:
        if not part.isdigit() or not 0 <= int(part) <= 255:
            return False
    return True

print(is_valid_ipv4("192.168.0.1"))
```


#### 36. Extract Email from String
- Input: "Contact: test.email@company.com"
- Output: "test.email@company.com"
```python

```

#### 37. String to Integer
- Input: "-123"
- Output: -123
```python
print(int("-123"))
```


#### 38. Find Common Character in All strings
- Input: ["bella", "label", "roller"]
- Output: ["e", "l", "l"]
```python
from collections import Counter
def common_chars(strs):
    common = Counter(strs[0])
    for s in strs[1:]:
        common &= Counter(s)

    return list(common.elements())

print(common_chars(["bella", "label", "roller"]))
```


#### 39. Permutation of a String
- Input: "abc"
- Output: ["abc", "acb", "bac", "bca", "cab", "cba"]
```python
def permutations(s):
    if len(s) <= 1:
        return [s]
    
    res = []
    for i, ch in enumerate(s):
        for perm in permutations(s[:i]+s[i+1:]):
            res.append(ch + perm)
    return res

print(permutations("abc"))
```

#### 40. Check if Rotation of Another String

- Input: s1="abcd", s2="cdab"
- Output: True
```python
def is_rotation(s1, s2):
    return len(s1) == len(s2) and s2 in (s1+s1)

print(is_rotation("abcd", "cdab"))
```


#### 41. Rearrange String so No Adjacent Characters are same
- Input: "aaabbc"
- Output: "ababac"
```python
from collections import Counter
import heapq

def raarrange_no_adj(s):
    cnt = Counter(s)
    heap = [(-v, ch) for ch, v in cnt.items()]
    heapq.heapify(heap)
    prev = (0, '')
    res = []

    while heap:
        v, ch = heapq.heappop(heap)
        res.append(ch)
        if prev[0] < 0:
            heapq.heappush(heap, prev)
        prev = (v + 1, ch)
    out = ''.join(res)
    return out if len(out) == len(s) else ''

print(raarrange_no_adj("aaabbc"))
```




#### 42. Convert Snake Case to Camel Case
- Input: "my_variable_name"
- Output: "myVariableName"
```python
def snake_to_camel(s):
    parts = s.split('_')
    return parts[0] + ''.join(p.title() for p in parts[1:])

print(snake_to_camel("my_variable_name"))
```



#### 43. Count Words in a Sentence
- Input: "This is a sentence"
- Output: 4
```python
import re
def count_words(s):
    return len(re.findall(r'\b\w+\b', s))


print(count_words("This is a sentence"))
```



#### 44. Capitalize First Letter of Each Word
- Input: "welcome to python"
- Ouput: "Welcome To Python"
```python
def capitalize_words(s):
    return ' '.join(w.capitalize() for w in s.split())

print(capitalize_words("welcome to python))
```


#### 45. Replace Spaces with %20 (URL Encoding)
- Input: "Mr John Smith"
- Output: "Mr%20John%20Smith"
```python
def url_encoder(s):
    return s.replace(' ', '%20')

print(url_encoder("Mr John Smith"))
```


#### 46. Check if Two String Are One Edit Away
- Input: "pale", "ple"
- Output: True
```python
def one_edit_away(s1, s2):
    if abs(len(s1) - len(s2)) > 1:
        return False

    # ensure s1 is shorter
    if len(s1) > len(s2): s1, s2 = s2, s1
    
    i = j = diff = 0
    while i < len(s1) and j < len(s2):
        if s1[i] != s2[j]:
            if diff:
                return False
            diff = 1
            if len(s1) == len(s2):
                i += 1
        else:
            i += 1
        j += 1
    return True

print(one_edit_away("pale", "ple")) # True
```


#### 47. Zigzag Conversion 
- Input: "PAYPALISHIRING", numRows=3
- Output: "PAHNAPLSIIGYIR"
```python

```


#### 48. Reverse Words in a sentence
- Input: "Hello World"
- Output: "World Hello"

```python
def reverse_words(s):
    return ' '.join(s.split()[::-1])

print(reverse_words("Hello World"))
```


#### 49. Find All Substring
- Input: "abc"
- Output: ["a", "ab", "abc", "b", "bc", "c"]
```python
def all_substring(s):
    return [s[i:j] for i in range(len(s)) for j in range(i+1, len(s)+1)]

print(all_substring("abc"))
```


#### 50. Check Isomorphoc String
- Input: s= "egg", t="add"
- Output: True
```python
def is_isomorphic(s, t):
    return len(set(zip(s, t))) == len(set(s)) == len(set(t))

print("egg", "add")
```




#### 51. Count Occurrences of Each Word
- Input: "this is a test this is fun"
- Output: {'this': 2, 'is':2, 'a':1, 'test':1, 'fun':1}

```python
from collections import Counter
def word_count(s):
    return dict(Counter(s.split()))

print(word_count("this is a test this is fun")) 
```

#### 52. Two-Sum with Sorted Input (Two-Pointer)

```python
def two_sum_sorted(nums, target):
    """
    Given a sorted list `nums` and integer `target`,
    return 1-based indices (i, j) such that nums[i-1] + nums[j-1] == target.
    """
    left, right = 0, len(nums) - 1
    while left < right:
        s = nums[left] + nums[right]
        if s == target:
            return (left + 1, right + 1)
        if s < target:
            left += 1
        else:
            right -= 1
    return None  # if no solution (per problem, won't happen)

# Example
print(two_sum_sorted([2, 7, 11, 15], 9))  # (1, 2)
```

### 8. Reverse a Linked List

```python
class ListNode:
    def __init__(self, val=0, nxt=None):
        self.val = val
        self.next = nxt

def reverseList(head: ListNode) -> ListNode:
    prev = None
    curr = head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev
```

---

### 9. Valid Parentheses

```python
def isValid(s: str) -> bool:
    stack = []
    mapping = {')':'(', ']':'[', '}':'{'}
    for ch in s:
        if ch in mapping:
            top = stack.pop() if stack else '#'
            if mapping[ch] != top:
                return False
        else:
            stack.append(ch)
    return not stack

# Examples
print(isValid("({[]})"))  # True
print(isValid("([)]"))    # False
```

---

### 10. Merge Two Sorted Arrays (In-Place)

```python
def merge(A: list[int], m: int, B: list[int], n: int) -> None:
    i, j, k = m - 1, n - 1, m + n - 1
    while j >= 0:
        if i >= 0 and A[i] > B[j]:
            A[k] = A[i]
            i -= 1
        else:
            A[k] = B[j]
            j -= 1
        k -= 1

# Example
A = [1,3,5,0,0,0]; m=3
B = [2,4,6];       n=3
merge(A, m, B, n)
print(A)  # [1,2,3,4,5,6]
```


### 1. With given input build expected output using Python?
- Given: str1 = "abc", str2 = "pqrst"
- Expected: str3 = "apbqcr s t"

**Solution:**
```python
class StringWeaver:
    def __init__(self, str1, str2):
        self.str1 = str1
        self.str2 = str2
        
    def weave(self):
        n1, n2 = len(self.str1), len(self.str2)
        min_len = min(n1, n2)
        
        interleaved_parts = []
        for i in range(min_len):
            interleaved_parts.append(str1[i])
            interleaved_parts.append(str2[i])
        
        interleaved = ''.join(interleaved_parts)
        
        if n1 > n2:
            leftover = str1[min_len:]
        else:
            leftover = str2[min_len:]
            
        if leftover:
            return interleaved + ' '+ ' '.join(leftover)
        else:
            return interleaved
        
        
if __name__ == "__main__":
    str1 = "abc"
    str2 = "pqrst"
    weaver = StringWeaver(str1, str2)
    result = weaver.weave()
    print(result)
```

### 2. With given input build expected output using Python?
- Given: l1 = ['a', 'k', 'a', 'b', 'j', 'k', 'k']
- Expected: d1 = {'a': 2, 'k': 3, 'b': 1, 'j': 1}

**Solution:**
```python
def count_occurance(l1):
    d1 = {}
    for i in l1:
        d1[i] = d1.get(i, 0) + 1
    return d1
```