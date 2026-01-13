
# MPI Communication Patterns — 10 Process Comparison

## Overview

This project demonstrates and compares various **MPI (Message Passing Interface)** communication patterns implemented in Python using the **mpi4py** library.
Each program was executed with **10 processes (`-n 10`)** to analyze how data is distributed, exchanged, and collected among processes.

---

## ⚙️ Environment

* **Language:** Python 3.12
* **Library:** mpi4py
* **MPI Implementation:** Microsoft MPI (MS-MPI)
* **Platform:** Windows 10, VS Code Terminal
* **Execution Command:**

  ```bash
  mpiexec -n 10 python filename.py
  ```

---

## 🧩 Programs and Observations

| Program                        | Communication Type            | Description                                                                                                                  | Key Observation                                                                                                                                                                                       |
| ------------------------------ | ----------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `scatter.py`                   | One-to-many                   | Distributes unique data chunks from the root process to all other processes.                                                 | Each process received and processed a unique element efficiently.                                                                                                                                     |
| `gather.py`                    | Many-to-one                   | Collects results from all processes into the root.                                                                           | Rank 0 gathered all computed results successfully.                                                                                                                                                    |
| `broadcast.py`                 | One-to-all                    | Shares the same data from the root to all processes.                                                                         | All processes received identical values instantly.                                                                                                                                                    |
| `reduce.py`                    | Many-to-one (aggregated)      | Reduces distributed data by summing values from all processes.                                                               | Root process received correctly combined data.                                                                                                                                                        |
| `alltoall.py`                  | All-to-all                    | Every process communicates with every other process.                                                                         | All ranks exchanged data, showing heavy but complete communication.                                                                                                                                   |
| `pointtoPointCommunication.py` | Pairwise                      | Direct send/receive between specific processes.                                                                              | Data sent and received correctly between paired ranks.                                                                                                                                                |
| `deadLockProblems.py`          | Blocking send/receive         | Demonstrates improper synchronization leading to deadlock.                                                                   | Some processes waited indefinitely due to blocking communication.                                                                                                                                     |
| **`virtualtopology.py`**       | **Grid / Cartesian Topology** | Creates a 2D virtual topology (3×3 grid) where each process communicates with its logical neighbors (UP, DOWN, LEFT, RIGHT). | Each process correctly identified its grid position and neighbor ranks. Process outputs confirmed proper grid mapping and successful execution of `do_something()` with varied result counts (10–18). |

---


## 🧾 Unified Conclusion

Through these experiments, it is clear that **MPI provides a flexible and scalable model for parallel computation**. Each communication pattern serves a distinct purpose in distributed processing:

* **Collective operations** (`scatter`, `gather`, `broadcast`, `reduce`) are efficient and well-suited for data distribution, collection, and aggregation across multiple processes.
* **All-to-all communication** enables complete data sharing but increases overhead as the number of processes grows, making it less efficient for large-scale systems.
* **Point-to-point communication** provides fine control and efficiency for targeted data transfers between specific processes, ideal when full synchronization isn’t required.
* The **deadlock example** highlights the importance of synchronization and the careful use of blocking calls (`send`, `recv`) to ensure smooth communication flow.
* The **virtual topology example** demonstrates how MPI can map processes into structured 2D grids for neighbor communication, useful in scientific computing, image processing, and simulations. Processes correctly identified their neighbors, and computation was distributed across ranks effectively.

Overall, **MPI ensures high performance and scalability in parallel applications**, but the communication pattern must be chosen based on the workload type:

* Use **scatter/gather/reduce** for computational workloads with distributed data.
* Use **broadcast** for initializing shared variables.
* Use **alltoall** when every process needs full dataset visibility.
* Use **Cartesian grid topologies** for neighbor-based computation on 2D or multidimensional datasets.
* Avoid potential deadlocks through **non-blocking communication** or proper ordering.

In summary, these MPI programs collectively demonstrate how **parallelism, synchronization, and inter-process communication** can significantly improve computational efficiency when applied correctly in distributed environments.

---

## 📚 References

* [mpi4py Documentation](https://mpi4py.readthedocs.io)
* [Microsoft MPI (MS-MPI)](https://learn.microsoft.com/en-us/message-passing-interface/microsoft-mpi)

