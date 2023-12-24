## Coding Challenges:
### 1. **Palindrome Check**
**Challenge:** Write a function to determine if a given string is a palindrome (reads the same backward as forward). Ignore non-alphanumeric characters.

**Solution:**
```go
package main

import (
	"fmt"
	"strings"
)

func isPalindrome(s string) bool {
	s = strings.ToLower(s)
	s = removeNonAlphanumeric(s)

	// Check if the string is a palindrome
	for i, j := 0, len(s)-1; i < j; {
		if s[i] != s[j] {
			return false
		}
		i++
		j--
	}
	return true
}

func removeNonAlphanumeric(s string) string {
	var result strings.Builder
	for _, char := range s {
		if (char >= 'a' && char <= 'z') || (char >= '0' && char <= '9') {
			result.WriteRune(char)
		}
	}
	return result.String()
}

func main() {
	fmt.Println(isPalindrome("A man, a plan, a canal: Panama"))  // true
	fmt.Println(isPalindrome("race a car"))						// false
	fmt.Println(isPalindrome("race car"))                      // true
}
```

### 2. **FizzBuzz:**
**Challenge:** Write a program that prints the numbers from 1 to 100. But for multiples of three, print "Fizz" instead of the number, and for the multiples of five, print "Buzz." For numbers that are multiples of both three and five, print "FizzBuzz."

**Solution:**
```go
package main

import "fmt"

func fizzBuzz() {
	for i := 1; i <= 100; i++ {
		if i%3 == 0 && i%5 == 0 {
			fmt.Println("FizzBuzz")
		} else if i%3 == 0 {
			fmt.Println("Fizz")
		} else if i%5 == 0 {
			fmt.Println("Buzz")
		} else {
			fmt.Println(i)
		}
	}
}

func main() {
	fizzBuzz()
}
```

### 3. **Reverse Linked List:**
**Challenge:** Write a function to reverse a singly linked list.

**Solution:**
```go
package main

import "fmt"

type ListNode struct {
	Val  int
	Next *ListNode
}

func reverseList(head *ListNode) *ListNode {
	var prev *ListNode
	current := head

	for current != nil {
		next := current.Next
		current.Next = prev
		prev = current
		current = next
	}

	return prev
}

func printList(head *ListNode) {
	for head != nil {
		fmt.Print(head.Val, " ")
		head = head.Next
	}
	fmt.Println()
}

func main() {
	list := &ListNode{1, &ListNode{2, &ListNode{3, nil}}}
	fmt.Print("Original List: ")
	printList(list)

	reversed := reverseList(list)
	fmt.Print("Reversed List: ")
	printList(reversed)
}
```


### 4. **Two Sum:**
**Challenge:** Given an array of integers, find two numbers such that they add up to a specific target number.

**Solution:**
```go
package main

import "fmt"

func twoSum(nums []int, target int) []int {
	numMap := make(map[int]int)

	for i, num := range nums {
		complement := target - num
		if idx, found := numMap[complement]; found {
			return []int{idx, i}
		}
		numMap[num] = i
	}

	return nil
}

func main() {
	nums := []int{2, 7, 11, 15}
	target := 9
	result := twoSum(nums, target)
	fmt.Println(result)  // Output: [0 1]
}
```

### 5. **Binary Search:**
**Challenge:** Implement binary search in a sorted array.

**Solution:**
```go
package main

import "fmt"

func binarySearch(nums []int, target int) int {
	low, high := 0, len(nums)-1

	for low <= high {
		mid := (low + high) / 2
		if nums[mid] == target {
			return mid
		} else if nums[mid] < target {
			low = mid + 1
		} else {
			high = mid - 1
		}
	}

	return -1
}

func main() {
	nums := []int{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
	target := 7
	result := binarySearch(nums, target)
	fmt.Println(result)  // Output: 6
}
```

### 6. **Merge Two Sorted Lists:**
**Challenge:** Merge two sorted linked lists into a single sorted linked list.

