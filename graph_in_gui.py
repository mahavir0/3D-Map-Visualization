import tkinter as tk
import numpy as np
import math

from mpl_toolkits import mplot3d
import pkg_resources.py2_warn
from pandas import DataFrame
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from tkinter import *

root= tk.Tk() 
root.title("Graph In GUI")
root.geometry("700x700")

def fun2():
    btn.destroy()
    #initializing the 3D graph1
    fig = plt.figure()
    #ax1 = mplot3d.Axes3D(fig)
    ax1 = fig.add_subplot(111,projection="3d")
    z_line = np.linspace(0, 15, 1000)
    x_line = np.cos(z_line)
    y_line = np.sin(z_line)
    ax1.plot3D(x_line, y_line, z_line, 'gray')
    graph3d = FigureCanvasTkAgg(fig,root)
    graph3d.get_tk_widget().pack(side=tk.LEFT)
    #for storing the values
    angles = []
    distance = []
    x = []
    y = []
    z = []
    k = 5
    c = 0

    #To open the file to read the data
    #file_name = input("Enter file name with .txt : ")
    file_name = 'my_fake_data_3.txt'
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
            ax1.scatter3D(x_point,y_point,z_point,cmap='hsv')

            #plt.pause(0.05)
            print("X : " + str(x_point) + " Y : "+ str(y_point) + " Z : " + str(z_point))
            label1 = Label(root,text=str(x_point))
            label2 = Label(root,text=str(y_point))
            label3 = Label(root,text=str(z_point))
            label1.pack()
            label2.pack()
            label3.pack()
            #for 360 degree add c==369
            if(c==360):
                k=k+10
                c=0
            plt.savefig('model.svg')
            #ax.plot3D(x, y, z, 'ro')
            #plt.axes(projection="3d")
            
        #plt.show()
        toolbar = NavigationToolbar2Tk(graph3d,root)
        toolbar.update()
        graph3d._tkcanvas.pack(side=tk.LEFT,)
        graph3d.mpl_connect('button_press_event', ax1.axes._button_press)
        graph3d.mpl_connect('button_release_event', ax1.axes._button_release)
        graph3d.mpl_connect('motion_notify_event', ax1.axes._on_move)
    finally:
        txt.close()

btn = tk.Button(root,text="press me!",command=fun2)
btn.place(x=10,y=10)

'''
figure2 = plt.Figure(figsize=(5,4), dpi=100)
ax2 = figure2.add_subplot(111)
line2 = FigureCanvasTkAgg(figure2, root)
line2.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
df2 = df2[['Year','Unemployment_Rate']].groupby('Year').sum()
df2.plot(kind='line', legend=True, ax=ax2, color='r',marker='o', fontsize=10)
ax2.set_title('Year Vs. Unemployment Rate')

figure3 = plt.Figure(figsize=(5,4), dpi=100)
ax3 = figure3.add_subplot(111)
ax3.scatter(df3['Interest_Rate'],df3['Stock_Index_Price'], color = 'g')
scatter3 = FigureCanvasTkAgg(figure3, root) 
scatter3.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
ax3.legend(['Stock_Index_Price']) 
ax3.set_xlabel('Interest Rate')
ax3.set_title('Interest Rate Vs. Stock Index Price')
'''
root.mainloop()