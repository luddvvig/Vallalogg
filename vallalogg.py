import csv
import os
from funktioner import ensure_csv_with_headers, datum_kontroll, validate_temperature

vallalogg = "vallalogg.csv"

def _print_search_results(results, search_term):
    """Funktion som skriver ut sökresultaten i ett snyggt format
    Args:
        results (list) lista med sökresultat
        search_term: Input för sökningen"""
    #kontroll om det finns resultat
    if not results:
        print(f"Inga resultat hittades för {search_term}.")
        print("Kontrollera att datumet är korrekt eller lägg till en ny post.")
        return
    # Visar antal resultat
    print(f"\nTotalt hittades {len(results)} post(er) för {search_term}.")
    #loop för utskrift
    for i, post in enumerate(results, 1):
        print(f"{i}. {post['Datum']} - {post['Plats']}")
        print(f"   Temp: {post['Temperatur']}°C | Snö: {post['Snotyp']} | Valla: {post['Valla']}  | Struktur: {post['Struktur']}")
        if post['Kommentar']:
            print(f"   Kommentar: {post['Kommentar']}")
    print("=" * 60)




def log_search():
    """
    Menyfunktion för att välja söksätt
    """
    #Loop för att hålla igpng menyn
    while True:
        print("=" * 50)
        print("\nFör att söka på datum (1)")
        print("För att söka på plats (2)")
        print("För att söka temperatur (3)")
        print("För att gå tillbaka till meny (M/m)")
        choice = input("Välj sökmetod här: ").strip().lower()
        if choice == "1":
            log_search_date()
        elif choice == "2":
            log_search_place()
        elif choice == "3":
            log_search_temp()
        elif choice == "m":
            break # går tillbaka till huvudmeny
        else:
            print("Välj från menyn!")

def log_search_temp():
    """
    Funktion för att söka vallarapport efter ett temperaturspann.
    """
    print("*" * 30)
    if not os.path.exists(vallalogg):
        print("Ingen vallalogg hittades. Skapa din första post först!")
        return
    
    print("Skriv först in lägsta tempdu vill söka på, sedan upp till vilken temp.")
    while True:
        try:
            #Tar in lägsta och högsta värde i temp-spannet
            temp_search_low = float(input("Välj lägsta temp du vill söka inom (+/-X): "))
            temp_search_high = float(input("Välj högsta temp du vill söka inom (+/-X): "))
            #extra kontroll så att värderna är float
            if isinstance(temp_search_low, float) and isinstance(temp_search_high, float):
                break
        except ValueError:
            print("\nOgiltig temperatur. Ange ett nummer (t.ex. -5 eller 2.5)\n")

    print(f"\nSöker efter loggar mellan {temp_search_low}°C och {temp_search_high}°C...\n")
    print("=" * 30)
    temp_range = str(temp_search_low) + "->" + str(temp_search_high)
    with open(vallalogg, "r", newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        #Här söker jag i spannet, och lägger till resultatet i en lista
        search_matching = [row for row in reader if temp_search_low <= float(row["Temperatur"]) <= temp_search_high]
        if search_matching:
            _print_search_results(search_matching, temp_range)
    print(temp_range)

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
    structure = input("Struktur: ")
    kommentar = input("Kommentar: ")

    print("\n" + "="*40)
    print("SAMMANFATTNING:")
    print(f"Datum: {datum}")
    print(f"Plats: {plats}")
    print(f"Temperatur: {temperatur}°C")
    print(f"Snötyp: {snotyp}")
    print(f"Valla: {valla}")
    print(f"Struktur: {structure}")
    print(f"Kommentar: {kommentar}")
    print("="*40)

    confirm = input("Spara denna post? J/N: ").strip().lower()
    
    if confirm == "j":
        with open(vallalogg, "a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow([datum, plats, temperatur, snotyp, valla, structure, kommentar])

            print(f"Post tillagd för {datum} i {plats}")
    else:
        print("Post inte sparad!")

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
        with open(vallalogg, "r",newline="", encoding=("utf-8")) as f:
            reader = csv.DictReader(f)
        
            search_matching = [row for row in reader if row["Datum"] == date_search]
            _print_search_results(search_matching,date_search)

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
    input("\nTryck Enter för att fortsätta...\n")
    print("=" * 50)

def log_search_place():
    if not os.path.exists(vallalogg):
        print("Ingen vallalogg hittades. Skapa din första post först!")
        return
    
    while True:
        place_search = input("Vilken plats vill du kolla? : ").lower()
        if place_search != type(str):
            break

    try:
        with open(vallalogg, "r", encoding=("utf-8")) as f:
            reader = csv.DictReader(f)
        
            search_matching = [row for row in reader if row["Plats"].lower() == place_search]
            if search_matching:
                _print_search_results(search_matching, place_search)        

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

    with open(vallalogg, "r", encoding=("utf-8")) as f:
        reader = csv.DictReader(f)  
        
        all_posts = list(reader)
        all_posts.sort(key=lambda x: x["Datum"], reverse=True)
    _print_search_results(all_posts, search_term="Alla loggar")
