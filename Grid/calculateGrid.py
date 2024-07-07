from Harvesine import  Harvesine

from Grid.Get1Quadrant import calculate1Q
from Grid.Get2Quadrant import calculate_ref_lists_2Q
from Grid.Get4Quadrant import calculate_ref_lists_4Q
from Grid.Get3Quadrant import calculate_ref_lists_3Q

from calculateClosestCenter import getCenter

from FileHandler import read_finalgrid_indexes
import os
import time


### A LÓGICA DAS .PY DE GETXQUADRANT SÃO IGUAIS. A UNICA COISA QUE MUDA SÃO OS ANGULOS. PARA MELHOR ENTENDIMENTO LER TESE, MAS 
### SE 1Q OS ANGULOS A CONSIDERAR SÃO 90 E 0
### SE 2Q OS ANGULOS A CONSIDERAR SÃO 90 E 190
### SE 3Q OS ANGULOS A CONSIDERAR SÃO -90 E 180
### SE 4Q OS ANGULOS A CONSIDERAR SÃO -90 E 0

### PARA ACHAR O NOVO VERTICE A LOGICA MUDA POIS SÃO VISTOS OS PONTOS QUE NÃO TEM ANGULOS NUMA CERTA DIREÇÃO
### SE 1Q SÃO VISTOS OS PONTOS QUE NÃO TEM VALORES ATRAS (180) E ABAIXO (-90)
### SE 2Q SÃO VISTOS OS PONTOS QUE NÃO TEM VALOROES ATRAS (0) E ABAIXO (-90)
### SE 3Q SÃO VISTOS OS PONTOS QUE NÃO TEM VALORES ATRAS (0) E ACIMA (90)
### SE 4Q SÃO VISTOS OS PONTOS QUE NÃO TEM VALORES ATRAS (90) E ACIMA (90)

### Basicamente vê-se se cada ponto, não tem ângulos na direção do referencial, de forma a achar um novo ponto de referencia


def calculat_quadrant_lists(centerCSV_List): #Criação dos quadrantes
    Lon_Ref, Lat_Ref,_ = centerCSV_List[0]

    first_quadrant = []
    second_quadrant = []
    third_quadrant = []
    fourth_quadrant = []

    grid_1Q = []
    grid_2Q = []
    grid_3Q = []
    grid_4Q = []

    #0 positive  xdir  --> append j positive
    #90 positive ydir --> append i positive
    #-90 negative xdir --> append i negative
    #180 negative ydir --> apend j negative

    for lon, lat, _ in centerCSV_List:
        harvesine = Harvesine(Lon_Ref,Lat_Ref,lon,lat)
        angle = harvesine.harvesine_angle()

        if 0 <= angle <= 90:  first_quadrant.append((lon, lat))     #1ºQ   
        elif 90 < angle <= 180: second_quadrant.append((lon, lat))#2ºQ
        elif  -180 < angle < -90: third_quadrant.append((lon, lat))  #3ºQ  
        elif -90 <= angle < 0: fourth_quadrant.append((lon, lat)) #4ºQ   

    if len(first_quadrant) != 0:
        print('1ºQ:', len(first_quadrant))
        grid_1Q, Index_I, Index_J,ref_list_i, ref_list_j =  calculate1Q(first_quadrant, Lon_Ref, Lat_Ref)    #Calculo 1Q

    
    if len(fourth_quadrant) != 0: 
        print('4ºQ',len(fourth_quadrant))
        grid_4Q, ref_list_i_negative = calculate_ref_lists_4Q(fourth_quadrant,Lon_Ref,Lat_Ref, Index_I)   #Calculo 4Q

    
    if len(second_quadrant) != 0: 
        print('2ºQ:', len(second_quadrant)) 
        grid_2Q, Index_J, ref_list_j_negative = calculate_ref_lists_2Q(second_quadrant, Lon_Ref, Lat_Ref, Index_J,ref_list_i)           #Calculo 2Q  

    
    if len(third_quadrant) != 0: 
        print('3ºQ:',len(third_quadrant))
        grid_3Q = calculate_ref_lists_3Q(third_quadrant,ref_list_i_negative,ref_list_j_negative) #Calculo 1Q

    
    return grid_1Q, grid_2Q, grid_3Q, grid_4Q



def create_grid_search(Index_I, Index_J): #Calculo matriz 3X3 -- DA PARA SER OTIMIZADO PARA EXPANDIR A MATRIZ COM BASE EM TRESHOLDS DE DISTANCIAS 
    indexes_to_search = []

    Index_I = int(Index_I)
    Index_J = int(Index_J)

    indexes_to_search.append((Index_I,Index_J-1))
    indexes_to_search.append((Index_I+1,Index_J-1))
    indexes_to_search.append((Index_I-1,Index_J-1))
    indexes_to_search.append((Index_I-1,Index_J+1))
    indexes_to_search.append((Index_I-1, Index_J))
    
    indexes_to_search.append((Index_I,Index_J))

    indexes_to_search.append((Index_I,Index_J+1))
    indexes_to_search.append((Index_I+1,Index_J))
    indexes_to_search.append((Index_I+1,Index_J+1))
    
    return indexes_to_search

    


def get_grid_to_search(current_city,filepath_grid): #Pego o ficheiro 'city.csv' que é uma GRID, está nas cities_grids

    
    grid = read_finalgrid_indexes(os.path.join(filepath_grid,current_city))
    

    return grid

def search_grid(Px,Py, indexes_to_search, grid ,max_distance): #Porcuro na grrid
    matching_indexes = []

    min_distance =  max_distance + 50
    
    coords_data = None
    indexes_data = None


    for i,j,lon,lat,risk in grid:
        for data in indexes_to_search:
            idxi, idxj = data
            if float(idxi) == float(i) and float(idxj) == float(j): #Se existe
                if float(idxj) not in matching_indexes and float(idxi) not in matching_indexes: # Se ainda não estiver na lsita
                    matching_indexes.append((i,j,lon,lat,risk)) #adiciono
                    break      
            
    for i,j,lon,lat,risk in matching_indexes: # Percorro a lista
        harvesine = Harvesine(Px,Py, lon,lat) #Distancia entre coordenada do GPS e o centro da lista
        distance = harvesine.harvesine_distance()  
        if distance < min_distance:     # Se distancia for menor que a atual
            min_distance = distance
            coords_data = (lon,lat,risk)
            indexes_data = (i,j)
        
                                      
    return indexes_data ,coords_data