#!/bin/python3
import time
import Adafruit_ADS1x15

# Constants
GAIN = 1
R1 = 9.5e6
R2 = 7e5

# Create ADS1115 ADC object
adc = Adafruit_ADS1x15.ADS1115()

def main():
    while True:
        try:
            # Read the raw ADC value from channel 0
            voltage = adc.read_adc(0, gain=GAIN)
            voltage = voltage * 0.125 / 32752
            print(voltage)
            # Calculate battery voltage using voltage divider formula
            battery_voltage = voltage * (R1 + R2) / R2
            
            # Print voltage readings
            print("Voltage: {:.2f} V".format(voltage))
            print("Battery Voltage: {:.2f} V".format(battery_voltage))
            
            # Sleep for 1 second
            time.sleep(1)
        
        except KeyboardInterrupt:
            print("\nExiting...")
            break

if __name__ == "__main__":
    main()
