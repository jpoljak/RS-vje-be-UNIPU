import asyncio


async def dohvati_podatke():
    await asyncio.sleep(3)
    podaci = [i for i in range(1, 11)]
    print("Podaci dohvaćeni.")
    return podaci


async def main():
    # samo await, bez gather() i create_task()
    podaci = await dohvati_podatke()
    print(podaci)


asyncio.run(main())
