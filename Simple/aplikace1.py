from pojisteny import Pojisteny
from spravapojisteni import SpravaPojisteni


sprava_pojisteni = SpravaPojisteni()

while True:
    volba = input("Vyberte činnost: \n1-přidat,\n 2-zobrazit,\n 3-vyhledat,\n 4-ukončit \n ")

    if volba == "1":
        jmeno = input("Jméno: ")
        prijmeni = input("Příjmení: ")
        vek = input("Věk: ")
        telefon = input("Telefonní číslo: ")
        pojisteny = Pojisteny(jmeno, prijmeni, vek, telefon)
        sprava_pojisteni.pridej_pojisteneho(pojisteny)
        print("Pojištěný byl přidán.")
        
    elif volba == "2":
        sprava_pojisteni.zobraz_seznam()
        
    elif volba == "3":
        jmeno = input("Jméno: ")
        prijmeni = input("Příjmení: ")
        pojisteny = sprava_pojisteni.vyhledej_pojisteneho(jmeno, prijmeni)
        if pojisteny:
            print(pojisteny)
            
        else:
            print("Pojištěný nebyl nalezen.")
            
    elif volba == "4":
        break
