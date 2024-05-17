import serial
import time
    
ser = serial.Serial('/dev/ttyAMA0',  9600, timeout=None)
ser.flush()

def cleanstr(in_str):
    """Removes non-numerical characters, only keeps 0123456789.-"""
    out_str = "".join([c for c in in_str if c in "0123456789.-"])
    if len(out_str) == 0:
        out_str = "-1"
    return out_str

def safefloat(in_str):
    """Converts to float. If there is an error, a deafault
    value is returned
    """
    try:
        out_str = float(in_str)
    except ValueError:
        out_str = -1.0
    return out_str

# Convert to decimal degrees
def decimal_degrees(raw_degrees):
    """Converts coordinates to decimal values"""
    try:
        degrees = float(raw_degrees) // 100
        d = float(raw_degrees) % 100 / 60
        return degrees + d
    except: 
        return raw_degrees

class GPS:
    """"Connect to GPS and read its values"""
    
    inp = []
    inp2 = []
    GGA = []
    RMC = []
    values = []
    
    
    def __init__(self):
        """Instantiates an object of the class
        and runs the refresh() method
        """
        self.serialexcept = False
        self.refresh()
        #self.closePort()
    
    def refresh(self):
        """Reads data from the GPS and stores them in
        a global array of the class
        """ 
        self.serialexcept = False         
        try:
            while True:    
                new_data = ser.readline()                 
                GPS.inp = new_data.decode('ISO-8859-1')
                #print(GPS.inp + "\n") # uncomment for debugging
                # GGA data for latitude, longitude, satellites,
                # altitude, and UTC position
                if GPS.inp[0:6] =='$GNGGA': 
                    GPS.GGA = GPS.inp.split(",")
                    #print(GPS.GGA) # uncomment for debugging
                    #print('GNGGA Read')
                    if len(GPS.GGA) >= 10:
                       # print('GGA Found')
                        break
                                       
                #time.sleep(0.1) #needed by the cmd in order not to crash
           
        except serial.SerialException as e:
            #self.refresh()
            #print('is exception, closing port')
            ser.close()
            time.sleep(0.01)
            ser.open()
            GPS.values = [-1.0, -1.0, -1.0, -1.0]  
         
                
        '''
            
            lat = -1.0
            lat_ns = -1.0
            long  = -1.0
            long_ew = -1.0
            GPS.values = [lat, lat_ns, long, long_ew]  
            '''         
        if GPS.GGA[2] == '':  # latitude. Technically a float
            lat =-1.0
        else:
            lat = decimal_degrees(safefloat(cleanstr(GPS.GGA[2])))
            
        if GPS.GGA[3] == '':  # this should be either N or S
            lat_ns = ""
        else:
            lat_ns=str(GPS.GGA[3])
        if lat_ns == "S":
            lat = -lat
                
        if  GPS.GGA[4] == '':  # longitude. Technically a float
            long = -1.0
        else:
            long = decimal_degrees(safefloat(cleanstr(GPS.GGA[4])))
            
        if  GPS.GGA[5] == '': # this should be either W or E
            long_ew = ""
        else:
            long_ew = str(GPS.GGA[5])
        if long_ew == "W":
            long = -long
        if GPS.GGA[7] == '': # number of satellites
            sats = 0


        GPS.values = [lat, lat_ns, long, long_ew, sats]
                 

             
       
    # Accessor methods for all the desired GPS values
    def getLatitude(self):
        """Returns the latitude"""
        return GPS.values[0]

    def getLongitude(self):
        """Returns the longitude"""
        return GPS.values[2]
    
    def getSatellites(self):
        """Returns the number of satellites the GPS is conencted to"""
        return GPS.values[4]
        

