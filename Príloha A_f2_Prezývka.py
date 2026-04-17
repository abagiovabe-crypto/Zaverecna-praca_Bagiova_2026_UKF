from tkinter import *

# vytvorenie hlavného okna aplikácie (základ celého GUI)
okno = Tk()

# názov okna – žiaci môžu meniť a sledovať zmenu
okno.title("Prezývka")

# funkcia, ktorá sa vykoná po kliknutí na tlačidlo
def vytvor_prezyvku():
    # získanie textu zo vstupného poľa (Entry)
    meno = vstup.get()
    
    # zmena textu vo výstupnom prvku (Label)
    vysledok.config(text="Super " + meno)


# TEXTOVÝ PRVOK (Label) – zobrazí pokyn pre používateľa
napis = Label(okno, text="Zadaj meno:")
napis.pack()


# VSTUPNÉ POLE (Entry) – používateľ doň zadáva text
vstup = Entry(okno)
vstup.pack()


# TLAČIDLO (Button) – po kliknutí spustí funkciu vytvor_prezdivku
tlacidlo = Button(okno, text="Vytvor", command=vytvor_prezyvku)
tlacidlo.pack()


# VÝSTUPNÝ TEXT (Label) – sem sa zobrazí výsledok programu
vysledok = Label(okno, text="")
vysledok.pack()


# spustenie programu – okno zostane otvorené a čaká na akcie používateľa
okno.mainloop()
