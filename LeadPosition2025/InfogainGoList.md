### Interview Questions on Golang:

**1. Microservices?**
Microservices are an architectural style where an application is structured as a collection of loosely coupled, independently deployable services. Each service typically focuses on a single business capability, communicates via lightweight mechanisms (like REST or gRPC), and can be developed, deployed, and scaled independently. Go is excellent for building microservices due to its small binary size, fast startup time, strong concurrency primitives, and efficient networking.

**2. Select case?**
The `select` statement in Go is used to wait on multiple channel operations. It blocks until one of its cases is ready (either a send or receive operation can proceed). If multiple cases are ready, `select` chooses one pseudo-randomly. It's often used with a `default` case to avoid blocking, or with the `context` package to handle timeouts or cancellations.

**3. Goroutines?**
Goroutines are lightweight, independently executing functions managed by the Go runtime. They are functions or methods that run concurrently with other functions or methods. Unlike OS threads, goroutines are multiplexed onto a smaller number of OS threads by the Go scheduler, making them very efficient for concurrent operations and handling high numbers of concurrent connections. You start a goroutine by simply prefixing a function call with the `go` keyword.

**4. Send & receive data from goroutines?**
Data is sent and received between goroutines primarily using **channels**. Channels are typed conduits through which goroutines can send and receive values.
* **Send:** `channel <- value` (e.g., `ch <- 42`)
* **Receive:** `value := <-channel` (e.g., `result := <-ch`)
  Channels provide a safe and synchronized way to communicate, ensuring that access to shared data is controlled, preventing race conditions.

**5. Polymorphism program in Golang?**
Go achieves polymorphism through **interfaces and implicit implementation**, rather than traditional class inheritance.
* **Program Example:** Define an interface (e.g., `Shape` with a `Area()` method). Then, create multiple structs (e.g., `Circle`, `Rectangle`) that *implicitly* implement the `Shape` interface by providing their own `Area()` method.
* **How it works:** Functions can then accept an `interface` type argument, allowing them to operate on any concrete type that satisfies that interface, demonstrating polymorphic behavior (e.g., a `PrintArea(s Shape)` function can take either a `Circle` or a `Rectangle`).

---

### General Technical Questions:

**1. Basic intro?**
(This is about your self-introduction. Keep it concise, highlighting your experience, skills, and why you're a good fit for a lead Golang role.)
"Hi, I'm [Your Name], a Lead Golang Developer with [X] years of experience designing, developing, and deploying scalable backend systems. My expertise lies in building high-performance microservices, leveraging Go's concurrency model, and working extensively with cloud platforms like GCP. I'm passionate about clean architecture, test-driven development, and mentoring teams to deliver robust software solutions."

**2. Monolith vs Microservices?**
* **Monolith:** A single, self-contained application where all components (UI, business logic, data access) are tightly coupled and deployed as a single unit.
* **Microservices:** An architectural style where an application is broken down into small, independent services, each running in its own process and communicating via lightweight mechanisms.

**3. What are the advantages of one over the other?**
* **Monolith Advantages:** Simpler development/deployment initially, easier debugging (single codebase), lower operational overhead in early stages.
* **Monolith Disadvantages:** Slower development velocity as it grows, difficult to scale individual components, technology lock-in, higher risk of single point of failure.
* **Microservices Advantages:** Independent development/deployment teams, easier to scale individual services, technology flexibility, better fault isolation, faster innovation cycles.
* **Microservices Disadvantages:** Increased operational complexity (distributed systems), higher network overhead, complex data consistency, distributed debugging challenges.

**4. What is Docker?**
Docker is a platform that uses OS-level virtualization to deliver software in packages called **containers**. A container is a lightweight, standalone, executable package of software that includes everything needed to run an application: code, runtime, system tools, system libraries, and settings. It provides consistency across different environments (development, testing, production), ensuring "it works on my machine" translates to "it works everywhere."

**5. How Kubernetes work?**
Kubernetes is an open-source container orchestration platform that automates the deployment, scaling, and management of containerized applications.
* **Key Components:**
    * **Master Node (Control Plane):** Manages the cluster (API Server, Scheduler, Controller Manager, etcd for cluster data).
    * **Worker Nodes:** Run containerized applications (Kubelet manages pods, Kube Proxy handles network proxy for services, Container Runtime like Docker runs containers).
* **How it works:** Developers define desired state (e.g., 3 replicas of a Go service) in YAML files. Kubernetes constantly works to match the actual state to the desired state, handling tasks like scheduling containers, self-healing (restarting failed containers), scaling up/down, load balancing, and rolling updates.

**6. What are Generics?**
Generics, introduced in Go 1.18, allow you to write functions and data structures that work with a *type parameter* rather than a specific concrete type. This enables writing flexible and reusable code without sacrificing type safety.
* **Use Case:** Creating a generic `Max` function that works for `int`, `float`, etc., or a generic `Stack` data structure that can hold any type, reducing code duplication.

**7. What is Normalization in DB?**
Database normalization is the process of structuring a relational database to reduce data redundancy and improve data integrity. It involves dividing large tables into smaller, related tables and defining relationships between them.
* **Normal Forms (1NF, 2NF, 3NF, BCNF):** Each normal form has specific rules to achieve increasing levels of data integrity and reduce anomalies (insertion, update, deletion).
* **Purpose:** Ensures data consistency, reduces storage space, and simplifies maintenance.

**8. How goroutine works?**
Goroutines are functions that run concurrently. When you use the `go` keyword, the function is executed as a goroutine. The Go runtime's scheduler manages these goroutines. It multiplexes many goroutines onto a small number of underlying OS threads. When a goroutine performs a blocking operation (like network I/O), the Go scheduler automatically de-schedules it and runs another runnable goroutine on the same OS thread, efficiently utilizing resources without blocking the entire thread.

**9. Write hello world using 2 different ways (regular and `sync.WaitGroup`)?**

**Regular Way:**
```go
package main

import "fmt"

func main() {
    fmt.Println("Hello, World!")
}
```

**Using `sync.WaitGroup`:**
```go
package main

import (
	"fmt"
	"sync"
)

func main() {
	var wg sync.WaitGroup // Declare a WaitGroup

	wg.Add(1) // Increment the counter for one goroutine

	go func() {
		defer wg.Done() // Decrement the counter when goroutine finishes
		fmt.Println("Hello from a Goroutine, World!")
	}()

	wg.Wait() // Block until the counter becomes zero
	fmt.Println("Main function finished.")
}
```

**10. Slice vs array in Golang?**
* **Array:** A fixed-size sequence of elements of the same type. Its size is part of its type (e.g., `[5]int`). Arrays are value types, meaning when you pass an array to a function, a copy is made. They are rarely used directly in Go except for specific fixed-size data structures.
* **Slice:** A dynamic, flexible view into an underlying array. Slices do not own the data themselves; they are a descriptor (pointer to array, length, capacity). They are reference types, meaning when you pass a slice, you are passing the descriptor, which allows modification of the underlying array. Slices are the preferred collection type in Go for most use cases due to their flexibility (`[]int`).

**11. How multiple `defer` statements work?**
Multiple `defer` statements in a function work like a **stack (LIFO - Last-In, First-Out)**. When a `defer` statement is encountered, the deferred function call (and its arguments) is pushed onto a stack. When the surrounding function returns (either normally or due to a panic), the deferred calls are executed in reverse order of their declaration (the last one deferred is executed first).
* **Use Cases:** Resource cleanup (closing files, unlocking mutexes, database connections), logging, panic recovery.