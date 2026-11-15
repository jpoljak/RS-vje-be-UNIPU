import asyncio
import time


async def fetch_data(param):
    print(f"Nešto radim s {param}...")
    await asyncio.sleep(param)
    print(f'Dovršio sam s {param}.')
    return f"Rezultat za {param}"


async def main():
    task1 = asyncio.create_task(fetch_data(1))  # schedule
    task2 = asyncio.create_task(fetch_data(2))  # schedule
    result1 = await task1
    print("Fetch 1 uspješno završen.")

    # main() bi sad završio, event loop bi se zatvorio i task2 bi bio prekinut.
    # Zato "držimo" main() živim barem onoliko koliko task2 još treba (2 - 1 = 1 s).
    # Dok main() spava, event loop ima vremena izvršiti task2.
    await asyncio.sleep(1.5)

    return [result1]


t1 = time.perf_counter()
results = asyncio.run(main())  # pokretanje event loop-a
t2 = time.perf_counter()
print(results)
print(f"Vrijeme izvođenja {t2 - t1:.2f} sekunde")
