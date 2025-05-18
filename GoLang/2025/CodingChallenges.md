## Golang Coding Questions

### 1. Remove Duplicate Elements from a Slice
This program removes duplicates from a slice of integers using a map to track seen elements.

```go
package main

import "fmt"

// removeDuplicates removes duplicate elements from a slice of integers.
func removeDuplicates(nums []int) []int {
    seen := make(map[int]bool)
    result := []int{}
    for _, num := range nums {
        if !seen[num] {
            seen[num] = true
            result = append(result, num)
        }
    }
    return result
}

func main() {
    nums := []int{1, 2, 2, 3, 4, 4, 5}
    fmt.Println("Original:", nums)
    fmt.Println("No duplicates:", removeDuplicates(nums))
}
```

**Explanation**: The `removeDuplicates` function uses a map to track unique elements, appending only unseen numbers to the result slice. Time complexity is O(n), where n is the slice length.

---

### 2. Reverse a Slice In Place
This program reverses a slice of integers in place by swapping elements from both ends.

```go
package main

import "fmt"

// reverseSlice reverses a slice of integers in place.
func reverseSlice(nums []int) {
    for i, j := 0, len(nums)-1; i < j; i, j = i+1, j-1 {
        nums[i], nums[j] = nums[j], nums[i]
    }
}

func main() {
    nums := []int{1, 2, 3, 4, 5}
    fmt.Println("Before:", nums)
    reverseSlice(nums)
    fmt.Println("After:", nums)
}
```

**Explanation**: The function swaps elements from the start and end, moving inward. Time complexity is O(n/2) ≈ O(n).

---

### 3. Find Maximum Product of Two Integers in an Array
Finds the maximum product of two integers in an array by tracking the two largest and two smallest numbers.

```go
package main

import (
	"fmt"
	"math"
)

// maxProduct finds the maximum product of two integers in an array.
func maxProduct(nums []int) int {
	max1, max2 := math.MinInt64, math.MinInt64 // Two largest
	min1, min2 := math.MaxInt64, math.MaxInt64 // Two smallest
	for _, num := range nums {
		if num > max1 {
			max2, max1 = max1, num
		} else if num > max2 {
			max2 = num
		}
		if num < min1 {
			min2, min1 = min1, num
		} else if num < min2 {
			min2 = num
		}
	}
	return max(max1*max2, min1*min2) // Compare max positives vs max negatives
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func main() {
	nums := []int{2, 3, -2, 4}
	fmt.Println("Max product:", maxProduct(nums))
}
```
---
### 4. Check if a String is a Palindrome
This program checks if a string is a palindrome by comparing characters from both ends.

```go
package main

import (
    "fmt"
    "strings"
)

// isPalindrome checks if a string is a palindrome (case-insensitive).
func isPalindrome(s string) bool {
    s = strings.ToLower(s)
    left, right := 0, len(s)-1
    for left < right {
        if s[left] != s[right] {
            return false
        }
        left++
        right--
    }
    return true
}

func main() {
    test := "Racecar"
    fmt.Printf("%s is palindrome: %v\n", test, isPalindrome(test))
}
```

**Explanation**: Converts the string to lowercase and compares characters inward. Time complexity is O(n).

---


### 5. Count Character Frequency in a String
Counts the frequency of each character in a string using a map.

```go
package main

import "fmt"

// charFrequency counts the frequency of each character in a string.
func charFrequency(s string) map[rune]int {
	freq := make(map[rune]int)
	for _, ch := range s {
		freq[ch]++
	}
	return freq
}

func main() {
	s := "hello"
	freq := charFrequency(s)
	for ch, count := range freq {
		fmt.Printf("%c: %d\n", ch, count)
	}
}
```
---
### 6. Check if Two Strings are Anagrams
This program checks if two strings are anagrams by comparing character frequencies.

```go
package main

import "fmt"

// areAnagrams checks if two strings are anagrams.
func areAnagrams(s1, s2 string) bool {
    if len(s1) != len(s2) {
        return false
    }
    freq := make(map[rune]int)
    for _, ch := range s1 {
        freq[ch]++
    }
    for _, ch := range s2 {
        freq[ch]--
        if freq[ch] == 0 {
            delete(freq, ch)
        }
    }
    return len(freq) == 0
}

func main() {
    s1, s2 := "listen", "silent"
    fmt.Printf("%s and %s are anagrams: %v\n", s1, s2, areAnagrams(s1, s2))
}
```

**Explanation**: Uses a map to count character frequencies in one string and decrements for the other. If the map is empty, they’re anagrams. Time complexity is O(n).

---
### 7. Group Words by Anagrams
Groups a list of strings by their anagrams using a sorted string as the key.

