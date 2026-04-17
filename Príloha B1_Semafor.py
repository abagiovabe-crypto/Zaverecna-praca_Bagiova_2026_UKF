from tkinter import *

# vytvorenie hlavného okna aplikácie
okno = Tk()
okno.title("Semafor slov")

# funkcia sa spustí po kliknutí na tlačidlo
# program v nej spracuje vstup a rozhodne sa, čo zobrazí
def rozhodni():
    farba = vstup.get()

    # podmienka riadi správanie programu podľa zadaného vstupu
    if farba == "červená":
        vystup.config(text="Stoj", fg="red")
    elif farba == "oranžová":
        vystup.config(text="Priprav sa", bg="orange")
    elif farba == "zelená":
        vystup.config(text="Choď")
    else:
        vystup.config(text="Neznáma farba")

# textový prvok s pokynom pre používateľa
napis = Label(okno, text="Zadaj farbu semaforu:")
napis.pack()

# vstupné pole, do ktorého používateľ zadáva text
vstup = Entry(okno)
vstup.pack()

# tlačidlo spustí funkciu rozhodni
tlacidlo = Button(okno, text="Zobraz reakciu", command=rozhodni)
tlacidlo.pack()

# výstupný textový prvok
vystup = Label(okno, text="Sem sa zobrazí reakcia programu.")
vystup.pack()

# spustenie aplikácie
okno.mainloop()
