# MobiAlert 

This program is the implementation of the approach proposed in my master thesis for a embedded system to alert cyclists about critical urban zones on a city.
To compute the risk zones of a city, it is necessary to extract an CSV from an existing GIS database, CityZones software, this one is necessary to go into the folder *Cities* folder. 
This work was developed on a raspberry PI Zero W, being compatible with other Raspberry PI's, as example the **(?)Raspberry PI 3 (?)** and the Raspberry PI Zero W 2.

## MobiAlert modules
The *Mobialert Pre-Processing* folder has a 'main.py' and performs the conversion of the CSV of CityZones, placing the output in the *Cities_grids* folder.
To start the indexing process you simply run the command line: 
`sudo python3 main.py`,
make sure that there are new cities on the *Cities* folder, otherwise the program won't run.

The *realinic.py* starts the operation of the cycling unit. To Start the program you simply run the command: 
`sudo python3 realinic.py`

If you want to start the program automattically then you need to acess: 
  `/etc/rc.local` ,
Isinde the file, scroll to the end of it and write the following command: 
`#sudo python3 'filepath_to_file' &` 
After that, when you power the Rasperry PI it will automatically start the MobiAlert unit.


