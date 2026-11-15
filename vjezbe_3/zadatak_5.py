import asyncio
import time


async def secure_data(podaci):
    await asyncio.sleep(3)  # simulacija enkripcije na poslužitelju
    return {
        'prezime': podaci['prezime'],
        'broj_kartice': hash(podaci['broj_kartice']),  # fake enkripcija
        'CVV': hash(podaci['CVV']),
    }


async def main():
    osjetljivi_podaci = [
        {'prezime': 'Anić', 'broj_kartice': '4111111111111111', 'CVV': '123'},
        {'prezime': 'Marić', 'broj_kartice': '5500000000000004', 'CVV': '456'},
        {'prezime': 'Horvat', 'broj_kartice': '340000000000009', 'CVV': '789'},
    ]

    zadaci = [asyncio.create_task(secure_data(p)) for p in osjetljivi_podaci]
    rezultati = await asyncio.gather(*zadaci)

    for rezultat in rezultati:
        print(rezultat)


t1 = time.perf_counter()
asyncio.run(main())
t2 = time.perf_counter()
print(f"Vrijeme izvođenja {t2 - t1:.2f} sekunde")