```go
package main

import (
	"fmt"
	"sort"
)

// groupAnagrams groups strings by their anagrams.
func groupAnagrams(strs []string) [][]string {
	groups := make(map[string][]string)
	for _, s := range strs {
		runes := []rune(s)
		sort.Slice(runes, func(i, j int) bool { return runes[i] < runes[j] })
		key := string(runes)
		groups[key] = append(groups[key], s)
	}
	result := make([][]string, 0, len(groups))
	for _, group := range groups {
		result = append(result, group)
	}
	return result
}

func main() {
	strs := []string{"eat", "tea", "tan", "ate", "nat", "bat"}
	fmt.Println(groupAnagrams(strs))
}
```

---

### 8. Sort a Slice of Structs
Sorts a slice of employee structs by age using the `sort` package.

```go
package main

import (
	"fmt"
	"sort"
)

// Employee represents an employee with name and age.
type Employee struct {
	Name string
	Age  int
}

// ByAge implements sort.Interface for sorting by age.
type ByAge []Employee

func (a ByAge) Len() int           { return len(a) }
func (a ByAge) Swap(i, j int)      { a[i], a[j] = a[j], a[i] }
func (a ByAge) Less(i, j int) bool { return a[i].Age < a[j].Age }

func main() {
	employees := []Employee{
		{"Alice", 30},
		{"Bob", 25},
		{"Charlie", 35},
	}
	fmt.Println("Before:", employees)
	sort.Sort(ByAge(employees))
	fmt.Println("After:", employees)
}
```

---

### 9. Find Two Numbers that Add Up to a Target
This program finds two numbers in an array that sum to a target using a hash map.

```go
package main

import "fmt"

// twoSum finds indices of two numbers that add up to target.
func twoSum(nums []int, target int) []int {
    seen := make(map[int]int)
    for i, num := range nums {
        complement := target - num
        if j, ok := seen[complement]; ok {
            return []int{j, i}
        }
        seen[num] = i
    }
    return nil
}

func main() {
    nums := []int{2, 7, 11, 15}
    target := 9
    fmt.Println("Indices:", twoSum(nums, target))
}
```

**Explanation**: Uses a map to store numbers and their indices, checking for the complement. Time complexity is O(n).

---

### 10. Find the Majority Element
Finds the element appearing more than n/2 times using Boyer-Moore Voting Algorithm.

```go
package main

import "fmt"

// majorityElement finds the majority element (appears > n/2 times).
func majorityElement(nums []int) int {
	candidate, count := nums[0], 1
	for i := 1; i < len(nums); i++ {
		if count == 0 {
			candidate = nums[i]
		}
		if nums[i] == candidate {
			count++
		} else {
			count--
		}
	}
	return candidate
}

func main() {
	nums := []int{2, 2, 1, 1, 1, 2, 2}
	fmt.Println("Majority element:", majorityElement(nums))
}
```

---

### 11. Detect a Cycle in a Linked List
Detects a cycle in a linked list using Floyd’s Cycle-Finding Algorithm.

```go
package main

import "fmt"

// ListNode represents a node in a linked list.
type ListNode struct {
	Val  int
	Next *ListNode
}

// hasCycle detects a cycle in a linked list.
func hasCycle(head *ListNode) bool {
	if head == nil || head.Next == nil {
		return false
	}
	slow, fast := head, head
	for fast != nil && fast.Next != nil {
		slow = slow.Next
		fast = fast.Next.Next
		if slow == fast {
			return true
		}
	}
	return false
}

func main() {
	// Example: 1->2->3->4->2 (cycle)
	head := &ListNode{1, &ListNode{2, &ListNode{3, &ListNode{4, nil}}}}
	head.Next.Next.Next.Next = head.Next // Create cycle
	fmt.Println("Has cycle:", hasCycle(head))
}
```
---
### 12. Reverse a Singly Linked List
This program reverses a singly linked list iteratively.

```go
package main

import "fmt"

// ListNode represents a node in a singly linked list.
type ListNode struct {
    Val  int
    Next *ListNode
}

// reverseList reverses a singly linked list.
func reverseList(head *ListNode) *ListNode {
    var prev *ListNode
    curr := head
    for curr != nil {
        next := curr.Next
        curr.Next = prev
        prev = curr
        curr = next
    }
    return prev
}

func main() {
    head := &ListNode{1, &ListNode{2, &ListNode{3, nil}}}
    reversed := reverseList(head)
    for reversed != nil {
        fmt.Print(reversed.Val, " ")
        reversed = reversed.Next
    }
}
```

**Explanation**: Iteratively reverses pointers by tracking previous and current nodes. Time complexity is O(n).

---

### 13. Generate All Permutations of a String
Generates all permutations of a string using backtracking.

```go
package main

import "fmt"

// permute generates all permutations of a string.
func permute(s string) []string {
	var result []string
	runes := []rune(s)
	var backtrack func(start int)
	backtrack = func(start int) {
		if start == len(runes) {
			result = append(result, string(runes))
			return
		}
		for i := start; i < len(runes); i++ {
			runes[start], runes[i] = runes[i], runes[start]
			backtrack(start + 1)
			runes[start], runes[i] = runes[i], runes[start]
		}
	}
	backtrack(0)
	return result
}

func main() {
	s := "abc"
	fmt.Println("Permutations:", permute(s))
}
```
---
### 14. Fibonacci with Memoization
This program computes Fibonacci numbers using memoization to optimize performance.

