from do_something import do_something
import time
import multiprocessing
import threading

def run_multiprocessing(size, num_procs):
    """Run the multiprocessing test."""
    print("\n🔹 Starting Multiprocessing Test")
    start = time.time()
    jobs = []

    for _ in range(num_procs):
        out_list = []
        process = multiprocessing.Process(target=do_something, args=(size, out_list))
        jobs.append(process)

    for p in jobs:
        p.start()

    for p in jobs:
        p.join()

    duration = time.time() - start
    print(" Multiprocessing complete.")
    print(f"⏱ Total Time (Processes: {num_procs}) = {duration:.2f} seconds\n")
    return duration


def run_multithreading(size, num_threads):
    """Run the multithreading test."""
    print("\n🔹 Starting Multithreading Test")
    start = time.time()
    threads = []

    for _ in range(num_threads):
        out_list = []
        thread = threading.Thread(target=do_something, args=(size, out_list))
        threads.append(thread)

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    duration = time.time() - start
    print(" Multithreading complete.")
    print(f"⏱ Total Time (Threads: {num_threads}) = {duration:.2f} seconds\n")
    return duration


if __name__ == "__main__":
    # Configurable parameters
    SIZE = 10000         # workload for each process/thread
    PROCESSES = 10       # number of processes
    THREADS = 10         # number of threads

    print("🚀 Parallel vs Distributed Computing Performance Test")
    print(f"Workload size: {SIZE}\n")

    mp_time = run_multiprocessing(SIZE, PROCESSES)
    mt_time = run_multithreading(SIZE, THREADS)

    # Comparison summary
    print(" Summary:")
    print(f"Multiprocessing Time : {mp_time:.2f} s")
    print(f"Multithreading Time  : {mt_time:.2f} s")
    if mp_time < mt_time:
        print("🏁 Result: Multiprocessing performed faster! ")
    else:
        print(" Result: Multithreading performed faster (unexpected) ")
