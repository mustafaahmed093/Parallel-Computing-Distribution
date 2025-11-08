import multiprocessing
import time
from do_something import do_something

def run_process():
    name = multiprocessing.current_process().name
    print(f"[🚀] Starting {name}")

    out_list = multiprocessing.Manager().list()
    size = 5 if name == "background_process" else 10
    do_something(size, out_list)

    time.sleep(1)
    print(f"[✅] Exiting {name}")

def launch_daemon_demo():
    bg_proc = multiprocessing.Process(name="background_process", target=run_process)
    bg_proc.daemon = True

    fg_proc = multiprocessing.Process(name="NO_background_process", target=run_process)
    fg_proc.daemon = False

    bg_proc.start()
    fg_proc.start()

    bg_proc.join(timeout=2)
    fg_proc.join()

if __name__ == "__main__":
    launch_daemon_demo()
