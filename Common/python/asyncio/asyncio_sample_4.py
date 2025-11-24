import asyncio
import time


async def fetch_data(param):
    await asyncio.sleep(param)
    return f"Result of {param}"


# different methods for running coroutines
async def main():
    # Create Tasks Manually
    task1 = asyncio.create_task(fetch_data(1))
    task2 = asyncio.create_task(fetch_data(2))
    result1 = await task1
    result2 = await task2
    print(f"Task 1 and 2 awaited results: {[result1, result2]}")

    # Gather Coroutines
    coroutines = [fetch_data(i) for i in range(1, 3)]
    results = await asyncio.gather(*coroutines, return_exceptions=True)
    print(f"Coroutine Results: {results}")

    # Gather Tasks (Recommended)
    tasks = [asyncio.create_task(fetch_data(i)) for i in range(1, 3)]
    results = await asyncio.gather(*tasks, return_exceptions=True)
    print(f"Task Results: {results}")

    # Task Group
    async with asyncio.TaskGroup() as tg:
        # ? All or Nothing: if one task fails, all of the tasks are cancelled!
        results = [tg.create_task(fetch_data(i)) for i in range(1, 3)]
        # All tasks are awaited when the context manager exits.
    print(f"Task Group Results: {[result.result() for result in results]}")

    return "Main Coroutine Done"


t1 = time.perf_counter()

results = asyncio.run(main())
print(results)

t2 = time.perf_counter()
print(f"Finished in {t2 - t1:.2f} seconds")
