from tkinter import *

# -------------------------
# OKNO 1 - bez použitia cyklu
# -------------------------
okno1= Tk()
okno1.title("Okno 1 - bez cyklu")

canvas1 = Canvas(okno1, width=300, height=100, bg="white")
canvas1.pack()

def kresli_bez_cyklu():
    canvas1.delete("all")

    # body sa kreslia manuálne - každý zvlášť
    canvas1.create_oval(10, 40, 20, 50, fill="black")
    canvas1.create_oval(30, 40, 40, 50, fill="black")
    canvas1.create_oval(50, 40, 60, 50, fill="black")
    canvas1.create_oval(70, 40, 80, 50, fill="black")
    canvas1.create_oval(90, 40, 100, 50, fill="black")

tlacidlo1 = Button(okno1, text="Kresli", command=kresli_bez_cyklu)
tlacidlo1.pack()

# -------------------------
# OKNO 2 - s použitím cyklu
# -------------------------
okno2=Tk()
okno2.title("Okno 2 - s cyklom")

canvas2 = Canvas(okno2, width=300, height=100, bg="white")
canvas2.pack()

def kresli_s_cyklom():
    canvas2.delete("all")

    # cyklus opakuje tú istú činnosť viackrát
    for i in range(5):
        x = 10 + i * 20
        canvas2.create_oval(x, 40, x + 10, 50, fill="black")

tlacidlo2 = Button(okno2, text="Kresli", command=kresli_s_cyklom)
tlacidlo2.pack()

okno1.mainloop()
okno2.mainloop()


