import threading
import time
from do_something import do_something

def worker(thread_id, size, out_list, rlock):
    """Thread worker that demonstrates reentrant locking."""
    print(f"[+] Thread {thread_id} started.")
    with rlock:
        # Re-acquire the same lock to show RLock behavior
        with rlock:
            do_something(size, out_list)
    print(f"[-] Thread {thread_id} finished.")

def run_rlock_threads(num_threads, size):
    """Initialize and run threads using RLock."""
    out_list = []
    rlock = threading.RLock()
    threads = []

    for i in range(num_threads):
        thread = threading.Thread(target=worker, args=(i, size, out_list, rlock))
        threads.append(thread)

    for thread in threads:
        thread.start()
        time.sleep(0.5)  # Delay for clearer output

    for thread in threads:
        thread.join()

    return out_list

if __name__ == "__main__":
    NUM_THREADS = 3
    SIZE = 7

    final_output = run_rlock_threads(NUM_THREADS, SIZE)

    print("\nFinal Output List:", final_output)
    print("Length of list (RLock):", len(final_output))
