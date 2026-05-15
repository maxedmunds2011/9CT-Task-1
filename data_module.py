import pandas as pd   

def display_dataset():
    dataset = pd.read_csv('PublicTransportViewpoint.csv')
    dataset = dataset.drop(columns=['Timestamp'])
    print(dataset)

def show_tables():
    locations = ['Central Coast', 'Sydney', 'Other']
    columns = ['location', 'train_reliable', 'bus_reliable', 'other_transport', 'often_transport', 'time_transport', 'word_transport', 'transport_rating']
    print("____________________________________________________________")
    print("|                                                          |")
    print("|                   === Select Table ===                   |")
    print("|                                                          |")
    print("|            1. Difference between two locations           |")
    print("|            2. Difference between two columns             |")
    print("|            3. One specific location                      |")
    print("|            4. Exit to main menu                          |")
    print("|__________________________________________________________|")
    while True:
        table_choice = input("Please select an option (1-4): ")
        transport_df = pd.read_csv('PublicTransportViewpoint.csv')
        # 1. Set columns equal to the first row (index 0)
       # transport_df.columns = transport_df.iloc[0]
        print(transport_df)

# 2. Remove the first row from the data and reset the index
        #transport_df = transport_df[1:].reset_index(drop=True)

        if table_choice == '1':
            while True:
                print(locations)
                first_location = input("Please enter the location you want to view: ")
                second_location = input("Please enter the location you want to compare it to: ")
                if first_location and second_location in locations:
                    if first_location and second_location != 'Other':
                        dropped_rows = transport_df[transport_df['location'] == "Other"].index
                        transport_df.drop(dropped_rows)
                        print(transport_df)
                    elif first_location and second_location != 'Central Coast':
                        transport_df = transport_df.drop (transport_df[transport_df['location'] == "Central Coast"].index)
                        print(transport_df)
                    elif first_location and second_location != 'Sydney':
                        transport_df = transport_df.drop (transport_df[transport_df['location'] == "Sydney"].index)
                        print(transport_df)
                    else:
                        print("Invalid locations. Try again.")

        elif table_choice == '2':
            print(columns)
            first_column = input("Please enter the column you want to view: ")
            second_column = input("Please enter the column you want to compare it to: ")
            while True:
                if first_column in columns and second_column in columns:
                    columns.remove(first_column, second_column)
                    new_df = transport_df.drop(columns=[columns])
                    new_table = pd.read_csv(new_df,
                                            header = None,
                                            names = [first_column, second_column]
                                            )
                    print(new_table)
                else:
                    print("Invalid column. Please select from the available columns.")

        elif table_choice == '3':
            print(locations)
            location = input("Please enter the location you want to view: ")
            while True:
                if location in locations:
                    locations.remove(location)
                    new_df = transport_df.drop(rows=[locations])
                    new_table = pd.read_csv(new_df,
                                            header = None,
                                            names = ['location', 'train_reliable', 'bus_reliable', 'other_transport', 'often_transport', 'time_transport', 'word_transport', 'transport_rating']
                                            )
                    print(new_table)
                else:
                    print("Invalid location. Please select from the available locations.")

        elif table_choice == '4':
            print("Returning to main menu.")
            break
        else:
            print("Invalid option. Please select a number between 1 and 5.")

show_tables()