```go
package main

import "fmt"

// fibonacci computes the nth Fibonacci number with memoization.
func fibonacci(n int) int {
    memo := make(map[int]int)
    var fib func(int) int
    fib = func(x int) int {
        if x <= 1 {
            return x
        }
        if val, ok := memo[x]; ok {
            return val
        }
        memo[x] = fib(x-1) + fib(x-2)
        return memo[x]
    }
    return fib(n)
}

func main() {
    n := 10
    fmt.Printf("Fibonacci(%d) = %d\n", n, fibonacci(n))
}
```

**Explanation**: Uses a map to cache results, avoiding redundant calculations. Time complexity is O(n).

---

---

---

### 15. Merge Two Sorted Linked Lists
Merges two sorted linked lists into one sorted list.

```go
package main

import "fmt"

// ListNode represents a node in a linked list.
type ListNode struct {
	Val  int
	Next *ListNode
}

// mergeTwoLists merges two sorted linked lists.
func mergeTwoLists(l1, l2 *ListNode) *ListNode {
	dummy := &ListNode{}
	current := dummy
	for l1 != nil && l2 != nil {
		if l1.Val <= l2.Val {
			current.Next = l1
			l1 = l1.Next
		} else {
			current.Next = l2
			l2 = l2.Next
		}
		current = current.Next
	}
	if l1 != nil {
		current.Next = l1
	} else {
		current.Next = l2
	}
	return dummy.Next
}

func main() {
	l1 := &ListNode{1, &ListNode{3, nil}}
	l2 := &ListNode{2, &ListNode{4, nil}}
	merged := mergeTwoLists(l1, l2)
	for merged != nil {
		fmt.Print(merged.Val, " ")
		merged = merged.Next
	}
}
```

---

### 16. Reverse Digits of an Integer
Reverses the digits of an integer, returning 0 if the result overflows.

```go
package main

import (
	"fmt"
	"math"
)

// reverse reverses the digits of an integer.
func reverse(x int) int {
	result := 0
	for x != 0 {
		digit := x % 10
		x /= 10
		if result > math.MaxInt32/10 || result < math.MinInt32/10 {
			return 0
		}
		result = result*10 + digit
	}
	return result
}

func main() {
	x := 123
	fmt.Println("Reversed:", reverse(x))
}
```

---

### 17. Print and Sum Prime Numbers with Digit-Sum < 10
Prints prime numbers with a digit sum less than 10 and computes their sum.

```go
package main

import "fmt"

// isPrime checks if a number is prime.
func isPrime(n int) bool {
	if n < 2 {
		return false
	}
	for i := 2; i*i <= n; i++ {
		if n%i == 0 {
			return false
		}
	}
	return true
}

// digitSum computes the sum of digits in a number.
func digitSum(n int) int {
	sum := 0
	for n > 0 {
		sum += n % 10
		n /= 10
	}
	return sum
}

func main() {
	sum := 0
	for i := 2; i < 100; i++ { // Assuming reasonable range
		if isPrime(i) && digitSum(i) < 10 {
			fmt.Print(i, " ")
			sum += i
		}
	}
	fmt.Println("\nSum:", sum)
}
```

---

### 18. Build Stack and Queue in Go
Implements a stack and queue using slices.

```go
package main

import "fmt"

// Stack implements a LIFO structure.
type Stack struct {
	items []int
}

func (s *Stack) Push(x int) {
	s.items = append(s.items, x)
}

func (s *Stack) Pop() int {
	if len(s.items) == 0 {
		return 0 // Error handling simplified
	}
	x := s.items[len(s.items)-1]
	s.items = s.items[:len(s.items)-1]
	return x
}

// Queue implements a FIFO structure.
type Queue struct {
	items []int
}

func (q *Queue) Enqueue(x int) {
	q.items = append(q.items, x)
}

func (q *Queue) Dequeue() int {
	if len(q.items) == 0 {
		return 0 // Error handling simplified
	}
	x := q.items[0]
	q.items = q.items[1:]
	return x
}

func main() {
	s := Stack{}
	s.Push(1)
	s.Push(2)
	fmt.Println("Stack Pop:", s.Pop()) // 2

	q := Queue{}
	q.Enqueue(1)
	q.Enqueue(2)
	fmt.Println("Queue Dequeue:", q.Dequeue()) // 1
}
```

---

### 19. Worker Pool Implementation with Goroutines
This program implements a worker pool using goroutines to process tasks concurrently.

```go
package main

import (
    "fmt"
    "sync"
)

// worker processes tasks from the jobs channel.
func worker(id int, jobs <-chan int, results chan<- int, wg *sync.WaitGroup) {
    defer wg.Done()
    for job := range jobs {
        results <- job * 2
        fmt.Printf("Worker %d processed job %d\n", id, job)
    }
}

func main() {
    const numJobs = 5
    const numWorkers = 3
    jobs := make(chan int, numJobs)
    results := make(chan int, numJobs)
    var wg sync.WaitGroup

    // Start workers
    for w := 1; w <= numWorkers; w++ {
        wg.Add(1)
        go worker(w, jobs, results, &wg)
    }

    // Send jobs
    for j := 1; j <= numJobs; j++ {
        jobs <- j
    }
    close(jobs)

    // Wait for workers to finish
    wg.Wait()
    close(results)

    // Collect results
    for result := range results {
        fmt.Println("Result:", result)
    }
}
```

