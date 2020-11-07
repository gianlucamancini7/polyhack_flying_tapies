#simulating smart lamp
import random

#generate some measurements
def simulate_measurement(measurement_happened, locked=False, unlocked=True):

    if measurement_happened:
        return random.choice([locked, unlocked])
    else:
        return None

#simulate loop
def simulate_actuator_1(id_):

    measurement_happened=random.choice([True, False])
    outcome=simulate_measurement(measurement_happened)

    return outcome, id_


if __name__ == "__main__":
    pass