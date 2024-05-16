from Hardware.grove_gps import GPS

global gps

def inicGPS():
    global gps
    
    gps = GPS()
    

def refreshGPS():
    gps.refresh()

def getCoordinates():
    global gps
    return (gps.getLongitude(),gps.getLatitude())
    