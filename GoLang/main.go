// Golang Interview Coding Problems - Easy and Best Solutions

package main

import (
	"fmt"
	"sync"
)

func main() {
	wg := sync.WaitGroup{}
	done := make(chan struct{})

	wg.Add(2)
	go func() { // Odd numbers
		defer wg.Done()
		for i := 1; i <= 10; i++ {
			done <- struct{}{}
			if i%2 != 0 {
				fmt.Println("Odd:", i)
			}
		}
	}()
	go func() { // Even numbers
		defer wg.Done()
		for i := 1; i <= 10; i++ {
			<-done
			if i%2 == 0 {
				fmt.Println("Even:", i)
			}
		}
	}()
	wg.Wait()
	close(done)
}
