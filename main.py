class Osoba:
    def __init__(self, imie, nazw, wiek):
        self.imie = imie
        self.nazw = nazw
        self.wiek = wiek
    def __del__(self):
        print(f"{self.imie} {self.nazw} zmarł.")
    def __str__(self):
        return f"Nazywam się {self.imie} {self.nazw}, mam {self.wiek} lat."
    def przedstaw(self):
        print(f"Nazywam się {self.imie} {self.nazw}, mam {self.wiek} lat.")
    def urodziny(self):
        self.wiek += 1
        self.przedstaw()

class Prostokat:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __str__(self):
        return f"O[{self.obwod()}] P[{self.pole()}] D[{self.przek()}]"
    def obwod(self):
        return self.a*2 + self.b*2
    def pole(self):
        return self.a * self.b
    def przek(self):
        return (self.a**2 + self.b**2)**0.5

ktos = Osoba("Jan", "Kowalski", 16)
k2 = ktos
ktos = 0
x = Prostokat(3, 4)
print(x)