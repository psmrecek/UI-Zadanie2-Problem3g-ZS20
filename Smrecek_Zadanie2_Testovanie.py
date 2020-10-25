# -----------------------------------------------------------
# UI - Zadanie 2 - Problem 3 g)
# ZS 2020
#
# Peter Smreček
# email xsmrecek@stuba.sk
# AIS ID 103130
# -----------------------------------------------------------

from Smrecek_Zadanie2_Kod import *
import random

def vytvorSachovnicu(n, navstivene):
    '''
    Pomocna funkcia ktora vygeneruje graf so zoznamom susednosti pouzivany na kontrolu spravnosti riesenia

    :param n: rozmer sachovnice
    :param navstivene: pole booleanov obsahujuce informacie o navstivenych polickach
    :return: graf so zoznamom susednosti
    '''

    sachovnica = []
    for x in range(n):
        for y in range(n):
            sachovnica.append(najdiSuradniceMoznostiPohybu(x, y, n, navstivene))
    return sachovnica

def vizualizuj(n, cesta):
    '''
    Funkcia na vykreslenie riesenia

    :param n: rozmer sachovnice
    :param cesta: pole suradnic reprezentujuce postupny pohyb kona po sachovnici
    '''

    for x in range(n):
        if x == 0:
            print("### | ", end="")
            for c in range(n):
                print("{:03d}".format(c), end=" ")
            print("\n" + "-"*(5+4*n))
        for y in range(n):
            if y == 0:
                print("{:03d}".format(x), end="")
                print(" | ", end="")
            if (x, y) in cesta:
                print("{:03d} ".format(cesta.index((x, y)) + 1), end="")
            else:
                print("{} ".format("###"), end="")
        print()

def skontroluj(n, cesta, vypisy = True):
    '''
    Testovacia funkcia skontroluje, ci je sachovnica vyplnena iba legalnymi heuristickymi tahmi kona a vypise
    informaciu, ci je sachovnica kompletna

    :param n: rozmer sachovnice
    :param cesta: pole suradnic reprezentujuce postupny pohyb kona po sachovnici
    :param vypisy: True pre postupne vypisy, False pre tichy rezim
    :return: 3 booleany reprezentujuce ci je sachovnica kompletne vyplnena, legalne vyplnena, heuristicky vyplnena
    '''

    sachovnica = vytvorSachovnicu(n, [[False for i in range(n)] for i in range(n)])
    minule = None
    korektna = True
    heuristicka = True
    vypis = ""

    navstivene = [[False for i in range(n)] for i in range(n)]

    for suradnice in cesta:
        if minule is not None and suradnice not in sachovnica[konvertor2dna1d(minule[0], minule[1], n)]:
            korektna = False
            vypis += "Z {:02d},{:02d} na {:02d},{:02d} bol nelegalny tah\n".format(minule[0], minule[1], suradnice[0], suradnice[1])
        if minule is not None:
            dalsie = heuristika(minule[0], minule[1], n, navstivene)
            if dalsie != [] and suradnice not in dalsie:
                heuristicka = False
                vypis += "Z {:02d},{:02d} na {:02d},{:02d} bol neheuristicky tah\n".format(minule[0], minule[1], suradnice[0], suradnice[1])
                vypis += "Vyber mal byt nad mnozinou {}\n".format(dalsie)
        minule = suradnice
        navstivene[suradnice[0]][suradnice[1]] = True

    if len(cesta) > 0:
        if heuristicka:
            vypis += "Sachovnica je heuristicky vyplnena\n"
        else:
            vypis += "----------------- Sachovnica nie je heuristicky vyplnena\n"

        if korektna:
            vypis += "Sachovnica je vyplnena legalnymi tahmi\n"
        else:
            vypis += "----------------- Sachovnica nie je vyplnena legalnymi tahmi\n"

    if len(cesta) == n ** 2:
        vypis += "Sachovnica je kompletna\n"
        if vypisy:
            print(vypis, end="")
        return True, korektna, heuristicka
    else:
        vypis += "Sachovnica nie je kompletna, pretoze riesenie bud nebolo najdene v stanovenom pocte krokov, alebo neexistuje\n"
        if vypisy:
            print(vypis, end="")
        return False, korektna, heuristicka

