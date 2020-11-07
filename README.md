# ASUS Robotics & AI Center Challenge - IoT Software Foundation for a Smart City: polyhack_flying_tapies

## Description
This repository was crafted by Polycraft with love.

The repository showcases the MVP built for the city of Hackwill's centralized API system managing all city's IOT devices control.
The centralized system has the following characteristics:

- IOT devices communicate with the centralized server through websockets.
- IOT devices' states are saved in system state which is saved in memory.
- Rules are dynamically loaded from a file containing serielized pickle instruction data. Rules support intertemporal relations
- All actions are performed completely asyncrhonously.
- Dynamic service registration is allowed: this means that new IOT devices can register via websocket and be part of the fleet

## Use the MVP
First clone the repository, create a virtual environment and get the requirements 
```
git clone https://github.com/gianlucamancini7/polyhack_flying_tapies.git
cd polyhack_flying_tapies
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```
And you should be good to go!

To start up the server, first load the rules which have been saved in pickle serialized files.
```
python api/__init__.py data/sensors.json data/rules_comp.data 
```

In order to generate a new pickle files containing new rules, first a new rule abstract syntax tree has to be written in ```rules.py```.
Then, run the following and a new data file will be created in ```data``` folder.

```
python api/rules.py
```

Finally, to start up a simulation of the IOT devices run in a new terminal window.
```
python devices/sendIt.py data/sensors.json     
```
