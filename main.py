from pojisteni import Pojisteni

while True:
    volba = input("Vyberte činnost: \n 1-přidat záznam\n 2-zobrazit všechny záznamy\n 3-vyhledat záznam\n 4-smazat záznam \n 5-ukončit program \n")

    if volba == "1":
        jmeno = input("Jméno: ")
        prijmeni = input("Příjmení: ")
        vek = input("Věk: ")
        telefon = input("Telefonní číslo: ")
        Pojisteni.pridej_pojisteneho(Pojisteni(jmeno, prijmeni, vek, telefon))
        print("Pojištěný byl přidán.")
    
    elif volba == "2":
        Pojisteni.zobraz_seznam()
        
    elif volba == "3":
        jmeno = input("Jméno: ")
        prijmeni = input("Příjmení: ")
        pojisteny = Pojisteni.vyhledej_pojisteneho(jmeno, prijmeni)
        if pojisteny:
            print(pojisteny)
        else:
            print("Pojištěný nebyl nalezen.")
            
    elif volba == "4":
        id_pojisteneho= input("Zadejte ID pojištěného, které chcete smazat:\n")
        Pojisteni.smaz_pojisteneho(id_pojisteneho)
    
    elif volba == "5":
        break