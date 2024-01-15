import pandas as pd
import os

def create_output_folder(folder_name):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

def convert_column_to_files(csv_file, output_folder):
    # Read data from CSV file
    data = pd.read_csv(csv_file)

    # Create the output folder
    create_output_folder(output_folder)

    # Iterate through columns and create separate files
    for column_name in data.columns:
        # Create a new DataFrame with index numbers
        column_data = pd.DataFrame({
            'Original_Values': data[column_name],
            'Index_Number': range(1, len(data) + 1)
        })

        # Create output file path
        output_file_path = os.path.join(output_folder, f'{column_name}_output.csv')

        # Save the DataFrame to a CSV file
        column_data.to_csv(output_file_path, index=False)

if __name__ == "__main__":
    # Specify the CSV file and output folder
    csv_file_path = 'your_input_file.csv'  # Replace with your CSV file path
    output_folder_path = 'output_folder'  # Replace with your desired output folder name

    # Convert each column to separate files
    convert_column_to_files(csv_file_path, output_folder_path)
