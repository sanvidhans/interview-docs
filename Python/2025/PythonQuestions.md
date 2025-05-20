## Python Interview Questions

#### 1. What are the key features of Python that make it suitable for microservices?
**Answer**: Python’s simplicity, readability, and extensive ecosystem make it ideal for microservices. 

Key features include:
- **Dynamic Typing**: Speeds up development.
- **Rich Libraries**: Frameworks like Flask, FastAPI, and Django for APIs.
- **Concurrency Support**: Asyncio and libraries like `aiohttp` for scalable services.
- **ORMs**: SQLAlchemy, Django ORM for database integration.
- **Deployment**: Easy integration with Docker, Kubernetes, and cloud platforms like AWS.

---

#### 2. How do you manage dependencies in a Python microservice?
**Answer**: Use `pip` with a `requirements.txt` file or `poetry`/`pipenv` for dependency management.

Example:
- Create `requirements.txt`: `pip freeze > requirements.txt`.
- Install: `pip install -r requirements.txt`.
- Use `poetry` for isolated environments: `poetry add <package>`.
- Pin versions to avoid breaking changes.

---

#### 3. Explain the difference between a list and a tuple in Python.
**Answer**:
- **List**: Mutable, defined with `[]`, e.g., `[1, 2, 3]`. Supports append, remove.
- **Tuple**: Immutable, defined with `()`, e.g., `(1, 2, 3)`. Faster, used for fixed data.
- Example: `my_list = [1, 2]; my_list.append(3)` vs. `my_tuple = (1, 2)` (cannot modify).

---

#### 4. What is the Global Interpreter Lock (GIL) and how does it affect Python microservices?
**Answer**: The- **GIL**: A mutex in CPython that ensures thread-safe execution of Python bytecode, limiting true multi-threading.
- **Impact**: Hinders CPU-bound tasks in multi-threaded apps but less relevant for I/O-bound microservices using asyncio or multiprocessing.
- **Workaround**: Use `multiprocessing` or frameworks like `gunicorn` with multiple workers.

---

#### 5. How do you handle error handling in Python microservices?
**Answer**: Use try-except blocks, custom exceptions, and logging. Example:
```python
try:
    result = 1 / 0
except ZeroDivisionError as e:
    logger.error(f"Division error: {e}")
    raise CustomAPIError("Invalid input", status_code=400)
```

---

#### 6. What are decorators in Python, and how are they used in microservices?
**Answer**: Decorators are functions that wrap other functions to extend behavior. Common in microservices for logging, authentication, or rate-limiting.
```python
import logging
def log(func):
    def wrapper(*args, **kwargs):
        logging.info(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@log
def process_data(data):
    return data.upper()
```

---

#### 7. How do you implement async programming in Python for microservices?
**Answer**: Use `asyncio` with `async def` and `await`. Frameworks like FastAPI leverage this for high-performance APIs.
```python
from fastapi import FastAPI
import aiohttp
app = FastAPI()

@app.get("/fetch")
async def fetch_data(url: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            return await resp.json()
```

---

#### 8. What is the difference between `__init__` and `__new__` in Python?
**Answer**:
- **`__new__`**: Static method, creates a new instance (called before `__init__`).
- **`__init__`**: Initializes the instance after creation.
- Use `__new__` for custom instance creation (e.g., singletons).

---

#### 9. How do you optimize Python code for performance in microservices?
**Answer**:
- Use **C extensions** (e.g., `numba`, `cython`) for CPU-bound tasks.
- Leverage **asyncio** for I/O-bound tasks.
- Profile with `cProfile` or `line_profiler`.
- Cache results with `functools.lru_cache`.
- Use efficient data structures (e.g., `set` for lookups).

---

#### 10. What are context managers, and how are they used?
**Answer**: Context managers handle resource setup/teardown (e.g., file operations). Use `with` statement or `@contextlib.contextmanager`.
```python
from contextlib import contextmanager
@contextmanager
def timer():
    start = time.time()
    yield
    print(f"Elapsed: {time.time() - start}s")

with timer():
    time.sleep(1)
```

---

#### 11. How do you implement a REST API in Python using FastAPI?
**Answer**: FastAPI provides a high-performance, async framework for APIs.
```python
from fastapi import FastAPI
app = FastAPI()

items = {"1": "Item 1"}

@app.get("/items/{item_id}")
async def read_item(item_id: str):
    return items.get(item_id, {"error": "Not found"})

@app.post("/items")
async def create_item(item: dict):
    items[str(len(items) + 1)] = item["name"]
    return {"id": len(items)}
```

