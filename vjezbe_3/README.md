# Vježbe 3 – asyncio (korutine, Task objekti, gather, event loop)

Rješenja zadataka za vježbu iz skripte RS3. Koriste se samo `asyncio`, `time` i `random` iz standardne biblioteke, pa nije potrebno ništa instalirati.

| Zadatak | Datoteka | Što radi |
|---|---|---|
| 1 | `zadatak_1.py` | korutina koja nakon 3 s vraća listu 1–10 (samo `await`) |
| 2 | `zadatak_2.py` | dvije korutine (3 s i 5 s) kroz `gather()`, ukupno ~5 s |
| 3 | `zadatak_3.py` | `autentifikacija()` i `autorizacija()` |
| 4 | `zadatak_4.py` | `provjeri_parnost()` za 10 nasumičnih brojeva, ~2 s |
| 5 | `zadatak_5.py` | `secure_data()` za 3 rječnika, ~3 s |
| 6 | `zadatak_6.py` | ispis `Dovršio sam s 2.` bez `await task2` |
| 7 | `zadatak_7.md` | objašnjenje rada event loopa |

## Pokretanje

```bash
python3 zadatak_1.py
```
