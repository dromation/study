import pandas as pd
from sklearn.linear_model import LinearRegression

def learn_from_data(unique_data_list):
    """
    Learns from the given data list and stores the trained model

    Args:
        unique_data_list (list): A list of lists containing the unique values and their corresponding indexes

    Returns:
        None
    """

    # Create a DataFrame from the unique data list
    data = pd.DataFrame(unique_data_list)

    # Separate the data into features and target values
    features = data['value']
    target_values = data['index']

    # Create a linear regression model
    model = LinearRegression()

    # Train the model on the data
    model.fit(features, target_values)

    # Save the trained model
    global trained_model
    trained_model = model

def predict_index(value):
    """
    Predicts the index value for a given value

    Args:
        value (str): The value to predict the index for

    Returns:
        int: The predicted index value
    """

    # Check if the trained model exists
    global trained_model
    if not trained_model:
        raise ValueError("Model not trained yet. Call learn_from_data() first.")

    # Convert the value to a NumPy array
    value_array = np.array([value])

    # Predict the index value
    predicted_index = trained_model.predict(value_array)[0]

    return int(predicted_index)


### THIS IS FOR THE MAIN APP
# Call the learn_from_data() function to train the model with the provided data
learn_from_data(unique_data_list)


# Replace "unique_data.csv" with the actual path to your CSV file
unique_data = scrape_table_data("unique_data.csv")
learn_from_data(unique_data)

# Predict the index value for a given value
value = input("Enter a value to predict the index for: ")
predicted_index = predict_index(value)
print("Predicted index for value:", predicted_index)