---

#### 12. How do you handle database connections in Python microservices?
**Answer**: Use ORMs like SQLAlchemy or connection pools (e.g., `psycopg2.pool`). Ensure connections are closed properly.
```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("postgresql://user:pass@localhost/db")
Session = sessionmaker(bind=engine)

def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()
```

---

#### 13. What is the difference between a shallow copy and a deep copy?
**Answer**:
- **Shallow Copy**: Copies the object but not nested objects (`copy.copy`).
- **Deep Copy**: Recursively copies all objects (`copy.deepcopy`).
- Example: `list.copy()` is shallow; `deepcopy(list)` is deep.

---

#### 14. How do you implement logging in Python microservices?
**Answer**: Use the `logging` module with handlers for console/file output. Configure log levels and formats.
```python
import logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("app.log"), logging.StreamHandler()]
)
logger = logging.getLogger(__name__)

logger.info("Service started")
```

---

#### 15. How do you write unit tests for a Python microservice?
**Answer**: Use `unittest` or `pytest`. Mock dependencies with `unittest.mock`.
```python
import pytest
from unittest.mock import patch
def get_data():
    return {"data": "test"}

def test_get_data():
    with patch("module.get_data", return_value={"data": "mocked"}):
        assert get_data() == {"data": "mocked"}
```

---

#### 16. What are generators in Python, and how are they useful in microservices?
**Answer**: Generators yield values lazily, saving memory. Useful for streaming large datasets.
```python
def stream_data(n):
    for i in range(n):
        yield i

@app.get("/stream")
async def stream():
    return StreamingResponse(stream_data(100), media_type="text/plain")
```

---

#### 17. How do you handle environment variables in Python?
**Answer**: Use `os.environ` or `python-dotenv` to load `.env` files.
```python
from dotenv import load_dotenv
import os
load_dotenv()
DB_URL = os.getenv("DATABASE_URL", "sqlite:///./test.db")
```

---

#### 18. What is the difference between `threading` and `multiprocessing` in Python?
**Answer**:
- **Threading**: Runs in the same memory space, limited by GIL for CPU-bound tasks.
- **Multiprocessing**: Runs separate processes, bypassing GIL, ideal for CPU-bound tasks.
- Use `multiprocessing` for parallel microservice tasks.

---

#### 19. How do you implement authentication in a Python microservice?
**Answer**: Use JWT with `PyJWT` or OAuth with `authlib`. Example with FastAPI:
```python
from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
import jwt
app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

async def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, "SECRET_KEY", algorithms=["HS256"])
        return payload["sub"]
    except:
        raise HTTPException(status_code=401, detail="Invalid token")
```

---

#### 20. How do you deploy a Python microservice?
**Answer**:
- Containerize with **Docker**.
- Orchestrate with **Kubernetes**.
- Deploy on cloud platforms (e.g., AWS ECS, Lambda).
- Use CI/CD pipelines (e.g., GitHub Actions).

---

#### 21. What is the difference between Flask and FastAPI?
**Answer**:
- **Flask**: Synchronous, lightweight, simple for small APIs.
- **FastAPI**: Asynchronous, built for performance, supports OpenAPI and type hints.
- FastAPI is better for scalable microservices.

---

#### 22. How do you handle large file uploads in Python microservices?
**Answer**: Use streaming with `aiofiles` or `Starlette` in FastAPI to process chunks.
```python
from fastapi import FastAPI, File, UploadFile
import aiofiles
app = FastAPI()

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    async with aiofiles.open(f"uploads/{file.filename}", "wb") as out_file:
        while content := await file.read(1024):
            await out_file.write(content)
    return {"filename": file.filename}
```

---

#### 23. How do you implement rate limiting in Python microservices?
**Answer**: Use `fastapi-limiter` or custom middleware with Redis.
```python
from fastapi import FastAPI
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
app = FastAPI()
limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter
app.add_exception_handler(429, _rate_limit_exceeded_handler)

@app.get("/limited")
@limiter.limit("5/minute")
async def limited_route():
    return {"message": "OK"}
```

---

#### 24. What are metaclasses in Python, and how are they used?
**Answer**: Metaclasses define the behavior of classes (class of a class). Used for custom class creation (e.g., ORMs).
```python
class SingletonMeta(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class Singleton(metaclass=SingletonMeta):
    pass
```

