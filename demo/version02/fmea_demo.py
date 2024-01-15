import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

import FMEATable
import FMEAIndexer

class FMEALearningApp:

    def __init__(self):
        self.fmea_table = FMEATable(pd.DataFrame('fmea_table.csv'))
        #self.fmea_table = FMEATable.load_from_file("fmea_table.csv")
    def run(self):
        # Launch the FMEA table class
        self.fmea_table.launch()

        # Wait for the button to be pressed
        button_pressed = False
        while not button_pressed:
            if input('Press enter to start learning.') == '':
                button_pressed = True

        # Index the FMEA table
        indexed_fmea_table = FMEAIndexer(self.fmea_table.table, self.fmea_table.index_table).index_fmea_table()

        # Create a new table with predictions
        new_table = pd.DataFrame({"ID": indexed_fmea_table['ID'], "Prediction": self.predict(indexed_fmea_table)})

        # Write predictions to a file
        new_table.to_csv("predictions.csv", index=False)

    def predict(self, fmea_table):
        # Collect data from table
        data = pd.DataFrame({
            'Failure Mode': fmea_table['Failure Mode'],
            'Cause': fmea_table['Cause'],
            'Detection Method': fmea_table['Detection Method'],
        })

        return data
app = FMEALearningApp()

if __name__ == "__main__":
    app.run()