package go_gctrace

import (
	"fmt"
	"sync"
)

func main() {
	go func() {
		list := make(map[int]int, 1e6)
		for i := 0; i < 1e6; i++ {
			list[i] = i
		}
	}()
	wg := sync.WaitGroup{}
	wg.Add(10)
	for i := 0; i <= 10; i++ {
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
