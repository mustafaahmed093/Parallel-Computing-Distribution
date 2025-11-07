import threading
import time
from do_something import do_something

def worker(thread_id, size, out_list, lock):
    """Worker function to perform task with thread-safe access."""
    print(f"[+] Thread {thread_id} started.")
    with lock:
        do_something(size, out_list)
    print(f"[-] Thread {thread_id} finished.")

def run_threads(num_threads, size):
    """Initialize and run multiple threads."""
    out_list = []
    lock = threading.Lock()
    threads = []

    # Create threads
    for i in range(num_threads):
        thread = threading.Thread(target=worker, args=(i, size, out_list, lock))
        threads.append(thread)

    # Start threads with delay
    for thread in threads:
        thread.start()
        time.sleep(0.5)  # Delay for clearer output order

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

    return out_list

if __name__ == "__main__":
    NUM_THREADS = 3
    SIZE = 7

    final_output = run_threads(NUM_THREADS, SIZE)

    print("\nFinal Output List:", final_output)
    print("Length of list (Lock):", len(final_output))
