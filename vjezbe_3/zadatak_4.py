import asyncio
import random
import time


async def provjeri_parnost(broj):
    await asyncio.sleep(2)  # "super zahtjevna operacija"
    if broj % 2 == 0:
        return f"Broj {broj} je paran."
    return f"Broj {broj} je neparan."


async def main():
    brojevi = [random.randint(1, 100) for _ in range(10)]
    zadaci = [asyncio.create_task(provjeri_parnost(broj)) for broj in brojevi]
    rezultati = await asyncio.gather(*zadaci)

    for rezultat in rezultati:
        print(rezultat)


t1 = time.perf_counter()
asyncio.run(main())
t2 = time.perf_counter()
print(f"Vrijeme izvođenja {t2 - t1:.2f} sekunde")
