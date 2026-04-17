from tkinter import *  # import knižnice na tvorbu grafického rozhrania

# vytvorenie hlavného okna aplikácie
okno = Tk()

# nastavenie názvu okna (zobrazí sa hore v lište)
okno.title("Moje prvé GUI")

# vytvorenie textu v okne (Label = textový prvok)
nadpis = Label(okno, text="Napíš svoju náladu:")
nadpis.pack()  # zobrazí prvok v okne

# vstupné pole, do ktorého používateľ píše text
vstup = Entry(okno)
vstup.pack()

# funkcia, ktorá sa vykoná po kliknutí na tlačidlo
def zobraz():
    # získanie textu z vstupného poľa
    text = vstup.get()
    
    # zmena textu v spodnom Labeli
    vystup.config(text=text)

# tlačidlo, ktoré po kliknutí spustí funkciu zobraz
tlacidlo = Button(okno, text="Zobraziť", command=zobraz)
tlacidlo.pack()

# výstupný text (na začiatku má prednastavený text)
vystup = Label(okno, text="Sem sa vypíše text.")
vystup.pack()

okno.mainloop()