**Explanation**: Creates a pool of workers that process jobs from a channel, collecting results concurrently. Uses `sync.WaitGroup` for synchronization.

---

### 20. Fan-in Pattern: Merge Two Channels
Merges two channels into one using goroutines.

```go
package main

import (
	"fmt"
	"sync"
)

// merge merges two channels into one.
func merge(ch1, ch2 <-chan int) <-chan int {
	out := make(chan int)
	var wg sync.WaitGroup
	wg.Add(2)

	go func() {
		for n := range ch1 {
			out <- n
		}
		wg.Done()
	}()
	go func() {
		for n := range ch2 {
			out <- n
		}
		wg.Done()
	}()

	go func() {
		wg.Wait()
		close(out)
	}()

	return out
}

func main() {
	ch1 := make(chan int)
	ch2 := make(chan int)

	go func() {
		for _, n := range []int{1, 3, 5} {
			ch1 <- n
		}
		close(ch1)
	}()
	go func() {
		for _, n := range []int{2, 4, 6} {
			ch2 <- n
		}
		close(ch2)
	}()

	for n := range merge(ch1, ch2) {
		fmt.Print(n, " ")
	}
}
```

---

### 21. Build a Concurrent Counter with Mutex
Implements a thread-safe counter using a mutex.

```go
package main

import (
	"fmt"
	"sync"
)

// Counter is a thread-safe counter.
type Counter struct {
	mu    sync.Mutex
	value int
}

func (c *Counter) Increment() {
	c.mu.Lock()
	c.value++
	c.mu.Unlock()
}

func (c *Counter) Value() int {
	c.mu.Lock()
	defer c.mu.Unlock()
	return c.value
}

func main() {
	var wg sync.WaitGroup
	counter := Counter{}
	for i := 0; i < 100; i++ {
		wg.Add(1)
		go func() {
			counter.Increment()
			wg.Done()
		}()
	}
	wg.Wait()
	fmt.Println("Counter value:", counter.Value())
}
```

---

### 22. Implement a Rate Limiter Using Goroutines and Channels
Implements a simple rate limiter allowing a fixed number of requests per second.

```go
package main

import (
	"fmt"
	"time"
)

// RateLimiter limits the rate of requests.
type RateLimiter struct {
	rate   int           // Requests per second
	tokens chan struct{} // Token bucket
}

func NewRateLimiter(rate int) *RateLimiter {
	rl := &RateLimiter{
		rate:   rate,
		tokens: make(chan struct{}, rate),
	}
	go rl.refill()
	return rl
}

func (rl *RateLimiter) refill() {
	ticker := time.NewTicker(time.Second / time.Duration(rl.rate))
	for range ticker.C {
		select {
		case rl.tokens <- struct{}{}:
		default:
		}
	}
}

func (rl *RateLimiter) Allow() bool {
	select {
	case <-rl.tokens:
		return true
	default:
		return false
	}
}

func main() {
	rl := NewRateLimiter(2) // 2 requests per second
	for i := 0; i < 5; i++ {
		if rl.Allow() {
			fmt.Println("Request", i, "allowed")
		} else {
			fmt.Println("Request", i, "denied")
		}
		time.Sleep(200 * time.Millisecond)
	}
}
```

---

### 23. Implement a Simple Producer-Consumer Scenario
Implements a producer-consumer pattern using goroutines and channels.

```go
package main

import (
	"fmt"
	"sync"
	"time"
)

func producer(ch chan<- int, wg *sync.WaitGroup) {
	defer wg.Done()
	for i := 1; i <= 5; i++ {
		ch <- i
		fmt.Println("Produced:", i)
		time.Sleep(100 * time.Millisecond)
	}
	close(ch)
}

func consumer(ch <-chan int, wg *sync.WaitGroup) {
	defer wg.Done()
	for num := range ch {
		fmt.Println("Consumed:", num)
		time.Sleep(200 * time.Millisecond)
	}
}

func main() {
	ch := make(chan int, 2)
	var wg sync.WaitGroup
	wg.Add(2)
	go producer(ch, &wg)
	go consumer(ch, &wg)
	wg.Wait()
}
```

---

### 24. Implement a Goroutine with Task Timeout Using `select`
Runs a task with a timeout using `select` and `time.After`.

```go
package main

import (
	"fmt"
	"time"
)

func main() {
	ch := make(chan string)
	go func() {
		time.Sleep(2 * time.Second) // Simulate long task
		ch <- "Task completed"
	}()

	select {
	case result := <-ch:
		fmt.Println(result)
	case <-time.After(1 * time.Second):
		fmt.Println("Task timed out")
	}
}
```

