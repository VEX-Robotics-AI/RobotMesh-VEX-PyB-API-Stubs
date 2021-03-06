"""VEX Distance Sensor."""


from collections.abc import Sequence

from __vex.decor import act, sense

from .abstract import Device
from .port import Ports
from .units_common import DistanceUnits


__all__: Sequence[str] = ('Sonar',)


class Sonar(Device):
    """Sonar (Distance Sensor)."""

    def __init__(self, index: Ports):
        """
        Create new sonar sensor object on the port specified in the parameter.

        Parameters:
        - index: to the brain port.
        """
        self.port: Ports = index

        self.max_distances: dict[DistanceUnits, float] = \
            dict[DistanceUnits, float]()

    @act
    def set_maximum(
            self,
            distance: float,
            distanceUnits: DistanceUnits = DistanceUnits.MM):
        """
        Set the maximum distance (default 2.5m).

        Parameters:
        - distance: maximum distance to be measured in units
        - distanceUnits: a DistanceUnits enum value for the measurement unit.
        """
        self.max_distances[distanceUnits] = distance

    @sense
    def distance(
            self,
            distanceUnits: DistanceUnits = DistanceUnits.MM) -> int:
        """
        Get the value of the sonar sensor.

        Parameters:
        - distanceUnits: The measurement unit for
                         the sonar device, DistanceUnits enum value.

        Returns:
        an integer that represents the unit value specified by the parameter.
        """
