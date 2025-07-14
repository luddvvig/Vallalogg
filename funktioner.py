import csv
import os

def ensure_csv_with_headers(filename):
    if not os.path.exists(filename):
        print(f"Skapar ny fil: {filename}")
        with open(filename, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Datum", "Plats", "Temperatur", "Snotyp", "Valla", "Kommentar"])
        print("***")
        print(f"Skapade ny CSV-fil: {filename}")

def datum_kontroll(datum):
    if len(datum) != 10:
        return False
    
    if datum[4] != "-" or datum[7] != "-":
        return False

    year = datum[0:4]
    month = datum[5:7]
    day = datum[8:10]

    if not (year.isdigit() and month.isdigit() and day.isdigit()):
        return False
    
    else:
        return True

def validate_temperature(temperatur_text):
    """
    Validerar och konverterar temperaturinmatning till float.
    
    Denna funktion försöker konvertera texten till ett decimaltal.
    Om det lyckas, returnerar den talet. Om det misslyckas (t.ex. om
    användaren skrev "kall" istället för "-5"), returnerar den None.
    
    Args:
        temperatur_text (str): Temperaturtext som ska konverteras
    
    Returns:
        float or None: Temperatur som decimaltal, eller None om ogiltig
    """
    try:
        # Försök konvertera texten till ett decimaltal
        return float(temperatur_text)
    except ValueError:
        # Om konverteringen misslyckas, returnera None
        return None