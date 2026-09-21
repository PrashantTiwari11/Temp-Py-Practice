# 81_python_asyncio_projects.py
# Asyncio - 10 practical programs/features
import asyncio

async def greet(name):
    await asyncio.sleep(0.1)
    return f"Hello, {name}"

async def fetch_data(item):
    await asyncio.sleep(0.1)
    return f"Data for {item}"

async def async_numbers(n):
    for i in range(1, n + 1):
        await asyncio.sleep(0)
        yield i

async def main():
    print("1. Async greeting:", await greet("Prashant"))

    results = await asyncio.gather(greet("Aman"), greet("Riya"))
    print("2. Gather:", results)

    for i in range(3, 0, -1):
        await asyncio.sleep(0.05)
        print("3. Countdown:", i)

    results = await asyncio.gather(
        fetch_data("users"), fetch_data("products"), fetch_data("orders")
    )
    print("4. Concurrent fetch:", results)

    values = [x async for x in async_numbers(5)]
    print("5. Async comprehension:", values)

    total = 0
    async for value in async_numbers(4):
        total += value
    print("6. Async generator sum:", total)

    try:
        await asyncio.wait_for(asyncio.sleep(0.05), timeout=0.2)
        print("7. Timeout test: completed")
    except asyncio.TimeoutError:
        print("7. Timeout test: timed out")

    task = asyncio.create_task(greet("Task User"))
    print("8. Created task:", await task)

    lock = asyncio.Lock()
    async with lock:
        print("9. Async lock: acquired safely")

    print("10. Async workflow:", await fetch_data("profile"))

asyncio.run(main())
