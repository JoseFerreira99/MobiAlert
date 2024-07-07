import time
from Hardware.grove_gps import GPS
from calculateClosestCenter import calculateMaxDistance
from FileHandler import write_log_file
from Grid.calculateGrid import create_grid_search, search_grid
from Hardware.Ledlib import *


filepath = '/home/admin/MobiAlert/Cities' #RPI
filepath_grid = '/home/admin/MobiAlert/Cities_grids' 
filepath_sessions = '/home/admin/MobiAlert/Sessions'

polygon_side = 50
maxdistance = calculateMaxDistance(polygon_side)


def main_second(grid,i,j,city,write_led_bar):
    #print('2ºinic entered')
    
    '''
        Numa segunda iteração é calculado a zona de risco com uso da cidade indexada e da busca rapida "search grid". 
    
        Retorna - idxs(i,j), coord (lon,lat,risk)
    '''
    
    
    global_timer = time.time()
    gps = GPS()
    lon,lat = gps.getLongitude(), gps.getLatitude()
    print('2Inic, coord:', lon,lat)

    while True:
        if lon == -1.0 or lat == -1.0: #Se coordenada é -1.0, quer dizer que o GPS não capturou nenhum dado
            write_led_bar.gps_not_working() #Update no hardware relevante
            refresh_count = 0

            if (time.time() - global_timer) % 2 > 1.99 and refresh_count == 0:  #Caso haja um erro de leitura, aguarda 2 segundos pela nova
                gps.refresh()
                lon,lat = gps.getLongitude(), gps.getLatitude()  
                refresh_count = 1
                    
        elif lon != -1.0 and lat !=- 1.0: #Se coordenada é diferente de -1.0 significa que o GPS capturou dados
            indexes_to_search = create_grid_search(i,j)  #Retorna a nome da cidade, precisa do filepath, das coordenadas do ciclista e da distancia maxim
            idxs, coord = search_grid(lon, lat, indexes_to_search, grid, maxdistance) #Retorna a cidade indexada, precisa do ficheiro cityzones e do filepath do ficheiro             
            write_led_bar.writeRisk(coord[2]) #Update LedBar
            write_log_file(filepath_sessions,city,coord,lon,lat)
            return idxs, coord #(i,j),(lon,lat,risk)
        
        
