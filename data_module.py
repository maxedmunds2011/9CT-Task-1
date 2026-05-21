import csv
import os
import time
import sys
import pandas as pd   
import matplotlib.pyplot as plt 


def animate_text(text, delay=0.1):
    if isinstance(text, str):
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()  # New line at the end
        return

    if isinstance(text, (list, tuple, set)):
        for item in text:
            sys.stdout.write(str(item))
            sys.stdout.flush()
            time.sleep(delay)
            sys.stdout.write("\n")
        print()
        return

    text_str = str(text)
    for char in text_str:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # New line at the end

    # This is created so in-depth in case of recurring lists or variables


def animate_by_row(lines, delay=0.5):
    """Animates a list of strings, printing one row at a time."""
    for line in lines:
        print(line)
        time.sleep(delay)


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

        menu = [
            "____________________________________________________________",
            "|                                                          |",
            "|                   === Select Table ===                   |",
            "|                                                          |",
            "|            1. Difference between two locations           |",
            "|            2. Difference between two columns             |",
            "|            3. One specific location                      |",
            "|            4. Exit to main menu                          |",
            "|__________________________________________________________|"
        ]
        animate_by_row(menu, delay=0.2)

        table_choice = input("Please select an option (1-4): ")
        transport_df = pd.read_csv('PublicTransportViewpoint.csv')

        if table_choice == '1':
                animate_text(table_locations, delay=0.1)
                first_location = input("Please enter the location you want to view: ")
                second_location = input("Please enter the location you want to compare it to: ")
                if first_location in table_locations and second_location in table_locations:
                    selected_locations = [first_location, second_location]
                    transport_df = transport_df[transport_df["location"].isin(selected_locations)]
                    print(transport_df)

        elif table_choice == '2':
                animate_text(table_columns, delay=0.1)
                first_column = input("Please enter the column you want to view: ")
                second_column = input("Please enter the column you want to compare it to: ")
                # Validate both inputs are valid column names
                if first_column in table_columns and second_column in table_columns:
                    # Select only the two requested columns
                    transport_df_c = transport_df[[first_column, second_column]]
                    print(transport_df_c)
                else:
                    print("One or both column names are invalid. Please choose from:", table_columns)

        elif table_choice == '3':
            animate_text(table_locations, delay=0.1)
            location = input("Please enter the location you want to view: ")
            if location in table_locations:
                transport_df_l = transport_df[transport_df["location"] == location]
                print(transport_df_l)
                
        elif table_choice == '4':
            print("Returning to main menu.")
            break

        else:
            print("Invalid option. Please select a number between 1 and 5.")


def graph_data():
    transport_df = pd.read_csv('PublicTransportViewpoint.csv')
    data_locations = ['Central Coast', 'Sydney', 'Other']
    numerical_columns = ['train_reliable', 'bus_reliable', 'transport_rating']
    numberstring_columns = ['often_transport', 'time_transport']
    for x in data_locations:
        loc_df = transport_df[transport_df['location'] == x]

        for y in numerical_columns:
            dictionary['locations'][x][y]['mean'] = loc_df[y].mean().round(2)
            dictionary['locations'][x][y]['median'] = loc_df[y].median().round(2)
            dictionary['locations'][x][y]['mode'] = loc_df[y].mode().round(2).tolist()
            dictionary['locations'][x][y]['min'] = loc_df[y].min()
            dictionary['locations'][x][y]['max'] = loc_df[y].max()
            dictionary['locations'][x][y]['number'] = loc_df[y].count()

        dictionary['locations'][x]['other_transport'] = loc_df['other_transport'].tolist()

        for y in numberstring_columns:
            series = loc_df[y]
            dictionary['locations'][x][y]['number1'] = series[series == 'Less than 15 minutes'].count()
            dictionary['locations'][x][y]['number2'] = series[series == '15 - 30 minutes'].count()
            dictionary['locations'][x][y]['number3'] = series[series == '30 - 45 minutes'].count()
            dictionary['locations'][x][y]['number4'] = series[series == '45 - 60 minutes'].count()
            dictionary['locations'][x][y]['number5'] = series[series == 'More than 60 minutes'].count()

        word_series = loc_df['word_transport']
        dictionary['locations'][x]['word_transport']['positive'] = word_series[word_series.isin(['good', 'yummy'])].count()
        dictionary['locations'][x]['word_transport']['negative'] = word_series[word_series.isin(['bad', 'unreliable', 'inconsistent', 'tiring'])].count()
        dictionary['locations'][x]['word_transport']['neutral'] = word_series[word_series.isin(['average', 'idk'])].count()
        dictionary['locations'][x]['word_transport']['transport'] = word_series[word_series.isin(['train', 'bus', 'car', 'walk'])].count()
        dictionary['locations'][x]['word_transport']['crowded'] = word_series[word_series.isin(['crowded', 'loud'])].count()
        dictionary['locations'][x]['word_transport']['other'] = word_series[~word_series.isin(['good', 'yummy', 'bad', 'unreliable', 'inconsistent', 'tiring', 'average', 'idk', 'train', 'bus', 'car', 'walk', 'crowded', 'loud'])].count()


