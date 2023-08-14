import numpy as np
from scipy.signal import find_peaks

def calculate_heart_rate(signal, sampling_rate):
    # Apply bandpass filter to isolate heart rate frequency range (0.5 - 3 Hz)
    filtered_signal = bandpass_filter(signal, lowcut=0.5, highcut=3, fs=sampling_rate)
    
    # Find peaks in the filtered signal
    peaks, _ = find_peaks(filtered_signal, height=0.5, distance=sampling_rate*0.5)
    
    # Calculate heart rate based on peak-to-peak intervals
    peak_intervals = np.diff(peaks) / sampling_rate
    heart_rate = 60 / np.mean(peak_intervals)
    
    return heart_rate

# Example usage
sampling_rate = 1000  # Sample rate in Hz
heart_rate = calculate_heart_rate(raw_signal, sampling_rate)
print(f"Heart rate: {heart_rate:.2f} BPM")