---

#### 25. How do you connect Python to a message queue like RabbitMQ?
**Answer**: Use `pika` for RabbitMQ. Publish/consume messages with queues.
```python
import pika
connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()
channel.queue_declare(queue="task_queue")
channel.basic_publish(exchange="", routing_key="task_queue", body="Hello!")
connection.close()
```

---

#### 26. How do you profile a Python microservice?
**Answer**: Use `cProfile` for runtime profiling, `line_profiler` for line-by-line analysis, or `py-spy` for sampling.
```python
import cProfile
def complex_function():
    return sum(i * i for i in range(10000))

cProfile.run("complex_function()")
```

---

#### 27. What is the difference between `__str__` and `__repr__`?
**Answer**:
- **`__str__`**: User-friendly string representation (for `print`).
- **`__repr__`**: Developer-friendly, ideally recreates the object (for debugging).
- Example: `str(obj)` vs. `repr(obj)`.

---

#### 28. How do you implement a circuit breaker in Python microservices?
**Answer**: Use `pybreaker` or custom logic to prevent cascading failures.
```python
import pybreaker
breaker = pybreaker.CircuitBreaker(fail_max=3, reset_timeout=60)

@breaker
def call_external_service():
    # Simulate API call
    raise Exception("Service down")

try:
    call_external_service()
except pybreaker.CircuitOpenError:
    print("Circuit open, fallback")
```

---

#### 29. How do you handle transactions in Python with SQL databases?
**Answer**: Use SQLAlchemy’s session or connection-level transactions.
```python
from sqlalchemy.orm import Session
def transfer_funds(db: Session, from_id: int, to_id: int, amount: int):
    try:
        db.begin()
        # Update accounts
        db.commit()
    except:
        db.rollback()
        raise
```

---

#### 30. How do you implement a CLI tool in Python?
**Answer**: Use `argparse` or `click` for command-line interfaces.
```python
import click
@click.command()
@click.argument("name")
def greet(name):
    click.echo(f"Hello, {name}!")

if __name__ == "__main__":
    greet()
```

---


#### 31. How do you ensure thread safety in Python microservices?
**Answer**: Python’s GIL limits true thread parallelism, but thread safety is needed for shared resources. Use locks (`threading.Lock`), `concurrent.futures`, or `multiprocessing` for CPU-bound tasks. For microservices, prefer asyncio for I/O-bound tasks.
```python
from threading import Lock
class SafeCounter:
    def __init__(self):
        self.value = 0
        self.lock = Lock()
    def increment(self):
        with self.lock:
            self.value += 1
```

---

#### 32. What is the difference between `@classmethod` and `@staticmethod`?
**Answer**:
- **`@classmethod`**: Takes `cls` as the first argument, can access class state.
- **`@staticmethod`**: No access to `cls` or `self`, behaves like a regular function within a class namespace.
- Example: Use `@classmethod` for alternative constructors, `@staticmethod` for utility functions.

---

#### 33. How do you implement a retry mechanism in Python microservices?
**Answer**: Use `tenacity` or custom logic with exponential backoff for retrying failed API calls or database operations.
```python
from tenacity import retry, stop_after_attempt, wait_exponential
@retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=4, max=10))
def fetch_data(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.json()
```

---

#### 34. How do you handle schema validation in FastAPI?
**Answer**: Use Pydantic models for request/response validation. FastAPI integrates Pydantic for automatic validation and OpenAPI docs.
```python
from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

class Item(BaseModel):
    name: str
    price: float

@app.post("/items")
async def create_item(item: Item):
    return item
```

---

#### 35. What is the role of `__slots__` in Python classes?
**Answer**: `__slots__` restricts attributes to a predefined set, reducing memory usage and improving attribute access speed. Useful for high-performance microservices with many objects.
```python
class Item:
    __slots__ = ['id', 'name']
    def __init__(self, id, name):
        self.id = id
        self.name = name
```

---

#### 36. How do you implement distributed tracing in Python microservices?
**Answer**: Use OpenTelemetry or Jaeger for tracing requests across services. Integrate with FastAPI via middleware.
```python
from opentelemetry import trace
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from fastapi import FastAPI
app = FastAPI()
FastAPIInstrumentor.instrument_app(app)
tracer = trace.get_tracer(__name__)

@app.get("/hello")
async def hello():
    with tracer.start_as_current_span("hello-span"):
        return {"message": "Hello"}
```

