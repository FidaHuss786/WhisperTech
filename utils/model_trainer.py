import pandas as pd
import os
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np

class ModelTrainer:
    def __init__(self, data_dir='data', model_file='models/emg_model.pkl'):
        """Initialize model trainer with data and model paths."""
        self.data_dir = data_dir
        self.model_file = model_file
        os.makedirs(os.path.dirname(model_file), exist_ok=True)
        self.model = None
        self.max_length = 0

    def load_data(self):
        """Load and combine data from all CSV files in data_dir."""
        data_frames = []
        for file in os.listdir(self.data_dir):
            if file.endswith('.csv'):
                label = file.split('.')[0]
                df = pd.read_csv(os.path.join(self.data_dir, file), header=None)
                df['label'] = label
                data_frames.append(df)
        if not data_frames:
            raise ValueError("No data files found in data directory")
        combined_df = pd.concat(data_frames, ignore_index=True)
        self.max_length = combined_df.shape[1] - 2  # Exclude timestamp and label
        return combined_df

    def train(self):
        """Train a Random Forest model on the collected data."""
        df = self.load_data()
        X = df.drop(columns=['label', 0])  # Drop timestamp and label
        y = df['label']

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        self.model = RandomForestClassifier(n_estimators=100, random_state=42)
        self.model.fit(X_train, y_train)

        y_pred = self.model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        print(f"[INFO] Model accuracy: {accuracy * 100:.2f}%")

        joblib.dump(self.model, self.model_file)
        print(f"[INFO] Model saved to {self.model_file}")

    def predict(self, data):
        """Predict the label for a given EMG data sample."""
        if self.model is None:
            if os.path.exists(self.model_file):
                self.model = joblib.load(self.model_file)
            else:
                raise ValueError("No trained model found. Please train the model first.")
        # Pad or truncate data to match training data length
        if len(data) < self.max_length:
            data = data + [0] * (self.max_length - len(data))
        elif len(data) > self.max_length:
            data = data[:self.max_length]
        return self.model.predict([data])[0]