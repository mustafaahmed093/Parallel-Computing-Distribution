import multiprocessing
import time
from do_something import do_something

def run_task():
    out_list = multiprocessing.Manager().list()
    print("[🚀] Task started")
    do_something(10, out_list)
    print(f"[✅] Task finished with {len(out_list)} results")

def monitor_process(proc):
    print("[🔍] Before start:", proc, proc.is_alive())
    proc.start()
    print("[⚙️] Running:", proc, proc.is_alive())
    time.sleep(2)
    proc.terminate()
    print("[🛑] Terminated:", proc, proc.is_alive())
    proc.join()
    print("[🔚] Joined:", proc, proc.is_alive())
    print("[📦] Exit code:", proc.exitcode)

if __name__ == "__main__":
    process = multiprocessing.Process(target=run_task)
    monitor_process(process)
