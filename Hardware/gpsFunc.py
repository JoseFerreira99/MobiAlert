from Hardware.grove_gps import *

def getgpsValues():
    ser = init_serial()  # Initialize the serial connection
    while True:
        gga_data = read_gps_data(ser)  # Read GPS data
        if gga_data:
            gps_values = get_gps_values(gga_data)  # Parse GPS values
            print(gps_values)
            return gps_values[0], gps_values[2]
              # Exit the loop after successfully obtaining GPS data

