import numpy as np
from PatchSpecs import PatchSpecs  # Class PatchSpecs

speed_of_light = 299792458  # Speed of light

freq_input = 0  # Center frequency
relative_permittivity = 0  # Antenna dielectric constant
dielectric_height = 0  # Dielectric antenna height

while True:
    try:
        freq_input = float(input("Enter frequency (GHz): "))  # Taking a frequency input
        break
    except ValueError:
        print("Invalid input")

while True:
    try:
        relative_permittivity = float(input("Enter dielectric constant: "))  # Taking relative permittivity input
        break
    except ValueError:
        print("Invalid input")

while True:
    try:
        dielectric_height = float(input("Enter dielectric height: "))  # Taking dielectric height input
        break
    except ValueError:
        print("Invalid input")

mstrip_ant = PatchSpecs(freq_input, relative_permittivity, dielectric_height, speed_of_light)  # Initialize
# class PatchSpecs
mstrip_ant.width_cal()
