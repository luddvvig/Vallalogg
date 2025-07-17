from vallalogg import add_to_logg, show_all_logs, log_search
from funktioner import exit_program

def main():

    print("Välkommen till Vallaloggen!")
    print("=" * 30)

    #Skapar en meny att välja från
    try:
        while True:
            print("=" * 30)
            print("\nFör att välja funktion, skriv in rätt nummer!\n")
            print("Vallalogg sök (1)")
            print("Alla vallaloggar (2)")
            print("Lägg till en ny post (3)")
            print("Avsluta (4)\n")

            choice_menu = input("Välj nummer här: ").strip()

            if choice_menu == "1":
                log_search()
            elif choice_menu == "2":
                show_all_logs()
            elif choice_menu == "3":
                add_to_logg()
            elif choice_menu == "4":
                exit_program()
            else:
                print("\nvälj från menyn tack!")
    except KeyboardInterrupt:
        print("\n")
        print("*" * 50)
        print("Tack för ditt besök, programmet stängs ner!")
        print("*" * 50)

            


if __name__ == "__main__":
    main()