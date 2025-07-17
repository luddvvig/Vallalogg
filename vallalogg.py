import csv
import os
from funktioner import ensure_csv_with_headers, datum_kontroll, validate_temperature

vallalogg = "vallalogg.csv"

def log_search():
    print("För att söka på datum (1)")
    print("För att söka på plats (2)")
    print("För att söka temperatur (3)")
    print("För att gå tillbaka till meny (4)")
    choice = input("Välj sökmetod här: ")
    if choice == "1":
        log_search_date()
    elif choice == "2":
        log_search_place()
    elif choice == "3":
        log_search_temp()
    else:
        print("Välj från menyn!")

def log_search_temp():
    print("*" * 30)
    if not os.path.exists(vallalogg):
        print("Ingen vallalogg hittades. Skapa din första post först!")
        return
    
    print("Skriv först in lägsta tempdu vill söka på, sedan upp till vilken temp.")
    while True:
        try:
            temp_search_low = float(input("Välj lägsta temp du vill söka inom (+/-X): "))
            temp_search_high = float(input("Välj högsta temp du vill söka inom (+/-X): "))
            if isinstance(temp_search_low, float) and isinstance(temp_search_high, float):
                break
        except ValueError:
            print("\nOgiltig temperatur. Ange ett nummer (t.ex. -5 eller 2.5)\n")

    print(f"\nSöker efter loggar mellan {temp_search_low}°C och {temp_search_high}°C...\n")
    print("=" * 30)

    search_matching = []


    with open(vallalogg, "r", newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)

        
        for row in reader:
            try:
                temp = float(row["Temperatur"])
                if temp_search_low <= temp <= temp_search_high:
                    search_matching.append(row)
            except ValueError:
                continue
    if not search_matching:
        print("Inga loggar hittades i detta temp-spann")
    else:
        print(f"Hittade {len(search_matching)} vallaloggar\n")
        for i, post in enumerate(search_matching, 1):    
            print(f"Post {i}:")
            print(f"  Plats: {post['Plats']}")
            print(f"  Temperatur: {post['Temperatur']}°C")
            print(f"  Snötyp: {post['Snotyp']}")
            print(f"  Valla: {post['Valla']}")
            if post['Kommentar']:
                print(f"  Kommentar: {post['Kommentar']}")

