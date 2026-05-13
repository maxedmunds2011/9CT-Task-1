import pandas as pd   

def display_dataset():
    dataset = pd.read_csv('PublicTransportViewpoint.csv')
    print(dataset)

def show_tables():
    locations = pd.read_csv('PublicTransportViewpoint.csv').location
    columns = pd.read_csv('PublicTransportViewpoint.csv').columns
    print("____________________________________________________________")
    print("|                                                          |")
    print("|                   === Select Table ===                   |")
    print("|                                                          |")
    print("|            1. Total table (all data)                     |")
    print("|            2. Difference between two locations           |")
    print("|            3. Difference between two columns             |")
    print("|            4. One specific location                      |")
    print("|            5. Exit to main menu                          |")
    print("|__________________________________________________________|")
    table_choice = input("Please select an option (1-5): ")
    transport_df = pd.read_csv('PublicTransportViewpoint.csv')
    for x in transport_df.location:
        if x == 'Other':
            print()
    while True:
        if table_choice == '1':
            table = pd.read_csv('PublicTransportViewpoint.csv',
                                header = "All Data Table",
                                names = ['location', 'train_reliable', 'bus_reliable', 'other_transport', 'often_transport', 'time_transport', 'word_transport', 'transport_rating']
                                )
            print(table)
        elif table_choice == '2':
            print(locations)
            first_location = input("Please enter the location you want to view: ")
            second_location = input("Please enter the location you want to compare it to: ")
            while True:
                if first_location in locations and second_location in locations:
                    locations.remove(first_location, second_location)
                    new_df = transport_df.drop(rows=[locations])
                    new_table = pd.read_csv(new_df,
                                            header = f"{first_location} vs {second_location} Table",
                                            names = ['location', 'train_reliable', 'bus_reliable', 'other_transport', 'often_transport', 'time_transport', 'word_transport', 'transport_rating']
                                            )
                    print(new_table)
                else:
                    print("Invalid location. Please select from the available locations.")
        elif table_choice == '3':
            print(columns)
            first_column = input("Please enter the column you want to view: ")
            second_column = input("Please enter the column you want to compare it to: ")
            while True:
                if first_column in columns and second_column in columns:
                    columns.remove(first_column, second_column)
                    new_df = transport_df.drop(columns=[columns])
                    new_table = pd.read_csv(new_df,
                                            header = f"{first_column} vs {second_column} Table",
                                            names = [first_column, second_column]
                                            )
                    print(new_table)
                else:
                    print("Invalid column. Please select from the available columns.")
        elif table_choice == '4':
            print(locations)
            location = input("Please enter the location you want to view: ")
            while True:
                if location in locations:
                    locations.remove(location)
                    new_df = transport_df.drop(rows=[locations])
                    new_table = pd.read_csv(new_df,
                                            header = f"{location} Table",
                                            names = ['location', 'train_reliable', 'bus_reliable', 'other_transport', 'often_transport', 'time_transport', 'word_transport', 'transport_rating']
                                            )
                    print(new_table)
                else:
                    print("Invalid location. Please select from the available locations.")
        elif table_choice == '5':
            print("Returning to main menu.")
            break
        else:
            print("Invalid option. Please select a number between 1 and 5.")