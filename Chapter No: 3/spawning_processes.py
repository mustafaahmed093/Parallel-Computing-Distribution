import multiprocessing
from do_something import do_something

def run_task(index):
    print(f"[⚙️] Process {index} started")
    out_list = multiprocessing.Manager().list()
    do_something(index * 1000, out_list)
    print(f"[✅] Process {index} finished with {len(out_list)} results")

def launch_processes():
    for i in range(6):
        proc = multiprocessing.Process(target=run_task, args=(i,))
        proc.start()
        proc.join()

if __name__ == "__main__":
    launch_processes()