**Solution:** 
```go
package main

import "fmt"

type ListNode struct {
	Val  int
	Next *ListNode
}

func mergeTwoLists(l1 *ListNode, l2 *ListNode) *ListNode {
	dummy := &ListNode{}
	current := dummy

	for l1 != nil && l2 != nil {
		if l1.Val < l2.Val {
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

func printList(head *ListNode) {
	for head != nil {
		fmt.Print(head.Val, " ")
		head = head.Next
	}
	fmt.Println()
}

func main() {
	list1 := &ListNode{1, &ListNode{3, &ListNode{5, nil}}}
	list2 := &ListNode{2, &ListNode{4, &ListNode{6, nil}}}

	fmt.Print("List 1: ")
	printList(list1)
	fmt.Print("List 2: ")
	printList(list2)

	merged := mergeTwoLists(list1, list2)
	fmt.Print("Merged List: ")
	printList(merged)
}
```

### 7. **Longest Common Prefix:**
**Challenge:** Write a function to find the longest common prefix string amongst an array of strings.

**Solution:**
```go
package main

import "fmt"

func longestCommonPrefix(strs []string) string {
	if len(strs) == 0 {
		return ""
	}

	prefix := strs[0]
	for _, str := range strs[1:] {
		for i := 0; i < len(prefix) && i < len(str); i++ {
			if prefix[i] != str[i] {
				prefix = prefix[:i]
				break
			}
		}
	}

	return prefix
}

func main() {
	strs := []string{"flower", "flow", "flight"}
	result := longestCommonPrefix(strs)
	fmt.Println(result)  // Output: "fl"
}
```

### 8. **Reverse Integer:**
**Challenge:** Reverse digits of an integer. Return 0 if the result overflows.

**Solution:**
```go
package main

import (
	"fmt"
	"math"
)

func reverse(x int) int {
	result := 0

	for x != 0 {
		pop := x % 10
		x /= 10

		if result > math.MaxInt32/10 || (result == math.MaxInt32/10 && pop > 7) {
			return 0
		}
		if result < math.MinInt32/10 || (result == math.MinInt32/10 && pop < -8) {
			return 0
		}

		result = result*10 + pop
	}

	return result
}

func main() {
	num := 12345
	result := reverse(num)
	fmt.Println(result)  // Output: 54321
}
```

### 9. **Valid Parentheses:**
**Challenge:** Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

**Solution:**
```go
package main

import "fmt"

func isValid(s string) bool {
	stack := []rune{}
	mapping := map[rune]rune{')': '(', '}': '{', ']': '['}

	for _, char := range s {
		if open, exists := mapping[char]; exists {
			if len(stack) == 0 || stack[len(stack)-1] != open {
				return false
			}
			stack = stack[:len(stack)-1] // Pop from stack
		} else {
			stack = append(stack, char)
		}
	}

	return len(stack) == 0
}

func main() {
	fmt.Println(isValid("()"))        // true
	fmt.Println(isValid("()[]{}"))    // true
	fmt.Println(isValid("(]"))         // false
	fmt.Println(isValid("([)]"))       // false
	fmt.Println(isValid("{[]}"))       // true
	fmt.Println(isValid("((("))        // false
}
```

### 10. **Count and Say:**
**Challenge:** The count-and-say sequence is a series of numbers with the following pattern: `1, 11, 21, 1211, 111221, ...`. Write a function to generate the nth term of the count-and-say sequence.

**Solution:**
```go
package main

import (
	"fmt"
	"strconv"
)

func countAndSay(n int) string {
	if n == 1 {
		return "1"
	}

	prev := countAndSay(n - 1)
	result := ""
	count := 1

	for i := 0; i < len(prev); i++ {
		if i+1 < len(prev) && prev[i] == prev[i+1] {
			count++
		} else {
			result += strconv.Itoa(count) + string(prev[i])
			count = 1
		}
	}

	return result
}

func main() {
	fmt.Println(countAndSay(1))   // "1"
	fmt.Println(countAndSay(4))   // "1211"
	fmt.Println(countAndSay(6))   // "312211"
	fmt.Println(countAndSay(8))   // "1113213211"
}
```

### 11. **Majority Element:**
**Challenge:** Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊n/2⌋ times.

