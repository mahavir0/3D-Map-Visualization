from mpl_toolkits import mplot3d
import pkg_resources.py2_warn
import matplotlib.pyplot as plt
import numpy as np
import math


def read_data(input_file):
    #initializing the 3D graph
    fig = plt.figure()
    ax = plt.axes(projection="3d")
    z_line = np.linspace(0, 15, 1000)
    x_line = np.cos(z_line)
    y_line = np.sin(z_line)
    ax.plot3D(x_line, y_line, z_line, 'gray')

    #for storing the values
    angles = []
    distance = []
    x = []
    y = []
    z = []
    k = 5
    c = 0

    #To open the file to read the data
    file_name = input_file
    try:
        txt = open(file_name)


        Lines = txt.readlines()
        total_lines = 0
        for i in Lines:
            c = c + 1
            pre_values = i.split('\n')
            values = pre_values[0].split(' ')
            #print(values)
            total_lines = total_lines + 1
            angles.append(int(values[0]))
            distance.append(int(values[1]))
            #print(values[0]+ "  " +values[1])

            x_point = math.cos(math.radians(int(values[0])))*int(values[1]) #calculating the x coordinates using cartezian equation
            y_point = math.sin(math.radians(int(values[0])))*int(values[1]) #calculating the y coordinates using cartezian equation
            z_point = k
            x.append(math.cos(math.radians(int(values[0])))*int(values[1]))
            y.append(math.sin(math.radians(int(values[0])))*int(values[1]))
            z.append(k)
            
            #ax.scatter3D(x_point,y_point,z_point)
            ax.scatter3D(x_point,y_point,z_point,cmap='hsv')

            #plt.pause(0.05)
            print("X : " + str(x_point) + " Y : "+ str(y_point) + " Z : " + str(z_point))
            if(c==180):
                k=k+10
                c=0
            plt.savefig('model.svg')
            #ax.plot3D(x, y, z, 'ro')
            #plt.axes(projection="3d")
            
        plt.show()
    finally:
        file_name.close()
        print("file has been closed")