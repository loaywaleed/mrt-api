import time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
# R2 = 1000
# R1 = 192000
R2 = 1000
R1 = 14000
def main():
    # Create the I2C bus
    i2c = busio.I2C(board.SCL, board.SDA)
    
    # Create the ADS object
    ads = ADS.ADS1115(i2c)
    
    # Create a single-ended input on channel 0
    chan = AnalogIn(ads, ADS.P0)
    
    # Configure the ADS1115 gain
    # Gain 1 corresponds to a full-scale range of +/- 4.096V
    ads.gain = 16
    
    while True:
        # Read the voltage from the ADS1115
        # voltage = chan.voltage
        voltage = chan.value * 0.256 / 32765
        # print("Voltage: {:.5f} V".format(voltage))      
        # current = voltage/700000
        # print("current: {:.2f} A".format(current))
        battery_voltage = voltage * (R1 + R2) / R2
        print("battery_voltage: {:.2f} V".format(battery_voltage))
        time.sleep(1)

if __name__ == "__main__":
    main()
