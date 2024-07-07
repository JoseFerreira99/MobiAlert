# Enhancing Cycling Safety in Smart Cities

This is the implementation of a data-driven embedded risk alert system to alert cyclists about critical urban zones on a city. 

This work was developed on a raspberry PI Zero W, being compatible with other Raspberry PI boards. Is exploits data from the CityZones tool available at http://cityzones.fe.up.pt

All codes are written in python 3, using additional libraries.

This implementation is referred as MobiAlert and SafeClying, being the core of both approaches. This is the code to be executed on the bicycle.

## Modules

The *Pre-Processing folder* contains a file named 'main.py' , which converts the CSV extracted from the GIS database, CityZones. This CSV file should be located in the *Cities* folder, and the conversion output is exported to the *Cities_Grids* file.
Before starting the program, it is necessary to ensure that there is at least one 'city.csv' file in either the *Cities* or *Cities_grids* folder on the device being used. Otherwise, the program will enter an infinite loop where nothing happens.

To start the indexing process, one must simply run the command line: 

```
python3 main.py
```

The *realinic.py* starts the operation of the cycling unit. To start the program, one must run the command: 

```
 python3 realinic.py
```

If the program has to be started automattically, during initialization, the Raspberry PI Zero board has to be configured for that. For that, use the following link: 

```
 /etc/rc.local](https://www.samwestby.com/tutorials/rpi-startupscript.html 
  ```

insert the following command line:

```
#sudo python3 'filepath_to_file' &
```

After that, when the Rasperry PI is initiated, it will automatically start the code.

## Hardware

This approach was designed to be implemented within the GrovePi hardware framework.

To initializate the UART Port for the GPS, proper configuration has to be performed. This is a guide for that: (https://sparklers-the-makers.github.io/blog/robotics/use-neo-6m-module-with-raspberry-pi/)

## Dependencies

These libraries have to be previously installed as follows:

Install the pip3 package:

```
sudo apt-get update
sudo apt-get install python3-pip
```

Install required libraries:
```
pip3 install pyserial
pip3 install numpy
pip3 install gpiozero
```

