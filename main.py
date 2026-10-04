import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from vector import SpinningVector
from fourier import c_k

FRAMES = 100
VECTORS = 100
WINDOW_SIZE = 400

t_values = np.linspace(0, 2 * np.pi, FRAMES)

vector_list = [SpinningVector(c_k(k), k) for k in range(-VECTORS, VECTORS)]

# Create the plot
fig, ax = plt.subplots()
ax.set_xlim([-WINDOW_SIZE, WINDOW_SIZE])
ax.set_ylim([-WINDOW_SIZE, WINDOW_SIZE])
ax.set_aspect("equal")

# Create animated arrows
length = len(vector_list)
quivers = ax.quiver(
    [0] * length,
    [0] * length,
    [0] * length,
    [0] * length,
    angles="xy", scale_units="xy", scale=1
)

# Create a trail line for the last vector
trail, = ax.plot([], [], color="blue")
trail_xdata, trail_ydata = [], []

def update(frame):
    t = t_values[frame]

    bases_x = []
    bases_y = []
    dirs_x = []
    dirs_y = []

    base = 0
    for v in vector_list:
        tip = v.position(t, base)
        direction = tip - base
        bases_x.append(base.real)
        bases_y.append(base.imag)
        dirs_x.append(direction.real)
        dirs_y.append(direction.imag)
        base = tip
    
    # Update the vectors position
    quivers.set_offsets(np.column_stack([bases_x, bases_y]))
    quivers.set_UVC(dirs_x, dirs_y)

    # Update the trail line
    x = tip.real
    y = tip.imag

    trail_xdata.append(x)
    trail_ydata.append(y)
    trail.set_data(trail_xdata, trail_ydata)

    return quivers, trail

animation = FuncAnimation(
    fig=fig,
    func=update,
    frames=FRAMES,
    interval=25,
    blit=True
)
plt.show()
        
