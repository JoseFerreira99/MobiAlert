# MobiAlert 

This program is the implementation of the approach proposed in my master thesis for a embedded system to alert cyclists about critical urban zones on a city. 
This work was developed on a raspberry PI Zero W, being compatible with other Raspberry PI's, as example the **(?)Raspberry PI 3 (?)** and the Raspberry PI Zero W 2.

## MobiAlert modules

The *Mobialert Pre-Processing folder* contains a file named 'main.py' , which converts the CSV extracted from the GIS database, CityZones. This CSV file should be located in the *Cities* folder, and the conversion output is exported to the *Cities_Grids* file.
Before starting the program, it is necessary to ensure that there is at least one 'city.csv' file in either the *Cities* or *Cities_grids* folder on the device being used. Otherwise, the program will enter an infinite loop where nothing happens

To start the indexing process you simply run the command line: 

`sudo python3 main.py`,

make sure that there are new cities on the *Cities* folder, otherwise the program won't run.

The *realinic.py* starts the operation of the cycling unit. To Start the program you simply run the command: 

`sudo python3 realinic.py`

If you want to start the program automattically, then on the Raspberry PI Zero W you need to acess: 

  `/etc/rc.local` 
  
Once inside the file, scroll to the end of it and write the following command: 

`#sudo python3 'filepath_to_file' &` 

After that, when you power the Rasperry PI it will automatically start the MobiAlert unit.


