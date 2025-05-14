import csv
import os
from datetime import datetime

class DataSaver:
    def __init__(self, data_dir='data'):
        """Initialize data saver with directory for CSV files."""
        self.data_dir = data_dir
        os.makedirs(self.data_dir, exist_ok=True)

    def save_sample(self, label, data):
        """Save EMG data to a CSV file for the given label."""
        filename = os.path.join(self.data_dir, f"{label}.csv")
        with open(filename, mode='a', newline='') as file:
            writer = csv.writer(file)
            timestamp = datetime.now().isoformat()
            writer.writerow([timestamp] + data)