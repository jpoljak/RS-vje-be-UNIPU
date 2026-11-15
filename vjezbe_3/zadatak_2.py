import asyncio
import time


async def dohvati_korisnike():
    await asyncio.sleep(3)
    return [
        {"id": 1, "ime": "Ana", "prezime": "Anić"},
        {"id": 2, "ime": "Marko", "prezime": "Marić"},
    ]


async def dohvati_proizvode():
    await asyncio.sleep(5)
    return [
        {"id": 1, "naziv": "Laptop", "cijena": 899.99},
        {"id": 2, "naziv": "Miš", "cijena": 19.99},
    ]


async def main():
    korisnici, proizvodi = await asyncio.gather(dohvati_korisnike(), dohvati_proizvode())
    print(f"Korisnici: {korisnici}")
    print(f"Proizvodi: {proizvodi}")


t1 = time.perf_counter()
asyncio.run(main())
t2 = time.perf_counter()
print(f"Vrijeme izvođenja {t2 - t1:.2f} sekunde")
