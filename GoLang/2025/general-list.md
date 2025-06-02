## Golang most asked questions

#### 1. What are the prominent features of Go? OR What are the benifits of using Go? OR Why Go is so popular?

#### 2. What do you mean by GOPATH and GOROOT? OR What is the difference between GOPATH and GOROOT? OR What GOPATH and GOROOT?

- GOPATH is a variable that defines your root of workspace directory.
- GOPATH stores your codebase and all the files that are necessary for your development
- If the environment variable is unset, GOPATH defaults to a subdirectory named go in the user's home directory
- You can check GOPATH by using this command `go env GOPATH`
- GOPATH is a root of your workspace and contains these directories like, src, pkg, and bin.
- src/: location of Go source code
- pkg/: location of compiled package code (for example: .a)
- bin/: location of executable programs built by Go
- GOROOT is a variable that defines your Go SDK is located
- GOROOT is for compiler and for the tools that come from go installation
- GOROOT should always be set tot he go installation directory
- You can check GOPATH by using this command `go env GOROOT`

#### 3. What do you mean by Go runtime? OR What is Go runtime? OR What is Go runtime environment?

- runtime is a package in a go standard library
- It is a part of every go program.
- It implements garbase collection, concurency, stack management etc.
- GOMAXPROCS: to control number of goroutines in the system
- GOGC: To set the initial garbage collection target percentage
- GORACE: To configures race condition detector for the programs and so on.


#### 4. What is the difference between Concurrency and Parallelism? OR What is concurrent execution and what is Parallel execution?

- Two or more processes are said to be concurrent if they are executing seemingly at the same time.
- Concurrent processes often share the same CPU
- While one process is executing on a CPU, other concurrent processes wait for the same CPU
- For example: Task1 and Task2 are executing seemingly at the same time on the same CPU
- Whenever Task1 is under execution; Task 2 is waiting, (same is true for Task2)
- Thus, Task 1 and Task 2 are executing CONCURRENTLY
- Concurrency could be achieve on a single as well as more CPUs.
- go runtime inherently supports concurrent execution of the goroutines. 
- Two or more processes are said to be parallel if they are executing exactly at the same time.
- Parallel processes do not share the same CPU
- While one process is executing on one CPU; other parallel processes keep executing on the other CPUs simultaneously.
- Parallelism cant not achieve on the single CPU.
- Notice that parallelism could be achieve on the multi core CPUs/ multi processors.

#### 5. Is Golang Platform Independent or Portable or both? OR Is Go a multi-platform language?

- Yes, it is a platform independent.
- A programming language is said to be platform independent if you can compile the code once and run the same compiled code on any operating system.
- Compile Once Run Anywhere (CORA)
- In case of Golang; we need to generate separate platform (OS) specific binaries as:
- GOOS=window GOARCH=amd64 go build -o bin/app-amd64.exe app.go

#### 6. Can interface types embed other interfaces?
- Yes, But, this could cause confusion as its always not clear, which methods are required by the interface and which are inherited from the embedded interfaces.

#### 7. Can interface methods have pointer receivers?
- Yes, this means that the receiver variable will be pointer to the underlying type, & not the value itself.

#### 8. Interfaces can cause panic:
- interfaces can cause runtime panic if a method is called on a nil interface value to avoid this always check for nil before calling a method on an interface.

#### 9. interface values are not pointer values:
- When an interface value is assigned to a variable, the value component is copied, meaning if the original value is a pointer, the copied value will not be a pointer, and changes made to the original value will not be reflected in the copied value.

#### 10. Components of interface values:
- interface values are made up of two components a `type` and a `value`.

#### 11. Interfaces are implicit
- In Go, interfaces are implemented implicitly meaning a type satisfies an interface if it has all the methods required by the interface.

#### 12. Nil Pointer?
- Go does not allow you to dereference a nil pointer because this can cause a panic if not handled properly

#### 13. How to dereference a variable?

#### 14. panic recover:
- be careful while using panic and recover within goroutines because not recovering from a panic within the same goroutine, can crash your program

#### 15. function variable:
- if you try to compare two function variables for equality; it will result in a compilation error; because function variables are NOT comparable in Go.

#### 16. closing a channel
- its crucial to ensure that a channel is closed only once because closing a close channel will result in a panic.

#### 17. range over channels:
- When using a for range loop to iterate over values from a channel, we aware that the loop will terminate when the channel is closed

### 18. Unbounded Goroutines?
- Be cautious when starting goroutines in loops because creating an unbounded number of goroutines can lead to excessive memory usage and performance issues.

#### 19. struct visibility:
- accessible from other packages, it need to start with an uppercase letter.

#### 20. value recivers:
- using a value receiver on a large struct can be inefficient because it makes copy of the entire struct instead use pointer receivers for efficiency.

#### 21. closures and goroutines
- be cautious when using closures(functions that capture variables from their surrounding scope) inside goroutines because goroutines may execute concurrently and modify the same variables, leading to race conditions.

#### 22. maps are unordered:
- In Go, if we try to print map elements; every time those will get printed in different order because unlike arrays and slices the maps in Go do not preserve the order.