#!/usr/bin/python           # This is server.py file
import time
import Adafruit_ADXL345
import socket               # Import socket module
import subprocess


# Alternatively you can specify the device address and I2C bus with parameters:
#accel = Adafruit_ADXL345.ADXL345(address=0x54, busnum=2)

# You can optionally change the range to one of:
#  - ADXL345_RANGE_2_G   = +/-2G (default)
#  - ADXL345_RANGE_4_G   = +/-4G
#  - ADXL345_RANGE_8_G   = +/-8G
#  - ADXL345_RANGE_16_G  = +/-16G
# For example to set to +/- 16G:
#accel.set_range(Adafruit_ADXL345.ADXL345_RANGE_16_G)

# Or change the data rate to one of:
#  - ADXL345_DATARATE_0_10_HZ = 0.1 hz
#  - ADXL345_DATARATE_0_20_HZ = 0.2 hz
#  - ADXL345_DATARATE_0_39_HZ = 0.39 hz
#  - ADXL345_DATARATE_0_78_HZ = 0.78 hz
#  - ADXL345_DATARATE_1_56_HZ = 1.56 hz
#  - ADXL345_DATARATE_3_13_HZ = 3.13 hz
#  - ADXL345_DATARATE_6_25HZ  = 6.25 hz
#  - ADXL345_DATARATE_12_5_HZ = 12.5 hz
#  - ADXL345_DATARATE_25_HZ   = 25 hz
#  - ADXL345_DATARATE_50_HZ   = 50 hz
#  - ADXL345_DATARATE_100_HZ  = 100 hz (default)
#  - ADXL345_DATARATE_200_HZ  = 200 hz
#  - ADXL345_DATARATE_400_HZ  = 400 hz
#  - ADXL345_DATARATE_800_HZ  = 800 hz
#  - ADXL345_DATARATE_1600_HZ = 1600 hz
#  - ADXL345_DATARATE_3200_HZ = 3200 hz
# For example to set to 6.25 hz:
#accel.set_data_rate(Adafruit_ADXL345.ADXL345_DATARATE_6_25HZ)


accel = Adafruit_ADXL345.ADXL345()
s = socket.socket()         # Create a socket object
host = '0.0.0.0'            # Get local machine name
port = 12345              # Reserve a port for your service.
print 'Server started!'
print 'Waiting for clients...'
print('Printing X, Y, Z axis values, press Ctrl-C to quit...')

s.bind((host, port))        # Bind to the port
s.listen(5)                 # Now wait for client connection.
c, addr = s.accept()        # Establish connection with client.
print 'Got connection from', addr
        
while True:
    try:
        # Create an ADXL345 instance.
        msg = c.recv(1024)
        print addr, ' SERVER >> ', msg
        # Read the X, Y, Z axis acceleration values and print them.
        x, y, z = accel.read()
        # Wait half a second and repeat.
        time.sleep(1)
        msg = 'X={0}, Y={1}, Z={2}'.format(x, y, z)
        c.send(msg);
        #c.close()                # Close the connection

    except:
        print 'No Connection'
        accel = Adafruit_ADXL345.ADXL345()
        s = socket.socket()         # Create a socket object
        host = '0.0.0.0'            # Get local machine name
        port = 12345               # Reserve a port for your service.
        s.bind((host, port))        # Bind to the port
        s.listen(5)                 # Now wait for client connection.
        c, addr = s.accept()        # Establish connection with client.
        print 'Got connection from', addr
    
