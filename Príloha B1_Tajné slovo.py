from tkinter import *

okno = Tk()
okno.title("Tajné slovo")

def skontroluj():
    slovo = vstup.get()

    # Program sa rozhoduje podľa toho, čo používateľ zadal.
    # Ide o jednoduchý príklad udalostného programovania:
    # po kliknutí na tlačidlo sa vykoná funkcia a tá vyhodnotí podmienku.
    if slovo == "slnko":
        vystup.config(text="Správne tajné slovo")
    else:
        vystup.config(text="Skús znova")

napis = Label(okno, text="Zadaj tajné slovo:")
napis.pack()

vstup = Entry(okno)
vstup.pack()

tlacidlo = Button(okno, text="Skontroluj", command=skontroluj)
tlacidlo.pack()

vystup = Label(okno, text="")
vystup.pack()

okno.mainloop()
