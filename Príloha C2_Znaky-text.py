from tkinter import *

okno = Tk()
okno.title("Body - for")

canvas = Canvas(okno, width=300, height=100, bg="white")
canvas.pack()

def kresli():
    canvas.delete("all")
    
    pocet = int(vstup.get())

    # cyklus riadi počet opakovaní
    for i in range(pocet):
        x = 10 + i * 20
        canvas.create_oval(x, 40, x+10, 50, fill="blue")

    # textový výstup
    vystup.config(text="Nakreslil som " + str(pocet) + " bodov.")

napis = Label(okno, text="Zadaj počet bodov:")
napis.pack()

vstup = Entry(okno)
vstup.pack()

tlacidlo = Button(okno, text="Kresli", command=kresli)
tlacidlo.pack()

vystup = Label(okno, text="")
vystup.pack()

okno.mainloop()
