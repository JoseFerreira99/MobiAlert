from functions import create_final_grid
import time

folderpath_cities = 'C:\\Users\35193\Documents\GitHub\MobiAlert\Cities'
folderpath_grids = 'Users\35193\Documents\GitHub\MobiAlert\Cities_grids'


start = time.time()

create_final_grid(folderpath_cities,folderpath_grids)

end = time.time()
print('MA - Preprocessing time:', end-start)