import time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
import requests

R2 = 1000
R1 = 14000
alpha = 0.1
nominal_voltage = 55
Nominal_Capacity = 80  # AH
energy = nominal_voltage * Nominal_Capacity

# Initialize global variables
current_integrator = 0
soc_value = 100  # Assuming the battery starts fully charged
current_time = time.time()


def soc(current):
    global current_integrator, soc_value, current_time
    if soc_value >= 100:
        current_integrator = 0
        soc_value = 100
    if current >= 300:
        print('OVER CURRENT')
    current_integrator += current * (time.time() - current_time) / (60 * 60)
    soc_value = (1 - current_integrator / 80) * 100
    current_time = time.time()
    time.sleep(0.000001)
    return soc_value


def main():
    # Create the I2C bus
    i2c = busio.I2C(board.SCL, board.SDA)

    # Create the ADS1115 object
    ads = ADS.ADS1115(i2c)

    # Initialize current measurement
    current_channel = AnalogIn(ads, ADS.P0)
    current_voltage = current_channel.voltage
    current = current_voltage * 0.5 * 300 / 0.075  # Assuming voltage-to-current conversion
    filtered_current = current

    try:
        while True:
            lastcurrent = current

            # Read voltage from channel 0 (P0) and compute current
            ads.gain = 16  # Set gain to 16 (corresponds to +/- 0.256V full-scale range)
            time.sleep(0.1)  # Delay to allow ADC to settle
            current_channel = AnalogIn(ads, ADS.P1)
            current_voltage = abs(current_channel.voltage)
            print("Current.voltage: {:.4f} V".format(current_voltage), end=" ")
            current = current_voltage * 0.5 * 300 / 0.075  # Assuming voltage-to-current conversion
            filtered_current = alpha * current + (1 - alpha) * lastcurrent
            print("Current: {:.2f} A".format(filtered_current), end=" ")

            # Read voltage from channel 1 (P1)
            ads.gain = 1  # Set gain to 1 (corresponds to +/- 4.096V full-scale range)
            time.sleep(0.1)  # Delay to allow ADC to settle
            chan = AnalogIn(ads, ADS.P0)
            voltage = chan.voltage
            battery_voltage = voltage * 63.0296 / 4.096  # Adjust based on resistor divider
            print("Battery Voltage 2: {:.2f} V".format(battery_voltage))
            soc_value = soc(filtered_current)
            remaining_energy = energy * soc_value / 100
            if filtered_current == 0:
                hours = float('inf')  # To handle division by zero
            else:
                hours = remaining_energy / (filtered_current * nominal_voltage)

            # Optionally send data to a server
            data = {
                "voltage": round(battery_voltage, 2),
                "current": round(filtered_current, 2),
                "hours": round(hours, 2),
                "soc": round(soc_value)
            }
            requests.post("http://localhost:5000/api/voltage_current_soc_temp", json=data)

            time.sleep(2)  # Sleep for 2 seconds before next readings

    except KeyboardInterrupt:
        print("Exiting...")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