**Solution:**
```go
package main

import (
	"fmt"
	"sort"
)

func majorityElement(nums []int) int {
	sort.Ints(nums)
	return nums[len(nums)/2]
}

func main() {
	arr := []int{3, 3, 4, 2, 4, 4, 2, 4, 4}
	result := majorityElement(arr)
	fmt.Println(result)  // Output: 4
}
```

### 12. **Rotate Image:**
**Challenge:** You are given an n x n 2D matrix representing an image. Rotate the image by 90 degrees (clockwise).

**Solution:**
```go
package main

import "fmt"

func rotate(matrix [][]int) {
	n := len(matrix)

	// Transpose the matrix
	for i := 0; i < n; i++ {
		for j := i; j < n; j++ {
			matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
		}
	}

	// Reverse each row
	for i := 0; i < n; i++ {
		for j := 0; j < n/2; j++ {
			matrix[i][j], matrix[i][n-j-1] = matrix[i][n-j-1], matrix[i][j]
		}
	}
}

func printMatrix(matrix [][]int) {
	for _, row := range matrix {
		fmt.Println(row)
	}
}

func main() {
	image := [][]int{
		{1, 2, 3},
		{4, 5, 6},
		{7, 8, 9},
	}
	fmt.Println("Original Matrix:")
	printMatrix(image)

	rotate(image)
	fmt.Println("Rotated Matrix:")
	printMatrix(image)
}
```

### 13. **Goroutine with Channels - Simple Example:**
**Challenge:** A basic example where a Goroutine sends data to a channel, and the main Goroutine receives and prints the data.

**Solution:**
```go
package main

import (
	"fmt"
	"time"
)

func sendData(ch chan int) {
	for i := 0; i < 5; i++ {
		ch <- i
		time.Sleep(time.Millisecond * 500)
	}
	close(ch)
}

func main() {
	dataChannel := make(chan int)

	go sendData(dataChannel)

	for num := range dataChannel {
		fmt.Println("Received:", num)
	}
}
```

### 14. **Goroutine with Channels - Fan-Out, Fan-In:**
**Challenge:** An example illustrating Fan-Out and Fan-In patterns using Goroutines and channels.

**Solution:**
```go
package main

import (
	"fmt"
	"math/rand"
	"sync"
	"time"
)

func produceData(ch chan int, wg *sync.WaitGroup) {
	defer wg.Done()
	rand.Seed(time.Now().UnixNano())
	for i := 0; i < 5; i++ {
		data := rand.Intn(100)
		ch <- data
		time.Sleep(time.Millisecond * 500)
	}
	close(ch)
}

func processData(inCh chan int, outCh chan int, wg *sync.WaitGroup) {
	defer wg.Done()
	for num := range inCh {
		result := num * 2
		outCh <- result
	}
	close(outCh)
}

func consumeData(ch chan int) {
	for num := range ch {
		fmt.Println("Processed:", num)
	}
}

func main() {
	// Fan-Out: Producing data from one Goroutine to multiple Goroutines
	dataChannel := make(chan int)
	processedDataChannel := make(chan int)
	var wg sync.WaitGroup

	wg.Add(1)
	go produceData(dataChannel, &wg)

	// Fan-Out: Multiple Goroutines processing data
	for i := 0; i < 3; i++ {
		wg.Add(1)
		go processData(dataChannel, processedDataChannel, &wg)
	}

	// Fan-In: Consuming processed data
	go consumeData(processedDataChannel)

	wg.Wait()
}
```

### 15. **Select Statement with Goroutines and Channels:**
**Challenge:** Using the `select` statement to synchronize multiple Goroutines through channels.

**Solution:**
```go
package main

import (
	"fmt"
	"time"
)

func producer(ch chan int, done chan bool) {
	for i := 0; i < 5; i++ {
		ch <- i
		time.Sleep(time.Millisecond * 500)
	}
	close(ch)
	done <- true
}

func consumer(ch chan int, done chan bool) {
	for {
		select {
		case num, ok := <-ch:
			if ok {
				fmt.Println("Received:", num)
			} else {
				done <- true
				return
			}
		}
	}
}

func main() {
	dataChannel := make(chan int)
	doneChannel := make(chan bool)

	go producer(dataChannel, doneChannel)
	go consumer(dataChannel, doneChannel)

	<-doneChannel // Wait for the producer and consumer to finish
	<-doneChannel
}
```

