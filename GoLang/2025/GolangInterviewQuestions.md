## Golang Interview Questions

### 1. What is Go programming language?
Go, also known as Golang, is an open-source programming language developed by Google. It is designed to be efficient, simple, and easy to use, with a strong emphasis on concurrency and scalability, making it ideal for modern software development, especially for networked and distributed systems.

---

### 2. What are the key features of Go?
Go has several standout features:
- **Simplicity**: A clean, concise syntax that’s easy to learn and use.
- **Concurrency**: Built-in support for concurrent programming with goroutines and channels.
- **Garbage Collection**: Automatic memory management to simplify development.
- **Static Typing**: Compile-time type checking for better performance and safety.
- **Fast Compilation**: Quick compilation times, even for large projects.
- **Cross-Platform**: Compiles to run on multiple platforms like Windows, macOS, and Linux.

---

### 3. Who developed Go and when was it released?
Go was developed by Robert Griesemer, Rob Pike, and Ken Thompson at Google. It was first released in 2009.

---

### 4. Is Go statically or dynamically typed?
Go is **statically typed**, meaning type checking occurs at compile-time, which enhances efficiency and catches errors early in the development process.

---

### 5. What is the difference between var, const, and := in Go?
- **var**: Used to declare a variable with an optional initial value. Example: `var x int = 10`.
- **const**: Declares a constant value that cannot change. Example: `const pi = 3.14`.
- **:=**: Short variable declaration that declares and initializes a variable in one step (only within functions). Example: `x := 10`.

---

### 6. How is Golang different from other programming languages?
Go stands out due to:
- **Simplicity**: Minimalist syntax reduces complexity.
- **Concurrency**: Native support for goroutines and channels simplifies parallel programming.
- **Garbage Collection**: Automatic memory management, unlike C or C++.
- **Static Typing**: Compile-time type safety, unlike Python or JavaScript.
- **Fast Compilation**: Faster builds compared to languages like C++ or Java.

---

### 7. How do you declare multiple variables in a single line in Go?
You can declare multiple variables in one line using:
- **var**: `var a, b, c int = 1, 2, 3`
- **Short declaration**: `a, b, c := 1, 2, 3`

---

### 8. What is the zero value of a variable in Go?
The zero value is the default value assigned to a variable when declared without initialization:
- `int`: `0`
- `string`: `""` (empty string)
- `bool`: `false`
- Pointers, slices, maps, etc.: `nil`

---

### 9. What is the purpose of the blank identifier (_) in Go?
The blank identifier (`_`) is used to ignore values or indicate that a value isn’t needed. For example:
- Ignoring a return value: `_, err := someFunction()`
- Placeholder in loops or imports when the variable isn’t used.

---

### 10. What is a package in Go?
A package is a collection of related Go source files that group functions, types, and variables together. It organizes code and enables reusability. Example: The `fmt` package provides formatting and printing functions.

---

### 11. How do you import packages in Go?
Use the `import` keyword:
- Single package: `import "fmt"`
- Multiple packages:
  ```go
  import (
      "fmt"
      "os"
  )
  ```

---

### 12. What is the main package in Go?
The `main` package is the entry point of a Go program. It must contain a `main()` function, which is executed when the program starts.

---

### 13. What is the purpose of the init() function in Go?
The `init()` function is a special function that runs automatically when a package is initialized. It’s used for setup tasks like initializing variables or registering resources.

---
### 14. Can you have multiple init functions in the same package?
Yes, you can have multiple `init()` functions in a single package. They execute in the order they are defined.

---
### 15. What is a function in Go and how is it defined?
A function is a block of code that performs a specific task. It’s defined with the `func` keyword:
```go
func add(a int, b int) int {
    return a + b
}
```

---
### 16. How do you return multiple values from a function in Go?
Specify multiple return types in the function signature:
```go
func swap(a, b int) (int, int) {
    return b, a
}
```

