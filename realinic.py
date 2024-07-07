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
    write_led_bar.allLedON() #Write ALL LED on the LED bar to indicate the program has started
    
    ''' 
        Função main_first: realiza o primeiro processamento de risco da unidade MobiAlert;
        Entrada: Objeto da barra de LED;
        Retorna: (i, j, lon, lat, risk), grid, cityname.csv.
    '''
    center, grid, city= main_first(write_led_bar) 

    prev_risk = center[4]  #Fetch the first risk of the cycling session
    
    '''
        Função main_second: realiza o segundo processamento de risco da unidade MobiAlert;
        Entrada: 'city.csv', i, j, city, objeto da barra de LED;
        Retorna: (i, j), (lon, lat, risk).
    '''
    
    idxscoord, centercoord = main_second(grid,center[0],center[1],city, write_led_bar) #   
    
    
    if centercoord[2] > prev_risk: #Comapração de risco para ativar buzzer, Se  risco > risco anterior, ativa buzzer
        prev_risk = centercoord[2] 
        buzzer.playBuzzer()             
    elif centercoord[2] < prev_risk: # Se não, simplesmente atualiza o risco anterior
        prev_risk = centercoord[2]
     
    while True:     #Loop do MA-CYcling
        '''
            Função main_second: realiza o segundo processamento de risco da unidade MobiAlert;
            Entrada: 'city.csv', i, j, city, objeto da barra de LED;
            Retorna: (i, j), (lon, lat, risk).
        '''

        if  (time.time()-global_timer) % 1 > 0.99: #Condição para correr de segundo em segundo 
            idxscoord, centercoord = main_second(grid,idxscoord[0],idxscoord[1],city,write_led_bar) 
        
        if centercoord[2] > prev_risk: #Comapração de risco para ativar buzzer, Se  risco > risco anterior, ativa buzzer
            prev_risk = centercoord[2]
            buzzer.playBuzzer()             
        elif centercoord[2] < prev_risk:# Se não, simplesmente atualiza o risco anterior
            prev_risk = centercoord[2]
            
if __name__ == "__main__": 
    main()