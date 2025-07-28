import csv
import os
import sys
from datetime import datetime

#För att kolla så att en csv-fil finns
def ensure_csv_with_headers(filename):
    # Om filen finns, kolla om den är tom eller saknar headers
    with open(filename, "r", newline="", encoding="utf-8") as f:
        content = f.read().strip()
        
    # Om filen är helt tom, lägg till headers
    if not content:
        print(f"Filen {filename} är tom, lägger till headers...")
        with open(filename, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["Datum", "Plats", "Temperatur", "Snotyp", "Valla", "Struktur", "Kommentar"])
        print("***")
        print(f"La till headers i CSV-fil: {filename}")
        return

    if not os.path.exists(filename):
        print(f"Skapar ny fil: {filename}")
        with open(filename, "w", newline="", encoding=("utf-8")) as f:
            #Lägger till en "meny" överst på tom csv-fil
            writer = csv.writer(f)
            writer.writerow(["Datum", "Plats", "Temperatur", "Snotyp", "Valla", "Struktur", "Kommentar"])
        print("***")
        print(f"Skapade ny CSV-fil: {filename}")

#Kontrollerar att datumsträngen är YYYY-MM-DD
def datum_kontroll(datum):
    """Kontrollerar att datumsträngen är i formatet YYYY-MM-DD."""
    try:
        datetime.strptime(datum, "%Y-%m-%d")
        return True
    except ValueError:
        # Om formatet är fel kastas ett ValueError
        return False

def validate_temperature(temperatur_text):

    try:
        # 
        return float(temperatur_text)
    except ValueError:
        # Om konverteringen misslyckas, returnera None
        return None 
    
def exit_program():
    print("Program is being shut down")
    sys.exit()

"""import os

def diagnose_file(filename):
    if not os.path.exists(filename):
        print(f"Filen {filename} existerar inte")
        return
    
    # Läs filens rå bytes
    with open(filename, "rb") as f:  # "rb" = read binary
        raw_content = f.read()
    
    print(f"Filens storlek: {len(raw_content)} bytes")
    print(f"Första 20 bytes (som nummer): {list(raw_content[:20])}")
    print(f"Första 100 tecken (försök som UTF-8): ", end="")
    
    try:
        print(repr(raw_content[:100].decode('utf-8')))
    except UnicodeDecodeError as e:
        print(f"Kunde inte tolka som UTF-8: {e}")
        print(f"Försöker som ISO-8859-1: {repr(raw_content[:100].decode('iso-8859-1'))}")

# Kör diagnosen
diagnose_file("vallalogg.csv")  """