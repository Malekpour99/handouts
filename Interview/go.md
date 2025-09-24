# Interview Questions

## Table of Contents

- [Interview Questions](#interview-questions)
  - [Table of Contents](#table-of-contents)
  - [Go](#go)
    - [Buffered Vs. Unbuffered Channels](#buffered-vs-unbuffered-channels)
    - [How to determine the size of buffered channel](#how-to-determine-the-size-of-buffered-channel)
    - [Closed Channels](#closed-channels)
    - [Deadlock in Go](#deadlock-in-go)
    - [Deadlock Vs. Blocking](#deadlock-vs-blocking)
    - [Goroutine Leak](#goroutine-leak)
      - [Detecting Goroutine Leaks](#detecting-goroutine-leaks)
      - [Handling Goroutine Leaks](#handling-goroutine-leaks)
    - [Goroutines (Go) Vs. Coroutines (Python)](#goroutines-go-vs-coroutines-python)
    - [Handling Race-Conditions](#handling-race-conditions)

## Go

### Buffered Vs. Unbuffered Channels

- Unbuffered Channels

  - `Capacity = 0`.
  - A **send blocks until there’s a receiver**, and **a receive blocks until there’s a sender**.
  - Forces **synchronization** between goroutines.
  - Great for `handoff` / `rendezvous` patterns.
  - Use when:
    - You want _strict synchronization_ between producer and consumer.
    - Data must be handed off _immediately_ (no queuing).

```go
ch := make(chan int) // unbuffered
go func() {
    ch <- 42 // blocks until receiver reads
}()
value := <-ch // blocks until sender writes
```

- Buffered Channels

  - `Capacity = n > 0`.
  - A **send blocks only when the buffer is full**, and a **receive blocks only when the buffer is empty**.
  - Provides **asynchronous** communication — producer and consumer don’t have to run in lockstep.
  - Use when:
    - You want to _decouple_ producers and consumers.
    - Temporary _queuing_ of data is okay (or desired).
    - You expect _bursts of work_ and don’t want producers to block immediately.

```go
ch := make(chan int, 3) // buffered with capacity 3
ch <- 1
ch <- 2
ch <- 3 // still non-blocking
// next send would block until a receiver consumes
```

---

### How to determine the size of buffered channel

1. Based on Producer vs Consumer Speed

- If **producers are faster than consumers**, you need a buffer big enough to **absorb bursts without blocking** immediately.
- Rule of thumb:
  - `Buffer size≈Producer rate×Expected processing latency`
- Example: Producer sends ~100 msgs/sec, consumer processes 1 msg in 50ms (20/sec).
  - `Buffer size ≈ 100×(1/20)=5`
  - So a buffer of `~5–10` gives headroom.

2. Based on Burstiness

- If **messages arrive in bursts but are consumed steadily**, the buffer should handle the burst size.
- Example: Producer dumps 100 messages in a second, consumer steadily processes 20/sec → `buffer ≥ 80` to avoid blocking.

3. System Constraints

- If **memory is limited** or **messages are large**, keep the buffer small to avoid excessive memory use.
- For tiny messages (ints, small structs), larger buffers may be acceptable.

4. Backpressure Strategy

- Sometimes you want a small buffer (e.g., 0–10) so **producers slow down when consumers can’t keep up**.
- This prevents unbounded growth and protects the system.

5. Empirical Tuning

- Often, you don’t know upfront.
- Start with a reasonable guess (like 10, 100, or 1000 depending on workload).
- Benchmark & profile (`go test -bench .`, `pprof`) to see latency and memory impact.
- **Increase if too much blocking, decrease if memory spikes**.

---

### Closed Channels

1. Writing (Send) to a Closed Channel

```go
ch := make(chan int)
close(ch)
ch <- 1  // ❌ panic: send on closed channel
```

- **Sending to a closed channel always panics**.
- Go runtime enforces this to **prevent silent data corruption**

2. Reading (Receive) from a Closed Channel

```go
ch := make(chan int, 2)
ch <- 42
close(ch)

v1, ok1 := <-ch // v1 = 42, ok1 = true
v2, ok2 := <-ch // v2 = 0,  ok2 = false
```

- If the channel still **has buffered values → you get those values**, `ok = true`.
- Once the **buffer is empty** → you get **the zero value of the element type**, and `ok = false`.
- This is how you detect that a channel is closed.
- when channel is open but buffer is empty, reading is blocked and `ok = true`.

3. Range over a Closed Channel

```go
ch := make(chan int, 2)
ch <- 1
ch <- 2
close(ch)

for v := range ch {
    fmt.Println(v) // prints 1, then 2, then exits
}
```

- A for range loop reads until the channel is **both closed and empty**.
- Clean way to drain all remaining values.
- On an **open channel**, the **loop will block forever** waiting for more values (unless you break manually or by using context/signal).

---

### Deadlock in Go

A **deadlock** in Go happens when **all goroutines are blocked**, waiting for something that will never happen. At that point, the program cannot make progress and usually panics with: `fatal error: all goroutines are asleep - deadlock!`

1. Unbuffered Channel with No Receiver

```go
ch := make(chan int) // unbuffered
ch <- 42             // blocks forever because no goroutine is receiving
```

- The sender is **blocked**, waiting for a receiver.
- If no receiver ever comes, this is a deadlock.

2. All Goroutines Blocked

```go
ch := make(chan int)
go func() {
    <-ch // waiting for a message
}()
<-ch    // main goroutine also waiting
```

- Both goroutines are waiting on each other → deadlock.

3. Channel Closed Wrongly

```go
ch := make(chan int)
close(ch)
ch <- 1 // panic: send on closed channel
```

- Not exactly a deadlock, but it can cause a similar blocking/error situation.

4. Full Buffered Channel with No Receiver

```go
ch := make(chan int, 2)
ch <- 1
ch <- 2
ch <- 3 // blocks because buffer is full and no one is receiving
```

- The sender waits forever → deadlock.

5. Improper `select` Usage

```go
ch1 := make(chan int)
ch2 := make(chan int)
select {
case ch1 <- 1:
case ch2 <- 2:
} // blocks if both channels are unready and no default case
```

- `select` blocks if no cases are ready and no `default` is provided.

- **Avoiding Deadlocks**:
- Use **buffered channels** when decoupling producer/consumer.
- Always ensure there’s a **receiver** if sending on unbuffered channels.
- Close channels carefully (**only the sender should close**).
- Use `select` with a `default` case if you don’t want to block.
- Keep goroutine coordination simple; avoid circular waits.
- Test with the race detector: `go run -race main.go`

### Deadlock Vs. Blocking

- **Blocking**
  - A goroutine is blocked when it’s **waiting for something** (e.g., a channel send/receive, mutex lock, or I/O) but other goroutines can still make progress.
  - Blocking is normal behavior in Go and part of concurrency design.

```go
ch := make(chan int)
go func() {
    val := <-ch // this goroutine blocks until a value is sent
    fmt.Println(val)
}()

ch <- 42 // main goroutine is sending, so eventually blocked goroutine resumes
```

- **Deadlock**

- A deadlock happens when a**ll goroutines in the program are blocked**, waiting for each other or some condition that can _never_ happen.
- Program **cannot make progress**, and Go runtime **panics**.

```go
ch := make(chan int)
ch <- 1 // main goroutine blocks, no other goroutine is receiving
```

---

### Goroutine Leak

A **goroutine leak** happens when **a goroutine is still running or blocked** even though it is **no longer needed**.

- Leaked goroutines **consume memory and resources**, potentially leading to performance issues or program crashes.
- Often caused by _blocked channels_, _forgotten goroutines_, or _infinite loops_.

Common Cases:

- Blocked on a channel forever
- Infinite loops without exit
- Context or signal not handled
- Waiting on external resource that never responds (e.g. Network call, DB query)

#### Detecting Goroutine Leaks

1. **Goroutine Dumps**

Print all active goroutines with stack traces:

```go
import "runtime/pprof"
pprof.Lookup("goroutine").WriteTo(os.Stdout, 1)
```

- Look for goroutines stuck on channels, `select`, or sleep that shouldn’t be running.

2. **`go tool pprof`**

```sh
go tool pprof http://localhost:8080/debug/pprof/goroutine
```

- Analyze the number and state of goroutines over time.
- Growing number of goroutines → potential leak.

3. **Monitoring / Logging**

- Track goroutine count using `runtime.NumGoroutine()`.
- Unexpected increase over time = possible leak.

#### Handling Goroutine Leaks

1. Use `context.Context` for Cancellation

- Write **context-aware code**, Pass a context and stop goroutine when context is canceled.

```go
ctx, cancel := context.WithCancel(context.Background())
go func(ctx context.Context) {
    for {
        select {
        case <-ctx.Done():
            return // exit goroutine
        default:
            // do work
        }
    }
}(ctx)

cancel() // stops goroutine
```

1. Close Channels Carefully

- Ensure goroutines exit when channels are closed.

3. Use `select` with Timeout

```go
select {
case msg := <-ch:
    // process msg
case <-time.After(time.Second):
    // exit or retry
}
// Prevents goroutines from blocking forever.
```

4. Avoid Infinite Loops Without Exit Condition

- Always provide an exit condition or cancellation mechanism.

5. Worker Pools

- Use a fixed number of workers and a task queue, so goroutines don’t grow unboundedly.

---

### Goroutines (Go) Vs. Coroutines (Python)

- **Goroutines (Go)**

  - Lightweight threads managed by the **Go runtime**.
  - Scheduled using Go’s `M:N` scheduler:
  - **Many goroutines (M) run on a smaller number of OS threads (N)**.
  - **Runtime handles preemption** (goroutines can be paused/resumed by the runtime).
  - Concurrency is achieved via `channels` and Go’s **CSP (Communicating Sequential Processes)** model.
  - Goroutines can run in _true parallel_ on multiple CPU cores.

- **Coroutines (Python)**

  - Special **functions that can be paused and resumed** (`async def`, `await`).
  - Cooperatively scheduled:
    - A **coroutine must explicitly `await` to give up control**.
    - If it never `awaits`, it will _block_ the event loop.
  - Concurrency is achieved via `async/await` and the **event loop** (`asyncio`).
  - No true parallelism in CPython (due to `GIL`); **only concurrency**.

---

### Handling Race-Conditions

- A `Mutex` (mutual exclusion) ensures **only one goroutine** enters a critical section at a time.

```go
package main

import (
  "fmt"
  "sync"
)

var (
  counter int
  lock    sync.Mutex
)

func worker(wg *sync.WaitGroup) {
  defer wg.Done()
  for i := 0; i < 100000; i++ {
    lock.Lock()
    counter++
    lock.Unlock()
  }
}

func main() {
  var wg sync.WaitGroup

  for i := 0; i < 5; i++ {
    wg.Add(1)
    go worker(&wg)
  }

  wg.Wait()
  fmt.Println("Final counter:", counter)
}
```

- When you have **many readers but few writers**, `RWMutex` allows **multiple goroutines to read simultaneously but only one to write**.

```go
var rw sync.RWMutex
var data = make(map[string]string)

func read(key string) string {
  rw.RLock()
  defer rw.RUnlock()
  return data[key]
}

func write(key, value string) {
  rw.Lock()
  defer rw.Unlock()
  data[key] = value
}
```

- For **counters**, Go has `sync/atomic` which is _faster_ than mutexes.

```go
package main

import (
  "fmt"
  "sync"
  "sync/atomic"
)

var counter int64

func worker(wg *sync.WaitGroup) {
  defer wg.Done()
  for i := 0; i < 100000; i++ {
    atomic.AddInt64(&counter, 1)
  }
}

func main() {
  var wg sync.WaitGroup

  for i := 0; i < 5; i++ {
    wg.Add(1)
    go worker(&wg)
  }

wg.Wait()
fmt.Println("Final counter:", counter)
}
```

- You can also use `channels` for writing and reading data which prevents race-conditions.
- Concurrent map access → `sync.Map` (built-in concurrent map)

---
