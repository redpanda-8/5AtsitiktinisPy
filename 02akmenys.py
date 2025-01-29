# 2. Užduoties sąlyga: Akmenų maišo žaidimas
# Maiše yra N akmenų. Vartotojas ir kompiuteris paeiliui traukia akmenis iš maišo. Per savo ėjimą kiekvienas žaidėjas gali 
# ištraukti nuo 1 iki 3 akmenų. Laimi tas, kuris paima paskutinį akmenį.
# Žaidimą pradeda vartotojas, pasirinkdamas kiek akmenų jis nori paimti. Po kiekvieno ėjimo programa turi atnaujinti 
# likusių akmenų skaičių ir nurodyti, kiek akmenų paėmė kompiuteris. Žaidimas tęsiasi, kol bus paimtas paskutinis akmuo.
# Reikalavimai:
# 1. Pradiniai duomenys: kompiuteris atsitiktinai sugeneruoja, kiek akmenų yra maišee. Tai turi būti skaičius tarp 15 
# ir 30 (arba vartotojas gali pasirinkti, kiek akmenų bus maiše pradžioje).
# 2. Vartotojo ėjimas:
# * Vartotojas kiekvieno savo ėjimo metu įveda skaičių nuo 1 iki 3, kuris nurodo, kiek akmenų jis nori paimti.
# * Jei vartotojas įveda neteisingą skaičių (pvz. daugiau akmenų nei liko arba mažiau nei 1 ar daugiau nei 3), 
# programa turi pranešti apie klaidą ir leisti bandyti dar kartą.
# 3. Kompiuterio ėjimas:
# * Po vartotojo ėjimo kompiuteris taip pat pasirenka, kiek akmenų nori paimti (nuo 1 iki 3).
# * Kompiuterio strategija gali būti atsitiktinė arba optimizuota, kad stengtųsi laimėti (pvz, siekti palikti vartotojui 
# nepalankų likusių akmenų skaičių).
# 4. Žaidimo eiga:
# * Po kiekvieno ėjimo programa turi parodyti likusių akmenų skaičių ir kas juos paėmė (vartotojas arba kompiuteris).
# * Žaidimas baigiasi, kai paimamas paskutinis akmuo. Laimi tas žaidėjas, kuris paima paskutinį akmenį.
# 5. Rezultato išvedimas:
# * Jei vartotojas paėmė paskutinį akmenį, programa turi pranešti, kad vartotojas laimėjo.
# * Jei kompiuteris paėmė paskutinį akmenį, programa turi pranešti, kad vartotojas pralaimėjo.
# * Po žaidimo pasiūlyti galimybę žaisti dar kartą.

import random

def zaidziam():
    while True:
        akmenys = random.randint(15, 30) # paima belekoki nr tarp 15 ir 30
        print(f"Su kiek akmenu pradedam: {akmenys}")
        # ZMOGUS RENKASI
        while akmenys > 0: # kol yra akmenu
            while True:
                zmogausIvedimas = input(f"\nKiek imi akmenu? (1-3): ")
                if zmogausIvedimas.isdigit() and 1 <= int(zmogausIvedimas) <= 3 and int(zmogausIvedimas) <= akmenys:
                    zmogausIvedimas = int(zmogausIvedimas)
                    akmenys -= zmogausIvedimas # is bendo kiekio atimam kiek ivede zmogus (kiek dar liko akmenu)
                    print(f"Tu paemei {zmogausIvedimas} akmenis. {akmenys} akmenu dar liko.")
                    break # uzbaigti kad nekartotu vel per nauja
                else: # jeigu netinka ka zmogus ivede
                    print("Netinka, ivesk skaiciu tarp 1 ir 3.")
            
            if akmenys == 0: # jeigu nebera akmenu
                print("Paemei paskutini - Laimejai")
                break # uzbaigti kad nekartotu vel per nauja

            # KOMPIUTERIS RENKASI
            kompoIvedimas = random.randint(1, min(3, akmenys))  # kompiuteris ima 1-3 akmenis, bet ne daugiau kaip liko
            akmenys -= kompoIvedimas # atimam is bendro akmenu skaiciaus kiek paeme kompas
            print(f"Kompiuteris paeme {kompoIvedimas} akmenis. {akmenys} akmenu dar liko.")
            
            if akmenys == 0: # jeigu nebera akmenu
                print("Kompiuteris paeme paskutini - Pralaimejai")
                break
        # AR DAR NORI ZAISTI
        arDarZaisti = input("\nAr dar nori zaisti? (taip/ne): ").lower()
        if arDarZaisti != "taip": # jeigu nebenori zaisti
            print("Aciu, kad zaidei. Bai bai")
            break

zaidziam() # reikia pakviesti funk kad pasileistu zaidimas
