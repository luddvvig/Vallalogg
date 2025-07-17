import csv
import os
import sys

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

    try:
        # 
        return float(temperatur_text)
    except ValueError:
        # Om konverteringen misslyckas, returnera None
        return None 
    
def exit_program():
    print("Program is being shut down")
    sys.exit()

