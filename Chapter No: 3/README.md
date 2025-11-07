
---

##  Python Multiprocessing: Practical Demonstrations

This chapter explores Python’s `multiprocessing` module by showcasing how to create, name, synchronize, manage, and terminate multiple processes using a shared CPU-bound function `do_something()` from `do_something.py`.

---

⚙️ 1. `naming_processes.py`  
**Goal:** Assign custom names to processes and observe execution timing.  
**Code Snippet:**
```python
multiprocessing.Process(name='do_something process 1', target=do_something, args=(1000, out_list1))
multiprocessing.Process(target=do_something, args=(1000, out_list2))
```
**Output:**  
- Process 1 list length: 1000  
- Process 2 list length: 1000  
- Total time: 0.43s  
**Insight:** Named and unnamed processes ran concurrently, reducing execution time compared to sequential runs.

---

⚙️ 2. `spawning_processes.py`  
**Goal:** Dynamically spawn multiple processes in a loop.  
**Code Snippet:**
```python
for i in range(6):
    multiprocessing.Process(target=myFunc, args=(i,)).start()
```
**Output:**  
Each process handled `i * 1000` workload independently.  
**Insight:** Linear scaling confirmed. Each process executed in isolation with predictable output size.

---

⚙️ 3. `killing_processes.py`  
**Goal:** Demonstrate process lifecycle: start, terminate, join.  
**Code Snippet:**
```python
p.start(); p.terminate(); p.join()
```
**Output:**  
- Process started and terminated cleanly  
- Exit code: 0  
**Insight:** Lifecycle control verified. Safe use of `.start()`, `.terminate()`, and `.join()`.

---

⚙️ 4. `run_background_processes_no_daemons.py`  
**Goal:** Compare daemon vs non-daemon behavior.  
**Code Snippet:**
```python
background_process.daemon = True
NO_background_process.daemon = False
```
**Output:**  
- Daemon exited with main process  
- Non-daemon completed and returned results  
**Insight:** Daemon processes depend on main thread; non-daemons run independently.

---

⚙️ 5. `processes_barrier.py`  
**Goal:** Synchronize processes using `Barrier` and `Lock`.  
**Code Snippet:**
```python
Barrier(2), Lock()
```
**Output:**  
Processes waited at barrier and printed results in sync.  
**Insight:** Barrier ensured coordination; Lock maintained safe access.

---

### ⚙️ 6. `process_pool.py`  
**Goal:** Use `Pool` for parallel execution.  
**Code Snippet:**
```python
pool.map(do_something, range(10))
```
**Output:**  
Squared results: `[0, 1, 4, ..., 81]`  
**Insight:** Workload distributed across 4 processes efficiently.

---

📊 Summary Table

| Script                             | Purpose                          | ✅ | Key Insight                                 |
|-----------------------------------|----------------------------------|----|---------------------------------------------|
| `naming_processes.py`             | Process naming & parallel run    | ✅ | Named processes reduce debug friction       |
| `spawning_processes.py`           | Loop-based process creation      | ✅ | Scalable and isolated execution             |
| `killing_processes.py`            | Lifecycle control                | ✅ | Safe termination and joining                |
| `run_background_processes_no_daemons.py` | Daemon vs non-daemon         | ✅ | Daemons exit early; non-daemons persist     |
| `processes_barrier.py`            | Sync with Barrier & Lock         | ✅ | Ordered execution achieved                  |
| `process_pool.py`                 | Parallelism with Pool            | ✅ | Efficient concurrent computation            |

---

🧠 Final Takeaways

- Multiprocessing unlocks true parallelism for CPU-heavy tasks.  
- Naming and lifecycle control simplify debugging and process management.  
- Daemon processes are tied to the main thread; non-daemons run independently.  
- Barriers and locks help coordinate and protect shared resources.  
- Pools offer a clean way to distribute tasks across multiple workers.

---
