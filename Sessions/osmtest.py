import csv
import simplekml


def csv_to_geojson():
    
    csv_file = '/home/jose/Documentos/GitHub/MobiAlert/Sessions/porto.csv'
    output_kml = "/home/jose/Documentos/GitHub/MobiAlert/Sessions/porto.kml"
    features = []
    kml = simplekml.Kml()
    with open(csv_file, 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        next(reader)
        for row in reader:
            center_lon = float(row[4].replace('(', ''))
            center_lat = float(row[5].replace(')', ''))
            point = kml.newpoint(name="Sample Point", coords=[(center_lon,center_lat)])  # Coordinates are (longitude, latitude)
            print(point)
        kml.save(output_kml)


csv_to_geojson()