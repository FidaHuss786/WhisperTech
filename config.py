# config.py
SERIAL_PORT = "COM9"  # Adjust to your Arduino's COM port
BAUD_RATE = 9600
SAMPLE_DURATION = 2  # Seconds to collect data
SAMPLING_RATE = 20  # Samples per second
WINDOW_SIZE = 5  # Moving average window size
THRESHOLD = 100  # Minimum amplitude for thresholding
DATA_FILE = "data/emg_data.csv"
MODEL_FILE = "models/emg_model.pkl"
PLOT_WINDOW = 100  # Number of samples to display in live plot