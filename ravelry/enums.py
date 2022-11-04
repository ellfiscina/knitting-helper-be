from enum import Enum


class FiberTypes(Enum):

    ANIMAL_FIBER = 0
    ANIMAL_DERIVED = 1
    SYNTHETIC = 2
    PLANT_FIBERS = 3


class AvailableAt(Enum):
    UNKNOWN = 0
    LINDE_HOBBY = 1
    HOBBII = 2
