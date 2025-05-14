import serial
import time

class SerialReader:
    def __init__(self, port='COM9', baudrate=9600, timeout=1):
        """Initialize serial connection to Arduino."""
        try:
            self.ser = serial.Serial(port, baudrate, timeout=timeout)
            time.sleep(2)  # Wait for Arduino to initialize
            print(f"[INFO] Connected to {port} at {baudrate} baud")
        except Exception as e:
            print(f"[ERROR] Failed to connect to serial port: {e}")
            self.ser = None

    def read_data(self):
        """Read a single EMG value from the serial port."""
        if self.ser and self.ser.in_waiting:
            try:
                line = self.ser.readline().decode('utf-8').strip()
                return float(line) if line else None
            except (ValueError, UnicodeDecodeError):
                return None
        return None

    def get_latest_data(self, duration=2, sampling_rate=20):
        """Collect EMG data for a specified duration."""
        data = []
        start_time = time.time()
        while time.time() - start_time < duration:
            value = self.read_data()
            if value is not None:
                data.append(value)
            time.sleep(1 / sampling_rate)
        return data

    def close(self):
        """Close the serial connection."""
        if self.ser and self.ser.is_open:
            self.ser.close()
            print("[INFO] Serial connection closed")