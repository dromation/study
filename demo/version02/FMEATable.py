import pandas as pd

class FMEATable:

    def __init__(self, table, filename):
        self.table = table
        self.filename = 'fmea_table.csv'
    def get_failure_modes(self):
        return self.table['Failure Mode'].tolist()

    def get_causes(self):
        return self.table['Cause'].tolist()

    def get_detections(self):
        return self.table['Detection Method'].tolist()

    def get_severity_ratings(self):
        return self.table['Severity'].tolist()

    def get_occurrence_ratings(self):
        return self.table['Occurrence'].tolist()

    def get_detection_ratings(self):
        return self.table['Detection'].tolist()

    def get_risk_priority_numbers(self):
        rpn = []
        for i in range(len(self.table)):
            rpn.append(self.table['Occurrence'][i] * self.table['Severity'][i] * self.table['Detection'][i])
        return rpn

    def calculate_risk_priority_number(self, occurrence, severity, detection):
        return occurrence * severity * detection

    def add_row(self, failure_mode, cause, detection_method, severity, occurrence, detection):
        new_row = {
            'Failure Mode': failure_mode,
            'Cause': cause,
            'Detection Method': detection_method,
            'Severity': severity,
            'Occurrence': occurrence,
            'Detection': detection
        }
        self.table = self.table.append(new_row, ignore_index=True)

    def delete_row(self, row_index):
        self.table.drop(self.table.index[row_index], inplace=True)

    def save_to_file(self, filename):
        self.table.to_csv(filename, index=False)

    def load_from_file(self, filename):
        self.table = pd.read_csv(filename)