---
### 17. What is a named return value in Go?
A named return value is a return variable named in the function signature, usable within the function:
```go
func add(a, b int) (sum int) {
    sum = a + b
    return // Implicitly returns sum
}
```

---
### 18. What is a variadic function in Go?
A variadic function accepts a variable number of arguments using the `...` operator:
```go
func sum(nums ...int) int {
    total := 0
    for _, num := range nums {
        total += num
    }
    return total
}
```

---

### 19. What are defer, panic, and recover in Go?
- **defer**: Schedules a function to run when the surrounding function returns.
- **panic**: Triggers a runtime error, halting normal execution.
- **recover**: Catches a panic to prevent program termination and handle it gracefully.

---

### 20. How does defer work in Go?
`defer` delays a function call until the surrounding function completes, executed in LIFO (last-in, first-out) order:
```go
func main() {
    defer fmt.Println("world")
    fmt.Println("hello")
}
// Outputs: hello world
```

---

### 21. What is the difference between panic and recover?
- **panic**: Initiates a runtime error, unwinding the stack until the program terminates or is caught.
- **recover**: Captures a panic in a deferred function, allowing the program to continue running.

---

### 22. What is a struct in Go?
A `struct` is a composite data type that groups variables (fields) of different types:
```go
type Person struct {
    Name string
    Age  int
}
```

---

### 23. How do you define and instantiate a struct in Go?
- **Define**:
  ```go
  type Person struct {
      Name string
      Age  int
  }
  ```
- **Instantiate**:
  ```go
  p := Person{Name: "John", Age: 30} // Struct literal
  // OR
  p := new(Person) // Returns a pointer
  p.Name = "John"
  p.Age = 30
  ```

---



### 24. How do you embed structs in Go?
Embedding includes one struct type within another without a field name:
```go
type Address struct {
    Street string
}
type Person struct {
    Name string
    Address // Embedded struct
}
```

---

### 25. What is a method in Go?
A method is a function tied to a specific type (receiver):
```go
type Person struct {
    Name string
}
func (p Person) SayHello() {
    fmt.Println("Hello, ", p.Name)
}
```

---

### 26. What is the difference between a function and a method in Go?
- **Function**: Standalone code block, e.g., `func add(a, b int) int`.
- **Method**: Function associated with a type via a receiver, e.g., `func (p Person) SayHello()`.

---

### 27. What is an interface in Go?
An interface defines a set of method signatures that a type must implement:
```go
type Shape interface {
    Area() float64
}
```

---

### 28. How do you implement an interface in Go?
A type implements an interface by defining all its methods:
```go
type Rectangle struct {
    Width, Height float64
}
func (r Rectangle) Area() float64 {
    return r.Width * r.Height
}
```

---

### 29. What is the empty interface and when would you use it?
The empty interface (`interface{}`) has no methods and can hold any type. Use it for generic programming when the type is unknown, e.g., in functions handling diverse data.

---

### 30. How does Go achieve polymorphism?
Go achieves polymorphism through interfaces. Functions accepting interfaces can work with any type implementing those interfaces, enabling flexible, type-agnostic code.

---

### 31. What are slices in Go?
Slices are dynamically-sized views into arrays:
```go
s := []int{1, 2, 3}
```

---

### 33. What is the difference between arrays and slices?
- **Array**: Fixed-size sequence, e.g., `[3]int{1, 2, 3}`.
- **Slice**: Dynamic, flexible view into an array, e.g., `[]int{1, 2, 3}`.

---

### 34. How do you append to a slice in Go?
Use the `append` function:
```go
s := []int{1, 2}
s = append(s, 3) // s is now [1, 2, 3]
```

---

### 35. What is the zero value of a slice in Go?
The zero value of a slice is `nil`, representing an empty slice.

---

### 36. How do you copy a slice in Go?
Use the `copy` function:
```go
src := []int{1, 2, 3}
dst := make([]int, len(src))
copy(dst, src)
```

---