### 16. **Worker Pool Pattern:**
**Challenge:** Using a worker pool pattern to parallelize tasks using Goroutines and channels.

**Solution:** 
```go
package main

import (
	"fmt"
	"sync"
	"time"
)

func worker(id int, jobs <-chan int, results chan<- int, wg *sync.WaitGroup) {
	defer wg.Done()
	for job := range jobs {
		fmt.Printf("Worker %d processing job %d\n", id, job)
		time.Sleep(time.Second)
		results <- job * 2
	}
}

func main() {
	numJobs := 10
	numWorkers := 3

	jobs := make(chan int, numJobs)
	results := make(chan int, numJobs)
	var wg sync.WaitGroup

	// Start workers
	for i := 1; i <= numWorkers; i++ {
		wg.Add(1)
		go worker(i, jobs, results, &wg)
	}

	// Provide jobs to workers
	for i := 1; i <= numJobs; i++ {
		jobs <- i
	}
	close(jobs)

	// Wait for all workers to finish
	wg.Wait()

	// Close the results channel after all workers are done
	close(results)

	// Collect and print results
	for result := range results {
		fmt.Println("Processed:", result)
	}
}
```

### 17. **Fibonacci Series:**
**Challenge:** Write a function in Golang to generate the Fibonacci series up to a given number.

**Solution:**
```go
package main

import "fmt"

func fibonacci(n int) []int {
    fib := make([]int, n)
    fib[0], fib[1] = 0, 1

    for i := 2; i < n; i++ {
        fib[i] = fib[i-1] + fib[i-2]
    }

    return fib
}

func main() {
    fmt.Println(fibonacci(10))
    // Output: [0 1 1 2 3 5 8 13 21 34]
}
```

### 18. **String Reversal:**
**Challenge:** Implement a function in Golang to reverse a given string.

**Solution:**
```go
package main

import "fmt"

func reverseString(s string) string {
    runes := []rune(s)
    for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
        runes[i], runes[j] = runes[j], runes[i]
    }
    return string(runes)
}

func main() {
    fmt.Println(reverseString("Hello, World!"))
    // Output: "!dlroW ,olleH"
}
```

### 19. **Palindrome Check:**
**Challenge:** Write a function in Golang to check if a given string is a palindrome.

**Solution:**
```go
package main

import (
    "fmt"
    "strings"
)

func isPalindrome(s string) bool {
    s = strings.ToLower(s)
    s = strings.ReplaceAll(s, " ", "")

    for i, j := 0, len(s)-1; i < j; i, j = i+1, j-1 {
        if s[i] != s[j] {
            return false
        }
    }

    return true
}

func main() {
    fmt.Println(isPalindrome("A man, a plan, a canal, Panama"))
    // Output: true
}
```

### 20. **Factorial Calculation:**
**Challenge:** Implement a function in Golang to calculate the factorial of a given number.

**Solution:**
```go
package main

import "fmt"

func factorial(n int) int {
    if n == 0 || n == 1 {
        return 1
    }
    return n * factorial(n-1)
}

func main() {
    fmt.Println(factorial(5))
    // Output: 120
}
```

### 21. **Two Sum:**
**Challenge:** Write a function in Golang to find all pairs in an array that add up to a specific target sum.

**Solution:**
```go
package main

import "fmt"

func twoSum(nums []int, target int) [][]int {
    pairs := [][]int{}

    for i, num1 := range nums {
        for j, num2 := range nums {
            if i != j && num1+num2 == target {
                pairs = append(pairs, []int{num1, num2})
            }
        }
    }

    return pairs
}

func main() {
    nums := []int{1, 2, 3, 4, 5}
    fmt.Println(twoSum(nums, 7))
    // Output: [[2 5] [5 2]]
}
```

### 22. **Binary Search:**
**Challenge:** Implement a binary search algorithm in Golang.

