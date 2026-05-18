import csv
import os
import pandas as pd   
import matplotlib.pyplot as plt 

dictionary = {
    'locations': {
        'Central Coast': {'train_reliable': {'mean': '', 'median': '', 'mode': '', 'min': '', 'max': '', 'number': ''},
                   'bus_reliable': {'mean': '', 'median': '', 'mode': '', 'min': '', 'max': '', 'number': ''},
                   'often_transport': {'number1': '', 'number2': '', 'number3': '', 'number4': '', 'number5': ''},
                   'time_transport': {'number1': '', 'number2': '', 'number3': '', 'number4': '', 'number5': ''},
                   'transport_rating': {'mean': '', 'median': '', 'mode': '', 'min': '', 'max': '', 'number': ''},
                   'other_transport': [''],
                   'word_transport': {'positive': [''], 'negative': ['']}},

        'Sydney': {'train_reliable': {'mean': '', 'median': '', 'mode': '', 'min': '', 'max': '', 'number': ''},
                   'bus_reliable': {'mean': '', 'median': '', 'mode': '', 'min': '', 'max': '', 'number': ''},
                   'often_transport': {'number1': '', 'number2': '', 'number3': '', 'number4': '', 'number5': ''},
                   'time_transport': {'number1': '', 'number2': '', 'number3': '', 'number4': '', 'number5': ''},
                   'transport_rating': {'mean': '', 'median': '', 'mode': '', 'min': '', 'max': '', 'number': ''},
                   'other_transport': [''],
                   'word_transport': {'positive': [''], 'negative': ['']}},

        'Other': {'train_reliable': {'mean': '', 'median': '', 'mode': '', 'min': '', 'max': '', 'number': ''},
                   'bus_reliable': {'mean': '', 'median': '', 'mode': '', 'min': '', 'max': '', 'number': ''},
                   'often_transport': {'number1': '', 'number2': '', 'number3': '', 'number4': '', 'number5': ''},
                   'time_transport': {'number1': '', 'number2': '', 'number3': '', 'number4': '', 'number5': ''},
                   'transport_rating': {'mean': '', 'median': '', 'mode': '', 'min': '', 'max': '', 'number': ''},
                   'other_transport': [''],
                   'word_transport': {'positive': [''], 'negative': ['']}}
    },
    'columns': {'train_reliable': {'mean': '', 'median': '', 'mode': '', 'min': '', 'max': '', 'number': ''},

                'bus_reliable': {'mean': '', 'median': '', 'mode': '', 'min': '', 'max': '', 'number': ''},

                'often_transport': {'number1': '', 'number2': '', 'number3': '', 'number4': '', 'number5': ''},
 
                'time_transport': {'number1': '', 'number2': '', 'number3': '', 'number4': '', 'number5': ''},

                'transport_rating': {'mean': '', 'median': '', 'mode': '', 'min': '', 'max': '', 'number': ''},
    }}


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def display_dataset():
    dataset = pd.read_csv('PublicTransportViewpoint.csv')
    print(dataset)


def show_tables():
    while True:

        table_locations = ['Central Coast', 'Sydney', 'Other']
        table_columns = ['location', 'train_reliable', 'bus_reliable', 'other_transport', 'often_transport', 'time_transport', 'word_transport', 'transport_rating']
    
        print("____________________________________________________________")
        print("|                                                          |")
        print("|                   === Select Table ===                   |")
        print("|                                                          |")
        print("|            1. Difference between two locations           |")
        print("|            2. Difference between two columns             |")
        print("|            3. One specific location                      |")
        print("|            4. Exit to main menu                          |")
        print("|__________________________________________________________|")

        table_choice = input("Please select an option (1-4): ")
        transport_df = pd.read_csv('PublicTransportViewpoint.csv')

        if table_choice == '1':
                print(table_locations)
                first_location = input("Please enter the location you want to view: ")
                second_location = input("Please enter the location you want to compare it to: ")
                if first_location and second_location in table_locations:
                    table_locations.remove(first_location)
                    table_locations.remove(second_location)
                    for x in table_locations:
                        transport_df_l = transport_df.drop(transport_df[transport_df["location"] == x].index)
                print(transport_df_l)

        elif table_choice == '2':
                print(table_columns)
                first_column = input("Please enter the column you want to view: ")
                second_column = input("Please enter the column you want to compare it to: ")
                if first_column and second_column in table_columns:
                    table_columns.remove (first_column)
                    table_columns.remove (second_column)
                    for x in table_columns:
                        transport_df_c = transport_df.drop(columns=x)
                print(transport_df_c)          

        elif table_choice == '3':
            print(table_locations)
            location = input("Please enter the location you want to view: ")
            if location in table_locations:
                table_locations.remove(location)
                for x in table_locations:
                    transport_df_l = transport_df.drop(transport_df[transport_df["location"] == x].index)     
            print(transport_df_l)
                
        elif table_choice == '4':
            print("Returning to main menu.")
            break

        else:
            print("Invalid option. Please select a number between 1 and 5.")


