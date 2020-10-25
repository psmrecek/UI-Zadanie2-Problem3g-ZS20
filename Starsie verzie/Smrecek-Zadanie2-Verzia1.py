# -----------------------------------------------------------
# UI - Zadanie 2 - Problem 3 g)
# ZS 2020
#
# Peter Smreček
# email xsmrecek@stuba.sk
# AIS ID 103130
# -----------------------------------------------------------

from Smrecek_Zadanie2_Pohyby import *


def zaciatokFunkcie(funkcia, zac):
    '''
    Pomocna debuggovacia funkcia ktora vypise ktora funkcia bola prave spustena a ukoncena.

    :param funkcia: nazov funkcie
    :param zac: boolean ci zacina alebo konci
    :return:
    '''
    text = ""
    if zac == True:
        text = "# Zaciatok funkcie {} #".format(funkcia)
    else:
        text = "# Koniec funkcie {} #".format(funkcia)

    ram = "#" * (len(text))

    print(ram)
    print(text)
    print(ram)

def Repeat(x):
    '''
    https://www.geeksforgeeks.org/python-program-print-duplicates-list-integers/
    :param x:
    :return:
    '''
    _size = len(x)
    repeated = []
    for i in range(_size):
        k = i + 1
        for j in range(k, _size):
            if x[i] == x[j] and x[i] not in repeated:
                repeated.append(x[i])
    return repeated

def konvertor1dna2d(cislo, n):
    return cislo // n, cislo % n

def pocetMoznostiPohybu(x, y, n, navstivene):
    moznosti = [moznostVpravo1hore2, moznostVpravo1dolu2, moznostVpravo2hore1, moznostVpravo2dolu1,
                moznostVlavo1hore2, moznostVlavo1dolu2, moznostVlavo2hore1, moznostVlavo2dolu1]
    return sum([moznost(x, y, n, navstivene) for moznost in moznosti])

def najdiSuradniceMoznostiPohybu(x, y, n, navstivene):
    moznosti = [suradniceVpravo1hore2, suradniceVpravo1dolu2, suradniceVpravo2hore1, suradniceVpravo2dolu1,
                suradniceVlavo1hore2, suradniceVlavo1dolu2, suradniceVlavo2hore1, suradniceVlavo2dolu1]
    return [moznost(x, y, n, navstivene) for moznost in moznosti if moznost(x, y, n, navstivene) != None]


def vytvorSachovnicu(n, navstivene):
    sachovnica = []
    for x in range(n):
        for y in range(n):
            sachovnica.append(najdiSuradniceMoznostiPohybu(x, y, n, navstivene))
    return sachovnica

def vizualizuj(n, cesta):
    for x in range(n):
        for y in range(n):
            if (x, y) in cesta:
                print("{:03d} ".format(cesta.index((x, y)) + 1), end="")
            else:
                print("{} ".format("###"), end="")
            minule = (x, y)
        print()

def skontroluj(n, cesta, sachovnica, vypisy = True):
    minule = None
    korektna = True
    heuristicka = True
    vypis = ""

    navstivene = [[False for i in range(n)] for i in range(n)]

    for suradnice in cesta:
        if minule is not None and suradnice not in sachovnica[konvertor2dna1d(minule[0], minule[1], n)]:
            korektna = False
            vypis += "Z {},{} na {},{} bol nelegalny tah\n".format(minule[0], minule[1], suradnice[0], suradnice[1])
        if minule is not None:
            dalsie = heuristika(minule[0], minule[1], n, navstivene)
            if dalsie != [] and suradnice not in dalsie:
                heuristicka = False
                vypis += "Z {},{} na {},{} bol neheuristicky tah\n".format(minule[0], minule[1], suradnice[0], suradnice[1])
                vypis += "Vyber mal byt nad mnozinou {}\n".format(dalsie)
        minule = suradnice
        navstivene[suradnice[0]][suradnice[1]] = True

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
        vypis += "----------------- Sachovnica nie je kompletna\n"
        if vypisy:
            print(vypis, end="")
        return False, korektna, heuristicka


def heuristika(x, y, n, navstivene):
    suradnice = najdiSuradniceMoznostiPohybu(x, y, n, navstivene)
    minHodnota = 9
    minSuradnice = []
    for sur in suradnice:
        moznosti = pocetMoznostiPohybu(sur[0], sur[1], n, navstivene)
        if moznosti < minHodnota:
            minSuradnice = [sur]
            minHodnota = moznosti
        elif moznosti == minHodnota:
            minSuradnice.append(sur)
    # if minSuradnice != []:
    return minSuradnice

