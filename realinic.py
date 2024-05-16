from MACyclling.main_first import main_first
from MACyclling.main_second import *
from Hardware.Ledlib import * 
from Hardware.Buzzer import *
import os
import time

led_bar = MY9221(16, 17)
write_led_bar = LedBar_Write(led_bar)  
buzzer = BuzzerHandler(5)

def main():
    global_timer = time.time()   
    print('MobiAlert Started: ')  
    write_led_bar.allLedON()
    print('Entering 1ºinic', time.time()-global_timer)    
    center, grid, city= main_first(write_led_bar)  #(i,j,lon,lat,risk) - (0,1,2,3,4) , grid
    prev_risk = center[4] #1º risk
    print('Ended 1ºinic :', time.time()-global_timer)
    #grid, (i,j), city, isntace
    #returns (i,j),(lon,lat,risk) (0,1), (0,1,2)
    print('Entering 2ºinic:', time.time()-global_timer)
    idxscoord, centercoord = main_second(grid,center[0],center[1],city, write_led_bar) 
    print('Ended 2ºinic:', time.time()-global_timer)
    if centercoord[2] > prev_risk:
        prev_risk = centercoord[2]
        buzzer.playBuzzer()             
    elif centercoord[2] < prev_risk:
        prev_risk = centercoord[2]
     
    while True:
        #grid, (i,j), city, ledbarwrite obj
        #returns (i,j),(lon,lat,risk) (0,1), (0,1,2)
        if  (time.time()-global_timer) % 1 > 0.99:
            print('Entering 2ºinic:', time.time()-global_timer)
            idxscoord, centercoord = main_second(grid,idxscoord[0],idxscoord[1],city,write_led_bar) #(i,j),(lon,lat,risk)
            print('Ended 2ºinic:', time.time()-global_timer)
        
        if centercoord[2] > prev_risk:
            prev_risk = centercoord[2]
            buzzer.playBuzzer()             
        elif centercoord[2] < prev_risk:
            prev_risk = centercoord[2]
            
if __name__ == "__main__": 
    main()