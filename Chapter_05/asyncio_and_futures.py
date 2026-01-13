import asyncio
import sys
from do_something import do_something


async def first_coroutine(num: int) -> str:
    count = 0
    for i in range(1, num + 1):
        count += 1
    await asyncio.sleep(4)
    return f"First coroutine (sum of N ints) result = {count}"


async def second_coroutine(num: int) -> str:
    count = 1
    for i in range(2, num + 1):
        count *= i
    await asyncio.sleep(4)
    return f"Second coroutine (factorial) result = {count}"


async def third_coroutine(size: int) -> str:
    loop = asyncio.get_running_loop()
    out_list = []
    # Run the CPU-bound function in a thread to avoid blocking the event loop
    await loop.run_in_executor(None, do_something, size, out_list)
    return f"Third coroutine (CPU-bound) processed {size} items; last={out_list[-1] if out_list else 'N/A'}"


async def main(num1: int, num2: int, size: int) -> None:
    # Create tasks for concurrent execution
    t1 = asyncio.create_task(first_coroutine(num1))
    t2 = asyncio.create_task(second_coroutine(num2))
    t3 = asyncio.create_task(third_coroutine(size))

    # Wait for all tasks to complete and collect their results
    results = await asyncio.gather(t1, t2, t3)

    # Print results
    for r in results:
        print(r)


if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: py -3 asyncio_and_futures.py <num1> <num2> <size>")
        sys.exit(1)

    num1 = int(sys.argv[1])
    num2 = int(sys.argv[2])
    size = int(sys.argv[3])

    asyncio.run(main(num1, num2, size))