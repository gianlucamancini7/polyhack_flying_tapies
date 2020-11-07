
# Measures distance between beacon and receiver


# relevant imports
import numpy as np
import random


def simulate_measurement(measurement_happened, lower_dist_beacon_receiver=0, upper_dist_beacon_receiver=30):
    # simulate measurements up to 30 meters

    if measurement_happened:
        return random.uniform(lower_dist_beacon_receiver, upper_dist_beacon_receiver)
    else:
        return None


# send the measurement to api
def simulate_sensor_3(id_):

    measurement_happened = random.choice([True, False])
    outcome = simulate_measurement(measurement_happened)

    return outcome, id_


if __name__ == "__main__":
    pass
