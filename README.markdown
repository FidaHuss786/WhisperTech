# EMG Signal Trainer

   A Python-based application to train and classify EMG signals from an Arduino-connected sensor.

   ## Setup
   1. Install dependencies: `pip install pyserial matplotlib numpy pandas scikit-learn joblib`
   2. Upload Arduino code to read EMG sensor data.
   3. Run: `python main.py`

   ## Features
   - Real-time EMG signal plotting
   - Signal smoothing and thresholding
   - Machine learning classification with Random Forest

   ## Directory Structure
   - `main.py`: Main GUI application
   - `utils/`: Helper modules for serial reading, plotting, data saving, and training
   - `data/`: CSV files for training data
   - `models/`: Trained model files