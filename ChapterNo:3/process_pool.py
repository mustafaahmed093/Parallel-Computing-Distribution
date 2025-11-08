import multiprocessing
from do_something import do_something

def compute_square(data):
    temp = []
    do_something(2, temp)
    return data * data

def run_pool(inputs, num_processes):
    with multiprocessing.Pool(processes=num_processes) as pool:
        results = pool.map(compute_square, inputs)
    return results

if __name__ == "__main__":
    INPUTS = list(range(10))
    NUM_PROCESSES = 4

    output = run_pool(INPUTS, NUM_PROCESSES)
    print("Pool:", output)
