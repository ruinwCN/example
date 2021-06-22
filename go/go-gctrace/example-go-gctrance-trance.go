package main

import (
	"fmt"
	"os"
	"runtime/trace"
	"sync"
)

func main() {

	f, _ := os.Create("trace.out")
	defer f.Close()
	trace.Start(f)
	defer trace.Stop()

	wg := sync.WaitGroup{}
	wg.Add(10)
	for i := 0; i < 10; i++ {
		go func() {
			list := make(map[int]int, 1e6)
			for i := 0; i < 1e6; i++ {
				list[i] = i
			}
			wg.Done()
		}()
	}
	wg.Wait()
	fmt.Println("done")
}