### 37. What is the capacity of a slice and how is it different from length?
- **Length**: Number of elements currently in the slice.
- **Capacity**: Number of elements the slice can hold before reallocation. Capacity ≥ Length.

---

### 38. How do you create slices using make in Go?
Use `make` to specify length and capacity:
```go
s := make([]int, 3, 5) // Length 3, capacity 5
```

---

### 39. What are maps in Go?
Maps are collections of key-value pairs:
```go
m := map[string]int{"a": 1, "b": 2}
```

---

### 40. How do you check if a key exists in a map?
Use the comma-ok idiom:
```go
value, ok := m["a"]
if ok {
    // Key exists
}
```

---

### 41. How do you delete a key from a map?
Use the `delete` function:
```go
delete(m, "a")
```

---

### 42. What is a pointer in Go?
A pointer stores the memory address of a variable:
```go
var p *int
i := 42
p = &i
```

---

### 43. How do you declare and dereference a pointer in Go?
- **Declare**: `var p *int`
- **Dereference**: `*p` accesses the value at the pointer’s address.

---

### 44. Can you have a pointer to a pointer in Go?
Yes:
```go
var pp **int
p := &i
pp = &p
```

---

### 45. What is the new keyword in Go?
`new` allocates memory for a type and returns a pointer:
```go
p := new(int) // *p is 0
```

---

### 46. What is the make keyword in Go?
`make` creates and initializes slices, maps, and channels:
```go
s := make([]int, 3)
```

---

### 47. What are the differences between make and new?
- **make**: Initializes slices, maps, channels; returns the type.
- **new**: Allocates memory for any type; returns a pointer.

---

### 48. What are goroutines in Go?
Goroutines are lightweight threads managed by the Go runtime for concurrent execution.

---

### 49. How do you create a goroutine?
Use the `go` keyword:
```go
go func() {
    // Concurrent code
}()
```

---

### 50. What are channels in Go?
Channels are typed conduits for communication between goroutines:
```go
c := make(chan int)
```

---

### 51. How do you send and receive values on a channel?
- **Send**: `c <- 42`
- **Receive**: `value := <-c`

---

### 52. What is the difference between buffered and unbuffered channels?
- **Unbuffered**: Blocks until sender and receiver are ready.
- **Buffered**: Allows sends up to capacity without blocking.

---

### 53. How do you close a channel and why would you do it?
Use `close(c)` to signal no more values will be sent, helping receivers detect the end of transmission.

---

### 54. What is a select statement in Go?
A `select` statement multiplexes multiple channel operations:
```go
select {
case v := <-c1:
    fmt.Println(v)
case c2 <- 1:
    fmt.Println("Sent")
}
```

---

### 55. How do you use select to multiplex channels?
`select` waits for one of multiple channel operations to proceed, executing the corresponding case.

---

### 56. What are the benefits of using goroutines?
- Concurrency for multi-core utilization.
- Simple syntax for concurrent code.
- Efficient, lightweight execution.

---

### 57. How do you prevent race conditions in Go?
Use synchronization tools like mutexes from the `sync` package to protect shared resources.

---

### 58. What is the sync package in Go?
The `sync` package provides primitives like mutexes and wait groups for synchronization.

---

### 59. What are Mutex and RWMutex in Go?
- **Mutex**: Ensures exclusive access to a resource.
- **RWMutex**: Allows multiple readers or one writer.

---

### 60. What is a WaitGroup in Go?
A `WaitGroup` waits for a set of goroutines to finish:
```go
var wg sync.WaitGroup
wg.Add(1)
go func() {
    defer wg.Done()
    // Work
}()
wg.Wait()
```

---

### 61. How do you use a WaitGroup to wait for goroutines to finish?
`Add` sets the number of goroutines, `Done` signals completion, and `Wait` blocks until all are done.

---

### 62. What is the context package in Go and how is it used?
The `context` package manages deadlines, cancellations, and values across goroutines, often for request scoping.

---

