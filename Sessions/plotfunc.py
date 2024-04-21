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
with open(filepath, 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # Skip the header
    next(csv_reader)  # Skip the second line
    for row in csv_reader:
        center_lon = float(row[1].replace('(', ''))
        center_lat = float(row[2].replace(')', ''))
        risk = float(row[3].replace(')', ''))
        point_lon = float(row[4])
        point_lat = float(row[5])
        lon_center.append(center_lon)
        lat_center.append(center_lat)
        lon_point.append(point_lon)
        lat_point.append(point_lat)
        risks.append(risk)

with open(filepath_1, 'r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        center_lon = float(row[2])
        center_lat = float(row[3])

        lons.append(center_lon)
        lats.append(center_lat)
        lon_point.append(point_lon)
        lat_point.append(point_lat)


# Plotting with different colors based on risk
plt.figure(figsize=(10, 6))
for i, risk in enumerate(risks):
    if risk == 1.0:
        plt.plot(lon_center[i], lat_center[i], 'gx', color='darkgreen')
        plt.plot(lon_point[i], lat_point[i], 'go',  color='lightgreen')
    elif risk == 2.0:
        plt.plot(lon_center[i], lat_center[i], 'yx', color='goldenrod')
        plt.plot(lon_point[i], lat_point[i], 'yo',  color='yellow')
    elif risk == 3.0:
        plt.plot(lon_center[i], lat_center[i], 'rx', color='red')
        plt.plot(lon_point[i], lat_point[i], 'ro',  color='red')

plt.plot(lons,lats, color = 'lightgrey')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('Cyclist Trajectory and Respective Centers')
plt.legend(['Risk Zone Center','Cyclist Trajectory'], loc='upper right',  labelcolor='white',facecolor='blue')
plt.grid(True)
plt.show()
