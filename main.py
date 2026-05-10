def main_menu():
    def start_screen():
        print("___________________________________________________________")
        print("|                                                         |")
        print("|                    === Main Menu ===                    |")
        print("|                                                         |")
        print("|            1. View dataset (.csv file)                  |")
        print("|            2. View tables                               |")
        print("|            3. View graphs                               |")
        print("|            4. Search for data                           |")
        print("|            5. Update an entry                           |")
        print("|            6. Save data and changes                     |")
        print("|            7. Exit system                               |")
        print("|_________________________________________________________|")
    start_screen()
    while True: 
        choice = input("Please select an option (1-7): ")
        if choice == '1':
            print()
        elif choice == '2':
            print()
        elif choice == '3':
            print()
        elif choice == '4':
            print()
        elif choice == '5':
            print()
        elif choice == '6':
            print()
        elif choice == '7':
            print("Exiting the system.")
            break
        else:
            print("Invalid option. Please select a number between 1 and 7.")
main_menu()