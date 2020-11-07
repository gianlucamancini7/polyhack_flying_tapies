SENSOR_TY = ['motion', 'proximity', 'noise']
ACTUATOR_TY = []


def is_sensor_ty(s):
    return s in SENSOR_TY


def is_actuator_ty(s):
    return s in ACTUATOR_TY
