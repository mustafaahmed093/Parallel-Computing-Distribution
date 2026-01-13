import concurrent.futures
import time
import do_something   # <-- IMPORT HERE

number_list = list(range(1, 11))


def evaluate(item):
    output = []
    do_something.do_something(item, output)
    print(f'Item {item}, result {output[-1] if output else None}')


if __name__ == '__main__':

    # -------- Sequential Execution --------
    start_time = time.perf_counter()
    for item in number_list:
        evaluate(item)
    print(f'Sequential Execution in {time.perf_counter() - start_time:.2f} seconds')

    # -------- Thread Pool Execution --------
    start_time = time.perf_counter()
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        for item in number_list:
            executor.submit(evaluate, item)
    print(f'Thread Pool Execution in {time.perf_counter() - start_time:.2f} seconds')

    # -------- Process Pool Execution --------
    start_time = time.perf_counter()
    with concurrent.futures.ProcessPoolExecutor(max_workers=5) as executor:
        for item in number_list:
            executor.submit(evaluate, item)
    print(f'Process Pool Execution in {time.perf_counter() - start_time:.2f} seconds')
