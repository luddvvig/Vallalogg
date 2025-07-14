import csv
from funktioner import ensure_csv_with_headers, datum_kontroll, validate_temperature


def add_to_logg():
    #Kollar så att det finns en csv-fil
    ensure_csv_with_headers("vallalogg.csv")
    print("Fyll i din rapport")
    print("*" * 30)

    while True:
        datum = input("Datum (YYYY-MM-DD): ")
        if datum_kontroll(datum):
            break
        else:
            print("Ogiltigt datum. Använd formatet YYYY-MM-DD (t.ex. 2025-01-15)")
    plats = input("Plats: ")
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

    with open("vallalogg.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([datum, plats, temperatur, snotyp, valla, kommentar])

    print(f"Post tillagd för {datum} i {plats}")


