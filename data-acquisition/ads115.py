import time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
import requests

R2 = 1000
R1 = 192000
# R2 = 1000
# R1 = 13000
def main():
    # Create the I2C bus
    i2c = busio.I2C(board.SCL, board.SDA)
    
    # Create the ADS1115 object
    ads = ADS.ADS1115(i2c)
    
    try:
        while True:
            # Read voltage from channel 0 (P0)
            ads.gain = 16  # Set gain to 16 (corresponds to +/- 0.256V full-scale range)
            time.sleep(0.1)  # Delay to allow ADC to settle
            chan = AnalogIn(ads, ADS.P0)
            voltage1 = chan.voltage
            battery_voltage1 = voltage1 * (R1 + R2) / R2
            print("Battery Voltage 1: {:.2f} V".format(battery_voltage1))
            # print("Battery Voltage 1: {:.2f} V".format(battery_voltage1))
            
            # Read voltage from channel 1 (P1)
            ads.gain = 2   # Set gain to 2 (corresponds to +/- 2.048V full-scale range)
            time.sleep(0.1)  # Delay to allow ADC to settle
            chan = AnalogIn(ads, ADS.P1)
            voltage2 = chan.voltage
            battery_voltage2 = voltage2 * (R1 + R2) / R2
            print("Battery Voltage 2: {:.2f} V".format(battery_voltage2))

            data = {
                "voltage": round(battery_voltage1, 2),
                "current": round(battery_voltage2, 2),
                "range": 25,
            }
            requests.post("http://localhost:5000/api/voltage_current_range", json=data)

            
            time.sleep(2)  # Sleep for 2 seconds before next readings
            
    except KeyboardInterrupt:
        print("Exiting...")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
