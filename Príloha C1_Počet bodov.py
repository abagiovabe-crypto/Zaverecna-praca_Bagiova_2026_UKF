from tkinter import *

# vytvorenie hlavného okna aplikácie
okno = Tk()
okno.title("Počet bodov")

# plocha na kreslenie (Canvas)
canvas = Canvas(okno, width=300, height=100)
canvas.pack()

# funkcia sa spustí po kliknutí na tlačidlo
def kresli():
    # vymaže predchádzajúci výstup (staré body)
    canvas.delete("all")
    
    # získanie hodnoty zo vstupného poľa
    pocet = int(vstup.get())

    # cyklus riadi počet opakovaní – koľko bodov sa vykreslí
    for i in range(pocet):
        # výpočet pozície každého bodu
        x = 10 + i * 20
        
        # vykreslenie jedného bodu (oválu)
        canvas.create_oval(x, 40, x+10, 50, fill="blue")

# textový pokyn pre používateľa
napis = Label(okno, text="Zadaj počet bodov:")
napis.pack()

# vstupné pole na zadanie čísla
vstup = Entry(okno)
vstup.pack()

# tlačidlo spúšťa funkciu kresli
tlacidlo = Button(okno, text="Kresli", command=kresli)
tlacidlo.pack()

# spustenie aplikácie
okno.mainloop()