**Solution:**
```go
package main

import "fmt"

func binarySearch(arr []int, target int) int {
    left, right := 0, len(arr)-1

    for left <= right {
        mid := (left + right) / 2

        if arr[mid] == target {
            return mid
        } else if arr[mid] < target {
            left = mid + 1
        } else {
            right = mid - 1
        }
    }

    return -1
}

func main() {
    arr := []int{1, 2, 3, 4, 5, 6, 7, 8, 9}
    fmt.Println(binarySearch(arr, 6))
    // Output: 5
}
```

### 23. **Valid Anagram:**
**Challenge:** Write a function in Golang to determine if two strings are anagrams.

**Solution:**
```go
package main

import (
    "fmt"
    "sort"
)

func isAnagram(s, t string) bool {
    if len(s) != len(t) {
        return false
    }

    sChars, tChars := []rune(s), []rune(t)
    
	sort.Slice(sChars, func(i, j int) bool { 
		return sChars[i] < sChars[j] 
	})
    
	sort.Slice(tChars, func(i, j int) bool { 
		return tChars[i] < tChars[j] 
	})

    return string(sChars) == string(tChars)
}

func main() {
    fmt.Println(isAnagram("listen", "silent"))
    // Output: true
}
```

### 24. **Reverse Linked List:**
**Challenge:** Implement a function in Golang to reverse a singly linked list.

**Solution:**
```go
package main

import "fmt"

type ListNode struct {
    Value int
    Next  *ListNode
}

func reverseLinkedList(head *ListNode) *ListNode {
    var prev *ListNode

    for head != nil {
        nextNode := head.Next
        head.Next = prev
        prev = head
        head = nextNode
    }

    return prev
}

func main() {
    head := &ListNode{Value: 1, Next: &ListNode{Value: 2, Next: &ListNode{Value: 3}}}
    reversedHead := reverseLinkedList(head)

    // Display the reversed linked list
    for node := reversedHead; node != nil; node = node.Next {
        fmt.Print(node.Value, " ")
    }
    // Output: 3 2 1
}
```

### 25. **Counting Elements:**
**Challenge:** Write a function in Golang to count the number of elements in an array that are smaller than the element at their index.

**Solution:**
```go
package main

import "fmt"

func countSmallerElements(nums []int) []int {
    count := make([]int, len(nums))

    for i := 0; i < len(nums); i++ {
        for j := i + 1; j < len(nums); j++ {
            if nums[j] < nums[i] {
                count[i]++
            }
        }
    }

    return count
}

func main() {
    nums := []int{5, 2, 6, 1}
    fmt.Println(countSmallerElements(nums))
    // Output: [2 1 1 0]
}
```

### 26. **Valid Parenthesis Expression:**
**Challenge:** Write a function in Golang to determine if a given string represents a valid parentheses expression.

**Solution:**
```go
package main

import "fmt"

func isValidParentheses(s string) bool {
    stack := []rune{}
    parenthesesMap := map[rune]rune{')': '(', '}': '{', ']': '['}

    for _, char := range s {
        if char == '(' || char == '{' || char == '[' {
            stack = append(stack, char)
        } else if openParen, exists := parenthesesMap[char]; exists {
            if len(stack) == 0 || stack[len(stack)-1] != openParen {
                return false
            }
            stack = stack[:len(stack)-1]
        }
    }

    return len(stack) == 0
}

func main() {
    fmt.Println(isValidParentheses("(){}[]"))
    // Output: true
}
```

### 27. **Meeting Rooms:**
**Challenge:** Given a list of meetings, write a function in Golang to determine if a person can attend all meetings without overlapping.

**Solution:**
```go
package main

import (
    "fmt"
    "sort"
)

type Meeting struct {
    Start, End int
}

func canAttendMeetings(meetings []Meeting) bool {
    sort.Slice(meetings, func(i, j int) bool { return meetings[i].Start < meetings[j].Start })

    for i := 1; i < len(meetings); i++ {
        if meetings[i].Start < meetings[i-1].End {
            return false
        }
    }

    return true
}

func main() {
    meetings := []Meeting{{0, 30}, {5, 10}, {15, 20}}
    fmt.Println(canAttendMeetings(meetings))
    // Output: false
}
```


