import csv 
import os
import datetime
import time


def fetch_files_in_folder(filepath): #Função para ver os ficheiros de uma certa pasta
    if os.path.exists(filepath) and os.path.isdir(filepath):
        files = [file for file in os.listdir(filepath) if os.path.isfile(os.path.join(filepath, file))]
  
        return files
    else:
        return []
  
  
    
def get_city_grid(filepath,filename): #Função para apanhar a cidade em questão
    grids = fetch_files_in_folder(filepath)
    if len(grids) != 0:
        for city in grids:
            if city == filename:
                return city
            else:
                return None


def write_log_file_session(filepath, current_city): #Função para escrever no log file o inicio da sessao
    filename = os.path.join(filepath, os.path.join(filepath, current_city)) #Crio um log file com o mesmo nome que o ficheiro retornado pelo cityzones
    current_time = datetime.datetime.now()
    with open(filename, 'a') as file:   #Open file
        file.write('session:')
        file.write(f"{current_time},{current_city}\n")
        
        
def write_log_file(filepath,current_city, center_info,Px,Py): #Função para escrever no log file as informações do centro, escreve centenas a milhares por sessão
    filename =  os.path.join(filepath, os.path.join(filepath,current_city))
    print(filename)
    current_time = datetime.datetime.now()
    current_time_UNIX = int(time.mktime(current_time.timetuple()) * 1000) #Convert timestamp to UNIX 
        
    with open(filename, 'a') as file:   #Open file
        file.write(f"{current_time_UNIX},{center_info},{Px},{Py}\n") #Write TIMESTAMP, LONGITUDE, LATITUDE, CENTER, RISKZONE
        file.flush()



def writeQuadrants(coordinates_list, filepath): #Função para escrever a grid num ficheiro csv
    if len(coordinates_list) !=0:
        with open(filepath, 'a') as file:
            for i, j, lon, lat in coordinates_list:
                file.write(f"{i},{j},{lon},{lat}\n")
                file.flush()

def writeFinalGrid(coordinates_list, filepath): #Função para escrever o risco num ficheiro csv
    if len(coordinates_list) !=0:
        with open(filepath, 'w') as file:
            for i, j, lon, lat ,risk in coordinates_list:
                file.write(f"{i},{j},{lon},{lat},{risk}\n")
                file.flush()



def read_log_file(filepath,current_city): #Função para ler  o ficheiro log de cada sessão [i,j, lon,lat,risk]

    filename =  os.path.join(filepath, os.path.join(filepath,current_city))
    csvList = []
    with open(filename,'r',newline='') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            i = row[0]
            j = row [1]
            lon = row[2] # Fetch Longitude 
            lat = row[3]
            risk = row[4]
            csvList.append((i,j,lon,lat,risk))
    return csvList


def read_final_grid_csv(filepath): #Função para ler a GRID
    csvList = []    
    with open(filepath, 'r', newline='') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            i = row[0]
            j = row [1]
            lon = row[2] # Fetch Longitude 
            lat = row[3]
            risk = row[4]
            csvList.append((i,j,lon,lat,risk))
    return csvList


def read_grid_csv(filepath): #Função para ler a GRRID sem o risco
    csvList = []    
    with open(filepath, 'r', newline='') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            i = row[0]
            j = row [1]
            lon = row[2] 
            lat = row[3]
            csvList.append((i,j,lon,lat))
    return csvList


def read_finalgrid_indexes(file_path): #Função para ler os indexes ?
    data = {}
    
    with open(file_path, 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip header row
        for row in reader:
            indexi, indexj, lon, lat, risk = map(float, row)
            data[(int(indexi), int(indexj))] = (lon, lat, risk)
    return data


def read_csv(filepath):  #Função para ler o Ficheiro CITYZONES
    #Leitura ficheiro CSV, Retorna o centro e a  riskzone em listas diferentes -- CITYZONES
   
    csvList = [] #Center Coordinates and RISK List        
    with open(filepath, 'r', newline='') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            lon = row[0] # Fetch Longitude 
            lat = row[1]
            risk = row[2]                            
            csvList.append((lon, lat, risk))   
    
    return csvList