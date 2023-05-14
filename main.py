from pojisteni import Pojisteni

while True:
    volba = input("Vyberte činnost: \n 1-přidat záznam\n 2-zobrazit všechny záznamy\n 3-vyhledat záznam\n 4-smazat záznam \n 5-ukončit program \n")

    if volba == "1":
        jmeno = input("Jméno: ")
        prijmeni = input("Příjmení: ")
        vek = input("Věk: ")
        telefon = input("Telefonní číslo: ")
        pojisteny = Pojisteni(jmeno, prijmeni, vek, telefon)
        Pojisteni.pridej_pojisteneho(pojisteny)
        print("Pojištěný byl přidán.")
        input("Stiskněte libovolnou klávesu pro pokračování...")
    elif volba == "2":
        Pojisteni.zobraz_seznam()
        input("Stiskněte libovolnou klávesu pro pokračování...")
    elif volba == "3":
        jmeno = input("Jméno: ")
        prijmeni = input("Příjmení: ")
        pojisteny = Pojisteni.vyhledej_pojisteneho(jmeno, prijmeni)
        if pojisteny:
            print(pojisteny)
            input("Stiskněte libovolnou klávesu pro pokračování...")
        else:
            print("Pojištěný nebyl nalezen.")
            input("Stiskněte libovolnou klávesu pro pokračování...")
    elif volba == "4":
        id_pojisteneho= input("Zadejte ID pojištěného, které chcete smazat:\n")
        Pojisteni.smaz_pojisteneho(id_pojisteneho)
        input("Stiskněte libovolnou klávesu pro pokračování...")
    elif volba == "5":
        break