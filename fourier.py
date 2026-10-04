import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
from scipy.interpolate import interp1d
from parametrize import parametrize

OFFSET = 0
PERIOD = 1 - OFFSET
OMEGA = (2 * np.pi) / PERIOD

def square_function(x):
    t = ((x - OFFSET) % PERIOD) + OFFSET
    return np.where((OFFSET <= t) & (t < OFFSET + PERIOD / 2), 1, -1)

# def c_k(k: int):
#     integrand = lambda x: square_function(x) * np.exp(-1j * k * OMEGA * x)
#     real_value, _ = quad(lambda x: np.real(integrand(x)), OFFSET, PERIOD)
#     imag_value, _ = quad(lambda x: np.imag(integrand(x)), OFFSET, PERIOD)
#     return (real_value + 1j * imag_value) / PERIOD

def make_continuous():
    x, y = parametrize("F_outline.jpg")
    z = x + 1j * y
    t = np.linspace(OFFSET, PERIOD, len(z))
    f = interp1d(t, z, kind="cubic", fill_value="extrapolate")
    return f

def c_k(k: int):
    f = make_continuous()
    integrand = lambda x: f(x) * np.exp(-1j * k * OMEGA * x)
    real_value, _ = quad(lambda x: np.real(integrand(x)), OFFSET, PERIOD)
    imag_value, _ = quad(lambda x: np.imag(integrand(x)), OFFSET, PERIOD)
    return (real_value + 1j * imag_value) / PERIOD

# f = make_continuous()
# k = 1
# integrand = lambda x: f(x) * np.exp(-1j * k * OMEGA * x)
# xs = np.linspace(OFFSET, PERIOD, 1000)
# vals = [integrand(x) for x in xs]
# plt.plot(xs, np.real(vals))
# plt.plot(xs, np.imag(vals))
# plt.show()