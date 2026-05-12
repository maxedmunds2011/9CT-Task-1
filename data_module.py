import pandas as pd

def display_dataset():
    dataset = pd.read_csv('PublicTransportViewpoint.csv')
    print(dataset)

display_dataset()