### 28. **Goroutine Basics:**
**Challenge:** Write a Golang program that uses Goroutines to print "Hello, World!" concurrently.

**Solution:**
```go
package main

import (
	"fmt"
	"sync"
)

func printHello() {
	fmt.Println("Hello, World!")
}

func main() {
	go printHello()
	// Ensure the Goroutine completes before the main function exits
	var wg sync.WaitGroup
	wg.Add(1)
	wg.Wait()
}
```

### 29. **Channel Communication:**
**Challenge:** Create two Goroutines. One Goroutine should send numbers from 1 to 10 to a channel, and the other Goroutine should receive the numbers and print them.

**Solution:**
```go
package main

import "fmt"

func sender(ch chan int) {
	for i := 1; i <= 10; i++ {
		ch <- i
	}
	close(ch)
}

func receiver(ch chan int) {
	for num := range ch {
		fmt.Println(num)
	}
}

func main() {
	ch := make(chan int)
	go sender(ch)
	go receiver(ch)

	// Ensure both Goroutines have completed before the main function exits
	var input string
	fmt.Scanln(&input)
}
```

### 30. **Concurrency with WaitGroup:**
**Challenge:** Modify the previous example to use `sync.WaitGroup` to ensure that both Goroutines have completed before the main function exits.

**Solution:**
```go
package main

import (
	"fmt"
	"sync"
)

func sender(ch chan int, wg *sync.WaitGroup) {
	defer wg.Done()
	for i := 1; i <= 10; i++ {
		ch <- i
	}
	close(ch)
}

func receiver(ch chan int, wg *sync.WaitGroup) {
	defer wg.Done()
	for num := range ch {
		fmt.Println(num)
	}
}

func main() {
	ch := make(chan int)
	var wg sync.WaitGroup

	wg.Add(2)
	go sender(ch, &wg)
	go receiver(ch, &wg)

	wg.Wait()
}
```

### 31. **Producer-Consumer with Channels:**
**Challenge:** Implement a simple producer-consumer scenario. Have one Goroutine act as a producer, generating numbers from 1 to 5 and sending them to a channel. Another Goroutine should act as a consumer, receiving the numbers and printing them.

**Solution:**
```go
package main

import (
	"fmt"
	"sync"
)

func producer(ch chan int, wg *sync.WaitGroup) {
	defer wg.Done()
	for i := 1; i <= 5; i++ {
		ch <- i
	}
	close(ch)
}

func consumer(ch chan int, wg *sync.WaitGroup) {
	defer wg.Done()
	for num := range ch {
		fmt.Println(num)
	}
}

func main() {
	ch := make(chan int)
	var wg sync.WaitGroup

	wg.Add(2)
	go producer(ch, &wg)
	go consumer(ch, &wg)

	wg.Wait()
}
```

### 32. **Select Statement with Timeout:**
**Challenge:** Implement a Goroutine that performs a task but times out after a certain duration. Use the `select` statement to handle both the task completion and the timeout.

**Solution:**
```go
package main

import (
	"fmt"
	"time"
)

func task(ch chan bool) {
	time.Sleep(3 * time.Second)
	ch <- true
}

func main() {
	ch := make(chan bool)

	go task(ch)

	select {
	case result := <-ch:
		fmt.Println("Task completed:", result)
	case <-time.After(2 * time.Second):
		fmt.Println("Task timed out")
	}
}
```

### 33. **print and sum prime numbers which has digits sum is less than 10**
**Challenge:** Find a prime numbers from 1 -100 and sum of it's digit and sum should be less than 10.

**Solution:**
```go
package main

import (
	"fmt"
)

func primeSum(num int) int {
	count := 0
	for i := 1; i <= num; i++ {
		if num%i == 0 {
			count++
		}
	}

	if count == 2 {
		sum := sumOfDigits(num)
		if sum < 10 {
			fmt.Print(num, " ")
			return sum
		}
	}
	return 0
}

func sumOfDigits(n int) int {
	sum := 0
	// Iterate through each digits of the number
	for n > 0 {
		// Extract the last digit
		digit := n % 10

		// add digit to the sum
		sum += digit

		// Remove the last digit from the number
		n = n / 10
	}
	return sum
}

func main() {
	allPrimeSum := 0
	allDigitSum := 0

	for i := 1; i <= 100; i++ {
		prSum := primeSum(i)
		if prSum > 0 {
			allDigitSum += prSum
			allPrimeSum += i
		}
	}
	fmt.Println()
	fmt.Println("All Prime Sum:", allPrimeSum)
	fmt.Println("All Prime Digit Sum:", allDigitSum)
}
```

