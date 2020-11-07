#simulating motion sensor

# relevant imports
import numpy as np
import random


#generate some measurements
def simulate_measurement(measurement_happened, no_motion=False, motion=True):

    if measurement_happened:
        return random.choice([no_motion, motion])
    else:
        return None

#simulate loop
def simulate_sensor_1(id_):

    measurement_happened=random.choice([True, False])
    outcome=simulate_measurement(measurement_happened)

    return id_, outcome


if __name__ == "__main__":
    pass

