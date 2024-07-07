import time

from calculateClosestCenter import calculateMaxDistance, getCenter
from functions import get_current_city,get_final_grid
from FileHandler import write_log_file, write_log_file_session
from Hardware.Ledlib import *
from Hardware.grove_gps import *

filepath = '/home/admin/MobiAlert/Cities' #RPI
filepath_grid = '/home/admin/MobiAlert/Cities_grids' 
filepath_sessions = '/home/admin/MobiAlert/Sessions'

polygon_side = 50
maxdistance = calculateMaxDistance(polygon_side)



def main_first(write_led_bar): 
    
    '''
    Numa primeira iteração é calculado a zona de risco sem uso da grid. 
    
    Retorna - Closest center (i,j,lon,lat,risk), grid(i,j,lon,lat,risk), city ('city'.csv)
    '''
    
    global_timer = time.time() #Ativo o timer para so atualizar de segundo em segundo  
    gps = GPS()
    lon,lat = gps.getLongitude(),gps.getLatitude() #Fetch GPS coordinates

    while True:     

        if lon == -1.0 or lat == -1.0: #Se coordenada é -1.0, quer dizer que o GPS não capturou nenhum dado
            write_led_bar.gps_not_working() #Update no hardware relevante
            refresh_count = 0 #Garantir que só faz uma leiruta do gps
            if (time.time() - global_timer) % 2 > 1.99 and refresh_count == 0: #Caso haja um erro de leitura, aguarda 2 segundos pela nova 
                gps.refresh() #Atualiza o GPS 
                lon,lat = gps.getLongitude(),gps.getLatitude()
                refresh_count = 1
                
        elif lon != -1.0 and lat != -1.0: #Se coordenada é diferente de -1.0 significa que o GPS capturou dados
       
            city = get_current_city(filepath,lon,lat, maxdistance)  #Retorna a nome da cidade, precisa do filepath, das coordenadas do ciclista e da distancia maxima
            grid = get_final_grid(city, filepath_grid) #Retorna a cidade indexada, precisa do ficheiro cityzones e do filepath do ficheiro
            closest_center = getCenter(lon,lat, grid, maxdistance) #retorna o cento mais proximo (i,j,lon,lat,risk), precisa das coordenadas do ciclista, da cidade indexada e da distancia maxima
            #print(closest_center)
            write_led_bar.writeRisk(closest_center[4]) #Update do hardware com o risco
            #print('1ºinic exiting', time.time()-global_timer)    
            write_log_file_session(filepath_sessions,city) #Escrever a sessão no logfile
            write_log_file(filepath_sessions,city,closest_center,lon,lat)  #Escrever informação relevant no log file
            return closest_center, grid,city #Retornar (i,j,lon,lat,risk)

