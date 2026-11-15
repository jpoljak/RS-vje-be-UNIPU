# Zadatak 7 – Kako se ponaša event loop

Primjer iz zadatka:

```python
import asyncio

async def timer(name, delay):
    for i in range(delay, 0, -1):
        print(f'{name}: {i} sekundi preostalo...')
        await asyncio.sleep(1)
    print(f'{name}: Vrijeme je isteklo!')

async def main():
    timers = [
        asyncio.create_task(timer('Timer 1', 3)),
        asyncio.create_task(timer('Timer 2', 5)),
        asyncio.create_task(timer('Timer 3', 7))
    ]

    await asyncio.gather(*timers)

asyncio.run(main())
```

## Što se događa korak po korak

1. **Pokretanje.** `asyncio.run(main())` stvori event loop i u njega ubaci `main()`. Loop ga odmah počne izvršavati.

2. **Raspoređivanje taskova.** U `main()` tri puta pozivamo `create_task()`. Svaki poziv od korutine `timer(...)` napravi Task i stavi ga u red čekanja, ali se ništa još ne ispisuje. Taskovi su u stanju *pending* (spremni, čekaju da dođu na red). Redoslijed je Timer 1, Timer 2, Timer 3.

3. **`main()` se pauzira.** Na `await asyncio.gather(*timers)` `main()` kaže loopu da će čekati dok se svi taskovi ne dovrše i predaje mu kontrolu. Od tog trenutka `main()` je suspendiran.

4. **Prvi krug.** Loop uzima taskove redom. Timer 1 ispiše `3 sekundi preostalo...` i dođe do `await asyncio.sleep(1)`, pa se suspendira, a loop ga vraća u red i javlja da ga treba probuditi za 1 s. Isto se dogodi Timeru 2 (`5 sekundi preostalo...`) i Timeru 3 (`7 sekundi preostalo...`). Sad su sva tri suspendirana, a loop nema što raditi pa čeka prvi istek sleepa. Zato su prva tri ispisa gotovo istovremeno.

5. **Sljedeći krugovi.** Nakon otprilike sekundu loop budi taskove istim redom kojim su zaspali. Svaki ispiše novo preostalo vrijeme i opet zaspi. Tako se u svakoj sekundi ispisuju po tri retka, jedan za svaki timer, dok god sva tri rade.

6. **Timer 1 završava (nakon 3 s).** Nakon trećeg buđenja petlja u Timeru 1 je gotova, ispiše se `Timer 1: Vrijeme je isteklo!` i taj task je *done*. Timeri 2 i 3 nastavljaju kao da se ništa nije dogodilo. Od te sekunde ispisuju se samo dva retka.

7. **Timer 2 završava (nakon 5 s).** Isto se dogodi s Timerom 2. Ostaje samo Timer 3, koji još dvije sekunde ispisuje `2 sekundi preostalo...` i `1 sekundi preostalo...`.

8. **Timer 3 završava (nakon 7 s).** Ispiše `Timer 3: Vrijeme je isteklo!` i task je gotov. Sad su svi taskovi koje je `gather` čekao gotovi, pa se `main()` probudi, vrati i `asyncio.run()` zatvori event loop.

## Stanja korutina

| Faza | Timer 1 | Timer 2 | Timer 3 |
|---|---|---|---|
| nakon `create_task()` | pending | pending | pending |
| prvi krug, dok izvršava kod | running | čeka red | čeka red |
| na `await sleep(1)` | suspended | suspended | suspended |
| nakon ~3 s | done | suspended | suspended |
| nakon ~5 s | done | done | suspended |
| nakon ~7 s | done | done | done |

(U jednom trenutku radi samo jedan task, a ostali su ili spremni ili spavaju. Ništa se ne izvršava paralelno, samo se taskovi izmjenjuju u trenucima kad neki od njih čeka.)

## Zašto traje ~7 s, a ne 15 s

Da smo timere pozvali jedan za drugim s običnim `await timer(...)`, trebalo bi 3 + 5 + 7 = 15 sekundi. Ovako, dok jedan timer "spava", loop radi na drugima, pa se čekanja preklapaju i ukupno vrijeme je jednako trajanju najdužeg timera, dakle 7 sekundi.