### 34. **Print Even Odd Number in Sequence**
**Challenge:** Write a program to print even and odd number in between 1 to 10 in alternatly, using two goroutine functions?

**Solution:**
```go
package main

import (
	"fmt"
	"sync"
)

func printOdd(ch chan struct{}, wg *sync.WaitGroup) {
	defer wg.Done()
	for i := 1; i <= 10; i++ {
		ch <- struct{}{}
		if i%2 == 1 {
			fmt.Print(i, " ")
		}
	}
}

func printEven(ch chan struct{}, wg *sync.WaitGroup) {
	defer wg.Done()
	for i := 1; i <= 10; i++ {
		<-ch
		if i%2 == 0 {
			fmt.Print(i, " ")
		}
	}
}

func main() {
	var wg sync.WaitGroup
	ch := make(chan struct{})
	wg.Add(2)
	go printOdd(ch, &wg)
	go printEven(ch, &wg)
	wg.Wait()
	close(ch)
	fmt.Println()
}
```


### 35. **Stack and Queue implementation:**
**Challenge:** Build Stack and Queue in golang.

**Solution:**
```go
package main

import "fmt"

type Stack struct {
	Val []int
}

type Queue struct {
	Val []int
}

func (s *Stack) Push(num int) int {
	s.Val = append(s.Val, num)
	return num
}

func (s *Stack) Pop() {
	if !s.IsEmpty() {
		fmt.Printf("\nPopped %v from stack\n", s.Val[len(s.Val)-1])
		s.Val = s.Val[:len(s.Val)-1]
	} else {
		fmt.Println("Stack is empty!")
	}
}

func (q *Queue) Enqueue(num int) int {
	q.Val = append(q.Val, num)
	return num
}

func (q *Queue) Dequeue() {
	if !q.IsEmpty() {
		fmt.Printf("\nDequeued %v from queue\n", q.Val[0])
		q.Val = q.Val[1:]
	} else {
		fmt.Println("Queue is empty!")
	}
}

func (q *Queue) IsEmpty() bool {
	if len(q.Val) == 0 {
		return true
	}
	return false
}

func (s *Stack) IsEmpty() bool {
	if len(s.Val) == 0 {
		return true
	}
	return false
}

func main() {
	// LastInFirstOut
	stk := Stack{}
	stk.Push(2)
	fmt.Println("Stack: ", stk.Val)
	stk.Push(3)
	fmt.Println("Stack: ", stk.Val)
	stk.Push(4)
	fmt.Println("Stack: ", stk.Val)
	stk.Push(6)
	fmt.Println("Stack: ", stk.Val)
	stk.Pop()
	fmt.Println("Stack: ", stk.Val)
	stk.Pop()
	fmt.Println("Stack: ", stk.Val)
	stk.Pop()
	fmt.Println("Stack: ", stk.Val)
	stk.Pop()
	fmt.Println("Stack: ", stk.Val)
	// FirstInFirstOut
	fmt.Println()
	que := Queue{}
	que.Enqueue(12)
	fmt.Println("Queue: ", que.Val)
	que.Enqueue(23)
	fmt.Println("Queue: ", que.Val)
	que.Enqueue(45)
	fmt.Println("Queue: ", que.Val)
	que.Enqueue(65)
	fmt.Println("Queue: ", que.Val)
	que.Enqueue(49)
	fmt.Println("Queue: ", que.Val)
	que.Dequeue()
	fmt.Println("Queue: ", que.Val)
	que.Dequeue()
	fmt.Println("Queue: ", que.Val)
	que.Dequeue()
	fmt.Println("Queue: ", que.Val)
	que.Dequeue()
	fmt.Println("Queue: ", que.Val)
}
```

