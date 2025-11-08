import multiprocessing
from multiprocessing import Barrier, Lock, Process
from time import time
from datetime import datetime
from do_something import do_something

def run_with_barrier(sync, lock):
    name = multiprocessing.current_process().name
    sync.wait()
    timestamp = datetime.fromtimestamp(time())
    with lock:
        print(f"{name} ---> {timestamp}")
        output = []
        do_something(2, output)
        print(f"{name} results: {output}")

def run_without_barrier():
    name = multiprocessing.current_process().name
    timestamp = datetime.fromtimestamp(time())
    print(f"{name} ---> {timestamp}")
    output = []
    do_something(2, output)
    print(f"{name} results: {output}")

def launch_processes():
    sync = Barrier(2)
    lock = Lock()

    processes = [
        Process(name="p1 - with_barrier", target=run_with_barrier, args=(sync, lock)),
        Process(name="p2 - with_barrier", target=run_with_barrier, args=(sync, lock)),
        Process(name="p3 - without_barrier", target=run_without_barrier),
        Process(name="p4 - without_barrier", target=run_without_barrier),
    ]

    for p in processes:
        p.start()

if __name__ == "__main__":
    launch_processes()
