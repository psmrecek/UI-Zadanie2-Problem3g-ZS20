# -----------------------------------------------------------
# UI - Zadanie 2 - Problem 3 g)
# ZS 2020
#
# Peter Smreček
# email xsmrecek@stuba.sk
# AIS ID 103130
# -----------------------------------------------------------

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

def main():
    zaciatokFunkcie(main.__name__, True)

    print("Main")

    zaciatokFunkcie(main.__name__, False)

if __name__ == "__main__":
    main()