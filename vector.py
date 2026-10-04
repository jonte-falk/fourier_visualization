import numpy as np

class SpinningVector:

    def __init__(self, magnitude: float, frequency: int):
        self.magnitude = magnitude
        self.frequency = frequency

    def position(self, t: float, base: complex):
        return base + self.magnitude * np.exp(self.frequency * 1j * t)