import numpy as np
class PatchSpecs:

    def __init__(self, freq, relative_permittivity, dielectric_height, speed_of_light):
        self.freq = freq
        self.relative_permittivity = relative_permittivity
        self.dielectric_height = dielectric_height
        self.speed_of_light = speed_of_light

    def frequency(self):
        freq_ghz = self.freq * 1000000000
        return freq_ghz

    def width_cal(self):
        numerator = self.speed_of_light
        denominator = (2*self.freq*1000000000)*np.sqrt((self.relative_permittivity+1)/2)
        width = np.divide(numerator,denominator)
        print(width)


