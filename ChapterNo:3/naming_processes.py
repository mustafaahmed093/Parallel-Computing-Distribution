import multiprocessing
import time
from do_something import do_something

def launch_processes(size):
    out_list1 = multiprocessing.Manager().list()
    out_list2 = multiprocessing.Manager().list()

    p1 = multiprocessing.Process(
        name="Worker-1",
        target=do_something,
        args=(size, out_list1)
    )

    p2 = multiprocessing.Process(
        target=do_something,
        args=(size, out_list2)
    )

    start = time.time()
    p1.start()
    p2.start()

    p1.join()
    p2.join()
    end = time.time()

    return out_list1, out_list2, end - start

if __name__ == "__main__":
    SIZE = 1000
    list1, list2, duration = launch_processes(SIZE)

    print(f"Worker-1 output length: {len(list1)}")
    print(f"Worker-2 output length: {len(list2)}")
    print(f"Execution time: {duration:.2f} seconds")
