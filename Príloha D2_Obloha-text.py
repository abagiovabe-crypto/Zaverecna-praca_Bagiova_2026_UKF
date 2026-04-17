def hviezdy(pocet):
    # hviezdy: znak na párnych pozíciách
    for i in range(pocet):
        for j in range(pocet):
            if j % 2 == 0:
                print("*", end="")
            else:
                print(" ", end="")
        print()


def vlocky(pocet):
    # vločky: znak na nepárnych pozíciách (opačný vzor)
    for i in range(pocet):
        for j in range(pocet):
            if j % 2 == 1:
                print("o", end="")
            else:
                print(" ", end="")
        print()


def kombinacia(pocet):
    # striedanie riadkov: hviezdy / vločky pre šikovnejších študentov
    for i in range(pocet):
        for j in range(pocet):
            if i % 2 == 0:
                # párny riadok → hviezdy
                if j % 2 == 0:
                    print("*", end="")
                else:
                    print(" ", end="")
            else:
                # nepárny riadok → vločky
                if j % 2 == 1:
                    print("o", end="")
                else:
                    print(" ", end="")
        print()


def main():
    print("Hviezdna obloha")
    print("1 - Hviezdy")
    print("2 - Vločky")
    print("3 - Kombinácia")

    volba = input("Vyber možnosť: ")
    pocet = int(input("Zadaj číslo: "))

    if volba == "1":
        hviezdy(pocet)

    elif volba == "2":
        vlocky(pocet)

    elif volba == "3":
        kombinacia(pocet)

    else:
        print("Neplatná voľba.")


main()
