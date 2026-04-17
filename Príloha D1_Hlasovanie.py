from tkinter import *

okno = Tk()
okno.title("Hlasovanie")

def vyhodnot():
    hlasy = vstup.get()

    pocet_a = 0
    pocet_b = 0
    pocet_c = 0

    # cyklus spracuje hlasy jeden po druhom
    for znak in hlasy:
        if znak == "A":
            pocet_a = pocet_a + 1
        elif znak == "B":
            pocet_b = pocet_b + 1
        elif znak == "C":
            pocet_c = pocet_c + 1

    # zobrazenie počtu hlasov
    vystup1.config(text="A: " + str(pocet_a))
    vystup2.config(text="B: " + str(pocet_b))
    vystup3.config(text="C: " + str(pocet_c))

    # určenie víťaza hlasovania
    if pocet_a > pocet_b and pocet_a > pocet_c:
        vysledok.config(text="Vyhrala možnosť A")
    elif pocet_b > pocet_a and pocet_b > pocet_c:
        vysledok.config(text="Vyhrala možnosť B")
    elif pocet_c > pocet_a and pocet_c > pocet_b:
        vysledok.config(text="Vyhrala možnosť C")
    else:
        vysledok.config(text="Výsledok je nerozhodný")

Label(okno, text="Zadaj hlasy (napr. ABACAB):").pack()

vstup = Entry(okno)
vstup.pack()

Button(okno, text="Vyhodnoť hlasovanie", command=vyhodnot).pack()

vystup1 = Label(okno, text="")
vystup1.pack()

vystup2 = Label(okno, text="")
vystup2.pack()

vystup3 = Label(okno, text="")
vystup3.pack()

vysledok = Label(okno, text="")
vysledok.pack()

okno.mainloop()
