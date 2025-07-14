from vallalogg import add_to_logg, show_all_logs, read_log
from funktioner import exit_program

def main():

    print("Välkommen till Vallaloggen!")
    print("=" * 30)
    
    while True:
        print("=" * 30)
        print("\nFör att välja funktion, skriv in rätt nummer!")
        print("Vallalogg sök datum (1)")
        print("Alla vallaloggar (2)")
        print("Lägg till en ny post (3)")
        print("Avsluta (4)")

        choice_menu = input("Välj nummer här: ").strip()

        if choice_menu == "1":
            read_log()
        elif choice_menu == "2":
            show_all_logs()
        elif choice_menu == "3":
            add_to_logg()
        elif choice_menu == "4":
            exit_program()
        else:
            print("\nvälj från menyn tack!")
            


if __name__ == "__main__":
    # Denna rad säkerställer att main() endast körs när filen körs direkt
    # och inte när den importeras som en modul
    main()