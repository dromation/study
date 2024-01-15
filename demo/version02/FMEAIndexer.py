import pandas as pd

class FMEAIndexer:

    def __init__(self, fmea_table, index_table):
        self.fmea_table = fmea_table
        self.index_table = index_table

    def index_fmea_table(self):
        indexed_fmea_table = []
        for i in range(len(self.fmea_table)):
            for feature in self.index_table['Feature']:
                if feature in self.fmea_table.columns:
                    index_number = self.index_table[self.index_table['Feature'] == feature]['Index'].values[0]
                    indexed_fmea_table.append((self.fmea_table.loc[i, feature], index_number))

        return indexed_fmea_table