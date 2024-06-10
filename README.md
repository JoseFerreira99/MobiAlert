# MobiAlert 

This program is the implementation of the approach proposed in my master thesis for a embedded system to alert cyclists about critical urban zones on a city.
To compute the risk zones of a city, it is necessary to extract an CSV from an existing GIS database, CityZones software, this one is necessary to go into the folder **"Cities"** folder. 

## MobiAlert modules
The **Mobialert Pre-Processing** folder has a *main.py* and performs the conversion of the CSV of CityZones, placing the output in the **"Cities_grids"** folder

The *realinic* starts the operation of the cycling unit. To Start the program you simply run the command:


`python3 realinic.py`

\```
<span style="background-color: #333; color: white; padding: 2px;">python3</span> realinic.py
\```
