def fuse_data(heart_rate, oxygen_saturation, accelerometer_data, temperature_data):
    # Simple averaging of data
    fused_heart_rate = np.mean(heart_rate)
    fused_oxygen_saturation = np.mean(oxygen_saturation)
    fused_accelerometer_data = np.mean(accelerometer_data, axis=0)
    fused_temperature_data = np.mean(temperature_data)
    
    return fused_heart_rate, fused_oxygen_saturation, fused_accelerometer_data, fused_temperature_data

# Example usage
fused_hr, fused_spo2, fused_accel, fused_temp = fuse_data(heart_rate, oxygen_saturation, accelerometer_data, temperature_data)
print(f"Fused Heart Rate: {fused_hr:.2f} BPM")
print(f"Fused Oxygen Saturation: {fused_spo2:.2f}%")
print(f"Fused Accelerometer Data: {fused_accel}")
print(f"Fused Temperature Data: {fused_temp:.2f}°C")