def existuje(n, pociatocneX, pociatocneY):
    '''
    Funkcia vypisu oznamujuca, ci ocakavame, ze heuristika z tychto suradnic na sachovnici najde cestu.

    :param n: rozmer sachovnice
    :param pociatocneX: sucasna suradnica x
    :param pociatocneY: sucasna suradnica y
    '''
    if n == 1:
        return ("Pre sachovnicu o rozmere 1 je riesnie trivialne")
    elif n < 5:
        return ("Pre sachovnice mensie ako 5 riesenie neexistuje, s vynimkou 1")
    elif n % 2 == 0:
        return ("Pre parne sachovnice riesenie existuje")
    elif (pociatocneX + pociatocneY) % 2 == 0:
        return ("Predpokladame, ze riesenie dosiahnutelne heuristikou existuje")
    else:
        return ("Predpokladame, ze riesenie dosiahnutelne heuristikou neexistuje")

def najdiAvypis(n, pociatocneX, pociatocneY, maxKrokov):
    '''
    Funkcia vypisu, ktora nad najdenou cestou zavola funkcie na jje kontrolu a vizualizaciu.

    :param n: rozmer sachovnice
    :param pociatocneX: sucasna suradnica x
    :param pociatocneY: sucasna suradnica y
    :param maxKrokov: maximalny pocet krokov hladania ktory sa nesmie prekrocit
    '''

    print("Sachovnica {}x{} s pociatocnymi bodmi {}, {}:".format(n, n, pociatocneX, pociatocneY))
    print(existuje(n, pociatocneX, pociatocneY))
    cesta = riadicHladania(n, pociatocneX, pociatocneY, maxKrokov)
    vizualizuj(n, cesta)
    skontroluj(n, cesta)
    print("-" * 150)

def generujVstupy(n, pocet):
    '''
    Funkcia generujuca pozadovany pocet unikatnych suradnic na mape pre potreby kontroly. Ak je pozadovany
    pocet suradnic vacsi ako celkovy pocet suradnic mapy, funkcia vrati vsetky suradnice mapy. Inak vrati nahodne
    zoradene pole suradnic.

    :param n: rozmer sachovnice
    :param pocet: pozadovany pocet unikatnych suradnic
    :return: set unikatnych suradnic ak je pozadovany pocet mensi ako vsetky suradnice sachovnice, vsetky suradnice sachovnice inak
    '''

    if pocet >= n ** 2:
        return [(x, y) for x in range(n) for y in range(n)]

    random.seed()
    n -= 1

    unikatnyZoznam = {(random.randint(0, n), random.randint(0, n))}
    while len(unikatnyZoznam) != pocet:
        unikatnyZoznam.add((random.randint(0, n), random.randint(0, n)))
    return unikatnyZoznam

def otestujVsetky(n, maxKrokov):
    '''
    Testovacia funkcia ktora otestuje ci existuje heuristicka cesta pre kona zo vsetkych suradnic mapy.

    :param n: rozmer sachovnice
    :param maxKrokov: maximalny pocet krokov hladania ktory sa nesmie prekrocit
    '''

    navstivene = [[False for i in range(n)] for i in range(n)]

    pocetZlych = 0
    pocetNeexistujucich = 0
    for x in range(n):
        for y in range(n):
            navrat = riadicHladania(n, x, y, maxKrokov)
            if navrat != []:
                kompKor = skontroluj(n, navrat, False)
                if sum(kompKor) != 3:
                    print("Zaciatok {:02d},{:02d} - Sachovnica nie je v poriadku - Vizualizujem".format(x, y))
                    print(navrat)
                    print(len(navrat))
                    skontroluj(n, navrat, True)
                    vizualizuj(n, navrat)
                    pocetZlych += 1
                else:
                    print("Zaciatok {:02d},{:02d} - Sachovnica bola najdena a spravne vygenerovana".format(x, y))
            else:
                pocetNeexistujucich += 1
                print("Pre n = {} riesenie zacinajuce na {:02d}, {:02d} neexistuje alebo nebolo najdene v zadanom pocte krokov ".format(n, x, y))

    print("\nPocet zlych je", pocetZlych)
    print("Pocet neexistujucich rieseni je ", pocetNeexistujucich)
    print("Pocet existujucich rieseni je ", n ** 2 - pocetNeexistujucich)
    print("-" * 150)

