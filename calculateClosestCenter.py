from Harvesine import Harvesine
import math
import time

# Função para obter o centro mais próximo dentro de uma distância máxima
def getCenter(Px,Py, grid, max_distance):
    Px = float(Px)
    Py = float(Py) 

    center_List = [] # Lista de centros com longitude, latitude e risco
    distance_List = []  # Lista de distâncias dos centros
  
    for i ,j ,lon ,lat ,risk in grid:
        harvesine = Harvesine(Px,Py, lon, lat) # Inicializa a classe Harvesine para calcular a distância
        distance = harvesine.harvesine_distance()  # Calcula a distância

        if distance < max_distance: # Verifica se a distância é menor que a distância máxima fornecida
            center_List.append((i ,j ,lon ,lat ,risk)) 
            distance_List.append(distance)

    if len(center_List) > 1:   
        distance = min(distance_List) # Obtém a menor distância 
        distance_index = getID(distance_List, distance) # Obtém o índice da menor distância, correspondente ao centro
        center_and_risk = getItem_byID(center_List, distance_index) # Obtém o centro correspondente ao índice da menor distância
        return center_and_risk
            
    elif len(center_List) == 1:                
        closest_center_coord = center_List[0][0], center_List[0][1], center_List[0][2], center_List[0][3], center_List[0][4] # Get centro

        return closest_center_coord 
    

# Função para obter o centro mais próximo a partir de uma lista de centros CSV
def getClosestCenter(Px, Py, centerCSV_List, max_distance): 
    Px = float(Px) # LON
    Py = float(Py) # LAT
           
    center_List = [] # Lista de centros com longitude e latitude
    distance_List = [] # Lista de distâncias dos centros
                  
    for center in centerCSV_List:  
        # Percorro todos os centros e calculo a distancia para cada um deles
        Cx = float(center[0])  # Longitude from CSV
        Cy = float(center[1])  # Latitude from CSV
        
        harvesine = Harvesine(Cx, Cy, Px, Py)   
        distance_meters = harvesine.harvesine_distance()   # Calculo de Todaas as distancias
                 
        if distance_meters < max_distance:   # Se distancia menor que max_distance
            center_List.append(center) 
            distance_List.append(distance_meters)
             
    if len(center_List) > 1:   
        distance = min(distance_List) # Get the minimum distance        
        distance_index = getID(distance_List, distance) # Get the index of the minimum distance, equal to center index                
        center_and_risk = getItem_byID(center_List, distance_index) # Get the center and risk list corresponding to the minimum distance            
            
        closest_center_coord = center_and_risk[0], center_and_risk[1] # Get centro
        #risk = center_and_risk[2] # get risco
    
        return closest_center_coord # Return list with LON, LAT, RISK, DISTANCE    

    elif len(center_List) == 1:                
        closest_center_coord = center_List[0][0], center_List[0][1] # Get centro
        #risk = center_List[0][2] # get risco  

        return closest_center_coord # Return list with LON, LAT, RISK, DISTANCE  

    return None # Return list with LON, LAT, RISK, DISTANCE  


#Get ID from list                             
def getID(list, point):
    return list.index(point)

#Get Item from ID
def getItem_byID(list,index):
    return list.__getitem__(index)
   
#Use Pytagoras to calculate the distance    
def calculateMaxDistance(side):    
    max_side = math.sqrt(2)*side #Teorema de pitagoras para quadrado    
    return max_side