def show_graphs():
    while True:

        graph_locations = ['Central Coast', 'Sydney', 'Other']
        graph_columns = ['train_reliable', 'bus_reliable', 'transport_rating', 'other_transport', 'often_transport', 'time_transport', 'word_transport']

        menu = [
            "____________________________________________________________",
            "|                                                          |",
            "|                   === Select Graph ===                   |",
            "|                                                          |",
            "|            1. Graph by single location                   |",
            "|            2  Graph by two locations                     |",
            "|            3  Graph by all locations                     |",
            "|            4. Graph by single column                     |",
            "|            5. Graph by two columns                       |",
            "|            6. Exit to main menu                          |",
            "|__________________________________________________________|"
        ]
        animate_by_row(menu, delay=0.2)

        graph_choice = input("Please select an option (1-6): ")
        transport_df = pd.read_csv('PublicTransportViewpoint.csv')
        graph_data()

        if graph_choice == '1':
            animate_text(graph_locations, delay=0.1)
            single_location = input("Please enter the location you want to view: ")
            if single_location in graph_locations:
                location_graph = transport_df[transport_df["location"] == single_location]
                animate_text(graph_columns, delay=0.1)
                column = input("Please enter the column you want to graph: ")
                if column in graph_columns:
                    if column in ('train_reliable', 'bus_reliable', 'transport_rating'):
                        counts = location_graph[column].value_counts().sort_index()
                        counts.plot(kind='bar', color=['blue', 'red', 'green', 'purple', 'yellow'], alpha=0.3, title=f'{column} for {single_location}')
                        plt.xlabel(column)
                        plt.ylabel('Count')
                        plt.tight_layout()
                        plt.show()

                    elif column == 'other_transport':
                        counts = location_graph[column]
                        counts = counts[counts != ""].value_counts().sort_index()
                        counts.plot(kind='bar', color=['blue', 'red', 'green', 'purple', 'yellow'], alpha=0.3, title=f'{column} for {single_location}')
                        plt.xlabel(column)
                        plt.ylabel('Count')
                        plt.tight_layout()
                        plt.show()

                    elif column in ('often_transport', 'time_transport'):
                        counts = location_graph[column].value_counts().reindex([
                            'Less than 15 minutes', '15 - 30 minutes', '30 - 45 minutes', '45 - 60 minutes', 'More than 60 minutes'
                        ], fill_value=0)
                        counts.plot(kind='bar', color=['blue', 'red', 'green', 'purple', 'yellow'], alpha=0.3, title=f'{column} for {single_location}')
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
                        pd.Series(words).plot(kind='bar', color=['blue', 'red', 'green', 'purple', 'yellow'], alpha=0.3, title=f'{column} for {single_location}')
                        plt.xlabel(column)
                        plt.ylabel('Count')
                        plt.tight_layout()
                        plt.show()

        elif graph_choice == '2':
            animate_text(graph_locations, delay=0.1)
            first_location = input("Please enter the first location you want to view: ")
            second_location = input("Please enter the second location you want to view: ")
            if first_location in graph_locations and second_location in graph_locations:
                location_graph = transport_df[transport_df["location"].isin([first_location, second_location])]

                animate_text(graph_columns, delay=0.1)
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
            animate_text("Graphing all locations together.", delay=0.1)
            location_graph = transport_df
                
            animate_text(graph_columns, delay=0.05)
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
            animate_text(graph_columns, delay=0.1)
            single_column = input("Please enter the column you want to view: ")
            if single_column in graph_columns:
                if single_column == 'train_reliable' or single_column == 'bus_reliable' or single_column == 'transport_rating':
                    counts = transport_df[single_column].value_counts().sort_index()
                    counts.plot(kind='bar', color=['blue', 'red', 'green', 'purple', 'yellow'], alpha=0.3, title=f'{single_column} for all locations')
                    plt.xlabel(single_column)
                    plt.ylabel('Count')
                    plt.tight_layout()
                    plt.show()
                
                elif single_column == 'other_transport':
                    counts = transport_df[transport_df[single_column] != ""][single_column].value_counts().sort_index()
                    counts.plot(kind='bar', color=['blue', 'red', 'green', 'purple', 'yellow'], alpha=0.3, title=f'{single_column} for all locations')
                    plt.xlabel(single_column)
                    plt.ylabel('Count')
                    plt.tight_layout()
                    plt.show()

                elif single_column == 'often_transport' or single_column == 'time_transport':
                    counts = transport_df[single_column].value_counts().reindex([
                        'Less than 15 minutes', '15 - 30 minutes', '30 - 45 minutes', '45 - 60 minutes', 'More than 60 minutes'
                    ], fill_value=0)
                    order = ['Less than 15 minutes', '15 - 30 minutes', '30 - 45 minutes', '45 - 60 minutes', 'More than 60 minutes']
                    counts.plot(kind='bar', color=['blue', 'red', 'green', 'purple', 'yellow'], alpha=0.3, title=f'{single_column} for all locations')
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
                    pd.Series(words).plot(kind='bar', color=['blue', 'red', 'green', 'purple', 'yellow'], alpha=0.3, title=f'{single_column} for all locations')
                    plt.xlabel(single_column)
                    plt.ylabel('Count')
                    plt.tight_layout()
                    plt.show()

        elif graph_choice == '5':
            while True:
                clear_screen()
                menu = [
                    "____________________________________________________________",
                    "|                                                          |",
                    "|               === Select Graph (Column) ===              |",
                    "|                                                          |",
                    "|            1. train_reliable & bus_reliable              |",
                    "|            2  train_reliable & transport_rating          |",
                    "|            3  bus_reliable & transport_rating            |",
                    "|            4. often_transport & time_transport           |",
                    "|            5. often_transport & transport_rating         |",
                    "|            6. time_transport & transport_rating          |",
                    "|            7. Exit to main menu                          |",
                    "|__________________________________________________________|"
                ]

                animate_by_row(menu, delay=0.2)

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

        elif graph_choice == '6':
            print("Returning to main menu.")
            break
                
        else:
            print("Invalid, try again.")


