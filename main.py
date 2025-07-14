from vallalogg import add_to_logg

def main():

    print("Välkommen till Vallaloggen!")
    print("=" * 30)
    
    add_to_logg()
    
    print("\nTack för att du använder Vallalogg!")

if __name__ == "__main__":
    # Denna rad säkerställer att main() endast körs när filen körs direkt
    # och inte när den importeras som en modul
    main()