def graph_data():
    transport_df = pd.read_csv('PublicTransportViewpoint.csv')
    data_locations = ['Central Coast', 'Sydney', 'Other']
    for x in data_locations:
        loc_df = transport_df[transport_df['location'] == x]

        dictionary['locations'][x]['train_reliable']['mean'] = loc_df['train_reliable'].mean().round(2)
        dictionary['locations'][x]['train_reliable']['median'] = loc_df['train_reliable'].median().round(2)
        dictionary['locations'][x]['train_reliable']['mode'] = loc_df['train_reliable'].mode().round(2).tolist()
        dictionary['locations'][x]['train_reliable']['min'] = loc_df['train_reliable'].min()
        dictionary['locations'][x]['train_reliable']['max'] = loc_df['train_reliable'].max()
        dictionary['locations'][x]['train_reliable']['number'] = loc_df['train_reliable'].count()

        dictionary['locations'][x]['bus_reliable']['mean'] = loc_df['bus_reliable'].mean().round(2)
        dictionary['locations'][x]['bus_reliable']['median'] = loc_df['bus_reliable'].median().round(2)
        dictionary['locations'][x]['bus_reliable']['mode'] = loc_df['bus_reliable'].mode().round(2).tolist()
        dictionary['locations'][x]['bus_reliable']['min'] = loc_df['bus_reliable'].min()
        dictionary['locations'][x]['bus_reliable']['max'] = loc_df['bus_reliable'].max()
        dictionary['locations'][x]['bus_reliable']['number'] = loc_df['bus_reliable'].count()

        dictionary['locations'][x]['transport_rating']['mean'] = loc_df['transport_rating'].mean().round(2)
        dictionary['locations'][x]['transport_rating']['median'] = loc_df['transport_rating'].median().round(2)
        dictionary['locations'][x]['transport_rating']['mode'] = loc_df['transport_rating'].mode().round(2).tolist()
        dictionary['locations'][x]['transport_rating']['min'] = loc_df['transport_rating'].min()
        dictionary['locations'][x]['transport_rating']['max'] = loc_df['transport_rating'].max()
        dictionary['locations'][x]['transport_rating']['number'] = loc_df['transport_rating'].count()

        dictionary['locations'][x]['other_transport'] = loc_df['other_transport'].tolist()

        word_series = loc_df['word_transport']
        dictionary['locations'][x]['word_transport']['positive'] = word_series[word_series.isin(['good', 'yummy'])].count()
        dictionary['locations'][x]['word_transport']['negative'] = word_series[word_series.isin(['bad', 'unreliable', 'inconsistent', 'tiring'])].count()
        dictionary['locations'][x]['word_transport']['neutral'] = word_series[word_series.isin(['average', 'idk'])].count()
        dictionary['locations'][x]['word_transport']['transport'] = word_series[word_series.isin(['train', 'bus', 'car', 'walk'])].count()
        dictionary['locations'][x]['word_transport']['crowded'] = word_series[word_series.isin(['crowded', 'loud'])].count()
        dictionary['locations'][x]['word_transport']['other'] = word_series[~word_series.isin(['good', 'yummy', 'bad', 'unreliable', 'inconsistent', 'tiring', 'average', 'idk', 'train', 'bus', 'car', 'walk', 'crowded', 'loud'])].count()

        often_series = loc_df['often_transport']
        dictionary['locations'][x]['often_transport']['number1'] = often_series[often_series == 'Less than 15 minutes'].count()
        dictionary['locations'][x]['often_transport']['number2'] = often_series[often_series == '15 - 30 minutes'].count()
        dictionary['locations'][x]['often_transport']['number3'] = often_series[often_series == '30 - 45 minutes'].count()
        dictionary['locations'][x]['often_transport']['number4'] = often_series[often_series == '45 - 60 minutes'].count()
        dictionary['locations'][x]['often_transport']['number5'] = often_series[often_series == 'More than 60 minutes'].count()

        time_series = loc_df['time_transport']
        dictionary['locations'][x]['time_transport']['number1'] = time_series[time_series == 'Less than 15 minutes'].count()
        dictionary['locations'][x]['time_transport']['number2'] = time_series[time_series == '15 - 30 minutes'].count()
        dictionary['locations'][x]['time_transport']['number3'] = time_series[time_series == '30 - 45 minutes'].count()
        dictionary['locations'][x]['time_transport']['number4'] = time_series[time_series == '45 - 60 minutes'].count()
        dictionary['locations'][x]['time_transport']['number5'] = time_series[time_series == 'More than 60 minutes'].count()