---

### 25. Alternate Printing Even and Odd Numbers Using Two Goroutines
Two goroutines alternate printing even and odd numbers.

```go
package main

import (
	"fmt"
	"sync"
)

func main() {
	var wg sync.WaitGroup
	oddCh := make(chan int)
	evenCh := make(chan int)

	wg.Add(2)
	go func() { // Odd numbers
		defer wg.Done()
		for i := 1; i <= 10; i += 2 {
			fmt.Println("Odd:", i)
			oddCh <- i
			<-evenCh
		}
	}()
	go func() { // Even numbers
=20
		defer wg.Done()
		for i := 2; i <= 10; i += 2 {
			<-oddCh
			fmt.Println("Even:", i)
			evenCh <- i
		}
	}()
	wg.Wait()
}
```

---

### 26. Create a REST API in Go using `net/http` and `chi`
This program implements a simple REST API using the `chi` router.

```go
package main

import (
    "encoding/json"
    "net/http"

    "github.com/go-chi/chi/v5"
)

type Item struct {
    ID   string `json:"id"`
    Name string `json:"name"`
}

var items = map[string]Item{
    "1": {ID: "1", Name: "Item 1"},
}

func main() {
    r := chi.NewRouter()

    // GET all items
    r.Get("/items", func(w http.ResponseWriter, r *http.Request) {
        json.NewEncoder(w).Encode(items)
    })

    // POST new item
    r.Post("/items", func(w http.ResponseWriter, r *http.Request) {
        var item Item
        if err := json.NewDecoder(r.Body).Decode(&item); err != nil {
            http.Error(w, err.Error(), http.StatusBadRequest)
            return
        }
        items[item.ID] = item
        w.WriteHeader(http.StatusCreated)
        json.NewEncoder(w).Encode(item)
    })

    http.ListenAndServe(":8080", r)
}
```

**Explanation**: Uses `chi` to define routes for GET and POST operations on items, stored in an in-memory map. Run with `go run .` and test with `curl`.

---


### 27. Todo REST APIs – Basic CRUD with In-Memory Storage
Implements a Todo REST API with CRUD operations using an in-memory store.

```go
package main

import (
	"encoding/json"
	"net/http"
	"sync"

	"github.com/go-chi/chi/v5"
)

type Todo struct {
	ID    string `json:"id"`
	Title string `json:"title"`
	Done  bool   `json:"done"`
}

type TodoStore struct {
	sync.RWMutex
	todos map[string]Todo
}

func NewTodoStore() *TodoStore {
	return &TodoStore{todos: make(map[string]Todo)}
}

func (s *TodoStore) Create(todo Todo) {
	s.Lock()
	s.todos[todo.ID] = todo
	s.Unlock()
}

func (s *TodoStore) Read(id string) (Todo, bool) {
	s.RLock()
	todo, ok := s.todos[id]
	s.RUnlock()
	return todo, ok
}

func (s *TodoStore) Update(id string, todo Todo) bool {
	s.Lock()
	if _, ok := s.todos[id]; !ok {
		s.Unlock()
		return false
	}
	s.todos[id] = todo
	s.Unlock()
	return true
}

func (s *TodoStore) Delete(id string) bool {
	s.Lock()
	if _, ok := s.todos[id]; !ok {
		s.Unlock()
		return false
	}
	delete(s.todos, id)
	s.Unlock()
	return true
}

func main() {
	store := NewTodoStore()
	r := chi.NewRouter()

	r.Get("/todos/{id}", func(w http.ResponseWriter, r *http.Request) {
		id := chi.URLParam(r, "id")
		if todo, ok := store.Read(id); ok {
			json.NewEncoder(w).Encode(todo)
		} else {
			http.Error(w, "Not found", http.StatusNotFound)
		}
	})

	r.Post("/todos", func(w http.ResponseWriter, r *http.Request) {
		var todo Todo
		if err := json.NewDecoder(r.Body).Decode(&todo); err != nil {
			http.Error(w, err.Error(), http.StatusBadRequest)
			return
		}
		store.Create(todo)
		w.WriteHeader(http.StatusCreated)
	})

	r.Put("/todos/{id}", func(w http.ResponseWriter, r *http.Request) {
		id := chi.URLParam(r, "id")
		var todo Todo
		if err := json.NewDecoder(r.Body).Decode(&todo); err != nil {
			http.Error(w, err.Error(), http.StatusBadRequest)
			return
		}
		if !store.Update(id, todo) {
			http.Error(w, "Not found", http.StatusNotFound)
			return
		}
		w.WriteHeader(http.StatusOK)
	})

	r.Delete("/todos/{id}", func(w http.ResponseWriter, r *http.Request) {
		id := chi.URLParam(r, "id")
		if !store.Delete(id) {
			http.Error(w, "Not found", http.StatusNotFound)
			return
		}
		w.WriteHeader(http.StatusNoContent)
	})

	http.ListenAndServe(":8080", r)
}
```

---

