Parallel and Distributed Computing – Performance Evaluation

📘 Project Overview

This project compares the performance of Multiprocessing and Multithreading in Python for CPU-intensive computations.
A prime number generator is used to measure how well each approach handles heavy computational workloads and parallel execution.

---

📁 Project Structure

```
project/
│
├── do_something.py          # Defines the CPU-heavy computational task
├── multiprocessing_test.py  # Runs and compares multiprocessing vs multithreading
└── README.md                # Project documentation
```

---

🔬 Computational Task — `do_something.py`

What It Does

The `do_something()` function executes a series of **CPU-intensive mathematical operations**, including:

1. **Prime Number Calculation** — Finds all primes from 2 to *n* using trial division (O(n√n)).
2. **Mathematical Computations** — Performs repeated calculations of square roots, trigonometric functions (sin, cos), and logarithms.
3. **Result Logging** — Tracks the total primes, the highest prime found, and computation results for each process/thread.

```python
def do_something(size, out_list):
    """
    Args:
        size (int): Range for computation
        out_list (list): List to store output
    """
```

 Why This Task?

✅ Heavy mathematical processing
✅ Minimal I/O involvement
✅ Ideal for showcasing multiprocessing efficiency

---

 ⚙️ Execution Flow

 Multiprocessing

```python
for i in range(50):
    process = multiprocessing.Process(target=do_something, args=(size, out_list))
    jobs.append(process)
```

Characteristics:

 Independent processes, each with its own memory space
 True parallelism (multi-core utilization)
 No interference from Python’s GIL
 Higher memory usage due to isolated processes

Multithreading

```python
for i in range(10):
    thread = threading.Thread(target=do_something, args=(size, out_list))
    jobs.append(thread)
```

Characteristics:

 All threads share the same memory space
 Limited by the **Global Interpreter Lock (GIL)** — prevents true parallel CPU execution
 Best suited for I/O-bound workloads
 Low memory footprint

---

📊 Comparative Performance

| Metric          | Multiprocessing                   | Multithreading                  |
| :-------------- | :-------------------------------- | :------------------------------ |
| Execution Speed | ⚡ Fast (true parallelism)         | 🐢 Slow (sequential due to GIL) |
| CPU Utilization | High (multi-core)                 | Low (single core active)        |
| Memory Usage    | High                              | Low                             |
| Scalability     | Excellent (scales with CPU cores) | Limited by GIL                  |
| Ideal Use       | CPU-bound tasks                   | I/O-bound tasks                 |

Why Multiprocessing Wins:

> Each process runs independently on a separate core, achieving true simultaneous execution, while threads remain sequential under GIL constraints.

---

🧠 The Global Interpreter Lock (GIL)

 Prevents multiple threads from executing Python bytecode at once
 Limits performance in CPU-bound workloads
 Multiprocessing bypasses GIL by creating separate interpreters
 Threads are still valuable for network, file, and GUI operations

---

🔧 Adjustable Parameters

```python
size = 10000      # Range for computation
procs = 50        # Number of processes
threads = 10      # Number of threads
```

Experiment Ideas:

Increase `size` → longer runtime, multiprocessing advantage increases
Raise `procs` beyond CPU cores → diminishing returns
Equalize `threads` & `procs` → threads fall behind
Decrease workload → multiprocessing overhead becomes noticeable

---

📈 Sample Output

```
Process completed: Found 1229 primes, Largest: 9973, Result: 45623.47
...
Multiprocessing time = 3.24s

Thread completed: Found 1229 primes, Largest: 9973, Result: 45623.47
...
Multithreading time = 14.67s
```
Observation: Multiprocessing achieved ~4–5× better performance despite running more workers.

---

🎯 Key Insights

Use Multiprocessing When:

Tasks are CPU-heavy (mathematics, encoding, data analysis)
Computation can be split into independent parts
You have multiple CPU cores

Use Multithreading When:

Task is I/O-bound (file, API, or network operations)
Memory optimization is important
GUI or background tasks require responsiveness

Avoid Both When:

Tasks are simple or too small for parallel overhead

---

🧩 Technical Highlights

 Process Lifecycle

1. Creation → `multiprocessing.Process()`
2. Start → `.start()`
3. Execution → runs independently
4. Join → `.join()` waits for completion

Always include:

```python
if __name__ == "__main__":
```

→ Prevents recursive process spawning and ensures Windows compatibility.

---

⚡ Performance Influencers

Multiprocessing:

* CPU core count
* Process creation cost
* Memory usage
* Inter-process communication

Multithreading:

 GIL contention
 Context switching overhead
 Task type (CPU vs I/O bound)

---

 📚 Concepts Covered

* Parallel programming paradigms
* Process vs thread models
* GIL limitations
* CPU-bound vs I/O-bound tasks
* Performance benchmarking
* Scalability analysis

---

🎓 Course Context

Developed for the Parallel and Distributed Computing course to demonstrate:

* Practical use of concurrency in Python
* Measuring real-world performance differences
* Understanding trade-offs between threads and processes

---

 ⚠️ Important Notes

* 🧠 High process count = more RAM usage
* 💻 Gains level off beyond physical core count
* 🧩 Platform performance may vary
* 🐍 Tested on Python 3.x

---

🏁 Conclusion

This experiment clearly shows that multiprocessing outperforms multithreading for CPU-intensive workloads.
Although multiprocessing uses more memory, it achieves true parallel execution, bypassing the GIL and providing 3–5× faster performance.

For large-scale data processing or computation-heavy applications, multiprocessing is the recommended approach.

---

👨‍💻 Author

Prepared for the Parallel and Distributed Computing coursework.

---

📄 License

Free for educational and academic use.

