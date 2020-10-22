# -----------------------------------------------------------
# UI - Zadanie 2 - Problem 3 g)
# ZS 2020
#
# Peter Smreček
# email xsmrecek@stuba.sk
# AIS ID 103130
# -----------------------------------------------------------

from pohyby import *

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

def konvertor2dna1d(x, y, n):
    return x * n + y

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

pocitadlo = 0
navrat = []

def DFSrekurzia(n, pociatocneX, pociatocneY, navstivene, cesta, maxKrokov):
    global pocitadlo
    pocitadlo += 1
    if pocitadlo == maxKrokov:
        return True

    navstivene[pociatocneX][pociatocneY] = True
    cesta.append((pociatocneX, pociatocneY))
    susedne = heuristika(pociatocneX, pociatocneY, n, navstivene)

    if len(cesta) == n ** 2:
        global navrat
        navrat = cesta
        return True

    for policko in susedne:
        if not navstivene[policko[0]][policko[1]]:
            if DFSrekurzia(n, policko[0], policko[1], navstivene, cesta, maxKrokov):
                return True

    cesta.pop()
    navstivene[pociatocneX][pociatocneY] = False

def riadic(n, pociatocneX, pociatocneY, maxKrokov):
    navstivene = [[False for i in range(n)] for i in range(n)]
    cesta = []
    global pocitadlo
    pocitadlo = 0
    global navrat
    navrat = []
    DFSrekurzia(n, pociatocneX, pociatocneY, navstivene, cesta, maxKrokov)

    return navrat

def otestujVsetky(n, maxKrokov):
    navstivene = [[False for i in range(n)] for i in range(n)]
    sachovnica = vytvorSachovnicu(n, navstivene)

    pocetZlych = 0
    pocetNeexistujucich = 0
    for x in range(n):
        for y in range(n):
            navrat = riadic(n, x, y, maxKrokov)
            # vizualizuj(n, navrat)
            # print(len(navrat))
            # print(navrat)
            if navrat != []:
                # print(navrat)
                # vizualizuj(n, navrat)
                kompKor = skontroluj(n, navrat, sachovnica, False)
                if sum(kompKor) != 3:
                    print("Zaciatok {},{} - Sachovnica nie je v poriadku - Vizualizujem".format(x, y))
                    print(navrat)
                    print(len(navrat))
                    skontroluj(n, navrat, sachovnica, True)
                    vizualizuj(n, navrat)
                    pocetZlych += 1
            else:
                pocetNeexistujucich += 1
                print("Pre n = {} neexistuje riesenie zacinajuce na {}, {}".format(n, x, y))

    print("\nPocet zlych je", pocetZlych)
    print("Pocet neexistujucich rieseni je ", pocetNeexistujucich)
    print("Pocet existujucich rieseni je ", n ** 2 - pocetNeexistujucich)

def main():
    # zaciatokFunkcie(main.__name__, True)

    # n = int(input("Zadaj n "))
    # n = 18

    # otestujVsetky(n, 20000)

    for i in range(0, 20):
        print("Testujem rozmer {} x {}".format(i,i))
        otestujVsetky(i, 20000)
        print("-"*100)

    # zaciatokFunkcie(main.__name__, False)

if __name__ == "__main__":
    main()