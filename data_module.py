import pandas as pd

def display_dataset():
    dataset = pd.read_csv('PublicTransportViewpoint.csv')
    print(dataset)

def show_tables():
    print("____________________________________________________________")
    print("|                                                          |")
    print("|                   === Select Table ===                   |")
    print("|                                                          |")
    print("|            1. Total table (all data)                     |")
    print("|            2. One selected location                      |")
    print("|            3. One selected column                        |")
    print("|            4. Difference between two locations           |")
    print("|__________________________________________________________|")
    table_choice = input("Please select an option (1-4): ")