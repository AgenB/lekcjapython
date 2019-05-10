class Osoba:
    def __init__(self, imie, nazw, wiek):
        self.imie = imie
        self.nazw = nazw
        self.wiek = wiek
    def przedstaw(self):
        print(f"Nazywam się {self.imie} {self.nazw}, mam {self.wiek} lat.")
    def urodziny(self):
        self.wiek += 1
        self.przedstaw()

ktos = Osoba("Jan", "Kowalski", 16)
ktos.przedstaw()
ktos.urodziny()