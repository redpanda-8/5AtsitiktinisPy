# Sukurkite žaidimą "žirklės, popierius, akmuo", kuriame vartotojas gali įvesti savo pasirinkimą, o kompiuteris
# atsitiktinai sugeneruoja savo pasirinkimą. Žaidimo rezultatas turi būti parodytas ekrane, nurodant, kas 
# laimėjo - vartotojas ar kompiuteris, arba ar žaidimas baigėsi lygiosiomis.

# Detalės:
# 1. Vartotojas įveda vieną iš trijų galimų pasirinkimų: "žirklės", "popierius", "akmuo".
# 2. Kompiuteris atsitiktinai sugeneruoja vieną iš šių pasirinkimų: "žirklės", "popierius" arba "akmuo".
# 3. Programa turi palyginti vartotojo ir kompiuterio pasirinkimus ir išvesti rezultatą:
# * Žirklės laimi prieš popierių, bet pralaimi prieš akmenį.
# * Popierius laimi prieš akmenį, bet pralaimi prieš žirkles.
# * Akmuo laimi prieš žirkles, bet pralaimi prieš popierių.
# 4. Jei abu pasirinkimai yra vienodi, žaidimas baigiasi lygiosiomis.

# Papildomi reikalavimai:
# * Jei vartotojas įveda neteisingą pasirinkimą (ne "žirklės", "popierius" ar "akmuo") - programa turi paprašyti 
# įvęsti iš naujo.
# * Galimybė žaisti dar kartą: vartotojo paklausti, ar norėtų pakartoti žaidimą po kiekvienos partijos.

import random

def paimtiKompiuterioEjima():
    return random.choice(["žirklės", "popierius", "akmuo"]) # grazink belekuri is situ 3

def kasLaimetojas(zmogausEjimas, kompiuterioEjimas):
    if zmogausEjimas == kompiuterioEjimas:
        return "lygios"
    elif (zmogausEjimas == "žirklės" and kompiuterioEjimas == "popierius") or \
         (zmogausEjimas == "popierius" and kompiuterioEjimas == "akmuo") or \
         (zmogausEjimas == "akmuo" and kompiuterioEjimas == "žirklės"):
        return "zmogus"
    else:
        return "Kompiuteris"

def zaidziam():
    while True:
        zmogausEjimas = input("Rinkis (žirklės, popierius, akmuo): ").lower() # ka iraso zmogus (.lower A>a pakeicia)
        if zmogausEjimas not in ["žirklės", "popierius", "akmuo"]:            # patikra ar ivede ka reikia
            print("Ne ta ivedei. Ivesk 'žirklės', 'popierius', arba 'akmuo'.")
            continue  # pakartotinai patikrinam ar dbr zmogus jau gerai ivede

        kompiuterioEjimas = paimtiKompiuterioEjima() # kompiuterio ejimas
        print(f"Kompiuteris: {kompiuterioEjimas}")

        result = kasLaimetojas(zmogausEjimas, kompiuterioEjimas) # kas laimejo

        if result == "lygios": # parodom zmogui rezultatus
            print("Lygios")
        elif result == "zmogus":
            print("Tu laimi")
        else:
            print("Kompiuteris laimi")

        arDarZaisti = input("Ar nori zaisti dar? (taip/ne): ").lower() # ar zmogus dar nori zaisti?
        if arDarZaisti != "taip": # jeigu nera = taip = nezaidziam
            print("Aciu kad zaidei! Bai bai!")
            break # reikia uzdaryti cikla, kad neklausinetu

zaidziam() # pakvieciam funkcija, kad suveiktu zaidimas
