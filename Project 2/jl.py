from joblib import Parallel, delayed
import time
import numpy as np

N_JOBS = -1  # Use all available cores


# Define a CPU-intensive matrix multiplication function
def matmul(size: int) -> np.ndarray:
    A = np.random.rand(size, size)
    B = np.random.rand(size, size)

    return A @ B


# Monte Carlo estimation of Pi
def monte_carlo_pi(num_samples):
    # np.random.seed()  # Ensure randomness across processes
    x = np.random.uniform(-1, 1, num_samples)
    y = np.random.uniform(-1, 1, num_samples)
    inside_circle = np.sum(x**2 + y**2 <= 1)
    return inside_circle


N = 100  # Set a large matrix size
K = 10000  # Number of times to run the matrix multiplication

print("Running matrix multiplication...")

# Parallel execution
t = time.perf_counter()
results_parallel = Parallel(n_jobs=N_JOBS)(delayed(matmul)(N) for _ in range(K))
print(f"Parallel: {time.perf_counter() - t:.2f} s")

# Serial execution
t = time.perf_counter()
results_serial = [matmul(N) for _ in range(K)]
print(f"Serial: {time.perf_counter() - t:.2f} s")

print("Running Monte Carlo estimation of Pi...")

N = 1_000_000
K = 1_000

# Parallel Execution
t = time.perf_counter()
inside = Parallel(n_jobs=N_JOBS)(delayed(monte_carlo_pi)(N) for _ in range(K))
pi = 4 * sum(inside) / (N * K)
print(f"Parallel: {time.perf_counter() - t:.2f} s, Pi Estimate: {pi}")

# Serial Execution
t = time.perf_counter()
inside = [monte_carlo_pi(N) for _ in range(K)]
pi = 4 * sum(inside) / (N * K)
print(f"Serial: {time.perf_counter() - t:.2f} s, Pi Estimate: {pi}")


#!/usr/bin/env python3
# countasync.py

import asyncio


async def count1():
    print("One")
    await asyncio.sleep(1)
    print("Two")


async def count2():
    print("Three")
    await asyncio.sleep(1)
    print("Four")


async def count3():
    print("Five")
    await asyncio.sleep(1)
    print("Six")


async def main():
    await asyncio.gather(count1(), count2(), count3())


if __name__ == "__main__":
    import time

    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    # print(f"{__file__} executed in {elapsed:0.2f} seconds.")
    print(f"executed in {elapsed:0.2f} seconds.")

import time


async def f():
    await asyncio.sleep(1)
    return 42


async def g():
    # Pause here and come back to g() when f() is ready
    r = await f()
    print("HELLO :)")
    return r


asyncio.run(g())


async def main():
    r = await g()
    print(r)


s = time.perf_counter()
main()
elapsed = time.perf_counter() - s
print(f"executed in {elapsed:0.2f} seconds.")
