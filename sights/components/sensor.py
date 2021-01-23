import argparse
from dataclasses import dataclass, field
from typing import Callable, List, Any


@dataclass
class Sensor:
    name: str
    description: str
    sensor_class: Any
    config_class: Any
    info: dict = field(init=False)


Sensors = List[Sensor]