def search_data():
    while True:
        search_locations = ['Central Coast', 'Sydney', 'Other']
        numbered_search_columns = ['train_reliable', 'bus_reliable', 'transport_rating']
        special_search_columns = ['other_transport', 'word_transport', 'often_transport', 'time_transport']
        numbered_search_values = ['mean', 'median', 'mode', 'min', 'max', 'number']

        menu = [
            "___________________________________________________________",
            "|                                                         |",
            "|                    === Search Data ===                  |",
            "|                                                         |",
            "|            1. Search by location                        |",
            "|            2. Search by column                          |",
            "|            3. Look up value meanings                    |",
            "|            4. Return to main menu                       |",
            "|_________________________________________________________|"
        ]
        animate_by_row(menu, delay=0.2)

        search_choice = input("Please select an option (1-4): ")
        transport_df = pd.read_csv('PublicTransportViewpoint.csv')

        if search_choice == '1':
            clear_screen()
            animate_text(search_locations, delay=0.1)
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
                    transport_df_other = transport_df.loc[transport_df['location'] == location, 'other_transport']
                    transport_df_other = transport_df_other[transport_df_other != ""]
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

                elif column in special_search_columns and (column == 'often_transport' or column == 'time_transport'):
                    clear_screen()
                    transport_df_ot = transport_df.loc[transport_df['location'] == location, column]
                    print(transport_df_ot)
                    print("This column has 5 different times, as you can see above.")

                    number_column_data = {
                        'number1': 'Less than 15 minutes',
                        'number2': '15 - 30 minutes',
                        'number3': '30 - 45 minutes',
                        'number4': '45 - 60 minutes',
                        'number5': 'More than 60 minutes'
                    }
                    for x in number_column_data:
                        dictionary['columns'][column][x] = transport_df_ot[transport_df_ot == number_column_data[x]].count()
                        print(f"The number of entries for '{number_column_data[x]}' is: {dictionary['columns'][column][x]}")


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

                number_column_data = {
                    'number1': 'Less than 15 minutes',
                    'number2': '15 - 30 minutes',
                    'number3': '30 - 45 minutes',
                    'number4': '45 - 60 minutes',
                    'number5': 'More than 60 minutes'
                }
                for x in number_column_data:
                    dictionary['columns'][column][x] = transport_df_ot[transport_df_ot == number_column_data[x]].count()
                    print(f"The number of entries for '{number_column_data[x]}' is: {dictionary['columns'][column][x]}")

        elif search_choice == '3':
            animate_text("This option will give you some insight into the data and the definitions for the values like the mean.", delay=0.05)
            explain_types = ['columns', 'values']
            print(f"The types of explanations you can get are: {explain_types}")
            explanation = input("Please enter what you want to know more about: ")
            if explanation in explain_types and explanation == 'columns':
                animate_text("The columns are the different categories of data that we have collected. They include:", delay=0.05)

                info = [
                    "location: The location of the person who filled out the survey.\n",
                    "train_reliable: How reliable the train is on a scale of 1-5, with 1 being very unreliable and 5 being very reliable.\n",
                    "bus_reliable: How reliable the bus is on a scale of 1-5, with 1 being very unreliable and 5 being very reliable.\n",
                    "other_transport: Any other form of transport that the person uses, such as walking or metro.\n",
                    "often_transport: How often the person uses public transport, with options such as 'Less than 15 minutes', '15 - 30 minutes', '30 - 45 minutes', '45 - 60 minutes', and 'More than 60 minutes'.\n",
                    "time_transport: How long it takes for the person to get to their destination using public transport, with options that are the same as 'often_transport'.\n",
                    "word_transport: A word that the person associates with public transport. It can be any word, but has been categorized into positive, neutral, negative, transport, crowded, and other.\n",
                    "transport_rating: A rating of how they feel about public transport on a scale of 1-10, with 1 being very negative and 10 being very positive.\n"
                ]

                animate_by_row(info, delay=0.3)
                
                continued = input("Press any key to continue...")

            elif explanation in explain_types and explanation == 'values':

                info = [
                    "The values are the different types of data that we have collected for each column. They include: \n",
                    "mean: The average value for a column. \n",
                    "median: The middle value for a column when the values are arranged in order. \n",
                    "mode: The most common value for a column. \n",
                    "min: The minimum value for a column. \n",
                    "max: The maximum value for a column. \n",
                    "number: The number of entries for a column. \n"
                ]
                
                animate_by_row(info, delay=0.3)

                continued = input("Press any key to continue...")

        elif search_choice == '4':
            print("Returning to main menu.")
            break 


