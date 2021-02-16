import tkinter as tk
import tkinter.filedialog
from tkinter import *
from PIL import ImageTk,Image
from test_read_data_to_plot_3D import read_data
from test_Testing_3d import real_time
      
root = tk.Tk()
root.title("3D Map Visualiser")
root.geometry("1150x600")

#to select file for direct mapaing of 3d map
def print_path():
    f = tk.filedialog.askopenfilename(
        parent=root, initialdir='D:\DE',
        title='Select file',
        filetypes=[('Text file','.txt')]
    )
    print(f)
    return f

def gui_real_time():
    print("real_time")
    real_time()

def gui_read_data():
    print("read_data")
    read_data(print_path())


#image button 1
ireal_time = Image.open('maxresdefault.png')
ireal_time = ireal_time.resize((500,500))
ireal_time = ImageTk.PhotoImage(ireal_time)
real_time_btn = tk.Button(root,image=ireal_time,command=gui_real_time)
real_time_btn.grid(row=0,column=0,padx=50,pady=50)

#image button 2
iread_data = Image.open('NF1504_WarsawHole_4m.png')
iread_data = iread_data.resize((500,500))
iread_data = ImageTk.PhotoImage(iread_data)
read_data_btn = tk.Button(root,image=iread_data,command=gui_read_data)
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
mainloop() 