### 28. JSON Validator Server
Validates POSTed JSON against a schema using a simple validator.

```go
package main

import (
	"encoding/json"
	"net/http"

	"github.com/go-chi/chi/v5"
)

// ExpectedSchema defines the expected JSON structure.
type ExpectedSchema struct {
	Name string `json:"name"`
	Age  int    `json:"age"`
}

func main() {
	r := chi.NewRouter()

	r.Post("/validate", func(w http.ResponseWriter, r *http.Request) {
		var data ExpectedSchema
		if err := json.NewDecoder(r.Body).Decode(&data); err != nil {
			http.Error(w, "Invalid JSON", http.StatusBadRequest)
			return
		}
		if data.Name == "" || data.Age < 0 {
			http.Error(w, "Invalid schema: name required, age >= 0", http.StatusBadRequest)
			return
		}
		w.Write([]byte("Valid JSON"))
	})

	http.ListenAndServe(":8080", r)
}
```

---

### 29. Build a Config Loader
Reads JSON/YAML config with environment variable override.

```go
package main

import (
	"encoding/json"
	"fmt"
	"os"

	"gopkg.in/yaml.v2"
)

type Config struct {
	Host string `json:"host" yaml:"host"`
	Port int    `json:"port" yaml:"port"`
}

func LoadConfig(filePath string, format string) (Config, error) {
	var cfg Config
	data, err := os.ReadFile(filePath)
	if err != nil {
		return cfg, err
	}
	switch format {
	case "json":
		err = json.Unmarshal(data, &cfg)
	case "yaml":
		err = yaml.Unmarshal(data, &cfg)
	default:
		return cfg, fmt.Errorf("unsupported format: %s", format)
	}
	if err != nil {
		return cfg, err
	}
	if host := os.Getenv("APP_HOST"); host != "" {
		cfg.Host = host
	}
	if port := os.Getenv("APP_PORT"); port != "" {
		var p int
		fmt.Sscanf(port, "%d", &p)
		cfg.Port = p
	}
	return cfg, nil
}

func main() {
	// Example JSON file: {"host":"localhost","port":8080}
	cfg, err := LoadConfig("config.json", "json")
	if err != nil {
		fmt.Println("Error:", err)
		return
	}
	fmt.Printf("Config: %+v\n", cfg)
}
```

---

### 30. Implement Middleware in Go HTTP Servers
Implements a logging middleware for HTTP requests.

```go
package main

import (
	"log"
	"net/http"
	"time"

	"github.com/go-chi/chi/v5"
)

func LoggingMiddleware(next http.Handler) http.Handler {
	return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		start := time.Now()
		log.Printf("Started %s %s", r.Method, r.URL.Path)
		next.ServeHTTP(w, r)
		log.Printf("Completed in %v", time.Since(start))
	})
}

func main() {
	r := chi.NewRouter()
	r.Use(LoggingMiddleware)
	r.Get("/", func(w http.ResponseWriter, r *http.Request) {
		w.Write([]byte("Hello, World!"))
	})
	http.ListenAndServe(":8080", r)
}
```

---

### 31. Implement Graceful Shutdown in Go HTTP Server
This program implements an HTTP server with graceful shutdown using `context`.

```go
package main

import (
    "context"
    "fmt"
    "net/http"
    "os"
    "os/signal"
    "time"
)

func main() {
    mux := http.NewServeMux()
    mux.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
        fmt.Fprintln(w, "Hello, World!")
    })

    server := &http.Server{
        Addr:    ":8080",
        Handler: mux,
    }

    // Start server in a goroutine
    go func() {
        if err := server.ListenAndServe(); err != nil && err != http.ErrServerClosed {
            fmt.Println("Server error:", err)
        }
    }()
    fmt.Println("Server running on :8080")

    // Handle shutdown
    stop := make(chan os.Signal, 1)
    signal.Notify(stop, os.Interrupt)
    <-stop
    fmt.Println("\nShutting down...")

    ctx, cancel := context.WithTimeout(context.Background(), 5*time.Second)
    defer cancel()
    if err := server.Shutdown(ctx); err != nil {
        fmt.Println("Shutdown error:", err)
    }
    fmt.Println("Server stopped")
}
```

**Explanation**: Listens for interrupt signals and shuts down the server gracefully, allowing active connections to complete within a timeout.

---

### 32. Design a URL Shortener Service
Implements a URL shortener with CRUD and short code generation.

