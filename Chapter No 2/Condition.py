import threading
import time
from do_something import do_something

def worker(thread_id, size, out_list, condition):
    print(f"Thread {thread_id} started.")
    do_something(size, out_list)
    with condition:
        print(f"Thread {thread_id} notifying condition.")
        condition.notify()
    print(f"Thread {thread_id} finished.")

def monitor(out_list, condition, total_expected):
    with condition:
        while len(out_list) < total_expected:
            condition.wait()
            print(f"Monitor: Current length = {len(out_list)}")

if __name__ == "__main__":
    out_list = []
    condition = threading.Condition()
    num_threads = 3
    size = 7
    total_expected = num_threads * size

    threads = [threading.Thread(target=worker, args=(i, size, out_list, condition)) for i in range(num_threads)]
    monitor_thread = threading.Thread(target=monitor, args=(out_list, condition, total_expected))

    monitor_thread.start()
    for t in threads:
        t.start()
        time.sleep(0.5)
    for t in threads:
        t.join()
    monitor_thread.join()

    print("\nFinal Output List:", out_list)
    print("Length of list (Condition):", len(out_list))
