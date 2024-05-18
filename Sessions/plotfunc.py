import matplotlib.pyplot as plt
import csv

filepath = '/home/jose/Documentos/GitHub/MobiAlert/Sessions/porto.csv'
filepath_1 = '/home/jose/Documentos/GitHub/MobiAlert/Cities_grids/porto.csv'

# Lists to store lon_center, lat_center, lon_point, and lat_point
lon_center = []
lat_center = []
lon_point = []
lat_point = []
risks = []

lons = []
lats = []
# Read the csv file and extract data
with open(filepath_1, 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # Skip the header
    for row in csv_reader:
        lon = float(row[2])
        lat = float(row[3])
        lons.append(lon)
        lats.append(lat)


with open(filepath, 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # Skip the header
    next(csv_reader)  # Skip the second line
    for row in csv_reader:
    
        center_lon = float(row[1].replace('(', '').replace("'", '').strip())
        center_lat = float(row[2].replace(')', '').replace("'", '').strip())
        risk = float(row[3].replace(')', '').replace("'",'').strip())
        point_lon = float(row[4].strip())
        point_lat = float(row[5].strip())
        
        lon_center.append(center_lon)
        lat_center.append(center_lat)
        lon_point.append(point_lon)
        lat_point.append(point_lat)
        risks.append(risk)


# Plotting with different colors based on risk
plt.figure(figsize=(10, 6))
for i, risk in enumerate(risks):
    if risk == 1.0:
        plt.scatter(lon_center[i], lat_center[i], color='darkgreen', marker='x')
        plt.scatter(lon_point[i], lat_point[i], color='lightgreen', marker='o')
    elif risk == 2.0:
        plt.scatter(lon_center[i], lat_center[i], color='goldenrod', marker='x')
        plt.scatter(lon_point[i], lat_point[i], color='yellow', marker='o')
    elif risk == 3.0:
        plt.scatter(lon_center[i], lat_center[i], color='red', marker='x')
        plt.scatter(lon_point[i], lat_point[i], color='red', marker='o')



plt.plot(lons,lats, color = 'lightgrey')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('Cyclist Trajectory and Respective Centers')
plt.legend(['Risk Zone Center','Cyclist Trajectory'], loc='upper right',  labelcolor='white',facecolor='blue')
plt.grid(True)
plt.show()
