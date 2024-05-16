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
    print('1ºinic entered') 
    global_timer = time.time() #Ativo o timer para so atualizar de segundo em segundo  

    gps = GPS()
    
    lon,lat = gps.getLongitude(),gps.getLatitude()
    print('1ºinic, 1ºcoord:' ,lon,lat)
    
    while True:       
       #lon,lat = gps.getLongitude(),gps.getLatitude() 
        #print(round((time.time() - global_timer) % 2, 2))
        if lon == -1.0 or lat == -1.0 or lon == 0 or lat == 0:
            refresh_count = 0
            if (time.time() - global_timer) % 2 > 1.99 and refresh_count == 0:
                print('GPS Cold Start Started:',(time.time()-global_timer))
                gps.refresh()
                lon,lat = gps.getLongitude(),gps.getLatitude()
                print('GPS Cold Start coord',lon,lat)
                print('GPS Cold Start Update::',(time.time()-global_timer))
                refresh_count = 1
                
        elif lon != -1.0 and lat != -1.0 or lon != 0 and lat != 0:
            print('GPS Cold Start Ended::',(time.time()-global_timer))
        
            city = get_current_city(filepath,lon,lat, maxdistance)  
            print('1Inic, city:', city)
            grid = get_final_grid(city, filepath_grid) #Escrevo a final grid no diretório "Cities_grid" com o nome igual ao do ficheiro Cities e dou fetch na mesma
            closest_center = getCenter(lon,lat, grid, maxdistance) #Numa primeira iteração da RPI verifico qual o ponto mais proximo, (lon, lat, risk)
            print(closest_center)
            write_led_bar.writeRisk(closest_center[4]) #Update LedBar
            print('1ºinic exiting', time.time()-global_timer)    
            write_log_file_session(filepath_sessions,city)
            write_log_file(filepath_sessions,city,closest_center,lon,lat)  #Escrevo no ficheiro log unix, cidade (nome do ficheiro), centro(lon,lat,risk), ponto apanhado pelo gps (lon,lat)
            return closest_center, grid,city #(i,j,lon,lat,risk) - (0,1,2,3,4)

    '''
    elif lon == -1.0 or lat == -1.0: #O GPS,  num start a frio precisa de 27.5s para apanhar as primeiras coordenadas        
        write_led_bar.gps_not_working()
        gps_refresh_timer = time.time()
        while True:  
            if (time.time()-gps_refresh_timer)%1.0  >= 0.99:        
                print('refreshing GPS', (time.time()-gps_refresh_timer) % 1.0)
                gps.refresh()
                lon,lat = gps.getLongitude(), gps.getLatitude()
                if lon != -1.0 and lat != -1.0: #se deu diferente
                    city = get_current_city(filepath,lon,lat, maxdistance)  #same de emcima
                    print('1Inic, city:', city)
                    grid = get_final_grid(city, filepath_grid) #Escrevo a final grid no diretório "Cities_grid" com o nome igual ao do ficheiro Cities e dou fetch na mesma
                    closest_center = getCenter(lon,lat, grid, maxdistance) #Numa primeira iteração da RPI verifico qual o ponto mais proximo, (lon, lat, risk)
                    write_led_bar.allLedOFF()
                    write_led_bar.writeRisk(closest_center[4])
                    print('1Inic, center found', closest_center) 
                    write_log_file_session(filepath_sessions,city)
                    write_log_file(filepath_sessions,city,closest_center,lon,lat)  #Escrevo no ficheiro log unix, cidade (nome do ficheiro), centro(lon,lat,risk), ponto apanhado pelo gps (lon,lat)
                    return closest_center, grid,city
    '''