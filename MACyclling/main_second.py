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
    print('2ºinic entered')
    
    gps = GPS()
    lon,lat = gps.getLongitude(), gps.getLatitude()
    print('2Inic, coord:', lon,lat)

    
    if lon != -1.0 and lat !=- 1.0 or lon != 0 and lat != 0: #se tudo ok
        indexes_to_search = create_grid_search(i,j) #crio busca em matriz
        print('2Inic, search ij:', indexes_to_search)
        idxs, coord = search_grid(lon, lat, indexes_to_search, grid, maxdistance) #Procuro na grid com base i,j             
        print('2Inic, center found:', idxs, coord)
        write_led_bar.writeRisk(coord[2]) #Update LedBar
        write_log_file(filepath_sessions,city,coord,lon,lat)
        #i,j, risk = idxs[0],idxs[1], coord[2]
        return idxs, coord #(i,j),(lon,lat,risk)
    
    elif lon == -1.0 or lat == -1.0 or lon == 0 or lat == 0: #Se deu merda
        write_led_bar.gps_not_working()
        gpstimer = time.time() #Ativo o timer para so atualizar de segundo em segundo
        while True:
            if (time.time() - gpstimer) % 2 > 1.99: #fazendo a divisao para resto 0
                print('GPS FUCKED 2ºMAIN', time.time() - gpstimer)
                gps.refresh()
                lon,lat = gps.getLongitude(), gps.getLatitude() 
                print('GPS FUCKED COORD 2ºMAIN', lon,lat)
                if lon != -1.0 and lat != -1.0: #se deu diferente
                    indexes_to_search = create_grid_search(i,j)
                    idxs, coord = search_grid(lon, lat, indexes_to_search, grid, maxdistance) #Procuro na grid com base o Index_I, Index_J, +3,-3, retorna index e coordenada             
                    print('Found Risk Zone', idxs, coord[2])
                    write_led_bar.allLedOFF()
                    write_led_bar.writeRisk(coord[2])
                    write_log_file(filepath_sessions,city,coord,lon,lat)
                    #i,j, risk = idxs[0],idxs[1], coord[2]
                    return idxs, coord #(i,j),(lon,lat,risk)