```go
package main

import (
	"crypto/sha256"
	"encoding/base64"
	"encoding/json"
	"net/http"
	"sync"

	"github.com/go-chi/chi/v5"
)

type URLStore struct {
	sync.RWMutex
	urls map[string]string
}

func NewURLStore() *URLStore {
	return &URLStore{urls: make(map[string]string)}
}

func (s *URLStore) Shorten(longURL string) string {
	hash := sha256.Sum256([]byte(longURL))
	short := base64.URLEncoding.EncodeToString(hash[:])[:6]
	s.Lock()
	s.urls[short] = longURL
	s.Unlock()
	return short
}

func (s *URLStore) Get(short string) (string, bool) {
	s.RLock()
	long, ok := s.urls[short]
	s.RUnlock()
	return long, ok
}

func main() {
	store := NewURLStore()
	r := chi.NewRouter()

	r.Post("/shorten", func(w http.ResponseWriter, r *http.Request) {
		var input struct{ URL string }
		if err := json.NewDecoder(r.Body).Decode(&input); err != nil {
			http.Error(w, err.Error(), http.StatusBadRequest)
			return
		}
		short := store.Shorten(input.URL)
		json.NewEncoder(w).Encode(map[string]string{"short_url": short})
	})

	r.Get("/{short}", func(w http.ResponseWriter, r *http.Request) {
		short := chi.URLParam(r, "short")
		if long, ok := store.Get(short); ok {
			http.Redirect(w, r, long, http.StatusFound)
		} else {
			http.Error(w, "Not found", http.StatusNotFound)
		}
	})

	http.ListenAndServe(":8080", r)
}
```

---

### 33. Create a CLI Tool Using Cobra
Implements a simple CLI tool with Cobra.

```go
package main

import (
	"fmt"
	"github.com/spf13/cobra"
)

func main() {
	var rootCmd = &cobra.Command{
		Use:   "mycli",
		Short: "A simple CLI tool",
	}
	var greetCmd = &cobra.Command{
		Use:   "greet [name]",
		Short: "Greets a user",
		Args:  cobra.MinimumNArgs(1),
		Run: func(cmd *cobra.Command, args []string) {
			fmt.Println("Hello,", args[0])
		},
	}
	rootCmd.AddCommand(greetCmd)
	rootCmd.Execute()
}
```

---

### 34. CLI Password Manager
Implements a CLI password manager with AES encryption.

```go
package main

import (
	"crypto/aes"
	"crypto/cipher"
	"crypto/rand"
	"encoding/base64"
	"fmt"
	"io"
	"os"

	"github.com/spf13/cobra"
)

type PasswordStore struct {
	file string
	key  []byte
}

func NewPasswordStore(file, key string) *PasswordStore {
	return &PasswordStore{file: file, key: []byte(key)}
}

func (s *PasswordStore) Save(service, password string) error {
	encrypted, err := s.encrypt(password)
	if err != nil {
		return err
	}
	f, err := os.OpenFile(s.file, os.O_APPEND|os.O_CREATE|os.O_WRONLY, 0644)
	if err != nil {
		return err
	}
	defer f.Close()
	_, err = fmt.Fprintf(f, "%s:%s\n", service, encrypted)
	return err
}

func (s *PasswordStore) encrypt(text string) (string, error) {
	block, err := aes.NewCipher(s.key)
	if err != nil {
		return "", err
	}
	b := make([]byte, aes.BlockSize+len(text))
	iv := b[:aes.BlockSize]
	if _, err := io.ReadFull(rand.Reader, iv); err != nil {
		return "", err
	}
	stream := cipher.NewCFBEncrypter(block, iv)
	stream.XORKeyStream(b[aes.BlockSize:], []byte(text))
	return base64.StdEncoding.EncodeToString(b), nil
}

func main() {
	store := NewPasswordStore("passwords.txt", "16bytekey1234567")
	var rootCmd = &cobra.Command{Use: "passmgr"}
	var saveCmd = &cobra.Command{
		Use:   "save [service] [password]",
		Short: "Save a password",
		Args:  cobra.ExactArgs(2),
		Run: func(cmd *cobra.Command, args []string) {
			if err := store.Save(args[0], args[1]); err != nil {
				fmt.Println("Error:", err)
			} else {
				fmt.Println("Password saved")
			}
		},
	}
	rootCmd.AddCommand(saveCmd)
	rootCmd.Execute()
}
```

---

### 35. Tail-Like Program
Reads the last N lines from a file.

```go
package main

import (
	"bufio"
	"fmt"
	"os"
)

// tail reads the last n lines from a file.
func tail(filename string, n int) ([]string, error) {
	file, err := os.Open(filename)
	if err != nil {
		return nil, err
	}
	defer file.Close()

	lines := make([]string, 0, n)
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
		if len(lines) > n {
			lines = lines[1:]
		}
	}
	return lines, scanner.Err()
}

func main() {
	lines, err := tail("input.txt", 3)
	if err != nil {
		fmt.Println("Error:", err)
		return
	}
	for _, line := range lines {
		fmt.Println(line)
	}
}
```

---

### 36. Count Unique Words in a File
Counts unique words in a file using a map.

```go
package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

// countUniqueWords counts unique words in a file.
func countUniqueWords(filename string) (map[string]int, error) {
	file, err := os.Open(filename)
	if err != nil {
		return nil, err
	}
	defer file.Close()

	words := make(map[string]int)
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		for _, word := range strings.Fields(strings.ToLower(scanner.Text())) {
			words[word]++
		}
	}
	return words, scanner.Err()
}

func main() {
	words, err := countUniqueWords("input.txt")
	if err != nil {
		fmt.Println("Error:", err)
		return
	}
	for word, count := range words {
		fmt.Printf("%s: %d\n", word, count)
	}
}
```

