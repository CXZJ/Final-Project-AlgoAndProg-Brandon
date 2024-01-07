import sounddevice as sd
import numpy as np

def calculate_db(data): # calculates decibels
    rms = np.sqrt(np.mean(data**2))
    db = 20 * np.log10(rms + 1e-6)  # Adding a small constant to avoid log(0)
    return db

def get_decibel():
    fs = 22200  # Set the sampling frequency

    recording = sd.rec(1, samplerate=fs, channels=1, dtype='float32') # records audio
    sd.wait()

    decibel_level = calculate_db(recording.flatten())  # Flatten the array
    return decibel_level
