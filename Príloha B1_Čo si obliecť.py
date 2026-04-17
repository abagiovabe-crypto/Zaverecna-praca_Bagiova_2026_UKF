from tkinter import *

okno = Tk()
okno.title("Čo si obliecť")

def rozhodni():
    pocasie = vstup.get()

    if pocasie == "slnečno":
        vystup.config(text="Zober si tričko.")
        okno.config(bg="lightyellow")

    elif pocasie == "dážď":
        vystup.config(text="Zober si dáždnik.")
        okno.config(bg="lightblue")

    elif pocasie == "sneh":
        vystup.config(text="Zober si bundu.")
        okno.config(bg="white")

    else:
        vystup.config(text="Neznáme počasie.")
        okno.config(bg="lightgray")

napis = Label(okno, text="Zadaj počasie:")
napis.pack()

vstup = Entry(okno)
vstup.pack()

tlacidlo = Button(okno, text="Zobraz odporúčanie", command=rozhodni)
tlacidlo.pack()

vystup = Label(okno, text="")
vystup.pack()

okno.mainloop()
