class Osoba:
    def __init__(self, imie, nazw):
        self.imie = imie
        self.nazw = nazw
    def przedstaw(self):
        print("Nazywam się {} {}".format(self.imie, self.nazw))

ktos = Osoba("Jan", "Kowalski")
ktos.przedstaw()