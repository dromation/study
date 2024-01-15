import pandas as pd
from kivymd.app import MDApp
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen

filename = 'test_fmea.csv'

class MyApp(MDApp):
    def build(self):
        # Read data from CSV file
        data = pd.read_csv("test_fmea.csv")

        # Get column names from the CSV file
        column_names = data.columns.to_list()

        # Create a DataTable widget
        dataTable = MDDataTable(size_hint=(0.9, 0.7),
                                column_data=column_names)

        # Add table data to the DataTable widget
        dataTable.data = data.to_dict('records')

        # Create a label to display the table title
        table_title = MDLabel(text="Allocated Data")

        # Create a screen layout
        screen = MDScreen()
        screen.add_widget(table_title)
        screen.add_widget(dataTable)

        return screen


if __name__ == '__main__':
    MyApp().run()