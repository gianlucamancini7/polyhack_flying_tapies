# simulating motion sensor

# relevant imports

import numpy as np
import random


def simulate_measurement(measurement_happened, no_suspicious_noise=False, suspicious_noise=True):

    if measurement_happened:
        return random.choice([no_suspicious_noise, suspicious_noise])
    else:
        return None

# send the measurement to api


def simulate_sensor_2(id_):

    measurement_happened = random.choice([True, False])
    outcome = simulate_measurement(measurement_happened)

    return outcome, id_


if __name__ == "__main__":
    pass
