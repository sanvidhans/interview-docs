# Golang Interview Preparation Guide

## Basic Syntax, Data Types, and Control Structures

**Data Types:**
- Basic types: `int`, `float64`, `string`, `bool`
- Composite types: arrays, slices, maps, structs, channels
- Zero values: `0` for numbers, `""` for strings, `false` for bools, `nil` for pointers/slices/maps

**Control Structures:**
```go
// If statement
if x > 0 {
    // code
} else if x == 0 {
    // code
} else {
    // code
}

// For loops (only loop in Go)
for i := 0; i < 10; i++ {}     // traditional
for key, value := range map {} // range
for condition {}               // while-like
for {}                        // infinite

// Switch
switch value {
case 1:
    // code
default:
    // code
}
```

## Functions, Methods, and Structs

**Functions:**
```go
func add(a, b int) int {
    return a + b
}

// Multiple returns
func divide(a, b float64) (float64, error) {
    if b == 0 {
        return 0, errors.New("division by zero")
    }
    return a / b, nil
}

// Variadic functions
func sum(nums ...int) int {
    total := 0
    for _, num := range nums {
        total += num
    }
    return total
}
```

**Structs and Methods:**
```go
type Person struct {
    Name string
    Age  int
}

// Method with receiver
func (p Person) Greet() string {
    return "Hello, " + p.Name
}

// Pointer receiver (can modify)
func (p *Person) Birthday() {
    p.Age++
}
```

## Interfaces and Basic Concurrency

**Interfaces:**
```go
type Writer interface {
    Write([]byte) (int, error)
}

// Empty interface
interface{} // can hold any type

// Type assertion
var i interface{} = "hello"
s := i.(string)
s, ok := i.(string) // safe assertion
```

**Basic Concurrency:**
```go
// Goroutine
go func() {
    fmt.Println("Running in goroutine")
}()

// Channels
ch := make(chan int)
go func() {
    ch <- 42 // send
}()
value := <-ch // receive

// Buffered channel
ch := make(chan int, 3)
```

## HTTP Server Development

```go
package main

import (
    "fmt"
    "net/http"
)

func handler(w http.ResponseWriter, r *http.Request) {
    fmt.Fprintf(w, "Hello, %s!", r.URL.Path[1:])
}

func main() {
    http.HandleFunc("/", handler)
    http.ListenAndServe(":8080", nil)
}

// Using ServeMux
mux := http.NewServeMux()
mux.HandleFunc("/api/users", usersHandler)
http.ListenAndServe(":8080", mux)
```

## JSON Handling and API Development

```go
type User struct {
    ID   int    `json:"id"`
    Name string `json:"name"`
    Email string `json:"email,omitempty"`
}

// Marshal (struct to JSON)
user := User{ID: 1, Name: "John"}
jsonData, err := json.Marshal(user)

// Unmarshal (JSON to struct)
var user User
err := json.Unmarshal(jsonData, &user)

// API handler
func usersHandler(w http.ResponseWriter, r *http.Request) {
    w.Header().Set("Content-Type", "application/json")
    
    switch r.Method {
    case "GET":
        users := []User{{ID: 1, Name: "John"}}
        json.NewEncoder(w).Encode(users)
    case "POST":
        var user User
        json.NewDecoder(r.Body).Decode(&user)
        // process user
        w.WriteHeader(http.StatusCreated)
    }
}
```

## Basic Testing and Error Handling

**Error Handling:**
```go
// Custom error
type ValidationError struct {
    Field string
    Message string
}

func (e ValidationError) Error() string {
    return fmt.Sprintf("%s: %s", e.Field, e.Message)
}

// Error wrapping (Go 1.13+)
import "errors"
err := errors.New("base error")
wrappedErr := fmt.Errorf("operation failed: %w", err)
```

**Testing:**
```go
// user_test.go
func TestAdd(t *testing.T) {
    result := Add(2, 3)
    expected := 5
    if result != expected {
        t.Errorf("Add(2, 3) = %d; want %d", result, expected)
    }
}

// Table-driven tests
func TestAdd(t *testing.T) {
    tests := []struct {
        a, b, expected int
    }{
        {2, 3, 5},
        {0, 0, 0},
        {-1, 1, 0},
    }
    
    for _, test := range tests {
        result := Add(test.a, test.b)
        if result != test.expected {
            t.Errorf("Add(%d, %d) = %d; want %d", 
                test.a, test.b, result, test.expected)
        }
    }
}
```

## Pointers

```go
var x int = 42
var p *int = &x  // p points to x
fmt.Println(*p)  // dereference: prints 42

// When to use pointers:
// 1. Modify the original value
func increment(x *int) {
    *x++
}

// 2. Avoid copying large structs
func processLargeStruct(s *LargeStruct) {
    // work with s
}

// 3. Optional values (can be nil)
var name *string // nil by default
```

## Advanced Concurrency Patterns

