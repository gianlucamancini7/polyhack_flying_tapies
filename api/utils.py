SENSOR_TY = ['motion', 'proximity', 'noise']
ACTUATOR_TY = ['doorlock', 'lamp']
DISCRETE_TY = ['motion', 'noise', 'doorlock']
CONTINOUS_TY = ['lamp', 'proximity']


def is_sensor_ty(s):
    return s in SENSOR_TY


def is_actuator_ty(s):
    return s in ACTUATOR_TY


def is_discrete(s):
    return s in DISCRETE_TY


def is_continous(s):
    return s in CONTINOUS_TY
