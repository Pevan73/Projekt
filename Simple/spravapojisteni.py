from pojisteny import Pojisteny

class SpravaPojisteni:
    def __init__(self):
        self.seznam_pojisteni = []

    def pridej_pojisteneho(self, pojisteny):
        self.seznam_pojisteni.append(pojisteny)

    def zobraz_seznam(self):
        for pojisteny in self.seznam_pojisteni:
            print('{:<10} {:<10} {:<10} {:<10}'.format(pojisteny.jmeno, pojisteny.prijmeni, pojisteny.vek, pojisteny.telefon))

    def vyhledej_pojisteneho(self, jmeno, prijmeni):
        for pojisteny in self.seznam_pojisteni:
            if pojisteny.jmeno == jmeno and pojisteny.prijmeni == prijmeni:
                return pojisteny
        return None