def show_graphs():
    while True:

        graph_locations = ['Central Coast', 'Sydney', 'Other']
        graph_columns = ['train_reliable', 'bus_reliable', 'transport_rating', 'other_transport', 'often_transport', 'time_transport', 'word_transport']

        print("____________________________________________________________")
        print("|                                                          |")
        print("|                   === Select Graph ===                   |")
        print("|                                                          |")
        print("|            1. Graph by single location                   |")
        print("|            2  Graph by two locations                     |")
        print("|            3  Graph by all locations                     |")
        print("|            4. Graph by single column                     |")
        print("|            5. Graph by two columns                       |")
        print("|            6. Exit to main menu                          |")
        print("|__________________________________________________________|")

        graph_choice = input("Please select an option (1-6): ")
        transport_df = pd.read_csv('PublicTransportViewpoint.csv')
        graph_data()

        if graph_choice == '1':
            print(graph_locations)
            single_location = input("Please enter the location you want to view: ")
            if single_location in graph_locations:
                location_graph = transport_df[transport_df["location"] == single_location]
                
                print(graph_columns)
                column = input("Please enter the column you want to graph: ")
                if column in graph_columns:
                    if column in ('train_reliable', 'bus_reliable', 'transport_rating'):
                        counts = location_graph[column].value_counts().sort_index()
                        counts.plot(kind='bar', color='blue', alpha=0.3, title=f'{column} for {single_location}')
                        plt.xlabel(column)
                        plt.ylabel('Count')
                        plt.tight_layout()
                        plt.show()

                    elif column == 'other_transport':
                        counts = location_graph[column]
                        counts = counts[counts != ""].value_counts().sort_index()
                        counts.plot(kind='bar', color='blue', alpha=0.3, title=f'{column} for {single_location}')
                        plt.xlabel(column)
                        plt.ylabel('Count')
                        plt.tight_layout()
                        plt.show()

                    elif column in ('often_transport', 'time_transport'):
                        counts = location_graph[column].value_counts().reindex([
                            'Less than 15 minutes', '15 - 30 minutes', '30 - 45 minutes', '45 - 60 minutes', 'More than 60 minutes'
                        ], fill_value=0)
                        counts.plot(kind='bar', color='blue', alpha=0.3, title=f'{column} for {single_location}')
                        plt.xlabel(column)
                        plt.ylabel('Count')
                        plt.tight_layout()
                        plt.show()

                    elif column == 'word_transport':
                        words = {
                            'positive': location_graph[column][location_graph[column].isin(['good', 'yummy'])].count(),
                            'negative': location_graph[column][location_graph[column].isin(['bad', 'unreliable', 'inconsistent', 'tiring'])].count(),
                            'neutral': location_graph[column][location_graph[column].isin(['average', 'idk'])].count(),
                            'transport': location_graph[column][location_graph[column].isin(['train', 'bus', 'car', 'walk'])].count(),
                            'crowded': location_graph[column][location_graph[column].isin(['crowded', 'loud'])].count(),
                            'other': location_graph[column][~location_graph[column].isin(['good', 'yummy', 'bad', 'unreliable', 'inconsistent', 'tiring', 'average', 'idk', 'train', 'bus', 'car', 'walk', 'crowded', 'loud'])].count()
                        }
                        pd.Series(words).plot(kind='bar', color='blue', alpha=0.3, title=f'{column} for {single_location}')
                        plt.xlabel(column)
                        plt.ylabel('Count')
                        plt.tight_layout()
                        plt.show()

        elif graph_choice == '2':
            print(graph_locations)
            first_location = input("Please enter the first location you want to view: ")
            second_location = input("Please enter the second location you want to view: ")
            if first_location and second_location in graph_locations:
                location_graph = transport_df[transport_df["location"].isin([first_location, second_location])]
                
                print(graph_columns)
                column = input("Please enter the column you want to graph: ")
                if column in graph_columns:
                    if column in ('train_reliable', 'bus_reliable', 'transport_rating'):
                        counts = location_graph.groupby('location')[column].value_counts().unstack(fill_value=0).sort_index()
                        counts.plot(kind='bar', color=['blue', 'orange', 'green', 'red', 'purple', 'brown', 'yellow', 'gray', 'pink', 'lightblue'], alpha=0.3, title=f'{column} for {first_location} and {second_location}')
                        plt.xlabel(column)
                        plt.ylabel('Count')
                        plt.tight_layout()
                        plt.show()

                    elif column == 'other_transport':
                        counts = location_graph[location_graph[column] != ""].groupby('location')[column].value_counts().unstack(fill_value=0).sort_index()
                        counts.plot(kind='bar', color=['blue', 'orange', 'green', 'red', 'purple'], alpha=0.3, title=f'{column} for {first_location} and {second_location}')
                        plt.xlabel(column)
                        plt.ylabel('Count')
                        plt.tight_layout()
                        plt.show()

                    elif column in ('often_transport', 'time_transport'):
                        counts = location_graph.groupby('location')[column].value_counts().unstack(fill_value=0).reindex([
                            'Less than 15 minutes', '15 - 30 minutes', '30 - 45 minutes', '45 - 60 minutes', 'More than 60 minutes'
                        ], axis=1, fill_value=0)
                        counts.plot(kind='bar', color=['blue', 'orange', 'green', 'red', 'purple'], alpha=0.3, title=f'{column} for {first_location} and {second_location}')
                        plt.xlabel(column)
                        plt.ylabel('Count')
                        plt.tight_layout()
                        plt.show()

                    elif column == 'word_transport':
                        words = {
                            'positive': location_graph[location_graph[column].isin(['good', 'yummy'])].groupby('location')[column].count(),
                            'negative': location_graph[location_graph[column].isin(['bad', 'unreliable', 'inconsistent', 'tiring'])].groupby('location')[column].count(),
                            'neutral': location_graph[location_graph[column].isin(['average', 'idk'])].groupby('location')[column].count(),
                            'transport': location_graph[location_graph[column].isin(['train', 'bus', 'car', 'walk'])].groupby('location')[column].count(),
                            'crowded': location_graph[location_graph[column].isin(['crowded', 'loud'])].groupby('location')[column].count(),
                            'other': location_graph[~location_graph[column].isin(['good', 'yummy', 'bad', 'unreliable', 'inconsistent', 'tiring', 'average', 'idk', 'train', 'bus', 'car', 'walk', 'crowded', 'loud'])].groupby('location')[column].count(),
                        }
                        pd.DataFrame(words).plot(kind='bar', color=['blue', 'orange', 'green', 'red', 'purple', 'brown'], alpha=0.3, title=f'{column} for {first_location} and {second_location}')
                        plt.xlabel(column)
                        plt.ylabel('Count')
                        plt.tight_layout()
                        plt.show()

        elif graph_choice == '3':
            print("Graphing all locations together.")
            location_graph = transport_df
                
            print(graph_columns)
            column = input("Please enter the column you want to graph: ")
            if column in graph_columns:
                if column in ('train_reliable', 'bus_reliable', 'transport_rating'):
                    counts = location_graph.groupby('location')[column].value_counts().unstack(fill_value=0).sort_index()
                    counts.plot(kind='bar', color=['blue', 'orange', 'green', 'red', 'purple', 'brown', 'yellow', 'gray', 'pink', 'lightblue'], alpha=0.3, title=f'{column} for all locations')
                    plt.xlabel(column)
                    plt.ylabel('Count')
                    plt.tight_layout()
                    plt.show()

                elif column == 'other_transport':
                    counts = location_graph[location_graph[column] != ""].groupby('location')[column].value_counts().unstack(fill_value=0).sort_index()
                    counts.plot(kind='bar', color=['blue', 'orange', 'green', 'red', 'purple'], alpha=0.3, title=f'{column} for all locations')
                    plt.xlabel(column)
                    plt.ylabel('Count')
                    plt.tight_layout()
                    plt.show()

                elif column in ('often_transport', 'time_transport'):
                    counts = location_graph.groupby('location')[column].value_counts().unstack(fill_value=0).reindex([
                        'Less than 15 minutes', '15 - 30 minutes', '30 - 45 minutes', '45 - 60 minutes', 'More than 60 minutes'
                    ], axis=1, fill_value=0)
                    counts.plot(kind='bar', color=['blue', 'orange', 'green', 'red', 'purple'], alpha=0.3, title=f'{column} for all locations')
                    plt.xlabel(column)
                    plt.ylabel('Count')
                    plt.tight_layout()
                    plt.show()

                elif column == 'word_transport':
                    words = {
                        'positive': location_graph[location_graph[column].isin(['good', 'yummy'])].groupby('location')[column].count(),
                        'negative': location_graph[location_graph[column].isin(['bad', 'unreliable', 'inconsistent', 'tiring'])].groupby('location')[column].count(),
                        'neutral': location_graph[location_graph[column].isin(['average', 'idk'])].groupby('location')[column].count(),
                        'transport': location_graph[location_graph[column].isin(['train', 'bus', 'car', 'walk'])].groupby('location')[column].count(),
                        'crowded': location_graph[location_graph[column].isin(['crowded', 'loud'])].groupby('location')[column].count(),
                        'other': location_graph[~location_graph[column].isin(['good', 'yummy', 'bad', 'unreliable', 'inconsistent', 'tiring', 'average', 'idk', 'train', 'bus', 'car', 'walk', 'crowded', 'loud'])].groupby('location')[column].count(),
                    }
                    pd.DataFrame(words).plot(kind='bar', color=['blue', 'orange', 'green', 'red', 'purple', 'brown'], alpha=0.3, title=f'{column} for all locations')
                    plt.xlabel(column)
                    plt.ylabel('Count')
                    plt.tight_layout()
                    plt.show()

        elif graph_choice == '4':
            print(graph_columns)
            single_column = input("Please enter the column you want to view: ")
            if single_column in graph_columns:
                if single_column == 'train_reliable' or single_column == 'bus_reliable' or single_column == 'transport_rating':
                    counts = transport_df[single_column].value_counts().sort_index()
                    counts.plot(kind='bar', color='blue', alpha=0.3, title=f'{single_column} for all locations')
                    plt.xlabel(single_column)
                    plt.ylabel('Count')
                    plt.tight_layout()
                    plt.show()
                
                elif single_column == 'other_transport':
                    counts = transport_df[transport_df[single_column] != ""][single_column].value_counts().sort_index()
                    counts.plot(kind='bar', color='blue', alpha=0.3, title=f'{single_column} for all locations')
                    plt.xlabel(single_column)
                    plt.ylabel('Count')
                    plt.tight_layout()
                    plt.show()

                elif single_column == 'often_transport' or single_column == 'time_transport':
                    counts = transport_df[single_column].value_counts().reindex([
                        'Less than 15 minutes', '15 - 30 minutes', '30 - 45 minutes', '45 - 60 minutes', 'More than 60 minutes'
                    ], fill_value=0)
                    counts.plot(kind='bar', color='blue', alpha=0.3, title=f'{single_column} for all locations')
                    plt.xlabel(single_column)
                    plt.ylabel('Count')
                    plt.tight_layout()
                    plt.show()

                elif single_column == 'word_transport':
                    words = {
                        'positive': transport_df[transport_df[single_column].isin(['good', 'yummy'])][single_column].count(),
                        'negative': transport_df[transport_df[single_column].isin(['bad', 'unreliable', 'inconsistent', 'tiring'])][single_column].count(),
                        'neutral': transport_df[transport_df[single_column].isin(['average', 'idk'])][single_column].count(),
                        'transport': transport_df[transport_df[single_column].isin(['train', 'bus', 'car', 'walk'])][single_column].count(),
                        'crowded': transport_df[transport_df[single_column].isin(['crowded', 'loud'])][single_column].count(),
                        'other': transport_df[~transport_df[single_column].isin(['good', 'yummy', 'bad', 'unreliable', 'inconsistent', 'tiring', 'average', 'idk', 'train', 'bus', 'car', 'walk', 'crowded', 'loud'])][single_column].count()
                    }
                    pd.Series(words).plot(kind='bar', color='blue', alpha=0.3, title=f'{single_column} for all locations')
                    plt.xlabel(single_column)
                    plt.ylabel('Count')
                    plt.tight_layout()
                    plt.show()

        elif graph_choice == '5':
            while True:
                print("____________________________________________________________")
                print("|                                                          |")
                print("|               === Select Graph (Column) ===              |")
                print("|                                                          |")
                print("|            1. train_reliable & bus_reliable              |")
                print("|            2  train_reliable & transport_rating          |")
                print("|            3  bus_reliable & transport_rating            |")
                print("|            4. often_transport & time_transport           |")
                print("|            5. often_transport & transport_rating         |")
                print("|            6. time_transport & transport_rating          |")
                print("|            7. Exit to main menu                          |")
                print("|__________________________________________________________|")

                column_choice = input("Please select an option (1-7): ")
                if column_choice == '1':
                    transport_df.groupby('location')[['train_reliable', 'bus_reliable']].mean().plot(kind='bar', color=['blue', 'orange', 'green', 'red', 'purple'], alpha=0.3, title='train_reliable & bus_reliable for all locations')
                    plt.xlabel('Location')
                    plt.ylabel('Mean Value')
                    plt.tight_layout()
                    plt.show()

                elif column_choice == '2':
                    transport_df.groupby('location')[['train_reliable', 'transport_rating']].mean().plot(kind='bar', color=['blue', 'orange', 'green', 'red', 'purple'], alpha=0.3, title='train_reliable & transport_rating for all locations')
                    plt.xlabel('Location')
                    plt.ylabel('Mean Value')
                    plt.tight_layout()
                    plt.show()

                elif column_choice == '3':
                    transport_df.groupby('location')[['bus_reliable', 'transport_rating']].mean().plot(kind='bar', color=['blue', 'orange', 'green', 'red', 'purple'], alpha=0.3, title='bus_reliable & transport_rating for all locations')
                    plt.xlabel('Location')
                    plt.ylabel('Mean Value')
                    plt.tight_layout()
                    plt.show()

                elif column_choice == '4':
                    counts = transport_df[['often_transport', 'time_transport']].value_counts().unstack(fill_value=0)
                    counts.plot(kind='bar', color=['blue', 'orange', 'green', 'red', 'purple'], alpha=0.3, title='often_transport & time_transport (Total Counts)')
                    plt.xlabel('often_transport')
                    plt.ylabel('Count')
                    plt.tight_layout()
                    plt.show()

                elif column_choice == '5':
                    counts = transport_df.groupby('often_transport')['transport_rating'].mean()
                    counts.plot(kind='bar', color='blue', alpha=0.3, title='Mean transport_rating by often_transport')
                    plt.xlabel('often_transport')
                    plt.ylabel('Mean Rating')
                    plt.tight_layout()
                    plt.show()

                elif column_choice == '6':
                    counts = transport_df.groupby('time_transport')['transport_rating'].mean()
                    counts.plot(kind='bar', color='blue', alpha=0.3, title='Mean transport_rating by time_transport')
                    plt.xlabel('time_transport')
                    plt.ylabel('Mean Rating')
                    plt.tight_layout()
                    plt.show()

                elif column_choice == '7':
                    print("Returning to main graph menu.")
                    break
                

