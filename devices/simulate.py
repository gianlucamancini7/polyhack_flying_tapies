#common scripts to simulate devices

from actuator_1 import simulate_actautor_1
from actuator_2 import simulate_actautor_2
from sensor_1 import simulate_sensor_1
from sensor_2 import simulate_sensor_2
from sensor_3 import simulate_sensor_3


#simulate sensor and actuators sending information

def simulation(ReceivedMessage):


    while ReceivedMessage != 'Error':

        simulate_sensor_1
        simulate_sensor_2
        simulate_sensor_3

        simulate_actautor_1
        simulate_actautor_2