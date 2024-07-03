import smbus
import time
import math

# MPU6050 registers and addresses
MPU6050_ADDR = 0x68
MPU6050_REG_ACCEL_XOUT_H = 0x3B
MPU6050_REG_ACCEL_YOUT_H = 0x3D
MPU6050_REG_ACCEL_ZOUT_H = 0x3F
MPU6050_REG_TEMP_OUT_H = 0x41
MPU6050_REG_GYRO_XOUT_H = 0x43
MPU6050_REG_GYRO_YOUT_H = 0x45
MPU6050_REG_GYRO_ZOUT_H = 0x47

#Threshold values 
ACCEL_THRESHOLD = 2 
GYRO_THRESHOLD = 2000

# Initialize I2C bus
bus = smbus.SMBus(1)

def read_raw_data(addr):
    high = bus.read_byte_data(MPU6050_ADDR, addr)
    low = bus.read_byte_data(MPU6050_ADDR, addr+1)
    value = (high << 8) + low
    if value > 32767:

        value -= 65536
    return value


try:
    # Variables for calculating speed along X and Y axes
    speed_x = 0.0
    speed_y = 0.0
    last_time = time.time()

    while True:
        # Read accelerometer data for X, Y, and Z axes
        accel_x = read_raw_data(MPU6050_REG_ACCEL_XOUT_H)
        accel_y = read_raw_data(MPU6050_REG_ACCEL_YOUT_H)
        accel_z = read_raw_data(MPU6050_REG_ACCEL_ZOUT_H)

        # Read temperature data
        temp_raw = read_raw_data(MPU6050_REG_TEMP_OUT_H)
        temp_celsius = (temp_raw / 340.0) + 36.53

        # Read gyroscope data for X, Y, and Z axes
        gyro_x = read_raw_data(MPU6050_REG_GYRO_XOUT_H)
        gyro_y = read_raw_data(MPU6050_REG_GYRO_YOUT_H)
        gyro_z = read_raw_data(MPU6050_REG_GYRO_ZOUT_H)

        # Calculate elapsed time since last reading
        current_time = time.time()
        delta_time = current_time - last_time

        # Calculate speed along X and Y axes (assuming one-dimensional motion)
        speed_x += (accel_x / 16384.0 *9.81) * delta_time
        speed_y += (accel_y / 16384.0 *9.81) * delta_time

        # Calculate combined speed using Pythagorean theorem
        speed_combined = math.sqrt(speed_x**2 + speed_y**2)

        # bang detected using acceleration
        magnitude = (accel_x**2 + accel_y**2 + accel_z**2) ** 0.5
        if ( magnitude > ACCEL_THRESHOLD ):    #2^14 == 16384 == 1g 
           # print("Acceleration exceeds 2g on either the X, Y, or Z axis.")
           pass
        
        # bang detected using Gyro data
        if (abs(gyro_x) > GYRO_THRESHOLD or 
            abs(gyro_y) > GYRO_THRESHOLD or 
            abs(gyro_z) > GYRO_THRESHOLD):
            print("Gyroscope exceeds threshold on either the X, Y, or Z axis.")
            
            
        # Print data
        #print("Combined Speed:", speed_combined, "units/time")
       # print("Temperature:", temp_celsius, "C")
        print("Gyroscope X:", gyro_x)
        print("Gyroscope Y:", gyro_y)
        print("Gyroscope Z:", gyro_z)

        # Update last time
        last_time = current_time

        # Wait for some time before reading again
        time.sleep(1)

except KeyboardInterrupt:
    print("Exiting...")
