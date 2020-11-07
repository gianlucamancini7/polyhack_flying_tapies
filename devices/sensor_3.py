
#Measures distance between beacon and receiver


#relevant imports 
import numpy as np
import random 


def simulate_measurement(measurement_happened, dist_beacon_receiver):

    if measurement_happened:
        return dist_beacon_receiver
    else:
        return None



#send the measurement to api
def simulate_sensor_2():

    measurement_happened=random.choice([True, False])
    outcome=simulate_measurement(measurement_happened)

    return id, outcome

    
    return



if __name__ == "__main__":
    pass