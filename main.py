from data_module import display_dataset, show_tables, search_data, clear_screen, change_data, show_graphs, save_data, animate_by_row
import os


def main_menu():
    while True: 
        def start_screen():
            screen = [
            "___________________________________________________________",
            "|                                                         |",
            "|                    === Main Menu ===                    |",
            "|                                                         |",
            "|            1. View dataset (.csv file)                  |",
            "|            2. View tables                               |",
            "|            3. View graphs                               |",
            "|            4. Search for data                           |",
            "|            5. Update an entry                           |",
            "|            6. Save data and changes                     |",
            "|            7. Exit system                               |",
            "|_________________________________________________________|"
            ]
            animate_by_row(screen, delay=0.2)

        start_screen()
        choice = input("Please select an option (1-7): ")
        clear_screen()

        if choice == '1':
                display_dataset()

        elif choice == '2':
                show_tables()

        elif choice == '3': 
                show_graphs()

        elif choice == '4':
                search_data()

        elif choice == '5':
                change_data()

        elif choice == '6':
                save_data()

        elif choice == '7':
                print("Exiting the system.")
                break

        else:
                print("Invalid option.")
            

if __name__ == "__main__":
       main_menu()