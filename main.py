from data_module import display_dataset, show_tables, search_data, clear_screen
import os


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

    while True: 
        start_screen() 
        choice = input("Please select an option (1-7): ")
        clear_screen()

        if choice == '1':
            display_dataset()

        elif choice == '2':
            show_tables()

        elif choice == '3': 
            print()

        elif choice == '4':
            search_data()

        elif choice == '5':
            print()

        elif choice == '6':
            print()

        elif choice == '7':
            print("Exiting the system.")
            break

        else:
            print("Invalid option.")
            

main_menu()