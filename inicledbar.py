from Hardware.Ledlib import *


### Funçaõ criada para script, para ligar a 'led bar' mal a RPI inicie

def main(): 
    led_bar = MY9221(16, 17)
    write_led_bar = LedBar_Write(led_bar) 
    
    write_led_bar.allLedON()
     

if __name__ == "__main__": 
    main()