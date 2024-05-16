
import os
from calculateClosestCenter import getClosestCenter
from FileHandler import fetch_files_in_folder, read_csv

from Grid.calculateGrid import calculat_quadrant_lists

from FileHandler import*


##### MA-PREPROCESSING FUNCTIONS
def create_final_grid(filepath, filepathgrid): #filepath to folder cities, filepath to folder [i][j] indexes   
    cities = fetch_files_in_folder(filepath)   
    grids = fetch_files_in_folder(filepathgrid)
        
    print('Starting Creation of the GRID:', cities, grids)
    
    if len(cities) != 0 and len(grids) != 0: #Se houver cidades para criar a grid e na pasta grid existirem cidades
        for (city, grid) in zip(cities,grids): #Para cada uma delas 
            if city == grid: #Se já existe a cidade na pasta GRIDS ignoro a criação da mesma
                print('ERROR: Grid already created for city:', city)
                
            elif city != grid: #Verifico se a grid esta criada comparando os nomes (são iguais. formato: "city.csv")
                centerCSV_List = read_csv(os.path.join(filepathgrid,os.path.join(filepath,city)))    #Leio o CSV da cidade
                q1,q2,q3,q4 = calculat_quadrant_lists(centerCSV_List) #Calculo os quadrantes indexados com base no CSV da cidade

                writeQuadrants(q1, os.path.join(filepathgrid,city)) #Escrevo q1-> q4 no ficheiro
                writeQuadrants(q2, os.path.join(filepathgrid,city))
                writeQuadrants(q3, os.path.join(filepathgrid,city))
                writeQuadrants(q4, os.path.join(filepathgrid,city)) 
                    
                grid_list = read_grid_csv(os.path.join(filepathgrid, os.path.join(filepathgrid,city))) #Leio o ficheiro da grid
                
                final_grid = merge_risk_with_grid(centerCSV_List, grid_list) #Junto os riscos às respetivas coordenadas 
                writeFinalGrid(final_grid, os.path.join(filepathgrid,os.path.join(filepathgrid,city)))# atualizo o ficheiro na pasta GRIDS
                print('Grid created:', city)
                
                        
    elif len(cities) != 0 and  len(grids) == 0: #Se houver cidades para indexar e a grid estiver vazia
        for city in cities:
            centerCSV_List = read_csv(os.path.join(filepathgrid,os.path.join(filepath,city)))     #CSV da cidade
            q1,q2,q3,q4 = calculat_quadrant_lists(centerCSV_List) #Calculo dos quadrantes

            writeQuadrants(q1, os.path.join(filepathgrid,city)) #Escrita q1->q4
            writeQuadrants(q2, os.path.join(filepathgrid,city))
            writeQuadrants(q3, os.path.join(filepathgrid,city))
            writeQuadrants(q4, os.path.join(filepathgrid,city))
                        
            grid_list = read_grid_csv(os.path.join(filepathgrid, os.path.join(filepathgrid,city))) #Leio o ficheiro da grid
                    
            final_grid = merge_risk_with_grid(centerCSV_List, grid_list) #Junto os riscos às respetivas coordenadas 
            print('Grid created:', city)
            writeFinalGrid(final_grid, os.path.join(filepathgrid,os.path.join(filepathgrid,city))) # atualizo o ficheiro na pasta GRIDS
            
            #final_grid = read_final_grid_csv(os.path.join(filepathgrid,os.path.join(filepathgrid,city)))
    
    elif len(cities) == 0: #Se não houver cidades ignora
        print('ERROR: No cities to create grid')  
        
        
        
######### MA-CYCLING FUNCTIONS
def get_current_city(filepath,Px,Py,maxdistance):
    
    cities = fetch_files_in_folder(filepath)

    if len(cities) != 0:
            for city in cities:
                centerCSV_List = read_csv(os.path.join(filepath,city))
                center = getClosestCenter(Px, Py, centerCSV_List, maxdistance)
                if  center is not None:
                    current_city = city
                    
                    return current_city
                else: return None 

def merge_risk_with_grid(centerList, grid):
    merged_list = []
    for lon,lat,risk in centerList:
        for i,j,lon1,lat1 in grid:
            if lon == lon1 and lat == lat1:
                merged_list.append((i,j,lon,lat,risk))
    return merged_list





def get_final_grid(city, filepathgrid):
    final_grid = read_final_grid_csv(os.path.join(filepathgrid,city))
    return final_grid    

        
