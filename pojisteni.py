try:
    import sqlite3  #import sqlite3
except ImportError:
    print("Modul sqlite3 není k dispozici. Nainstalovat jej můžete pomocí příkazu: pip install pysqlite3") #ošetření výjimky
else:
    # vytvoření spojení s databází a kurzoru
    db_path='pojisteni.db'
    conn = sqlite3.connect('pojisteni.db')
    c = conn.cursor()

# vytvoření tabulky pojisteni
c.execute('''CREATE TABLE IF NOT EXISTS pojisteni
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
             jmeno TEXT,
             prijmeni TEXT,
             vek INTEGER,
             telefon TEXT)''')

# ukončení spojení s databází
conn.commit()
conn.close()

class Pojisteni:
    def __init__(self, jmeno, prijmeni, vek, telefon):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.vek = vek
        self.telefon = telefon

    def __str__(self):
        return f"{self.jmeno} {self.prijmeni} ({self.vek} let, tel. {self.telefon})"

    # Přidání pojištěného
    def pridej_pojisteneho(self):       
        conn = sqlite3.connect('pojisteni.db')
        c = conn.cursor()

        c.execute("INSERT INTO pojisteni (jmeno, prijmeni, vek, telefon) VALUES (?, ?, ?, ?)", (self.jmeno, self.prijmeni, self.vek, self.telefon))

        conn.commit()
        conn.close()
    
    # zobrazení seznamu - dle Stack Overflow je tohle "pretty clean" způsob, jak mít hezký výstup v konzoli
    @classmethod
    def zobraz_seznam(cls):
        conn = sqlite3.connect('pojisteni.db')
        c = conn.cursor()

        # vybereme všechny záznamy
        c.execute("SELECT * FROM pojisteni")
        results = c.fetchall()

        # a hezky si je seřadíme do sloupečků
        if results:
            print("{:<5} {:<20} {:<20} {:<10} {:<15}".format("ID", "Jméno", "Příjmení", "Věk", "Telefon"))
            print("="*70)
            for row in results:
                pojisteny = cls(row[1], row[2], row[3], row[4])
                pojisteny.id = row[0]
                print("{:<5} {:<20} {:<20} {:<10} {:<15}".format(str(pojisteny.id), pojisteny.jmeno, pojisteny.prijmeni, str(pojisteny.vek), pojisteny.telefon))
        else:
            print("Žádní pojistení nebyli nalezeni.")
            conn.close()
            return


        conn.close()

    # Vyhledáme pojištěného podle jména a příjmení
    def vyhledej_pojisteneho(jmeno, prijmeni):
        conn = sqlite3.connect('pojisteni.db')
        c = conn.cursor()

        c.execute("SELECT * FROM pojisteni WHERE jmeno = ? AND prijmeni = ?", (jmeno, prijmeni))
        result = c.fetchone()

        if result:
            pojisteny = Pojisteni(result[1], result[2], result[3], result[4])
            pojisteny.id = result[0]
            return pojisteny

        conn.close()
        return None
    
    # A tady můžeme záznam vymazat podle ID z výpisu
    @classmethod
    def smaz_pojisteneho(cls, id_pojisteneho):
    # ošetření negramota u klávesnice
        try:
            id = int(id_pojisteneho)
        except ValueError:
            print("Zadaná hodnota musí být číslo.")
            conn.close()
            return
        conn = sqlite3.connect('pojisteni.db')
        c = conn.cursor()
        
        c.execute("SELECT * FROM pojisteni WHERE id = ?", (id,))
        result = c.fetchone()
        if result:
            pojisteny = cls(result[1], result[2], result[3], result[4])
            pojisteny.id = result[0]
            print(f"Chcete smazat následujícího pojisteného: {pojisteny}?") # Ujistíme se, že fakt, opravdu chceme smazat zrovna tento záznam
            potvrzeni = input("Zadejte 'ano' pro smazání, nebo cokoli jiného pro návrat zpět: ")    
            if potvrzeni == 'ano':
                c.execute("DELETE FROM pojisteni WHERE id = ?", (id,))
                conn.commit()
                print("Pojištěný byl smazán.")
        else:
            print("Pojištěný s daným ID nebyl nalezen.")
        
        conn.commit()
        conn.close()