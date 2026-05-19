# Python Data Analysis

This document gives a rundown of how the system works, for each option at the main menu screen.


## Display Dataset
Displays the entire PublicTransportViewpoint_csv file, then loads the main menu again.


## Show Tables
Gives you four options for table data:

### Difference between two locations
Choose two locations out of Central Coast, Sydney and Other. The unchosen option will be removed from the full table and only the locations selected will be included.

### Difference between two columns
Choose two columns out of the csv file columns. The rest are removed from the full table and only the columns selected (all locations) will be included.

### One specific location
Choose one location out of the three. The table will only include data from that location (but all columns).

### Exit to main menu
Returns the user to the main menu screen.


## Show Graphs
Gives you 6 options for graph data:

### Graph by single location
Choose one location out of the three, then a specific column. The graph will represent only the chosen location's data for the column.

### Graph by two locations
Choose two locations out of the three, then a specific column. The graph will exclude the unchosen column and clearly show the difference between the locations.

### Graph by all locations
All locations have been chosen, choose a specific column, and the graph shows the difference between all three.

### Graph by single column
Choose a column out of the ones avaliable. Depending on the column chosen, a different graph will be created accordingly.

### Graph by two columns
Rather than given full opportunity, a set list of column comparisons are to be chosen from to be visualised as a graph.

### Exit to main menu
Returns the user to the main menu screen.


## Search Data
Gives you 4 options for search data:

### Search by location
A location is chosen out of the three, then a specific column, then a value out of: mean, median, mode, min, max and number

