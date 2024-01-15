import pandas as pd

def scrape_table_data(filename):
    """
    Scrapes data from a CSV table and stores each column to a list

    Args:
        filename (str): The path to the CSV file

    Returns:
        list: A list of lists containing the unique values and their corresponding indexes
    """

    # Read the table data
    table_data = pd.read_csv(filename)

    # Create empty lists to store data
    unique_data_list = []

    # Iterate over each column in the table
    for column in table_data.columns:
        # Convert the column data to a set to remove duplicates
        column_data = set(table_data[column])

        # Assign an index number to each value
        index = 1
        for value in column_data:
            unique_data_list.append((value, index))
            index += 1

    # Convert the list of tuples to a list of lists
    unique_data = []
    for value, index in unique_data_list:
        unique_data.append([value, index])

    return unique_data