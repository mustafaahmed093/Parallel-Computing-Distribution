 Thread Synchronization in Python  
Mechanisms: Lock, RLock, Semaphore, Condition

This project showcases how Python’s `threading` module handles concurrent access to shared resources using a unified function (`do_something.py`). Each synchronization primitive is tested to observe its behavior and impact on thread safety.

---

 🔐 1. Lock  
Purpose: Ensures exclusive access — only one thread modifies `out_list` at a time.  
Observed Behavior:
```
Thread 0 started. Thread 0 finished.  
Thread 1 started. Thread 1 finished.  
Thread 2 started. Thread 2 finished.  
Length of list (Lock): 21
```  
Result: ✅ Safe and expected output. No race conditions.

---

🔁 2. RLock (Reentrant Lock)  
Purpose: Allows the same thread to acquire the lock multiple times without deadlock.  
Observed Behavior:
Similar to Lock — sequential thread execution.  
Result: ✅ Consistent and safe. Ideal for nested locking.

---

### 🚦 3. Semaphore  
Purpose: Limits the number of threads accessing a resource concurrently.  
Observed Behavior:
```
Thread 0 waiting for permit...  
Thread 0 started.  
Thread 1 waiting for permit...  
Thread 2 waiting for permit...  
Thread 1 started.  
Thread 0 finished.  
Thread 1 finished.  
Thread 2 started.  
Thread 2 finished.  
Length of list (Semaphore): 21
```  
Result: ✅ Controlled parallelism. List integrity maintained.

---

 4. Condition  
Purpose: Allows threads to wait for a signal before proceeding.  
Observed Behavior:  
```
Thread 0 notifying condition.  
Thread 1 notifying condition.  
Thread 2 notifying condition.  
Monitor: Current length = 7  
Monitor: Current length = 14  
Monitor: Current length = 21
```  
Result: ✅ Threads coordinate via signals. Monitor tracks progress accurately.

---

### 📊 Comparative Summary

| Synchronization Type | Main Use                        | Behavior               | Safety | Best For                   |
|----------------------|----------------------------------|------------------------|--------|----------------------------|
| Lock                 | Prevents simultaneous access     | Sequential execution   | ✅     | General thread safety      |
| RLock                | Reentrant locking                | Similar to Lock        | ✅     | Nested locking scenarios   |
| Semaphore            | Limits concurrent access         | Controlled parallelism | ✅     | Managing limited resources |
| Condition            | Waits for signals/conditions     | Event-driven flow      | ✅     | Producer-consumer models   |

---

### 🧠 Final Thoughts  
All four mechanisms — Lock, RLock, Semaphore, and Condition — successfully preserved data integrity and avoided race conditions.  
- Use Lock/RLock for mutual exclusion.  
- Use Semaphore to control concurrency.  
- Use Condition for coordination and signaling.

---

 ▶️ How to Run  
Execute each script individually to observe behavior:

```bash
python Chapter_02/Lock.py  
python Chapter_02/RLock.py  
python Chapter_02/Semaphore.py  
python Chapter_02/Condition.py
```

---
