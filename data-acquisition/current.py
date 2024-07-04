import time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

def main():
    # Create the I2C bus
    i2c = busio.I2C(board.SCL, board.SDA)
    
    # Create the ADS object
    ads = ADS.ADS1115(i2c)
    
    # Create a single-ended input on channel 0
    chan = AnalogIn(ads, ADS.P0)  # This initializes channel 0

# 2/3: +/-6.144V
# 1: +/-4.096V
# 2: +/-2.048V
# 4: +/-1.024V
# 8: +/-0.512V
# 16: +/-0.256V

    # Configure the ADS1115 gain
    # Gain 16 corresponds to a full-scale range of +/- 0.256V
    ads.gain = 16
    
    try:
        while True:
            # Read the voltage from the ADS1115
            #current = chan.value
            current = chan.voltage
            current = current * 0.25 * 300 / .075  # Assuming voltage-to-current conversion
            print("Current: {:.2f} A".format(current))
            # print("voltage: {:.2f} v".format(chan.voltage))    
            # print("digital valure: {} res".format(chan.value))    
            time.sleep(3)
    except KeyboardInterrupt:
        print("Exiting...")
    except Exception as e:
        print(f"An error occurred: {e}")
        # Log the error to a file if needed

if __name__ == "__main__":
    main()
