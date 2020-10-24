'''
Funkcie kontrolujuce ci existuje moznost pohybu danym smerom. Vracaju True alebo False podla smeru pohybu.
'''

def moznostVpravo1hore2(x, y, n, navstivene):
    return x + 1 < n and y + 2 < n and not navstivene[x+1][y+2]

def moznostVpravo1dolu2(x, y, n, navstivene):
    return x + 1 < n and y - 2 >= 0 and not navstivene[x+1][y-2]

def moznostVpravo2hore1(x, y, n, navstivene):
    return x + 2 < n and y + 1 < n and not navstivene[x+2][y+1]

def moznostVpravo2dolu1(x, y, n, navstivene):
    return x + 2 < n and y - 1 >= 0 and not navstivene[x+2][y-1]

def moznostVlavo1hore2(x, y, n, navstivene):
    return x - 1 >= 0 and y + 2 < n and not navstivene[x-1][y+2]

def moznostVlavo1dolu2(x, y, n, navstivene):
    return x - 1 >= 0 and y - 2 >= 0 and not navstivene[x-1][y-2]

def moznostVlavo2hore1(x, y, n, navstivene):
    return x - 2 >= 0 and y + 1 < n and not navstivene[x-2][y+1]

def moznostVlavo2dolu1(x, y, n, navstivene):
    return x - 2 >= 0 and y - 1 >= 0 and not navstivene[x-2][y-1]

'''
Funkcie vracajuce suradnice pohybu danym smerom, ak je tento pohyb mozny.
'''

def suradniceVpravo1hore2(x, y, n, navstivene):
    if moznostVpravo1hore2(x, y, n, navstivene):
        return x + 1, y + 2

def suradniceVpravo1dolu2(x, y, n, navstivene):
    if moznostVpravo1dolu2(x, y, n, navstivene):
        return x + 1, y - 2

def suradniceVpravo2hore1(x, y, n, navstivene):
    if moznostVpravo2hore1(x, y, n, navstivene):
        return x + 2, y + 1

def suradniceVpravo2dolu1(x, y, n, navstivene):
    if moznostVpravo2dolu1(x, y, n, navstivene):
        return x + 2, y - 1

def suradniceVlavo1hore2(x, y, n, navstivene):
    if moznostVlavo1hore2(x, y, n, navstivene):
        return x - 1, y + 2

def suradniceVlavo1dolu2(x, y, n, navstivene):
    if moznostVlavo1dolu2(x, y, n, navstivene):
        return x - 1, y - 2

def suradniceVlavo2hore1(x, y, n, navstivene):
    if moznostVlavo2hore1(x, y, n, navstivene):
        return x - 2, y + 1

def suradniceVlavo2dolu1(x, y, n, navstivene):
    if moznostVlavo2dolu1(x, y, n, navstivene):
        return x - 2, y - 1

def konvertor2dna1d(x, y, n):
    '''
    Funkcia konvertujuca suradnice 2D pola na suradnice 1D pola.

    :param x: suradnica x
    :param y: suradnica y
    :param n: rozmer sachovnice
    :return: index v 1D poli
    '''
    return x * n + y