def DFS(n, pociatocneX, pociatocneY, sachovnica):
    zaciatokFunkcie(DFS.__name__, True)

    stack = [(pociatocneX, pociatocneY)]
    cesta = []
    pocitadloZastavenia = 0
    pocetKrokov = 1
    # print(stack.__len__())
    minuly = (pociatocneX, pociatocneY)

    navstivene = [[False for i in range (n)] for i in range(n)]
    # print(navstivene)

    # sucasny = minuly
    # navstivene[sucasny[0]][sucasny[1]] = True
    # cesta.append(sucasny)
    # print(sucasny)
    # sucasny = heuristika(sucasny[0], sucasny[1], n, navstivene)
    # while(sucasny != None):
    #     print(sucasny)
    #     navstivene[sucasny[0]][sucasny[1]] = True
    #     cesta.append(sucasny)
    #     sucasny = heuristika(sucasny[0], sucasny[1], n, navstivene)

    aktualny = (pociatocneX, pociatocneY)
    navstivene[aktualny[0]][aktualny[1]] = True
    cesta.append(aktualny)
    # print(aktualny)
    sucasny = heuristika(aktualny[0], aktualny[1], n, navstivene)
    aktualny = sucasny[0]
    while(sucasny != []):
        print("Vysledok heuristiky: z aktualneho {} na nasledujuci {}".format(aktualny, sucasny))
        aktualny = sucasny[0]
        # print(aktualny)
        navstivene[aktualny[0]][aktualny[1]] = True
        cesta.append(aktualny)
        sucasny = heuristika(aktualny[0], aktualny[1], n, navstivene)



    # while pocetKrokov < n ** 2:
    #     pocitadloZastavenia += 1
    #     if pocitadloZastavenia == 2000000:
    #         print("Cesta sa nenasla v stanovenom pocte krokov")
    #         break
    #
    #     sucasny = heuristika(minuly[0], minuly[1], n, navstivene)
    #     if sucasny == None:
    #         print("Koniec")
    #         break
    #
    #     print(minuly)
    #     print(sucasny)
    #
    #     if not navstivene[sucasny[0]][sucasny[1]]:
    #         cesta.append(sucasny)
    #         navstivene[sucasny[0]][sucasny[1]] = True
    #         pocetKrokov += 1
    #         minuly = sucasny
    #     minuly = sucasny




        # sucasny = stack.pop()
        # nasledujuci = heuristika(sucasny[0], sucasny[1], n, navstivene)
        # print(sucasny)
        # print(nasledujuci)
        # # konvertovane = konvertor2dna1d(sucasny[0], sucasny[1], n)
        #
        # # if minuly.__len__() != 0 and sucasny not in sachovnica[konvertor2dna1d(minuly[0], minuly[1], n)]:
        # #     print("Teraz")
        # #     continue
        #
        # if not navstivene[konvertor2dna1d(nasledujuci[0], nasledujuci[1], n)]:
        #     cesta.append(nasledujuci)
        #     minuly = cesta[-1]
        #     pocetKrokov += 1
        #     navstivene[konvertor2dna1d(nasledujuci[0], nasledujuci[1], n)] = True
        #
        # # minuly = sucasny
        #
        # # if sucasny not in cesta:
        # #     cesta.append(sucasny)
        # # print(sucasny)
        #
        #
        # for policko in sachovnica[konvertor2dna1d(nasledujuci[0], nasledujuci[1], n)]:
        #     if not navstivene[konvertor2dna1d(policko[0], policko[1], n)]:
        #         stack.append(policko)
        #
        # # print(Repeat(cesta))




    print(cesta.__len__())
    print(cesta)
    vizualizuj(n, cesta)
    skontroluj(n, cesta, sachovnica)

    zaciatokFunkcie(DFS.__name__, True)

def legalnyTah(zX, zY, naX, naY):
    rozdielX = abs(zX-naX)
    rozdielY = abs(zY-naY)
    if (rozdielX == 1 and rozdielY == 2) or (rozdielX == 2 and rozdielY == 1):
        return True
    return False


pocitadlo = 0
navrat = []

