import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

from pymavlink import mavutil

from mpl_toolkits.mplot3d import Axes3D

import numpy as np

from matplotlib.cbook import get_sample_data
#from mayavi import mlab
import plotly.graph_objects as go
import matplotlib.image as image
from matplotlib.offsetbox import (OffsetImage, AnnotationBbox)

import matplotlib.pyplot as plt
from matplotlib.cbook import get_sample_data




fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

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

    i=i+10
    ax.plot([x[i], x[i+1]], [y[i], y[i+1]], [z[i], z[i+1]], color=c[i], linewidth=2)
    ax.plot([x[i+1], x[i+2]], [y[i+1], y[i+2]], [z[i+1], z[i+2]], color='orange', linewidth = 2)
    



ani = FuncAnimation(plt.gcf(), animate, interval=20)
plt.tight_layout()
#ax.set_xlim([-1, 1])
#ax.set_ylim([-1, 1])
#ax.set_zlim([-1, 1]) 
ax.set_box_aspect([1, 1, 1])
plt.show()