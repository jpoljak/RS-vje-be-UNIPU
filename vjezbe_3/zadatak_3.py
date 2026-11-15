import asyncio

baza_korisnika = [
    {'korisnicko_ime': 'mirko123', 'email': 'mirko123@gmail.com'},
    {'korisnicko_ime': 'ana_anic', 'email': 'aanic@gmail.com'},
    {'korisnicko_ime': 'maja_0x', 'email': 'majaaaaa@gmail.com'},
    {'korisnicko_ime': 'zdeslav032', 'email': 'deso032@gmail.com'}
]

baza_lozinka = [
    {'korisnicko_ime': 'mirko123', 'lozinka': 'lozinka123'},
    {'korisnicko_ime': 'ana_anic', 'lozinka': 'super_teska_lozinka'},
    {'korisnicko_ime': 'maja_0x', 'lozinka': 's324SDFfdsj234'},
    {'korisnicko_ime': 'zdeslav032', 'lozinka': 'deso123'}
]


async def autorizacija(korisnik_iz_baze, lozinka):
    await asyncio.sleep(2)  # simulacija dekripcije lozinke i provjere
    ime = korisnik_iz_baze['korisnicko_ime']
    for zapis in baza_lozinka:
        if zapis['korisnicko_ime'] == ime and zapis['lozinka'] == lozinka:
            return f"Korisnik {ime}: Autorizacija uspješna."
    return f"Korisnik {ime}: Autorizacija neuspješna."


async def autentifikacija(korisnik):
    await asyncio.sleep(3)  # simulacija upita prema bazi u Cloudu
    for zapis in baza_korisnika:
        if (zapis['korisnicko_ime'] == korisnik['korisnicko_ime']
                and zapis['email'] == korisnik['email']):
            return await autorizacija(zapis, korisnik['lozinka'])
    return f"Korisnik {korisnik['korisnicko_ime']} nije pronađen."


async def main():
    ispravan = {'korisnicko_ime': 'ana_anic', 'email': 'aanic@gmail.com', 'lozinka': 'super_teska_lozinka'}
    kriva_lozinka = {'korisnicko_ime': 'mirko123', 'email': 'mirko123@gmail.com', 'lozinka': 'pogresna'}
    nepoznat = {'korisnicko_ime': 'nepoznati', 'email': 'x@gmail.com', 'lozinka': 'abc'}

    print(await autentifikacija(ispravan))
    print(await autentifikacija(kriva_lozinka))
    print(await autentifikacija(nepoznat))


asyncio.run(main())