def main():
    '''
    Pouzivatelske rozhranie. Menu programu.

    '''

    print("Zvolte 0 pre ukoncenie programu\nZvolte 1 pre testovanie nahodnych vstupov\nZvolte 2 pre testovanie konkretneho vstupu\nZvolte 3 pre testovanie vsetkych vstupov pre interval rozmerov\nZvolte 4 pre vzorovy test")
    program = input()

    while program != "0":
        if program == "1":
            print("Pre otestovanie a vizualizaciu A nahodnych vstupov sachovnice N x N s maximalnym poctom krokov B v tisicoch zadajte 3 cisla v poradi \"N A B\":")
            vstup = input().split(" ")
            n = int(vstup[0])
            a = int(vstup[1])
            b = int(vstup[2]) * 1000
            nahodneSuradnice = generujVstupy(n, a)
            print("Boli vygenerovane nahodne suradnice", nahodneSuradnice)
            print("-" * 150)
            for index, item in enumerate(nahodneSuradnice):
                print("Vypis", index + 1)
                najdiAvypis(n, item[0], item[1], b)
        elif program == "2":
            print("Pre otestovanie a vizualizaciu jedneho konkretneho rozmeru zadajte zadajte vstup vo formate \"N pociatocneX pociatocneY maximalnyPocetKrokovVtisicoch\":")
            vstup = input().split(" ")
            n = int(vstup[0])
            pociatocneX = int(vstup[1])
            pociatocneY = int(vstup[2])
            maxKrokov = int(vstup[3]) * 1000
            najdiAvypis(n, pociatocneX, pociatocneY, maxKrokov)
        elif program == "3":
            print("Pre otestovanie existencie cesty pre vsetky suradnice daneho rozmeru zadajte \"pociatocneN koncoveN maximalnyPocetKrokovVtisicoch\":")
            vstup = input().split(" ")
            pociatocneN = int(vstup[0])
            koncoveN = int(vstup[1])
            maxKrokov = int(vstup[2]) * 1000
            for i in range(pociatocneN, koncoveN + 1):
                print("Testujem rozmer {} x {}".format(i, i))
                otestujVsetky(i, maxKrokov)
        elif program == "4":
            print("Spustil sa vzorovy test pre 10 vstupov pre mapu velkosti 8 x 8")
            n = 8
            b = 20000
            suradnice = [(5, 7), (1, 6), (0, 2), (4, 5), (5, 6), (7, 2), (7, 3), (6, 5), (2, 7), (0, 7)]
            print("Boli zvolene suradnice", suradnice)
            print("-" * 150)
            for index, item in enumerate(suradnice):
                print("Vypis", index + 1)
                najdiAvypis(n, item[0], item[1], b)
        else:
            print("Nespravna volba")

        print(
            "Zvolte 0 pre ukoncenie programu\nZvolte 1 pre testovanie nahodnych vstupov\nZvolte 2 pre testovanie konkretneho vstupu\nZvolte 3 pre testovanie vsetkych vstupov pre interval rozmerov\nZvolte 4 pre vzorovy test")
        program = input()

    print("Koniec programu")

if __name__ == "__main__":
    main()