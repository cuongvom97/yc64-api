from enum import Enum


class ProductType(str, Enum):
    MEDICINE = "MEDICINE"
    VACCINE = "VACCINE"
    FEED = "FEED"
    RICE = "RICE"
    BRAN = "BRAN"
    CORN = "CORN"
    OTHER = "OTHER"