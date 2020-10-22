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
