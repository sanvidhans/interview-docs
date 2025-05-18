## Python FastAPI Framework Interview Questions

## ✨ Fundamentals

### 1. **What is FastAPI?**
FastAPI is a modern, high-performance Python web framework for building APIs. It leverages Python type hints for data validation, serialization, and documentation. Built on Starlette (ASGI) and Pydantic, it supports asynchronous programming, automatic OpenAPI/Swagger documentation, and offers exceptional performance.

---

### 2. **What are the main advantages of FastAPI over Flask or Django REST Framework?**
- **Async Support**: Native async/await support (unlike Flask).  
- **Performance**: Built on ASGI (Starlette) for high concurrency.  
- **Automatic Docs**: Auto-generated Swagger UI and ReDoc.  
- **Type Hints**: Built-in validation, serialization, and error handling via Pydantic.  
- **Modern Standards**: OpenAPI, JSON Schema, OAuth2.

---

3. **How does FastAPI leverage Python type hints?**
    
    Type hints define expected data types for parameters, request bodies, and responses. FastAPI uses them to:  
- Validate incoming data.  
- Convert data between JSON and Python objects.  
- Generate API documentation with expected data types.  

---
4. **What is ASGI, and why does FastAPI use it?**

ASGI (Asynchronous Server Gateway Interface) enables async-capable servers (e.g., Uvicorn). FastAPI uses ASGI to handle asynchronous requests efficiently, supporting non-blocking I/O operations for scalability with high concurrency.

---
5. **Explain the request–response flow in a FastAPI app.**
   1. Request received by ASGI server (e.g., Uvicorn).  
   2. FastAPI parses URL, headers, and parameters.  
   3. Validates data using type hints and Pydantic models.  
   4. Executes the route handler (synchronous or async).  
   5. Serializes the response using the defined response model.  
   6. Returns HTTP response with status code, headers, and body.  


## 🛣️ Routing & Path Parameters

6. **How do you declare routes (endpoints) in FastAPI?**
 
 Use decorators with HTTP methods (e.g., `@app.get("/items")`):  
   ```python
   from fastapi import FastAPI
   app = FastAPI()

   @app.get("/items")
   async def read_items():
       return [{"item": "Foo"}]
   ```

7. **How do you capture path parameters and enforce types?**

Define parameters in the URL path and annotate their types:  
   ```python
   @app.get("/items/{item_id}")
   async def read_item(item_id: int):  # Enforces integer type
       return {"item_id": item_id}
   ```
   Invalid types trigger automatic validation errors.

8. **What’s the difference between `path`, `query`, `body`, and `header` parameters, and how do you define each?**
- **Path**: Part of the URL (e.g., `/{item_id}`).  
- **Query**: After `?` (e.g., `?skip=0`). Declared as non-path function parameters.  
- **Body**: Sent in the request body (requires Pydantic model or `Body(...)`).  
- **Header**: Extracted from HTTP headers using `Header(...)`. 


9. **How do you return custom status codes and headers from an endpoint?**
- **Status Code**: Set `status_code` in the decorator:  
    ```python
    @app.post("/items", status_code=201)
    ```
    For dynamic codes, return a `Response` object.  
- **Headers**: Return a `Response` with `headers` parameter:  
    ```python
    from fastapi import Response
    return Response(content=data, headers={"X-Header": "value"})
    ```

10. **How can you handle wildcard (“catch-all”) paths?**
Use `:path` to capture all subpaths:  
    ```python
    @app.get("/files/{file_path:path}")
    async def read_file(file_path: str):
        return {"file_path": file_path}
    ```
    Handles `/files/some/folder/file.txt` → `file_path = "some/folder/file.txt"`.

---

## 🔍 Data Validation & Serialization

11. **What role does Pydantic play in FastAPI?**

Pydantic provides data validation, parsing, and serialization using Python type hints. FastAPI uses Pydantic models to:  
   - Validate request bodies, query parameters, and path parameters.  
   - Automatically generate API documentation (OpenAPI/Swagger).  
   - Convert complex data types (e.g., `datetime`, `UUID`) to/from JSON. 

12. **How do you define and nest Pydantic models for request and response schemas?**
```python
   from pydantic import BaseModel

   class Item(BaseModel):
       name: str
       price: float

   class User(BaseModel):
       id: int
       items: list[Item]  # Nested model

   @app.post("/users")
   async def create_user(user: User):  # Request body schema
       return user
   ```

