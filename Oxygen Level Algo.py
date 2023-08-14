def calculate_oxygen_saturation(red_light_intensity, infrared_light_intensity):
    # Calculate ratio of red and infrared light intensities
    ratio = red_light_intensity / infrared_light_intensity
    
    # Calculate oxygen saturation using empirical formula (SpO2)
    spo2 = -45.060 * ratio**2 + 30.354 * ratio + 94.845
    
    return spo2

# Example usage
red_intensity = 100  # Red light intensity value
infrared_intensity = 200  # Infrared light intensity value
oxygen_saturation = calculate_oxygen_saturation(red_intensity, infrared_intensity)
print(f"Oxygen saturation: {oxygen_saturation:.2f}%")