---

#### 37. What is the difference between `pickle` and `json` for serialization?
**Answer**:
- **pickle**: Binary, Python-specific, supports complex objects but is less secure.
- **json**: Text-based, interoperable, safer but limited to basic types.
- Use `json` for microservices APIs, `pickle` for internal caching.

---

#### 38. How do you implement a background task in a Python microservice?
**Answer**: Use Celery for distributed task queues or FastAPI’s `BackgroundTasks`.
```python
from fastapi import FastAPI, BackgroundTasks
app = FastAPI()

def send_email(email: str):
    print(f"Sending email to {email}")

@app.post("/send-email")
async def send_email_endpoint(email: str, background_tasks: BackgroundTasks):
    background_tasks.add_task(send_email, email)
    return {"message": "Email scheduled"}
```

---

#### 39. How do you manage database migrations in Python microservices?
**Answer**: Use Alembic (with SQLAlchemy) or Django’s migration system. Define migrations and apply with `alembic upgrade head`.
```python
from alembic import op
import sqlalchemy as sa

def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String)
    )
```

---

#### 40. What are descriptors in Python, and how are they used?
**Answer**: Descriptors are classes implementing `__get__`, `__set__`, or `__delete__` to control attribute access. Used in ORMs for property validation.
```python
class NonNegative:
    def __get__(self, obj, owner):
        return obj._value
    def __set__(self, obj, value):
        if value < 0:
            raise ValueError("Value must be non-negative")
        obj._value = value

class Item:
    price = NonNegative()
    def __init__(self, price):
        self.price = price
```

---

#### 41. How do you optimize database queries in Python microservices?
**Answer**:
- Use indexes for frequent queries.
- Select only needed columns (`SELECT name` vs. `SELECT *`).
- Use joins efficiently or denormalize for performance.
- Cache results with Redis or `functools.lru_cache`.

---

#### 42. How do you implement a caching layer in Python microservices?
**Answer**: Use Redis or `functools.lru_cache` for in-memory caching.
```python
import redis
from functools import wraps
client = redis.Redis(host='localhost', port=6379)

def cache(func):
    @wraps(func)
    def wrapper(*args):
        key = f"{func.__name__}:{args}"
        if value := client.get(key):
            return value.decode()
        result = func(*args)
        client.setex(key, 3600, result)
        return result
    return wrapper
```

---

#### 43. What is the difference between `is` and `==` in Python?
**Answer**:
- **`is`**: Checks identity (same object in memory).
- **`==`**: Checks equality (same value).
- Example: `a = [1]; b = [1]; a == b` is `True`, but `a is b` is `False`.

---

#### 44. How do you implement a health check endpoint in a Python microservice?
**Answer**: Add a `/health` endpoint to check service and dependency status.
```python
from fastapi import FastAPI
app = FastAPI()

@app.get("/health")
async def health_check():
    # Check DB, Redis, etc.
    return {"status": "healthy"}
```

---

#### 45. How do you handle file uploads with validation in Python?
**Answer**: Use FastAPI with Pydantic to validate file types and sizes.
```python
from fastapi import FastAPI, File, UploadFile, HTTPException
app = FastAPI()

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    if not file.content_type.startswith("image/"):
        raise HTTPException(400, detail="Images only")
    return {"filename": file.filename}
```

---

#### 46. What is the role of `mypy` in Python development?
**Answer**: `mypy` is a static type checker for Python, ensuring type safety. Useful in microservices for catching type errors early.
```python
from typing import List
def sum_numbers(numbers: List[int]) -> int:
    return sum(numbers)
```

---

#### 47. How do you implement a message queue consumer in Python?
**Answer**: Use `pika` for RabbitMQ or `aiokafka` for Kafka.
```python
import pika
connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()
channel.queue_declare(queue="tasks")

def callback(ch, method, properties, body):
    print(f"Received: {body}")

channel.basic_consume(queue="tasks", on_message_callback=callback, auto_ack=True)
channel.start_consuming()
```

---

#### 48. How do you handle configuration drift in microservices?
**Answer**:
- Use configuration management tools (e.g., Consul, Vault).
- Store configs in environment variables or external services (e.g., AWS Secrets Manager).
- Automate deployment with IaC (e.g., Terraform).

---

