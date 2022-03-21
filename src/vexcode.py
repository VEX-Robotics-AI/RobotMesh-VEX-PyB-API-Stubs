__all__ = [
    'Ports',
    'Brain', 'BrainButton', 'BrainLcd', 'BrainSound', 'NoteType',
    'Bumper',
    'ColorHue', 'Colorsensor',
    'Sonar',
    'Controller', 'ControllerAxis', 'ControllerButton',
    'Gyro', 'GyroCalibrationType',
    'Motor',
    'BrakeType', 'DirectionType', 'TorqueUnits', 'TurnType', 'VelocityUnits',
    'FadeType', 'Touchled',
    'TimeUnits', 'wait',
    'DistanceUnits', 'RotationUnits',
    'DEGREES', 'TURNS',
    'PERCENT',
    'SECONDS',
    'INCHES', 'MM',
    'FORWARD', 'REVERSE',
    'LEFT', 'RIGHT'
]


from vex import (
    Ports,
    Brain, BrainButton, BrainLcd, BrainSound, NoteType,
    Bumper,
    ColorHue, Colorsensor,
    Sonar,
    Controller, ControllerAxis, ControllerButton,
    Gyro, GyroCalibrationType,
    Motor,
    BrakeType, DirectionType, TorqueUnits, TurnType, VelocityUnits,
    FadeType, Touchled,
    TimeUnits, wait,
    DistanceUnits, RotationUnits,
    DEGREES, TURNS,
    PERCENT,
    SECONDS,
    INCHES, MM,
    FORWARD, REVERSE,
    LEFT, RIGHT
)
from drivetrain import Drivetrain


MSEC = TimeUnits.MSEC
SEC = SECONDS


drivetrain = Drivetrain(Motor(Ports.PORT1),
                        Motor(Ports.PORT6, True))


def vr_thread(*args):
    pass