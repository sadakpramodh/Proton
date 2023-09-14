import pandas as pd

class CSVReader:
    def __init__(self, csv_file_path):
        self.csv_file_path = csv_file_path

    def read_csv(self):
        try:
            df = pd.read_csv(self.csv_file_path)
            return df
        except Exception as e:
            return str(e)  # Handle any exceptions during CSV file reading
