from tkinter import *

# Vytvorenie hlavného okna aplikácie
okno = Tk()
okno.title("Školská vizitka")

# FUNKCIA = je základný princíp udalostného programovania:
# Program čaká na udalosť od používateľa a reaguje na ňu, t.j
# Funkcia sa nevykoná hneď po spustení programu, ale spustí sa až po kliknutí na tlačidlo.
def zobraz_vizitku():
    meno = vstup_meno.get()
    trieda = vstup_trieda.get()
    vystup.config(text="Volám sa " + meno + " a chodím do triedy " + trieda + ".")

# Textové prvky - pokyny pre používateľa
label_meno = Label(okno, text="Zadaj meno:")
label_meno.pack()

# Vstupné pole na meno
vstup_meno = Entry(okno)
vstup_meno.pack()

label_trieda = Label(okno, text="Zadaj triedu:")
label_trieda.pack()

# Vstupné pole na triedu
vstup_trieda = Entry(okno)
vstup_trieda.pack()

# Tlačidlo spúšťa funkciu zobraz_vizitku
tlacidlo = Button(okno, text="Zobraz vizitku", command=zobraz_vizitku)
tlacidlo.pack()

# Výstupný textový prvok, do ktorého sa zobrazí výsledná veta
vystup = Label(okno, text="Tu sa zobrazí vizitka.")
vystup.pack()

# Spustenie hlavného cyklu aplikácie
okno.mainloop()
