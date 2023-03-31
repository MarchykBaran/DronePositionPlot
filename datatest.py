
import csv
import random
import time

# Import mavutil
from pymavlink import mavutil
# Import Graphing Library

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import pandas as pd
from matplotlib.animation import FuncAnimation


# Create the connection
# From topside computer
master = mavutil.mavlink_connection('tcp:192.168.10.110:5760')
#192.168.10.110:5760

namafile = 'data3D.csv'
header1 = "x_value"
header2 = "y_value"
header3 = "z_value"
header4 = "color"

color = 'purple'

fieldnames = [header1, header2, header3, header4]

with open(namafile, 'w') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    csv_writer.writeheader()



while True:
    msg = master.recv_match()
    if not msg:
        continue
    #Get Data from Drone
    if msg.get_type() == 'STATUSTEXT':
        value = msg.to_dict()
        textvalue = (value['text'])
        #Filer out unwanted data
        if 'confidence' in textvalue:
            if 'High' in textvalue:
                #color = 1
                color = 'green'
                print(textvalue)
                print(color)
            if 'Medium' in textvalue:
                #color = 2
                color = 'yellow'
                print(textvalue)
                print(color)
            if 'Low 'in textvalue:
                #color = 3
                color = 'red'
                print(textvalue)
                print(color)
            if 'VISO' in textvalue:
                #color = 4
                color = 'purple'
                #color = (128, 0, 128, 1.0)
                print(textvalue)
                print(color)

    if msg.get_type() == 'VISION_POSITION_ESTIMATE':
        position = msg.to_dict()
        #Store Data into Variables
        x_value = (position['x'])
        y_value = (position['y'])
        z_value = (position['z'])
        


        fieldnames = [header1, header2, header3, header4]

        
        #Write Data into a file
        with open(namafile, 'a') as csv_file:
            csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            info = {
                header1: x_value,
                header2: y_value,
                header3: z_value,
                header4: color
            }

            csv_writer.writerow(info)
            print(x_value, y_value, z_value, color)

        


