"""VEX module."""


from collections.abc import Sequence
from importlib.metadata import version
import sys

from .abstract import Device
from .port import Ports
from .brain import Brain, BrainButton, BrainLcd, BrainSound, NoteType
from .bumper_switch_sensor import Bumper
from .color_sensor import ColorHue, Colorsensor
from .distance_sensor import Sonar
from .controller import Controller, ControllerAxis, ControllerButton
from .gyro_sensor import Gyro, GyroCalibrationType
from .motor import (
    BrakeType, DirectionType, Motor, TorqueUnits, TurnType, VelocityUnits
)
from .touch_led import FadeType, Touchled
from .time import TimeUnits, wait
from .units_common import DistanceUnits, RotationUnits

from . import interactive


__all__: Sequence[str] = (
    '__version__',
    'Device',
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
    'LEFT', 'RIGHT',
    'interactive',
)


__version__: str = version(distribution_name='RobotMesh-VEX-PyB-API-Stubs')


# CONSTANTS
# =========
INT29_MAX: int = 0x1FFFFFFF

DEGREES: RotationUnits = RotationUnits.DEG
TURNS: RotationUnits = RotationUnits.REV

PERCENT: VelocityUnits = VelocityUnits.PCT

SECONDS: TimeUnits = TimeUnits.SEC

INCHES: DistanceUnits = DistanceUnits.IN
MM: DistanceUnits = DistanceUnits.MM

FORWARD: DirectionType = DirectionType.FWD
REVERSE: DirectionType = DirectionType.REV

LEFT: TurnType = TurnType.LEFT
RIGHT: TurnType = TurnType.RIGHT


# ALIASES
# =======
sys.sleep = wait
