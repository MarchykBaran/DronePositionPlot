
import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

from pymavlink import mavutil

from mpl_toolkits.mplot3d import Axes3D

import numpy as np
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from matplotlib.cbook import get_sample_data
#from mayavi import mlab
import plotly.graph_objects as go


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Define the colors for the lines
#colors = ['purple', 'purple', 'r', 'y', 'g','r', 'r', 'y', 'purple','r', 'r', 'y', 'g','r', 'r', 'y', 'g','r', 'r', 'y', 'g','r', 'r', 'y', 'b','r']


ax.set_title('3D Position of Drone')
ax.set_zlabel('Z-Axis')
ax.set_ylabel('Y-Axis')
ax.set_xlabel('X-Axis')

ax.set_aspect("auto")

namafile = 'data3D.csv' 
header1 = "x_value"
header2 = "y_value"
header3 = "z_value"
header4 = "color"

index = count()


def animate(i):
    data = pd.read_csv('data3D.csv')
    x = data[header1]
    y = data[header2]
    z = -(data[header3])
    c = data[header4]

    ax.plot([x[i], x[i + 1]], [y[i], y[i + 1]], [z[i], z[i + 1]], color = c[i])
    #ax.plot(x, y, z, color = c[i])
    #ax.plot3D(x, y, -z, color = c[i])
    #ax.plot3D(x, y, -z, color = c[i])
    #ax.plot3D([x[i], x[i + 1]], [y[i], y[i + 1]], [z[i], z[i + 1]], color = c[i])
    #ax.scatter(x, y, -z, color = c[i])
    #ax.plot_surface(x, y, -z, color = c[i])
    i = i + 5

ani = FuncAnimation(plt.gcf(), animate, interval=20)
plt.tight_layout()
ax.set_xlim([-1, 1])
ax.set_ylim([-1, 1])
ax.set_zlim([-1, 1]) 
ax.set_box_aspect([1, 1, 1])
plt.show()