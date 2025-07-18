import csv
import os
import sys
from datetime import datetime

#För att kolla så att en csv-fil finns
def ensure_csv_with_headers(filename):
    if not os.path.exists(filename):
        print(f"Skapar ny fil: {filename}")
        with open(filename, "w", newline="") as f:
            #Lägger till en "meny" överst på tom csv-fil
            writer = csv.writer(f)
            writer.writerow(["Datum", "Plats", "Temperatur", "Snotyp", "Valla", "Kommentar"])
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