def search_data():
    while True:
        search_locations = ['Central Coast', 'Sydney', 'Other']
        numbered_search_columns = ['train_reliable', 'bus_reliable', 'transport_rating']
        special_search_columns = ['other_transport', 'word_transport', 'often_transport', 'time_transport']
        numbered_search_values = ['mean', 'median', 'mode', 'min', 'max', 'number']

        print("___________________________________________________________")
        print("|                                                         |")
        print("|                    === Search Data ===                  |")
        print("|                                                         |")
        print("|            1. Search by location                        |")
        print("|            2. Search by column                          |")
        print("|            3. Look up value meanings                    |")
        print("|            4. Return to main menu                       |")
        print("|_________________________________________________________|")

        search_choice = input("Please select an option (1-4): ")
        transport_df = pd.read_csv('PublicTransportViewpoint.csv')

        if search_choice == '1':
            clear_screen()
            print(search_locations)
            location = input("Please enter the location you want to search for: ")
            if location in search_locations:
                clear_screen()
                print(f"Numbered Search Columns: {numbered_search_columns}")
                print(f"Special Search Columns: {special_search_columns}")
                column = input("Please enter the column you want to search for: ")
                if column in numbered_search_columns:
                    clear_screen()
                    print(f"Numbered Search Values: {numbered_search_values}")
                    value = input("Please enter the value you want to search for: ")
                    if value in (numbered_search_values):
                        clear_screen()

                        if value == 'mean':
                            dictionary['locations'][location][column][value] = transport_df[transport_df['location'] == location][column].mean().round(2)
                            print(f"The mean of {column} for {location} is: {dictionary['locations'][location][column][value]}")
                        elif value == 'median':
                            dictionary['locations'][location][column][value] = transport_df[transport_df['location'] == location][column].median().round(2)
                            print(f"The median of {column} for {location} is: {dictionary['locations'][location][column][value]}")
                        elif value == 'mode':
                            dictionary['locations'][location][column][value] = transport_df[transport_df['location'] == location][column].mode().round(2).tolist()
                            print(f"The mode of {column} for {location} is: {dictionary['locations'][location][column][value]}")
                        elif value == 'min':
                            dictionary['locations'][location][column][value] = transport_df[transport_df['location'] == location][column].min()
                            print(f"The minimum of {column} for {location} is: {dictionary['locations'][location][column][value]}")
                        elif value == 'max':
                            dictionary['locations'][location][column][value] = transport_df[transport_df['location'] == location][column].max()
                            print(f"The maximum of {column} for {location} is: {dictionary['locations'][location][column][value]}")
                        elif value == 'number':
                            dictionary['locations'][location][column][value] = transport_df[transport_df['location'] == location][column].count()
                            print(f"The number of entries for {column} for {location} is: {dictionary['locations'][location][column][value]}")


                elif column in special_search_columns and column == 'other_transport':
                    clear_screen()
                    transport_df_other = transport_df['other_transport']
                    search_locations.remove (location)
                    for x in search_locations:
                        transport_df_other = transport_df_other.drop(transport_df[transport_df["location"] == x].index)
                    
                    for y in transport_df_other:
                        if y == "":
                            transport_df_other = transport_df_other.drop(transport_df[transport_df["other_transport"] == y].index)

                    print(transport_df_other)


                elif column in special_search_columns and column == 'word_transport':
                    clear_screen()
                    transport_df_word = transport_df['word_transport']
                    search_locations.remove (location)
                    for x in search_locations:
                        transport_df_word = transport_df_word.drop(transport_df[transport_df["location"] == x].index)
                    words = {
                        'positive': 0,
                        'neutral': 0,
                        'negative': 0,
                        'transport': 0,
                        'crowded': 0,
                        'other': 0
                    }
                    for y in transport_df_word:
                        if y == "bad" or y == "unreliable" or y == "inconsistent" or y == "tiring":
                            words['negative'] += 1
                        elif y == "average" or y == "idk":
                            words['neutral'] += 1
                        elif y == "good" or y == "yummy":
                            words['positive'] += 1
                        elif y == "train" or y == "bus" or y == "car" or y == "walk":
                            words['transport'] += 1
                        elif y == "crowded" or y == "loud":
                            words['crowded'] += 1
                        else:
                            words['other'] += 1       
                    print(words)

                elif column in special_search_columns and column == 'often_transport' or column == 'time_transport':
                    if column == 'often_transport':
                        clear_screen()
                        transport_df_often = transport_df['often_transport']
                        search_locations.remove (location)
                        for x in search_locations:
                            transport_df_often = transport_df_often.drop(transport_df[transport_df["location"] == x].index)
                        
                        print(transport_df_often)
                    
                    elif column in special_search_columns and column == 'time_transport':
                        clear_screen()
                        transport_df_time = transport_df['time_transport']
                        search_locations.remove (location)
                        for x in search_locations:
                            transport_df_time = transport_df_time.drop(transport_df[transport_df["location"] == x].index)
                        
                        print(transport_df_time)
                    
                    print("This column has 5 different times, as you can see above.")

                    dictionary['locations'][location][column]['number1'] = transport_df_often[transport_df_often == 'Less than 15 minutes'].count()
                    dictionary['locations'][location][column]['number2'] = transport_df_often[transport_df_often == '15 - 30 minutes'].count()
                    dictionary['locations'][location][column]['number3'] = transport_df_often[transport_df_often == '30 - 45 minutes'].count()
                    dictionary['locations'][location][column]['number4'] = transport_df_often[transport_df_often == '45 - 60 minutes'].count()
                    dictionary['locations'][location][column]['number5'] = transport_df_often[transport_df_often == 'More than 60 minutes'].count()

                    print(f"The number of entries for 'Less than 15 minutes' for {location} is: {dictionary['locations'][location][column]['number1']}")
                    print(f"The number of entries for '15 - 30 minutes' for {location} is: {dictionary['locations'][location][column]['number2']}")
                    print(f"The number of entries for '30 - 45 minutes' for {location} is: {dictionary['locations'][location][column]['number3']}")
                    print(f"The number of entries for '45 - 60 minutes' for {location} is: {dictionary['locations'][location][column]['number4']}")
                    print(f"The number of entries for 'More than 60 minutes' for {location} is: {dictionary['locations'][location][column]['number5']}")


        elif search_choice == '2':
            clear_screen()
            print(f"Numbered Search Columns: {numbered_search_columns}")
            special_search_columns.remove ('other_transport')
            special_search_columns.remove ('word_transport')
            print(f"Special Search Columns: {special_search_columns}")
            column = input("Please enter the column you want to search for: ")

            if column in numbered_search_columns:
                clear_screen()
                print(f"Numbered Search Values: {numbered_search_values}")
                value = input("Please enter the value you want to search for: ")
                if value in (numbered_search_values):
                    clear_screen()

                    if value == 'mean':
                        dictionary['columns'][column][value] = transport_df[column].mean().round(2)
                        print(f"The mean of {column} is: {dictionary['columns'][column][value]}")
                    elif value == 'median':
                        dictionary['columns'][column][value] = transport_df[column].median().round(2)
                        print(f"The median of {column} is: {dictionary['columns'][column][value]}")
                    elif value == 'mode':
                        dictionary['columns'][column][value] = transport_df[column].mode().round(2).tolist()
                        print(f"The mode of {column} is: {dictionary['columns'][column][value]}")
                    elif value == 'min':
                        dictionary['columns'][column][value] = transport_df[column].min()
                        print(f"The minimum of {column} is: {dictionary['columns'][column][value]}")
                    elif value == 'max':
                        dictionary['columns'][column][value] = transport_df[column].max()
                        print(f"The maximum of {column} is: {dictionary['columns'][column][value]}")
                    elif value == 'number':
                        dictionary['columns'][column][value] = transport_df[column].count()
                        print(f"The number of entries for {column} is: {dictionary['columns'][column][value]}")

            elif column in special_search_columns:
                clear_screen()
                if column == 'often_transport':
                    transport_df_ot = transport_df['often_transport']
                    print(transport_df_ot)

                elif column == 'time_transport':
                    transport_df_ot = transport_df['time_transport']
                    print(transport_df_ot)
                
                print("This column has 5 different times, as you can see above.")

                dictionary['columns'][column]['number1'] = transport_df_ot[transport_df_ot == 'Less than 15 minutes'].count()
                dictionary['columns'][column]['number2'] = transport_df_ot[transport_df_ot == '15 - 30 minutes'].count()
                dictionary['columns'][column]['number3'] = transport_df_ot[transport_df_ot == '30 - 45 minutes'].count()
                dictionary['columns'][column]['number4'] = transport_df_ot[transport_df_ot == '45 - 60 minutes'].count()
                dictionary['columns'][column]['number5'] = transport_df_ot[transport_df_ot == 'More than 60 minutes'].count()

                print(f"The number of entries for 'Less than 15 minutes' is: {dictionary['columns'][column]['number1']}")
                print(f"The number of entries for '15 - 30 minutes' is: {dictionary['columns'][column]['number2']}")
                print(f"The number of entries for '30 - 45 minutes' is: {dictionary['columns'][column]['number3']}")
                print(f"The number of entries for '45 - 60 minutes' is: {dictionary['columns'][column]['number4']}")
                print(f"The number of entries for 'More than 60 minutes' is: {dictionary['columns'][column]['number5']}")

        elif search_choice == '3':
            print("This option will give you some insight into the data and the definitions for the values like the mean.")
            explain_types = ['columns', 'values']
            print(f"The types of explanations you can get are: {explain_types}")
            explanation = input("Please enter what you want to know more about: ")
            if explanation in explain_types and explanation == 'columns':
                print("The columns are the different categories of data that we have collected. They include:")

                print("location: The location of the person who filled out the survey." \
                "")
                print("train_reliable: How reliable the train is on a scale of 1-5, with 1 being very unreliable and 5 being very reliable." \
                "")
                print("bus_reliable: How reliable the bus is on a scale of 1-5, with 1 being very unreliable and 5 being very reliable." \
                "")
                print("other_transport: Any other form of transport that the person uses, such as walking or metro." \
                "")
                print("often_transport: How often the person uses public transport, with options such as 'Less than 15 minutes', '15 - 30 minutes', '30 - 45 minutes', '45 - 60 minutes', and 'More than 60 minutes'." \
                "")
                print("time_transport: How long it takes for the person to get to their destination using public transport, with options that are the same as 'often_transport'." \
                "")
                print("word_transport: A word that the person associates with public transport. It can be any word, but has been categorized into positive, neutral, negative, transport, crowded, and other." \
                "")
                print("transport_rating: A rating of how they feel about public transport on a scale of 1-10, with 1 being very negative and 10 being very positive." \
                "")

                continued = input("Press any key to continue...")

            elif explanation in explain_types and explanation == 'values':
                print("The values are the different types of data that we have collected for each column. They include:" \
                "")
                print("mean: The average value for a column." \
                "")
                print("median: The middle value for a column when the values are arranged in order." \
                "")
                print("mode: The most common value for a column." \
                "")
                print("min: The minimum value for a column."
                      )
                print("max: The maximum value for a column." \
                "")
                print("number: The number of entries for a column." \
                "")

                continued = input("Press any key to continue...")

        elif search_choice == '4':
            print("Returning to main menu.")
            break 