---

### 37. Concurrent Web Crawler
Crawls internal links from a root URL concurrently.

```go
package main

import (
	"fmt"
	"net/http"
	"sync"

	"golang.org/x/net/html"
)

type Crawler struct {
	visited map[string]bool
	mu      sync.Mutex
	wg      sync.WaitGroup
}

func NewCrawler() *Crawler {
	return &Crawler{visited: make(map[string]bool)}
}

func (c *Crawler) Crawl(url string) {
	c.mu.Lock()
	if c.visited[url] {
		c.mu.Unlock()
		return
	}
	c.visited[url] = true
	c.mu.Unlock()

	c.wg.Add(1)
	go func() {
		defer c.wg.Done()
		resp, err := http.Get(url)
		if err != nil {
			fmt.Println("Error:", err)
			return
		}
		defer resp.Body.Close()

		node, err := html.Parse(resp.Body)
		if err != nil {
			fmt.Println("Error:", err)
			return
		}
		c.extractLinks(node, url)
	}()
}

func (c *Crawler) extractLinks(n *html.Node, baseURL string) {
	if n.Type == html.ElementNode && n.Data == "a" {
		for _, attr := range n.Attr {
			if attr.Key == "href" {
				// Simplified: only crawl same domain
				if strings.HasPrefix(attr.Val, baseURL) {
					c.Crawl(attr.Val)
				}
			}
		}
	}
	for child := n.FirstChild; child != nil; child = child.NextSibling {
		c.extractLinks(child, baseURL)
	}
}

func main() {
	c := NewCrawler()
	c.Crawl("https://example.com")
	c.wg.Wait()
	for url := range c.visited {
		fmt.Println(url)
	}
}
```

---

### 38. Read JSON from Stdin and Unmarshal into a Struct
Reads JSON from stdin and unmarshals it into a struct.

```go
package main

import (
	"encoding/json"
	"fmt"
	"os"
)

type Data struct {
	Name string `json:"name"`
	Age  int    `json:"age"`
}

func main() {
	var data Data
	if err := json.NewDecoder(os.Stdin).Decode(&data); err != nil {
		fmt.Println("Error:", err)
		return
	}
	fmt.Printf("Name: %s, Age: %d\n", data.Name, data.Age)
}
```

---

### 39. Demonstrate Graceful Shutdown with Cleanup Logic
Demonstrates graceful shutdown with cleanup using `context`.

```go
package main

import (
	"context"
	"fmt"
	"net/http"
	"os"
	"os/signal"
	"time"
)

func main() {
	mux := http.NewServeMux()
	mux.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		fmt.Fprintln(w, "Hello, World!")
	})

	server := &http.Server{
		Addr:    ":8080",
		Handler: mux,
	}

	go func() {
		if err := server.ListenAndServe(); err != nil && err != http.ErrServerClosed {
			fmt.Println("Server error:", err)
		}
	}()
	fmt.Println("Server running on :8080")

	stop := make(chan os.Signal, 1)
	signal.Notify(stop, os.Interrupt)
	<-stop
	fmt.Println("\nShutting down...")

	ctx, cancel := context.WithTimeout(context.Background(), 5*time.Second)
	defer cancel()

	// Cleanup logic
	go func() {
		fmt.Println("Cleaning up resources...")
		time.Sleep(1 * time.Second) // Simulate cleanup
		fmt.Println("Cleanup complete")
	}()

	if err := server.Shutdown(ctx); err != nil {
		fmt.Println("Shutdown error:", err)
	}
	fmt.Println("Server stopped")
}
```

---

### 40. Concurrency-Safe Caching in Go
Implements a thread-safe cache with mutex.

```go
package main

import (
	"fmt"
	"sync"
	"time"
)

// Cache is a thread-safe cache with expiration.
type Cache struct {
	mu    sync.RWMutex
	items map[string]struct {
		value      interface{}
		expiration int64
	}
}

func NewCache() *Cache {
	return &Cache{items: make(map[string]struct {
		value      interface{}
		expiration int64
	})}
}

func (c *Cache) Set(key string, value interface{}, duration time.Duration) {
	c.mu.Lock()
	c.items[key] = struct {
		value      interface{}
		expiration int64
	}{value, time.Now().Add(duration).UnixNano()}
	c.mu.Unlock()
}

func (c *Cache) Get(key string) (interface{}, bool) {
	c.mu.RLock()
	item, ok := c.items[key]
	c.mu.RUnlock()
	if !ok || item.expiration < time.Now().UnixNano() {
		return nil, false
	}
	return item.value, true
}

func main() {
	cache := NewCache()
	cache.Set("key1", "value1", 1*time.Second)
	if val, ok := cache.Get("key1"); ok {
		fmt.Println("Found:", val)
	}
	time.Sleep(2 * time.Second)
	if _, ok := cache.Get("key1"); !ok {
		fmt.Println("Key expired")
	}
}
```