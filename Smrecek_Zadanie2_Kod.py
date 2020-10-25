# -----------------------------------------------------------
# UI - Zadanie 2 - Problem 3 g)
# ZS 2020
#
# Peter Smreček
# email xsmrecek@stuba.sk
# AIS ID 103130
# -----------------------------------------------------------

from Smrecek_Zadanie2_Pohyby import *

def pocetMoznostiPohybu(x, y, n, navstivene):
    '''
    Pomocna funkcia pre zratanie poctu moznosti pohybu z daneho policka

    :param x: suradnica x
    :param y: suradnica y
    :param n: rozmer sachovnice
    :param navstivene: pole booleanov obsahujuce informacie o navstivenych polickach
    :return: pocet moznosti pohybu z aktualneho policka na este nenavstivene policka
    '''

    moznosti = [moznostVpravo1hore2, moznostVpravo1dolu2, moznostVpravo2hore1, moznostVpravo2dolu1,
                moznostVlavo1hore2, moznostVlavo1dolu2, moznostVlavo2hore1, moznostVlavo2dolu1]
    return sum([moznost(x, y, n, navstivene) for moznost in moznosti])

def najdiSuradniceMoznostiPohybu(x, y, n, navstivene):
    '''
    Pomocna funkcia hladajuca suradnice moznosti pohybu z daneho policka

    :param x: suradnica x
    :param y: suradnica y
    :param n: rozmer sachovnice
    :param navstivene: pole booleanov obsahujuce informacie o navstivenych polickach
    :return: pole suradnic dostupnych z aktualneho policka
    '''

    moznosti = [suradniceVpravo1hore2, suradniceVpravo1dolu2, suradniceVpravo2hore1, suradniceVpravo2dolu1,
                suradniceVlavo1hore2, suradniceVlavo1dolu2, suradniceVlavo2hore1, suradniceVlavo2dolu1]
    return [moznost(x, y, n, navstivene) for moznost in moznosti if moznost(x, y, n, navstivene) != None]

def heuristika(x, y, n, navstivene):
    '''
    Funkcia vyberajuca nasledujuce suradnice skoku kona. Skonstruovana podla heuristiky "Warnsdorff's rule".

    :param x: suradnica x
    :param y: suradnica y
    :param n: rozmer sachovnice
    :param navstivene: pole booleanov obsahujuce informacie o navstivenych polickach
    :return: pole suradnic s minimalnym poctom nasledujucich tahov
    '''

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

    return minSuradnice

pocitadlo = 0
# Globalna premenna ratajuca pocet spusteni funkcie rekurzivneho hladania

navrat = []
# Navratove pole ziskane z funkcie rekurzivneho hladania

def DFSrekurzia(n, pociatocneX, pociatocneY, navstivene, cesta, maxKrokov):
    '''
    Rekurzivna funkcia hladania do hlbky. Hladanie prebieha dovtedy, dokym nie je najdena cesta, nie su prehladane
    vsetky moznosti, alebo nie je prekroceny maximalny pocet krokov hladania.

    :param n: rozmer sachovnice
    :param pociatocneX: sucasna suradnica x
    :param pociatocneY: sucasna suradnica y
    :param navstivene: pole booleanov obsahujuce informacie o navstivenych polickach
    :param cesta: aktualne najdena cesta
    :param maxKrokov: maximalny pocet krokov hladania ktory sa nesmie prekrocit
    :return: True ak je cesta najdena alebo je prekroceny pocet krokov, False inak
    '''

    global pocitadlo
    pocitadlo += 1
    if pocitadlo == maxKrokov:
        # Ak je prektoceny maximalny pocet krokov, funkcia sa rekurzivne vracia
        return True

    navstivene[pociatocneX][pociatocneY] = True
    # Sucasne policko kde sa nachadza kon je oznacene za navstivene

    cesta.append((pociatocneX, pociatocneY))
    # Sucasne policko sa pridava do pola reprezentujuceho sucasnu cestu kona

    susedne = heuristika(pociatocneX, pociatocneY, n, navstivene)
    # Vytvorenie pola moznosti skoku podla heuristiky

    if len(cesta) == n ** 2:
        # Ak bola cesta najdena cela, funkcia sa rekurzivne vracia
        # Globalna premenna s najdenou cestou je nastavena na sucasnu cestu
        global navrat
        navrat = cesta
        return True

    for policko in susedne:
        # Cyklus prehladavania heuristicky susednych policok (policok, ktore maju rovnaky pocet nasledujucich tahov)
        if not navstivene[policko[0]][policko[1]]:
            # Kontrola, ci policko este nebolo navstivene, pretoze hoci pole susednosti zahrnalo len nenavstivene
            # policka v case jeho vytvarania, stav ich navstivenia sa mohol v rekurzii zmenit
            if DFSrekurzia(n, policko[0], policko[1], navstivene, cesta, maxKrokov):
                # Rekurzivne volanie funkcie prehladavania do hlbky. Ak sa vratila hodnota True, funkcia sa rekurzivne vracia
                return True

    cesta.pop()
    navstivene[pociatocneX][pociatocneY] = False
    # Sucasne policko bolo prehladane a nevyhovuje. Odobera sa z cesty a nastavuje sa ako neprehladane. Funkcia vracia False
    return False

def riadicHladania(n, pociatocneX, pociatocneY, maxKrokov):
    '''
    Riadiaca funkcia hladania cesty kona. Nastavuje globalne premenne na pociatocne hodnoty pred kazdym hladanim
    a vracia najdenu cestu.

    :param n: rozmer sachovnice
    :param pociatocneX: sucasna suradnica x
    :param pociatocneY: sucasna suradnica y
    :param maxKrokov: maximalny pocet krokov hladania ktory sa nesmie prekrocit
    :return: najdena cesta kona po mape reprezentovana polom suradnic
    '''

    navstivene = [[False for i in range(n)] for i in range(n)]
    cesta = []
    global pocitadlo
    pocitadlo = 0
    global navrat
    navrat = []
    DFSrekurzia(n, pociatocneX, pociatocneY, navstivene, cesta, maxKrokov)

    return navrat