### 63. How do you handle timeouts and cancellations with context?
Use `context.WithTimeout` or `context.WithCancel`:
```go
ctx, cancel := context.WithTimeout(context.Background(), 5*time.Second)
defer cancel()
```

---

### 64. What is the difference between context.Background() and context.TODO()?
- **Background()**: Empty, non-cancelable root context.
- **TODO()**: Placeholder for future specific context.

---

### 65. What is the difference between Go modules and GOPATH?
- **GOPATH**: Legacy single-directory dependency management.
- **Go Modules**: Per-project dependency management with versioning.

---

### 66. How do you initialize a Go module?
Run `go mod init module-name`, e.g., `go mod init example.com/myproject`.

---

### 67. What is the go.mod file?
The `go.mod` file defines a module’s name, version, and dependencies.

---

### 68. What is the go.sum file?
The `go.sum` file contains checksums for dependency integrity.

---

### 69. How do you manage dependencies in Go?
Use `go mod` commands, e.g., `go get example.com/package` to add dependencies.

---

### 70. What are Go tools like go build, go run, go test, etc.?
- `go build`: Compiles code into a binary.
- `go run`: Compiles and runs code.
- `go test`: Executes tests.

---

### 71. How do you format code in Go?
Run `go fmt` to apply standard Go formatting.

---

### 72. How do you write tests in Go?
Create `_test.go` files with functions like:
```go
func TestAdd(t *testing.T) {
    if add(1, 2) != 3 {
        t.Errorf("Expected 3, got %d", add(1, 2))
    }
}
```

---

### 73. What is the testing package in Go?
The `testing` package supports writing tests, benchmarks, and examples.

---

### 74. How do you write benchmarks in Go?
Use `Benchmark` functions:
```go
func BenchmarkAdd(b *testing.B) {
    for i := 0; i < b.N; i++ {
        add(1, 2)
    }
}
```

---

### 75. What is a table-driven test in Go?
A test using a table of inputs and expected outputs:
```go
func TestAdd(t *testing.T) {
    tests := []struct{ a, b, expected int }{
        {1, 2, 3},
        {4, 5, 9},
    }
    for _, tt := range tests {
        if got := add(tt.a, tt.b); got != tt.expected {
            t.Errorf("Expected %d, got %d", tt.expected, got)
        }
    }
}
```

---

### 76. What are common Go project structures?
- Single package in one directory.
- Multiple packages in subdirectories.
- `cmd/` for binaries, `pkg/` for libraries, `internal/` for private code.

---

### 77. What is the error type in Go?
The `error` interface has an `Error() string` method to represent errors.

---

### 78. How do you create custom errors in Go?
Define a type implementing `error`:
```go
type MyError struct {
    Msg string
}
func (e MyError) Error() string {
    return e.Msg
}
```

---

### 79. What is the errors.New and fmt.Errorf function?
- `errors.New`: Creates a basic error: `errors.New("oops")`.
- `fmt.Errorf`: Formats an error: `fmt.Errorf("oops: %v", details)`.

---

### 80. How do you wrap errors in Go?
Use `fmt.Errorf` with `%w`:
```go
err := fmt.Errorf("wrapped: %w", originalErr)
```

---

### 81. How do you compare errors in Go?
Use `errors.Is`:
```go
if errors.Is(err, targetErr) {
    // Matches err or wrapped err
}
```

---

### 82. What is error unwrapping in Go?
Unwrapping extracts the underlying error with `errors.Unwrap` or checks type with `errors.As`.

---

### 83. What is the purpose of the io package in Go?
The `io` package provides interfaces and functions for I/O operations like reading and writing.

---

### 84. What is the difference between io.Reader and io.Writer?
- `io.Reader`: Reads data from a source.
- `io.Writer`: Writes data to a destination.

---

### 85. What are the benefits of using interfaces like io.Reader?
- Abstraction for generic I/O operations.
- Reusability across different types.
- Easier testing with mocks.

