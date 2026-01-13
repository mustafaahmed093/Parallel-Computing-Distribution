import asyncio
import random
from do_something import do_something


async def task_A(end_time: float):
    print("task_A called")
    # CPU-bound work offloaded to a thread
    out_list = []
    loop = asyncio.get_running_loop()
    await loop.run_in_executor(None, do_something, random.randint(1000, 5000), out_list)
    print(f"task_A processed {len(out_list)} items; last={out_list[-1] if out_list else 'N/A'}")

    # Non-blocking pause
    await asyncio.sleep(random.randint(0, 2))
    if (loop.time() + 1.0) < end_time:
        await task_B(end_time)
    else:
        print("Stopping loop from task_A")


async def task_B(end_time: float):
    print("task_B called")
    out_list = []
    loop = asyncio.get_running_loop()
    await loop.run_in_executor(None, do_something, random.randint(1000, 5000), out_list)
    print(f"task_B processed {len(out_list)} items; last={out_list[-1] if out_list else 'N/A'}")

    await asyncio.sleep(random.randint(0, 2))
    if (loop.time() + 1.0) < end_time:
        await task_C(end_time)
    else:
        print("Stopping loop from task_B")


async def task_C(end_time: float):
    print("task_C called")
    out_list = []
    loop = asyncio.get_running_loop()
    await loop.run_in_executor(None, do_something, random.randint(1000, 5000), out_list)
    print(f"task_C processed {len(out_list)} items; last={out_list[-1] if out_list else 'N/A'}")

    await asyncio.sleep(random.randint(0, 2))
    if (loop.time() + 1.0) < end_time:
        await task_A(end_time)
    else:
        print("Stopping loop from task_C")


async def main():
    loop = asyncio.get_running_loop()
    end_time = loop.time() + 60  # ~60 seconds
    await task_A(end_time)


if __name__ == "__main__":
    asyncio.run(main())