**Worker Pool:**
```go
func workerPool(jobs <-chan int, results chan<- int) {
    for job := range jobs {
        results <- job * 2 // simulate work
    }
}

func main() {
    jobs := make(chan int, 100)
    results := make(chan int, 100)
    
    // Start 3 workers
    for w := 1; w <= 3; w++ {
        go workerPool(jobs, results)
    }
    
    // Send jobs
    for j := 1; j <= 5; j++ {
        jobs <- j
    }
    close(jobs)
    
    // Collect results
    for a := 1; a <= 5; a++ {
        <-results
    }
}
```

**Fan-in/Fan-out:**
```go
// Fan-out: distribute work
func fanOut(in <-chan int) (<-chan int, <-chan int) {
    out1 := make(chan int)
    out2 := make(chan int)
    
    go func() {
        defer close(out1)
        defer close(out2)
        for val := range in {
            out1 <- val
            out2 <- val
        }
    }()
    
    return out1, out2
}

// Fan-in: merge channels
func fanIn(ch1, ch2 <-chan int) <-chan int {
    out := make(chan int)
    go func() {
        defer close(out)
        for {
            select {
            case val, ok := <-ch1:
                if !ok {
                    ch1 = nil
                } else {
                    out <- val
                }
            case val, ok := <-ch2:
                if !ok {
                    ch2 = nil
                } else {
                    out <- val
                }
            }
            if ch1 == nil && ch2 == nil {
                break
            }
        }
    }()
    return out
}
```

## Context Package

```go
import "context"

// With timeout
ctx, cancel := context.WithTimeout(context.Background(), 5*time.Second)
defer cancel()

// With cancellation
ctx, cancel := context.WithCancel(context.Background())
defer cancel()

// With values
ctx = context.WithValue(ctx, "userID", 123)
userID := ctx.Value("userID").(int)

// Usage in HTTP
func handler(w http.ResponseWriter, r *http.Request) {
    ctx := r.Context()
    
    select {
    case <-time.After(5 * time.Second):
        // work completed
    case <-ctx.Done():
        // request cancelled
        http.Error(w, "Request cancelled", http.StatusRequestTimeout)
        return
    }
}
```

## Interface Design and Composition

```go
// Small, focused interfaces
type Reader interface {
    Read([]byte) (int, error)
}

type Writer interface {
    Write([]byte) (int, error)
}

type ReadWriter interface {
    Reader
    Writer
}

// Composition over inheritance
type Engine struct {
    Power int
}

func (e Engine) Start() {
    fmt.Println("Engine started")
}

type Car struct {
    Engine  // embedded
    Brand string
}

car := Car{
    Engine: Engine{Power: 200},
    Brand: "Toyota",
}
car.Start() // calls Engine.Start()
```

## Memory Management and GC

**Key Points:**
- Go has automatic garbage collection
- Stack vs Heap allocation
- Escape analysis determines allocation location
- Use `go build -gcflags="-m"` to see escape analysis

**Performance Tips:**
```go
// Avoid frequent allocations
// Bad
for i := 0; i < 1000; i++ {
    slice := make([]int, 100) // allocates each time
}

// Good
slice := make([]int, 100)
for i := 0; i < 1000; i++ {
    // reuse slice
}

// Pool for reusing objects
var pool = sync.Pool{
    New: func() interface{} {
        return make([]byte, 1024)
    },
}

buf := pool.Get().([]byte)
defer pool.Put(buf)
```

## Error Handling Patterns

```go
// Sentinel errors
var ErrNotFound = errors.New("not found")

// Custom error types
type NetworkError struct {
    Op  string
    Err error
}

func (e *NetworkError) Error() string {
    return fmt.Sprintf("network error in %s: %v", e.Op, e.Err)
}

// Error wrapping (Go 1.13+)
if err != nil {
    return fmt.Errorf("failed to process user %d: %w", userID, err)
}

// Error checking
if errors.Is(err, ErrNotFound) {
    // handle not found
}

var netErr *NetworkError
if errors.As(err, &netErr) {
    // handle network error
}
```

## Testing Strategies

```go
// Unit test
func TestCalculate(t *testing.T) {
    result := Calculate(10, 5)
    assert.Equal(t, 15, result)
}

// Benchmark
func BenchmarkCalculate(b *testing.B) {
    for i := 0; i < b.N; i++ {
        Calculate(10, 5)
    }
}

// Integration test with HTTP
func TestAPIEndpoint(t *testing.T) {
    req := httptest.NewRequest("GET", "/api/users", nil)
    rr := httptest.NewRecorder()
    
    handler := http.HandlerFunc(usersHandler)
    handler.ServeHTTP(rr, req)
    
    assert.Equal(t, http.StatusOK, rr.Code)
}

// Test with dependencies (mocking)
type MockDB struct{}
func (m MockDB) GetUser(id int) (*User, error) {
    return &User{ID: id, Name: "Test"}, nil
}
```

## Go Modules and Dependency Management

```bash
# Initialize module
go mod init github.com/username/project

# Add dependency
go get github.com/gin-gonic/gin

# Update dependencies
go mod tidy

# Vendor dependencies
go mod vendor
```

**go.mod file:**
```
module github.com/username/project

go 1.21

require (
    github.com/gin-gonic/gin v1.9.1
)

replace github.com/old/package => github.com/new/package v1.0.0
```

