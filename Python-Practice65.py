# 59_python_concurrency_basics.py
# Python Concurrency Basics - 10 practical programs/features
# Uses only the standard library.

import asyncio
import concurrent.futures
import queue
import threading
import time

# 1. Basic thread
def hello():
    print("1. Thread says hello")

t = threading.Thread(target=hello)
t.start()
t.join()

# 2. Thread with arguments
def greet(name):
    print(f"2. Hello, {name}")

t = threading.Thread(target=greet, args=("Python",))
t.start()
t.join()

# 3. Multiple threads
def worker(number):
    time.sleep(0.05)
    print(f"3. Worker {number} finished")

threads = [threading.Thread(target=worker, args=(i,)) for i in range(3)]
for t in threads:
    t.start()
for t in threads:
    t.join()

# 4. Thread-safe counter using Lock
counter = 0
lock = threading.Lock()

def increment():
    global counter
    for _ in range(1000):
        with lock:
            counter += 1

threads = [threading.Thread(target=increment) for _ in range(4)]
for t in threads:
    t.start()
for t in threads:
    t.join()
print("4. Locked counter:", counter)

# 5. Queue for producer/consumer
q = queue.Queue()

def producer():
    for item in range(3):
        q.put(item)
    q.put(None)

def consumer():
    while True:
        item = q.get()
        if item is None:
            q.task_done()
            break
        print("5. Consumed:", item)
        q.task_done()

p = threading.Thread(target=producer)
c = threading.Thread(target=consumer)
p.start(); c.start()
p.join(); c.join()

# 6. ThreadPoolExecutor
def square(x):
    return x * x

with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
    results = list(executor.map(square, range(5)))
print("6. Thread pool results:", results)

# 7. ProcessPoolExecutor
def cube(x):
    return x ** 3

if __name__ == "__main__":
    with concurrent.futures.ProcessPoolExecutor(max_workers=2) as executor:
        results = list(executor.map(cube, range(4)))
    print("7. Process pool results:", results)

# 8. Async coroutine
async def async_hello():
    await asyncio.sleep(0.05)
    return "async task complete"

print("8.", asyncio.run(async_hello()))

# 9. Run async tasks concurrently
async def async_job(n):
    await asyncio.sleep(0.05)
    return n * 10

async def run_jobs():
    return await asyncio.gather(*(async_job(i) for i in range(5)))

print("9. Async gather:", asyncio.run(run_jobs()))

# 10. Async timeout
async def slow_task():
    await asyncio.sleep(1)
    return "done"

async def timeout_demo():
    try:
        return await asyncio.wait_for(slow_task(), timeout=0.1)
    except asyncio.TimeoutError:
        return "task timed out safely"

print("10. Timeout:", asyncio.run(timeout_demo()))
