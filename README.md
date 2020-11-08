# ASUS Robotics & AI Center Challenge - IoT Software Foundation for a Smart City: polyhack_flying_tapies

## Description
This repository was crafted by Polycraft with love.

The repository showcases the MVP built for the city of Hackwill's centralized API system managing all city's IOT devices control. The centralized system provides the fundation for a Smart City centralized API system which, if needed, can be scaled up effectively using this repository as a baseline. The centralized system has the following characteristics:

- IOT devices communicate with the centralized server through websockets.
- IOT devices' states are saved in system state which is saved in memory.
- Rules are dynamically loaded from a file containing serielized pickle instruction data. Rules support intertemporal relations.
- All actions are performed completely asyncrhonously.
- Dynamic service registration is allowed.

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

In order to generate new pickle files containing new rules the following steps can be completed:
- new rule abstract syntax tree has to be written in ```rules.py```.
- then, run the following and a new data file ```rules_comp.data``` will be created in ```data``` folder.

```
python api/rules.py
```

Finally, to start up a simulation of the IOT devices run in a new terminal window.
```
python devices/sendIt.py data/sensors.json     
```
The simulation will show when the connection between the devices and the server is made and when an instruction to the actuators is given. As better outlined in the following sections, an additional randomized rule ```rules_random_fire.data``` has been implemented for the purpose of showcasing the connection betweent the server and the devices in the simulation.

#### API Features
In this section, further insights into the main features of the codebase are reported below.

1. Sensor Configuration: Each sensor configuration data is stored in ```data/sensors.json``` file. Each device has a serialized ID and a device type. The list of devices are dynamically loaded when the server startups. One extension of the project is giving to all devices, which are not loaded initially, the ability to be loaded subsequently as it can be seen in the ```__init__.py``` file.

2. Dynamic Rule Loading: Rules can be generated using the ```api/rules.py``` utility, which then serializes them to disk, where they
can be stored and then dynamically loaded by the API. Internally, the rules are stored as an AST for a boolean-like logic, which affords great flexibility for rule creation. In this way a system designer can add rules to the system dynamically, without having to deal with the source code directly.

3. Asynchronous System: Since the communication model is completely based on WebSockets, the resulting codebase uses asynchronous practices to be able to achieve the best possible scalability.

4. Dynamic Simulation: We have provided also the tools for creating a simulation of the whole network, which also dynamically loads from the ```data/sensors.json``` file. In this way, testing with more or less system is a breeze. Furthermore, each of the simulation services tries to mimic the real world network as much as possible, for example by each maintaining an individual websocket connection rather than sharing one. This combines the convenience of being able to run the network with a single command with showing the flexibility of the system. 