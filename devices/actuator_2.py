# simulate smart lamp

import random

# generate some measurements


def simulate_measurement(measurement_happened, lower_bound=0, upper_bound=1):

    if measurement_happened:
        return random.uniform(lower_bound, upper_bound)
    else:
        return None

# simulate loop


def simulate_actuator_2(id_):

    measurement_happened = random.choice([True, False])
    outcome = simulate_measurement(measurement_happened)

    return outcome, id_


if __name__ == "__main__":
    pass
