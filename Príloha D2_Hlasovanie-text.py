def vyhodnot(hlasy):
    # Premenné slúžia na počítanie hlasov pre jednotlivé možnosti.
    pocet_a = 0
    pocet_b = 0
    pocet_c = 0

    # Cyklus spracúva vstup po jednotlivých znakoch.
    # Každý znak predstavuje jeden hlas.
    for znak in hlasy:
        # Podmienky určujú, ku ktorej možnosti sa daný hlas pripočíta.
        if znak == "A":
            pocet_a = pocet_a + 1
        elif znak == "B":
            pocet_b = pocet_b + 1
        elif znak == "C":
            pocet_c = pocet_c + 1

    # Výpis počtu hlasov
    print("A:", pocet_a)
    print("B:", pocet_b)
    print("C:", pocet_c)

    # Podmienky porovnávajú počty hlasov a určujú výsledok hlasovania.
    if pocet_a > pocet_b and pocet_a > pocet_c:
        print("Vyhrala možnosť A")
    elif pocet_b > pocet_a and pocet_b > pocet_c:
        print("Vyhrala možnosť B")
    elif pocet_c > pocet_a and pocet_c > pocet_b:
        print("Vyhrala možnosť C")
    else:
        print("Výsledok je nerozhodný")


def main():
    hlasy = input("Zadaj hlasy (napr. ABACAB): ")

    # Zavolanie funkcie, ktorá spracuje vstup a vyhodnotí hlasovanie.
    vyhodnot(hlasy)


main()
