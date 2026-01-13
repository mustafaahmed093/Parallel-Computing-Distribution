# Chapter 05 – Comparison of Asyncio, Threading, and Multiprocessing

This README summarizes and compares the results obtained from multiple Python concurrency programs executed in **Chapter_05**. The objective is to understand how **asyncio**, **ThreadPoolExecutor**, and **ProcessPoolExecutor** behave under different workloads.

---

## 1. Asyncio Task Manipulation (`asyncio_task_manipulation.py`)

### Observed Behavior

* `factorial`, `fibonacci`, and `binomial_coefficient` tasks run **concurrently**.
* Output lines are **interleaved**, confirming cooperative multitasking.
* `do_something.py` is executed using `asyncio.to_thread()`.

### Key Results

```
Asyncio.Task - factorial(10) = 3628800
Asyncio.Task - fibonacci(10) = 55
Asyncio.Task - binomial_coefficient(20, 10) = 184756.0
```

### Conclusion

* Asyncio handles **I/O-bound or sleep-based tasks efficiently**.
* CPU-bound work (`do_something`) must be offloaded to a thread.
* Asyncio does **not provide real parallelism for CPU-heavy tasks**.

---

## 2. Concurrent Futures Pooling (`concurrent_futures_pooling.py`)

### Execution Modes Tested

1. Sequential Execution
2. Thread Pool Execution (5 threads)
3. Process Pool Execution (5 processes)

### Observed Timings

| Execution Mode | Time (Approx.) |
| -------------- | -------------- |
| Sequential     | ~0.00 s        |
| Thread Pool    | ~0.01 s        |
| Process Pool   | ~0.29–0.40 s   |

### Observations

* Thread pool output is **unordered**, showing concurrency.
* Process pool execution is **slower for small workloads** due to process startup overhead.

### Conclusion

* Threads do **not speed up CPU-bound work** due to the GIL.
* Process pools enable **true parallelism**, but only benefit **large workloads**.

---

## 3. Asyncio with Futures (`asyncio_and_futures.py`)

### Purpose

Demonstrates how asyncio integrates:

* Pure async coroutines
* CPU-bound work using executors

### Output Summary

```
First coroutine result = 10
Second coroutine (factorial) result = 2432902008176640000
Third coroutine processed 1000000 items
```

### Conclusion

* Asyncio works best as an **orchestrator**.
* CPU-bound tasks must be delegated to threads or processes.

---

## 4. Asyncio Coroutine Chaining (`asyncio_coroutine.py`, `asyncio_event_loop.py`)

### Observed Behavior

* Tasks A, B, and C call each other recursively.
* Program eventually ends with `KeyboardInterrupt`.

### Reason

* Infinite coroutine cycle without termination condition.
* Event loop keeps scheduling tasks until manually stopped.

### Conclusion

* Asyncio requires **explicit termination logic**.
* Recursive coroutine chaining can cause **runaway execution**.

---

## Overall Comparison Summary

| Model               | Best For                     | Limitations           |
| ------------------- | ---------------------------- | --------------------- |
| Asyncio             | I/O-bound, cooperative tasks | No CPU parallelism    |
| ThreadPoolExecutor  | Blocking I/O                 | GIL limits CPU speed  |
| ProcessPoolExecutor | CPU-bound workloads          | High startup overhead |

---

## Final Conclusion

* **Asyncio** is ideal for managing many I/O-bound tasks efficiently.
* **Threads** help avoid blocking but do not improve CPU-heavy performance.
* **Processes** provide true parallelism and are best for large CPU-bound workloads.

This coursework demonstrates that **choosing the correct concurrency model depends on the nature of the task**, not the syntax used.

---