13. **How can you set default values, optional fields, and field-level validations?**
- **Defaults**: Use `Field(default=...)` or Python’s `Optional` type.  
- **Validation**: Use `Field` constraints like `gt`, `max_length`, or custom validators.  
```python
from pydantic import Field

class Item(BaseModel):
    name: str = Field(..., min_length=3, regex="^[A-Za-z ]+$")
    price: float = Field(gt=0, description="Must be positive")
    discount: Optional[float] = None  # Optional field
```

14. **How do you customize JSON encoders (e.g., for `datetime` or `UUID`)?**
Override the `json_encoder` in a Pydantic model’s `Config`:  
```python
from datetime import datetime

class CustomModel(BaseModel):
    timestamp: datetime

    class Config:
        json_encoder = {datetime: lambda dt: dt.isoformat()}
```
For global overrides, use `app.json_encoder`.

15. **What happens if client data fails validation?**
FastAPI automatically returns a `422 Unprocessable Entity` error with details about invalid fields, generated by Pydantic. Example response:  
   ```json
   {
     "detail": [
       {
         "loc": ["body", "price"],
         "msg": "ensure this value is greater than 0",
         "type": "value_error.number.not_gt"
       }
     ]
   }
   ```

---

## 🔗 Dependency Injection

16. **What is FastAPI’s dependency injection system?**

FastAPI’s DI system allows reusable components (e.g., database sessions, auth) to be injected into routes. It promotes modularity, reduces code duplication, and simplifies testing. Dependencies are declared with `Depends()`.

17. **How do you declare a dependency (e.g., a database session) and use it in multiple endpoints?**
```python
from fastapi import Depends

def get_db():
    db = SessionLocal()
    try:
        yield db  # Injects database session
    finally:
        db.close()

@app.get("/items")
async def read_items(db: Session = Depends(get_db)):
    return db.query(Item).all()
```

18. **What’s the difference between `Depends()` and `BackgroundTasks`?**
   - **`Depends()`**: Runs before the request and returns a value (e.g., auth check, database session).  
   - **`BackgroundTasks`**: Runs code **after** sending the response (e.g., sending emails, logging).  


19. **How do you manage “scoped” dependencies (per-request, per-session)?**
   
Use `yield` for per-request dependencies (e.g., database sessions):  
```python
def get_db():
    db = SessionLocal()
    yield db  # Created per request
    db.close()  # Closed after response
```
For session/singleton scopes, use context managers or tools like `lifespan`.

20. **How do you override dependencies for testing?**

Use `app.dependency_overrides` to replace dependencies during tests:  
```python
def override_get_db():
    return TestingSessionLocal()

app.dependency_overrides[get_db] = override_get_db
```

---

## ⚡ Asynchronous & Concurrency

21. **How does FastAPI support both sync and async view functions?**

FastAPI runs `async def` endpoints in the event loop (non-blocking) and `def` endpoints in a thread pool (blocking but avoids event loop starvation). ASGI enables this by handling async natively and offloading sync code to threads.

22. **When should you use `async def` versus `def` endpoints?**
- Use **`async def`** for I/O-bound tasks (e.g., database calls, external APIs).  
- Use **`def`** for CPU-bound tasks (e.g., heavy computations) or legacy sync code.  

23. **How do you perform background tasks or scheduled jobs?**
   
Use `BackgroundTasks` to run code post-response (e.g., logging, emails):  
```python
from fastapi import BackgroundTasks

def log_task(message: str):
    log.info(message)

@app.post("/items")
async def create_item(background_tasks: BackgroundTasks):
    background_tasks.add_task(log_task, "Item created")
    return {"status": "ok"}
```
For **scheduled jobs**, use `Celery` or `APScheduler`.


24. **How can you limit concurrency or rate-limit requests?**
- Use libraries like `SlowAPI` or custom middleware:  
    ```python
    from fastapi.middleware import Middleware
    from slowapi import Limiter, _rate_limit_exceeded_handler
    ```
- Track client IP/API keys and enforce limits using dependencies or middleware.


25. **How do you integrate WebSockets in FastAPI?**
 ```python
   from fastapi import WebSocket

   @app.websocket("/ws")
   async def websocket_endpoint(websocket: WebSocket):
       await websocket.accept()
       while True:
           data = await websocket.receive_text()
           await websocket.send_text(f"Echo: {data}")
   ```

---

## 🔒 Security & Auth

