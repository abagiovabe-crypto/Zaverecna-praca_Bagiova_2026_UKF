from tkinter import *

okno = Tk()
okno.title("Interaktívne plátno")

canvas = Canvas(okno, width=400, height=250, bg="white")
canvas.pack()

# -------------------------
# Hviezdy – kreslené pomocou cyklu
# -------------------------
def hviezdy():
    canvas.delete("all")

    # cyklus opakovane kreslí hviezdy
    for i in range(6):
        x = 40 + i * 60
        y = 80

        # jednoduchá hviezda ako polygon
        canvas.create_polygon(x, y,
            x+10, y+30,
            x-20, y+10,
            x+20, y+10,
            x-10, y+30,
            fill="yellow")

# -------------------------
# Pozadie – zmena farby plátna
# -------------------------
def pozadie():
    # prepínanie medzi bielou a čiernou
    if canvas["bg"] == "white":
        canvas.config(bg="black")
    else:
        canvas.config(bg="white")

# -------------------------
# Vločky – modré kruhy
# -------------------------
def vlocky():
    canvas.delete("all")

    # cyklus kreslí vločky
    for i in range(8):
        x = 30 + i * 40
        y = 120

        canvas.create_oval(x, y, x+15, y+15, fill="lightblue")

# -------------------------
# Tlačidlá
# -------------------------
tlacidlo1 = Button(okno, text="Hviezdy", command=hviezdy)
tlacidlo1.pack()

tlacidlo2 = Button(okno, text="Pozadie", command=pozadie)
tlacidlo2.pack()

tlacidlo3 = Button(okno, text="Vločky", command=vlocky)
tlacidlo3.pack()

okno.mainloop()
