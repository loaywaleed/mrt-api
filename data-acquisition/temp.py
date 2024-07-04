import time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

# Define the acceptable voltage range for stable readings
MIN_VOLTAGE = 0.6  # Example threshold values
MAX_VOLTAGE = 0.8  # Example threshold values

def main():
    # Create the I2C bus
    i2c = busio.I2C(board.SCL, board.SDA)
    
    # Create the ADS object
    ads = ADS.ADS1115(i2c)
    
    # Create a single-ended input on channel 0
    chan = AnalogIn(ads, ADS.P0)
    
    # Configure the ADS1115 gain
    ads.gain = 1  # Gain of 1 for ±4.096V

    while True:
        # Read the voltage from the ADS1115
        voltage = chan.voltage
        
        # Check if the voltage is within the acceptable range
        if MIN_VOLTAGE <= voltage <= MAX_VOLTAGE:
            # Convert voltage to temperature in Celsius
            temp_celsius = (voltage - 0.5) * 100 + 10
            
            # Print raw ADC value, voltage, and temperature for debugging
            print(f"Raw ADC Value: {chan.value}")
            print(f"Voltage: {voltage:.4f} V")
            print(f"Temperature: {temp_celsius:.2f} °C")
        
        time.sleep(1)

if __name__ == "__main__":
    main()