def change_data():



    print("This option will allow you to change the data in the dataset. You can change the values for the columns or the locations.")  
    while True:
        change_locations = ['Central Coast', 'Sydney', 'Other']


        print("____________________________________________________________")
        print("|                                                          |")
        print("|                   === Change Data ===                    |")
        print("|                                                          |")
        print("|            1. Change location data                       |")
        print("|            2. Change column data                         |")
        print("|            3. Change other data                          |")
        print("|            4. Exit to main menu                          |")
        print("|__________________________________________________________|")

        change_choice = input("Please select an option (1-4): ")

        if change_choice == '1':
            print("This option will allow you to change the location data for a specific entry. You can change the location to either Central Coast, Sydney, or Other.")

            change_dataset = pd.read_csv('PublicTransportViewpoint.csv')
            print(change_dataset)

            print(f"Choose a location to change out of: {change_locations}")
            change_location = input("Please enter the location you want to change: ")

            if change_location in change_locations:
                change_locations.remove(change_location)
                for x in change_locations:
                    change_dataset = change_dataset.drop(change_dataset[change_dataset["location"] == x].index)
                
                print(change_dataset)
                index = int(input("Please enter the index of the entry you want to change: "))
                change_dataset.at[index, 'location'] = input("Please enter the new location: ")
                change_dataset.to_csv('PublicTransportViewpoint.csv', index=False)
                print("Location data changed successfully.")

        elif change_choice == '2':
            print("This option will allow you to change the column data for a specific entry. You can change the data for any of the columns, but you must follow the same format as the original data.")

            change_dataset = pd.read_csv('PublicTransportViewpoint.csv')
            print(change_dataset)

            index = int(input("Please enter the index of the entry you want to change: "))
            column = input("Please enter the column you want to change: ")
            new_value = input("Please enter the new value: ")

            if column in change_dataset.columns:
                change_dataset.at[index, column] = new_value
                change_dataset.to_csv('PublicTransportViewpoint.csv', index=False)
                print("Column data changed successfully.")


def save_data():
    transport_df = "PublicTransportViewpoint.csv"
    with open('output.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(transport_df)
        with open('output.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(transport_df)