---

### 86. What is a type assertion in Go?
Checks an interface value’s concrete type:
```go
var i interface{} = "hello"
s, ok := i.(string)
```

---

### 87. What is a type switch in Go?
Switches on a value’s type:
```go
switch v := i.(type) {
case string:
    fmt.Println(v)
case int:
    fmt.Println(v)
}
```

---

### 88. What are constants in Go?
Constants are immutable values:
```go
const pi = 3.14
```

---

### 89. What is iota in Go?
`iota` simplifies enumerated constants:
```go
const (
    a = iota // 0
    b        // 1
    c        // 2
)
```

---

### 90. How is memory management handled in Go?
Go uses a garbage collector to automatically manage memory allocation and deallocation.

---

### 91. What is garbage collection in Go?
The process of freeing unused memory automatically using a concurrent mark-and-sweep algorithm.

---

### 92. What is the unsafe package in Go?
The `unsafe` package allows low-level operations like pointer arithmetic, bypassing type safety.

---

### 93. What is reflection in Go?
Reflection inspects and manipulates types and values at runtime via the `reflect` package.

---

### 94. What is the reflect package used for?
- Inspecting types and values.
- Dynamic function calls.
- Creating or modifying values.

---

### 95. What is embedding and how does it differ from inheritance?
Embedding composes structs by including them, unlike inheritance, which creates a subclass relationship.

---

### 96. What is shadowing in Go?
A variable in an inner scope hides an outer variable with the same name:
```go
x := 1
if true {
    x := 2 // Shadows outer x
}
```

---

### 97. What is the difference between value receivers and pointer receivers?
- **Value Receiver**: `(t T)` works on copies, callable on values and pointers.
- **Pointer Receiver**: `(t *T)` works on pointers, modifying the original.

---

### 98. What is the difference between deep copy and shallow copy?
- **Shallow Copy**: Copies references (e.g., slices).
- **Deep Copy**: Copies values into new memory.

---

### 99. What is the difference between concurrency and parallelism?
- **Concurrency**: Managing multiple tasks simultaneously.
- **Parallelism**: Executing tasks at the same time on multiple cores.

---

### 100. How does Go support concurrency?
Through goroutines (concurrent execution) and channels (communication).

---

### 101. What is the runtime package in Go?
The `runtime` package interacts with the Go runtime for goroutine control, memory management, etc.

---

### 102. What is the difference between runtime.Gosched() and time.Sleep()?
- `runtime.Gosched()`: Yields to other goroutines.
- `time.Sleep()`: Pauses for a duration.

---

### 103. What is the build constraint or build tag in Go?
A comment like `// +build linux` controls file inclusion based on build conditions.

---

### 104. How do you create and use tags in struct fields?
Add tags in backticks:
```go
type Person struct {
    Name string `json:"name"`
}
```
Used by packages like `encoding/json`.

---

### 105. What is the go:generate directive?
A comment like `//go:generate mockgen ...` runs a command with `go generate`.

---

### 106. How does Go handle JSON encoding and decoding?
Using `encoding/json`:
- `json.Marshal`: Encodes to JSON.
- `json.Unmarshal`: Decodes from JSON.

---

### 107. What are common packages used for web development in Go?
- `net/http`: HTTP server/client.
- `html/template`: HTML templating.
- `database/sql`: SQL database access.

---

### 108. What is the net/http package?
Provides HTTP server and client functionality.

---

### 109. How do you create an HTTP server in Go?
```go
http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
    fmt.Fprintf(w, "Hello")
})
http.ListenAndServe(":8080", nil)
```

---

### 110. What are third-party web frameworks in Go?
- Gin: Lightweight and fast.
- Echo: Minimalist.
- Revel: Full-stack.

---

### 111. What are some best practices in Go programming?
- Use clear naming.
- Keep functions focused.
- Handle errors properly.
- Leverage concurrency safely.
- Write tests.
- Use Go modules.

---