## Handling Circular Dependencies

**Problem:** Package A imports B, Package B imports A

**Solutions:**
1. **Extract common interface:**
```go
// common/interfaces.go
type UserService interface {
    GetUser(id int) (*User, error)
}

// user/service.go - implements interface
// order/service.go - uses interface, not concrete type
```

2. **Dependency Injection:**
```go
type OrderService struct {
    userService UserService // interface, not concrete
}

func NewOrderService(us UserService) *OrderService {
    return &OrderService{userService: us}
}
```

3. **Event-driven architecture:**
```go
type EventBus interface {
    Publish(event Event)
    Subscribe(eventType string, handler EventHandler)
}
```

## Key Packages

**net/http:**
```go
// Server
http.HandleFunc("/", handler)
http.ListenAndServe(":8080", nil)

// Client
resp, err := http.Get("https://api.example.com")
defer resp.Body.Close()
```

**io:**
```go
// Copy
io.Copy(dst, src)

// Read all
data, err := io.ReadAll(reader)

// Pipe
r, w := io.Pipe()
```

**fmt:**
```go
fmt.Printf("%d %s %.2f\n", 42, "hello", 3.14159)
fmt.Sprintf("formatted string: %v", value)
```

**context:**
```go
ctx, cancel := context.WithTimeout(context.Background(), 30*time.Second)
defer cancel()
```

**time:**
```go
now := time.Now()
time.Sleep(time.Second * 5)
timer := time.NewTimer(time.Minute)
ticker := time.NewTicker(time.Second)
```

**sync:**
```go
var mu sync.Mutex
var wg sync.WaitGroup
var once sync.Once
```

## Microservices Architecture

**Key Concepts:**
- Service discovery
- Load balancing
- Circuit breaker pattern
- API Gateway
- Distributed tracing

```go
// Service registration
type Service struct {
    Name    string
    Address string
    Port    int
    Health  string
}

// Circuit breaker
type CircuitBreaker struct {
    maxFailures int
    timeout     time.Duration
    state       State
}

func (cb *CircuitBreaker) Call(fn func() error) error {
    if cb.state == Open {
        return ErrCircuitOpen
    }
    
    err := fn()
    if err != nil {
        cb.failures++
        if cb.failures >= cb.maxFailures {
            cb.state = Open
        }
    }
    return err
}
```

## Design Patterns in Go

**Singleton:**
```go
type singleton struct{}

var instance *singleton
var once sync.Once

func GetInstance() *singleton {
    once.Do(func() {
        instance = &singleton{}
    })
    return instance
}
```

**Factory:**
```go
type Animal interface {
    Speak() string
}

func CreateAnimal(animalType string) Animal {
    switch animalType {
    case "dog":
        return &Dog{}
    case "cat":
        return &Cat{}
    default:
        return nil
    }
}
```

**Observer:**
```go
type Observer interface {
    Update(data interface{})
}

type Subject struct {
    observers []Observer
}

func (s *Subject) Attach(o Observer) {
    s.observers = append(s.observers, o)
}

func (s *Subject) Notify(data interface{}) {
    for _, observer := range s.observers {
        observer.Update(data)
    }
}
```

## Troubleshooting and Debugging

**Tools:**
- `go build -race` - race condition detection
- `go tool pprof` - profiling
- `dlv` (Delve) - debugger
- `go vet` - static analysis

**Common Issues:**
```go
// Race condition
var counter int
go func() { counter++ }()
go func() { counter++ }()

// Fix with mutex
var mu sync.Mutex
go func() {
    mu.Lock()
    counter++
    mu.Unlock()
}()

// Memory leak - goroutine not terminating
go func() {
    for {
        select {
        case <-done: // add cancellation
            return
        case <-time.After(time.Second):
            // work
        }
    }
}()
```

## Gin Framework

```go
import "github.com/gin-gonic/gin"

func main() {
    r := gin.Default()
    
    // Middleware
    r.Use(gin.Logger())
    r.Use(gin.Recovery())
    
    // Routes
    r.GET("/users/:id", getUser)
    r.POST("/users", createUser)
    
    // Group routes
    api := r.Group("/api/v1")
    {
        api.GET("/users", getUsers)
        api.POST("/users", createUser)
    }
    
    r.Run(":8080")
}

func getUser(c *gin.Context) {
    id := c.Param("id")
    user := User{ID: id, Name: "John"}
    c.JSON(200, user)
}

func createUser(c *gin.Context) {
    var user User
    if err := c.ShouldBindJSON(&user); err != nil {
        c.JSON(400, gin.H{"error": err.Error()})
        return
    }
    c.JSON(201, user)
}
```

## Scenario-Based Questions

**Designing Scalable API:**
- Use connection pooling
- Implement rate limiting
- Add caching layer (Redis)
- Use async processing for heavy tasks
- Implement circuit breaker
- Add monitoring and metrics

**Handling High Traffic:**
- Horizontal scaling
- Load balancing
- Database read replicas
- CDN for static content
- Queue systems for async processing
- Optimize database queries
- Use connection pooling