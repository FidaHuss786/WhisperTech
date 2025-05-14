import tkinter as tk
from tkinter import simpledialog, messagebox
import threading
import time
from utils.serial_reader import SerialReader
from utils.plotter import RealTimePlotter
from utils.data_saver import DataSaver
from utils.model_trainer import ModelTrainer

class EMGApp:
    def __init__(self, root):
        """Initialize the EMG application GUI."""
        self.root = root
        self.root.title("EMG Signal Trainer")
        self.serial_reader = SerialReader()
        self.data_saver = DataSaver()
        self.model_trainer = ModelTrainer()

        self.label = tk.Label(root, text="Choose an action:")
        self.label.pack(pady=10)

        self.train_button = tk.Button(root, text="Train", command=self.train_interface)
        self.train_button.pack(pady=5)

        self.test_button = tk.Button(root, text="Test", command=self.test_interface)
        self.test_button.pack(pady=5)

    def train_interface(self):
        """Handle the training interface."""
        word = simpledialog.askstring("Train Word", "Enter the word to train (e.g., yes, no):")
        if not word:
            return

        def collect_and_save():
            messagebox.showinfo("Record", f"Get ready to say '{word}' in 3 seconds...")
            time.sleep(3)

            data = self.serial_reader.get_latest_data()

            if len(data) < 10:
                messagebox.showwarning("Warning", "Not enough valid data.")
                return

            self.data_saver.save_sample(word, data)
            messagebox.showinfo("Success", f"Saved {len(data)} samples for '{word}'")

        # Plot in main thread, data collection in background
        plotter = RealTimePlotter(self.serial_reader)
        plotter.start_plot()
        threading.Thread(target=collect_and_save).start()

    def test_interface(self):
        """Handle the testing interface."""
        def collect_and_predict():
            messagebox.showinfo("Record", "Recording signal for prediction in 3 seconds...")
            time.sleep(3)

            data = self.serial_reader.get_latest_data()

            if len(data) < 10:
                messagebox.showwarning("Warning", "Not enough valid data.")
                return

            try:
                self.model_trainer.train()  # Train model with all available data
                prediction = self.model_trainer.predict(data)
                messagebox.showinfo("Prediction", f"Predicted word: {prediction}")
            except Exception as e:
                messagebox.showerror("Error", f"Prediction failed: {str(e)}")

        # Plot in main thread, prediction in background
        plotter = RealTimePlotter(self.serial_reader)
        plotter.start_plot()
        threading.Thread(target=collect_and_predict).start()


if __name__ == "__main__":
    root = tk.Tk()
    app = EMGApp(root)
    root.mainloop()