def DFSrekurzia(n, pociatocneX, pociatocneY, navstivene, cesta):
    global pocitadlo
    pocitadlo += 1
    navstivene[pociatocneX][pociatocneY] = True

    # print(pociatocneX, pociatocneY)
    cesta.append((pociatocneX, pociatocneY))
    susedne = heuristika(pociatocneX, pociatocneY, n, navstivene)                   # heuristika
    # susedne = sachovnica[konvertor2dna1d(pociatocneX, pociatocneY, n)]            # bez heuristiky



    # for policko in susedne:
    #     if not navstivene[policko[0]][policko[1]]:
    #         if not DFSrekurzia(n, policko[0], policko[1], navstivene, cesta, sachovnica):
    #             cesta.pop()

    if pocitadlo == 20000:
        return True
    if len(cesta) == n ** 2:
        # print("teraz")
        # print(cesta)
        global navrat
        navrat = cesta
        return True

    for policko in susedne:
        if not navstivene[policko[0]][policko[1]]:
            # DFSrekurzia(n, policko[0], policko[1], navstivene, cesta)
            if DFSrekurzia(n, policko[0], policko[1], navstivene, cesta):
                return True

    cesta.pop()
    navstivene[pociatocneX][pociatocneY] = False

    # if susedne != []:
    #     policko = susedne[0]
    #     DFSrekurzia(n, policko[0], policko[1], navstivene, cesta, sachovnica)


def riadic(n, pociatocneX, pociatocneY, sachovnica):
    navstivene = [[False for i in range(n)] for i in range(n)]
    cesta = []
    global pocitadlo
    pocitadlo = 0
    navrat = DFSrekurzia(n, pociatocneX, pociatocneY, navstivene, cesta)

    return navrat

def otestujVsetky(n, sachovnica):
    pocetZlych = 0
    pocetNeexistujucich = 0
    for x in range(n):
        for y in range(n):
            riadic(n, x, y, sachovnica)
            global navrat
            # print(len(navrat))
            # print(navrat)
            if navrat != []:
                print(navrat)
                kompKor = skontroluj(n, navrat, sachovnica, False)
                if sum(kompKor) != 3:
                    print("Zaciatok {},{} - Sachovnica nie je v poriadku - Vizualizujem".format(x, y))
                    print(navrat)
                    print(len(navrat))
                    skontroluj(n, navrat, sachovnica, True)
                    vizualizuj(n, navrat)
                    pocetZlych += 1
                navrat = []
            else:
                pocetNeexistujucich += 1
    print("\nPocet zlych je", pocetZlych)
    print("Pocet neexistujucich rieseni je ", pocetNeexistujucich)
    print("Pocet existujucich rieseni je ", n ** 2 - pocetNeexistujucich)


def main():
    zaciatokFunkcie(main.__name__, True)

    # n = int(input("Zadaj n "))
    n = 19
    pociatocneX = 0
    pociatocneY = 0

    # x, y = [int(vstup) for vstup in input("Zadaj X a Y: ").split()]

    # while(x != -1):
    #     print("Pocet moznosti je", pocetMoznostiPohybu(x, y, n))
    #     x, y = [int(vstup) for vstup in input("Zadaj X a Y: ").split()]

    # for x in range(n):
    #     for y in range(n):
    #         print("{} {} - {}".format(x, y, pocetMoznostiPohybu(x, y, n)))
    #         print("Mozno sa pohnut na", najdiSuradniceMoznostiPohybu(x, y, n))
    #         print()

    navstivene = [[False for i in range(n)] for i in range(n)]
    sachovnica = vytvorSachovnicu(n, navstivene)
    # for x in range(n):
    #     for y in range(n):
    #         # print("{}, {} : {}".format(x, y, sachovnica[konvertor2dna1d(x, y, n)]))

            # DFS(n, x, y, sachovnica)

    # DFS(n, 0, 0, sachovnica)

    # cesta = riadic(n, 2, 3, sachovnica)
    # print(cesta)
    # skontroluj(n, cesta, sachovnica, True)
    # vizualizuj(n, cesta)
    otestujVsetky(n, sachovnica)
    # cesta = []
    # DFSrekurzia(n, 0, 1, navstivene, cesta)


    # print(legalnyTah(0, 0, 2, 2))

    # zaciatokFunkcie(main.__name__, False)

if __name__ == "__main__":
    main()