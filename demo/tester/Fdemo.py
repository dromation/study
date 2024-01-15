import pandas as pd
from kivymd.app import MDApp
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.label import MDLabel


class MyApp(MDApp):
    def build(self):
        # Read data from CSV file
        data = pd.read_csv("allocated_data.csv")

        # Create a DataTable widget
        dataTable = MDDataTable(
            data=data.to_dict('records'),
            columns=[
                {"text": "Failure Mode", "width": 200},
                {"text": "Cause", "width": 200},
                {"text": "Detection Method", "width": 150},
                {"text": "Severity", "width": 100},
                {"text": "Occurrence", "width": 100},
                {"text": "Detection", "width": 100},
            ],
        )

        # Create a label to display the table title
        table_title = MDLabel(text="Allocated Data")

        # Create a screen layout
        screen = Screen()
        screen.add_widget(table_title)
        screen.add_widget(dataTable)

        return screen


if __name__ == '__main__':
    MyApp().run()