def add_to_logg():
    #Kollar så att det finns en csv-fil
    ensure_csv_with_headers(vallalogg)
    print("Fyll i din rapport")
    print("*" * 30)

    while True:
        datum = input("Datum (YYYY-MM-DD): ")
        if datum_kontroll(datum):
            break
        else:
            print("Ogiltigt datum. Använd formatet YYYY-MM-DD (t.ex. 2025-01-15)")
    plats = input("Plats: ").lower()
    while True:
        temperatur_text = input("Temperatur (+C/-C): ")
        temperatur = validate_temperature(temperatur_text)
        if temperatur is not None:
            break
        else:
            print("Ogiltig temperatur. Ange ett nummer (t.ex. -5 eller 2.5)")
    snotyp = input("Snötyp: ").lower()
    valla = input("Valla: ").lower()
    kommentar = input("Kommentar: ")

    with open(vallalogg, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([datum, plats, temperatur, snotyp, valla, kommentar])

    print(f"Post tillagd för {datum} i {plats}")


def log_search_date():
    print("*" * 30)
    if not os.path.exists(vallalogg):
        print("Ingen vallalogg hittades. Skapa din första post först!")
        return

    while True:
        date_search = input("Vilket datum vill du kolla? (YYYY-MM-DD): ")
        if datum_kontroll(date_search):
            break
        else:
                print("Ogiltigt datum. Använd formatet YYYY-MM-DD")
    
    try:
        with open(vallalogg, "r") as f:
            reader = csv.DictReader(f)
        
            search_matching = []
            for row in reader:
                if row["Datum"] == date_search:
                    search_matching.append(row)
        
        
        if search_matching:
            print(f"Vallalogg för {date_search}")
            print("=" * 50)
        

            for i, post in enumerate(search_matching, 1):
                
                print(f"Post {i}:")
                print(f"  Plats: {post['Plats']}")
                print(f"  Temperatur: {post['Temperatur']}°C")
                print(f"  Snötyp: {post['Snotyp']}")
                print(f"  Valla: {post['Valla']}")
                if post['Kommentar']:
                    print(f"  Kommentar: {post['Kommentar']}")

            print(f"\nTotalt hittades {len(search_matching)} post(er) för detta datum.")
        else:
            print(f"\nIngen vallalogg hittades för {date_search}.")
            print("Kontrollera att datumet är korrekt eller lägg till en ny post.")

    except FileNotFoundError:
        print("Vallalogg-filen kunde inte hittas.")
    except PermissionError:
        print("Kan inte läsa vallalogg-filen. Kontrollera att den inte är öppen i ett annat program.")
    except csv.Error as e:
        # Detta händer om CSV-filen är korrupt eller har fel format
        print(f"Fel vid läsning av CSV-filen: {e}")
    except Exception as e:
        # Fångar upp alla andra oväntade fel
        print(f"Ett oväntat fel uppstod: {e}")

def log_search_place():
    if not os.path.exists(vallalogg):
        print("Ingen vallalogg hittades. Skapa din första post först!")
        return
    
    while True:
        try:
            place_search = input("Vilken plats vill du kolla? : ").lower()
            if place_search != type(str):
                break
        except ValueError:
                print("Hittar inte, testa igen! (Kontrollera stavning)")
    
    
    
    try:
        with open(vallalogg, "r") as f:
            reader = csv.DictReader(f)
            
            search_matching = []
            for row in reader:
                if row["Plats"] == place_search:
                    search_matching.append(row)
                else:
                    print("Ingen plats matchar, testa igen! (kontrollera din stavning)")
        
        
        if search_matching:
            print(f"Vallalogg för {place_search}")
            print("=" * 50)
        

            for i, post in enumerate(search_matching, 1):
                
                print(f"Post {i}:")
                print(f"  Plats: {post['Plats']}")
                print(f"  Temperatur: {post['Temperatur']}°C")
                print(f"  Snötyp: {post['Snotyp']}")
                print(f"  Valla: {post['Valla']}")
                if post['Kommentar']:
                    print(f"  Kommentar: {post['Kommentar']}")

            print(f"\nTotalt hittades {len(search_matching)} post(er) för detta datum.")
        else:
            print(f"\nIngen vallalogg hittades för {place_search}.")
            print("Kontrollera att platsen är korrekt eller lägg till en ny post.")

    except FileNotFoundError:
        print("Vallalogg-filen kunde inte hittas.")
    except PermissionError:
        print("Kan inte läsa vallalogg-filen. Kontrollera att den inte är öppen i ett annat program.")
    except csv.Error as e:
        # Detta händer om CSV-filen är korrupt eller har fel format
        print(f"Fel vid läsning av CSV-filen: {e}")
    except Exception as e:
        # Fångar upp alla andra oväntade fel
        print(f"Ett oväntat fel uppstod: {e}")

def show_all_logs():
    if not os.path.exists(vallalogg):
        print("Ingen vallalogg hittades. Skapa din första post först!")
        return

    with open(vallalogg, "r") as f:
        reader = csv.DictReader(f)  
        
        all_posts = list(reader)
        all_posts.sort(key=lambda x: x["Datum"], reverse=True)

        print(f"\n=== Alla vallalogg-poster ({len(all_posts)} st) ===")
        print("=" * 60)

        for i, post in enumerate(all_posts, 1):
                print(f"\n{i}. {post['Datum']} - {post['Plats']}")
                print(f"   Temperatur: {post['Temperatur']}°C | Snötyp: {post['Snotyp']} | Valla: {post['Valla']}")
                if post['Kommentar']:
                    print(f"   Kommentar: {post['Kommentar']}")
