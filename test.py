from Hardware.grove_gps import *

def main():
    gps = GPS()
    refresh_count = 0
    inic_timer = time.time()

    while True:
        if (time.time() - inic_timer) % 2 > 1.99:
            if refresh_count == 0:
                print('Refresh GPS')
                gps.refresh()
                print(gps.getLongitude(), gps.getLatitude())
                refresh_count = 1
        else:
            refresh_count = 0
                 
        
if __name__ == "__main__":
    main()        