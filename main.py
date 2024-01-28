import numpy as np
from PatchSpecs import PatchSpecs
speed_of_light = 299792458

while True:
    try:
        freq_input = int(input("Enter frequency (GHz): "))
        relative_permittivity = int(input("Enter dielectric constant: "))
        dielectric_height = int(input("Enter dielectric height: "))
        center_freq = PatchSpecs(freq_input, relative_permittivity, dielectric_height, speed_of_light)
        freq = center_freq.frequency()
        break
    except ValueError:
        print("Invalid input")

center_freq.width_cal()