#### 49. What is the difference between `yield from` and `yield` in Python?
**Answer**:
- **`yield`**: Yields a single value from a generator.
- **`yield from`**: Delegates to another iterable, yielding its values.
```python
def sub_generator():
    yield from [1, 2, 3]
def main_generator():
    yield from sub_generator()
```

---

#### 50. How do you implement API versioning in Python microservices?
**Answer**: Use URL path versioning (e.g., `/v1/items`) or header-based versioning in FastAPI.
```python
from fastapi import FastAPI
app = FastAPI()

@app.get("/v1/items")
async def read_items_v1():
    return {"version": "v1"}
```

---

#### 51. How do you handle large-scale logging in distributed microservices?
**Answer**: Use a centralized logging system like ELK Stack or Fluentd. Integrate with `logging` and `structlog` for structured logs.
```python
import structlog
structlog.configure(processors=[structlog.processors.JSONRenderer()])
logger = structlog.get_logger()
logger.info("Service started", service_id="123")
```

---

#### 52. What is the role of `asyncio.run` vs. `asyncio.create_task`?
**Answer**:
- **`asyncio.run`**: Runs an async coroutine and manages the event loop, used as the entry point.
- **`asyncio.create_task`**: Schedules a coroutine to run concurrently within an existing loop.
- Use `create_task` in microservices for parallel tasks.

---

#### 53. How do you implement a singleton pattern in Python?
**Answer**: Use a metaclass or module-level instance for singletons.
```python
class Singleton:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
```

---

#### 54. How do you secure a Python microservice?
**Answer**:
- Use HTTPS with TLS.
- Validate inputs with Pydantic.
- Implement JWT/OAuth for authentication.
- Use `secrets` for sensitive data.
- Scan dependencies with `safety`.

---

#### 55. How do you implement a GraphQL API in Python?
**Answer**: Use `ariadne` or `strawberry` for GraphQL APIs.
```python
from fastapi import FastAPI
from strawberry import Schema, type, field
from strawberry.fastapi import GraphQLRouter

@type
class Query:
    @field
    def hello(self) -> str:
        return "Hello, GraphQL!"

schema = Schema(query=Query)
app = FastAPI()
app.include_router(GraphQLRouter(schema), prefix="/graphql")
```

---

#### 56. How do you handle circuit breaking in distributed systems?
**Answer**: Use `pybreaker` to open circuits on repeated failures, with fallback logic.
```python
import pybreaker
breaker = pybreaker.CircuitBreaker(fail_max=3, reset_timeout=60)

@breaker
def call_service():
    raise Exception("Service unavailable")

def fallback():
    return {"message": "Using fallback"}

try:
    result = call_service()
except pybreaker.CircuitOpenError:
    result = fallback()
```

---

#### 57. How do you implement a cron job in Python microservices?
**Answer**: Use `APScheduler` for scheduling tasks.
```python
from apscheduler.schedulers.background import BackgroundScheduler
def job():
    print("Running scheduled task")
scheduler = BackgroundScheduler()
scheduler.add_job(job, 'interval', minutes=5)
scheduler.start()
```

---

#### 58. What is the difference between `list comprehension` and `generator expression`?
**Answer**:
- **List Comprehension**: Creates a list in memory (`[x for x in range(10)]`).
- **Generator Expression**: Yields values lazily (`(x for x in range(10))`).
- Use generators for memory efficiency in microservices.

---

#### 59. How do you implement a load balancer for Python microservices?
**Answer**: Use Nginx, HAProxy, or cloud-native load balancers (e.g., AWS ALB). For internal balancing, use `gunicorn` with multiple workers or Kubernetes services.
```python
# Run: gunicorn -w 4 -b 0.0.0.0:8000 main:app
from fastapi import FastAPI
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello"}
```

---

#### 60. How do you implement a rate limiter with Redis in Python?
**Answer**: Use Redis for token bucket or sliding window rate limiting.
```python
import redis
from fastapi import FastAPI, HTTPException
app = FastAPI()
client = redis.Redis(host='localhost', port=6379)

def rate_limit(key: str, limit: int, window: int):
    count = client.incr(key)
    if count == 1:
        client.expire(key, window)
    if count > limit:
        raise HTTPException(429, detail="Rate limit exceeded")
    return count

@app.get("/limited")
async def limited():
    rate_limit("user:127.0.0.1", limit=5, window=60)
    return {"message": "OK"}
```

---

