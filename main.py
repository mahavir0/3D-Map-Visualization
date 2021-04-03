import tkinter as tk
import tkinter.filedialog
import tkinter.messagebox
import os
import os.path
###########################################################
import serial.tools.list_ports
###########################################################
from tkinter import *
from PIL import ImageTk,Image
from test_read_data_to_plot_3D import read_data
from test_Testing_3d import real_time
      
root = tk.Tk()
root.title("3D Map Visualiser")
root.geometry("1150x600")

###########################################################
background_image = PhotoImage(file = "176960-cube-abstract.png")
#adding the background image
background_label = Label(root, image=background_image)
background_label.place(x=0,y=0)
#adding the text on the background
welcome_text = Label(root,text="Welcome")
welcome_text.place(x=555,y=18)
###########################################################

#make particular folder for model and data
model_folder = "model"
data_folder = "data"

try:
    os.makedirs(model_folder, exist_ok= True)
    os.makedirs(data_folder, exist_ok=True)
except OSError as e:
    if e.errno != errno.EEXIST:
        raise

#to select file for direct mapaing of 3d map
def print_path():
    f = tk.filedialog.askopenfilename(
        parent=root, initialdir='D:\DE',
        title='Select file',
        filetypes=[('Text file','.txt')]
    )
    print("File Path = ",f)
    return f

def gui_real_time():
    print("real_time")
    real_time()

def gui_read_data():
    print("read_data")
    file_to_scan = print_path()
    if file_to_scan == '' :
        tk.messagebox.showwarning("Error 404","File not found\nPlease select a file to continue...!")
    else:
        read_data(file_to_scan,root)

def pre_check_real_time():
    print("checking arduino is connected or not")
    tk.messagebox.showinfo("Attention","Checking Arduino Connection.....\nThis may take few seconds !\nPress \'OK\' to continue")
    myports = [tuple(p) for p in list(serial.tools.list_ports.comports())]
    try:
        arduino_port = [port for port in myports if 'COM6' in port ][0]
    except IndexError:
        arduino_port = ('COM6', 'Arduino Uno (COM6)', 'USB VID:PID=2341:0043 SER=558343231333510182E1 LOCATION=1-1')
    if arduino_port not in myports:
        print("Arduino is not connected !")
        tk.messagebox.showerror("Fatal Error","Arduino Device is not connected !")
    else:
        print("Arduino is connected !")
        tk.messagebox.showinfo("Device Connected","Arduino Device is connected ! \nWorking at PORT \'COM6\' \nPress \'OK\' to continue")
        gui_real_time()
    
#image button 1
ireal_time = Image.open('maxresdefault.png')
ireal_time = ireal_time.resize((500,500))
ireal_time = ImageTk.PhotoImage(ireal_time)
real_time_btn = tk.Button(root,text="REAL TIME",image=ireal_time,compound=TOP,command=pre_check_real_time)
real_time_btn.grid(row=0,column=0,padx=50,pady=50)

#image button 2
iread_data = Image.open('NF1504_WarsawHole_4m.png')
iread_data = iread_data.resize((500,500))
iread_data = ImageTk.PhotoImage(iread_data)
read_data_btn = tk.Button(root,text="READ DATA",image=iread_data,compound=TOP,command=gui_read_data)
read_data_btn.grid(row=0,column=1,pady=50)




#file menu upper boundry
#root = Tk() 
menu = Menu(root) 
root.config(menu=menu) 
filemenu = Menu(menu) 
menu.add_cascade(label='File', menu=filemenu) 
filemenu.add_command(label='New') 
filemenu.add_command(label='Open...') 
filemenu.add_separator() 
filemenu.add_command(label='Exit', command=root.quit) 
helpmenu = Menu(menu) 
menu.add_cascade(label='Help', menu=helpmenu) 
helpmenu.add_command(label='About') 

root.resizable(False,False)
root.mainloop() 