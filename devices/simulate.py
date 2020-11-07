#common scripts to simulate devices

#relevant imports
import random

#import actuators and sensors
from actuator_1 import simulate_actuator_1
from actuator_2 import simulate_actuator_2
from sensor_1 import simulate_sensor_1
from sensor_2 import simulate_sensor_2
from sensor_3 import simulate_sensor_3

#import configurations
from configuration import id_1,id_2,id_3,id_4,id_5

import time
#simulate sensor and actuators sending information

async def simulation(websocket, IntervalCommunicationRange=[0, 5]):


    while True:

        #pause for a random interval
        IntervalCommunication=random.uniform(IntervalCommunicationRange)
        time.sleep(IntervalCommunication)

        #simulate sensors
        sensor_1_response, id1=simulate_sensor_1(id_1)
        sensor_2_response, id2=simulate_sensor_2(id_2)
        sensor_3_response, id3=simulate_sensor_3(id_3)

        #simulate actuators
        actuator_1_response, id4 =simulate_actuator_1(id_4)
        actuator_2_response, id5 =simulate_actuator_2(id_5)

        ids=[id1,id2,id3,id4,id5]
        
        measurements={
            id1: sensor_1_response,
            id2: sensor_2_response,
            id3: sensor_3_response,
            id4: actuator_1_response,
            id5: actuator_2_response
            }

        #loop to send shuffled measurements at different time interval

        #shuffle the ids
        random.shuffle(ids)

        for id_ in ids:
            
            #wait for a random interval
            IntervalCommunication=random.uniform(IntervalCommunicationRange)

            response= {
                "id":id_,
                "measurement": measurements[id_]
            }

            await websocket.send(response)