26. **How do you secure endpoints with API keys or HTTP Basic auth?**
 - **API Key**:  
    ```python
    from fastapi.security import APIKeyHeader
    api_key = APIKeyHeader(name="X-API-Key")

    @app.get("/secure")
    async def secure_endpoint(key: str = Depends(api_key)):
        return {"key": key}
    ```
- **HTTP Basic Auth**:  
    ```python
    from fastapi.security import HTTPBasic, HTTPBasicCredentials
    security = HTTPBasic()
    ```

27. **How do you implement OAuth2 (password flow, JWT tokens) in FastAPI?**
```
python
   from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

   oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

   @app.post("/token")
   async def login(form_data: OAuth2PasswordRequestForm = Depends()):
       # Validate user, return JWT
       return {"access_token": user.username, "token_type": "bearer"}
```
Use `python-jose` for JWT encoding/decoding.

28. **What built-in support exists for CORS and JSON Web Tokens?**
- **CORS**:  
    ```python
    from fastapi.middleware.cors import CORSMiddleware
    app.add_middleware(CORSMiddleware, allow_origins=["*"])
    ```
- **JWT**: Not built-in but integrates with `python-jose` or `PyJWT`.

29. **How do you hash and verify passwords securely?**

Use `passlib` with bcrypt:  
```python
   from passlib.context import CryptContext
   pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

   hashed_password = pwd_context.hash("secret")
   pwd_context.verify("secret", hashed_password)  # Returns True/False
```

30. **How do you restrict access to certain endpoints based on scopes or roles?**

Extend OAuth2 scopes:  
```python
from fastapi.security import SecurityScopes

async def require_admin(security_scopes: SecurityScopes, token: str = Depends(oauth2_scheme)):
    if "admin" not in security_scopes.scopes:
        raise HTTPException(403, "Insufficient permissions")
```

---
## 🧪 Testing & Validation

31. **How do you test FastAPI applications?**
  
  Use `TestClient` from `fastapi.testclient`:  
   ```python
   from fastapi.testclient import TestClient
   client = TestClient(app)

   def test_read_item():
       response = client.get("/items/1")
       assert response.status_code == 200
   ```


32. **What tools/libraries do you use for API testing (e.g., `TestClient`)?**
 - `TestClient` for HTTP/WebSocket testing.  
   - `pytest` for test orchestration.  
   - `unittest.mock` for mocking.


33. **How can you mock dependencies, databases, or external services in tests?**

Override dependencies:  
   ```python
   app.dependency_overrides[database_dependency] = mock_database
   ```
   Use `pytest-mock` for granular mocking.


34. **How do you test WebSocket endpoints?**
```python
   with client.websocket_connect("/ws") as websocket:
       websocket.send_text("Hello")
       data = websocket.receive_text()
       assert data == "Echo: Hello"
   ```

35. **What strategies do you use for integration vs. unit tests in FastAPI?**
- **Unit Tests**: Mock external services.  
- **Integration Tests**: Use real dependencies (e.g., test DB).

## 🚀 Performance & Deployment

36. **What built-in features help FastAPI achieve high performance?**
- ASGI (async support).  
- Pydantic (fast validation via Rust-based core).  
- Starlette’s lightweight routing.  

37. **How do you bundle and serve a FastAPI app in production (e.g., Uvicorn, Gunicorn, Docker)?**
- **Uvicorn/Gunicorn**:  
     ```bash
     gunicorn -w 4 -k uvicorn.workers.UvicornWorker app:app
     ```
- **Docker**:  
    ```dockerfile
    FROM python:3.9
    RUN pip install fastapi uvicorn
    COPY ./app /app
    CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0"]

38. **How can you enable HTTP/2, gRPC, or GraphQL with FastAPI?**
- **HTTP/2**: Enabled via Uvicorn.  
- **gRPC**: Use `grpcio` separately.  
- **GraphQL**: Integrate with `strawberry` or `graphene`.

39. **What monitoring, logging, and error-tracking best practices do you follow?**
- **Logging**: Python’s `logging` module with JSON formatting.  
- **APM**: Tools like Sentry or Prometheus.  
- **Middleware**: Log request/response metrics.

40. **How do you perform blue/green or canary deployments with FastAPI?**
- **Blue/Green**: Use load balancers (e.g., Nginx, AWS ALB).  
- **Canary**: Gradually route traffic (e.g., Istio, Kubernetes).  