def change_data():



    animate_text("This option will allow you to change the data in the dataset. You can change the values for the columns or the locations.", delay=0.05)
    while True:
        change_locations = ['Central Coast', 'Sydney', 'Other']

        menu = [
            "____________________________________________________________",
            "|                                                          |",
            "|                   === Change Data ===                    |",
            "|                                                          |",
            "|            1. Change location data                       |",
            "|            2. Change column data                         |",
            "|            3. Exit to main menu                          |",
            "|__________________________________________________________|"
        ]
        animate_by_row(menu, delay=0.2)
        change_choice = input("Please select an option (1-3): ")

        if change_choice == '1':
            animate_text("This option will allow you to change the location data for a specific entry. You can change the location to either Central Coast, Sydney, or Other.", delay=0.05)

            change_dataset = pd.read_csv('PublicTransportViewpoint.csv')
            print(change_dataset)

            print(f"Choose a location to change out of: {change_locations}")
            change_location = input("Please enter the location you want to change: ")

            if change_location in change_locations:
                matching_rows = change_dataset[change_dataset["location"] == change_location]
                if matching_rows.empty:
                    print(f"No rows found for {change_location}.")
                else:
                    print(matching_rows)
                    index = int(input("Please enter the index of the entry you want to change: "))
                    if index in change_dataset.index:
                        new_location = input("Please enter the new location: ")
                        change_dataset.at[index, 'location'] = new_location
                        change_dataset.to_csv('PublicTransportViewpoint.csv', index=False)
                        print("Location data changed successfully.")
                    else:
                        print("Invalid index. No changes were saved.")

        elif change_choice == '2':
            animate_text("This option will allow you to change the column data for a specific entry. You can change the data for any of the columns, but you must follow the same format as the original data.", delay=0.05)

            change_dataset = pd.read_csv('PublicTransportViewpoint.csv')
            print(change_dataset)

            index = int(input("Please enter the index of the entry you want to change: "))
            column = input("Please enter the column you want to change: ")
            new_value = input("Please enter the new value: ")

            if column in change_dataset.columns:
                change_dataset.at[index, column] = new_value
                change_dataset.to_csv('PublicTransportViewpoint.csv', index=False)
                print("Column data changed successfully.")

        elif change_choice == '3':
            print("Returning to main menu.")
            break