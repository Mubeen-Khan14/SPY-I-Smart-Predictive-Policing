#import os
from tkinter import *
from PIL import ImageTk,Image
from pandas import DataFrame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


import tkinter as tk, threading
import imageio

data1 = {'Country': ['US','CA','GER','UK','FR'],
         'GDP_Per_Capita': [45000,42000,52000,49000,47000]
        }
df1 = DataFrame(data1,columns=['Country','GDP_Per_Capita'])


data2 = {'Year': [1920,1930,1940,1950,1960,1970,1980,1990,2000,2010],
         'Unemployment_Rate': [9.8,12,8,7.2,6.9,7,6.5,6.2,5.5,6.3]
        }
df2 = DataFrame(data2,columns=['Year','Unemployment_Rate'])


data3 = {'Interest_Rate': [5,5.5,6,5.5,5.25,6.5,7,8,7.5,8.5],
         'Stock_Index_Price': [1500,1520,1525,1523,1515,1540,1545,1560,1555,1565]
        }  
df3 = DataFrame(data3,columns=['Interest_Rate','Stock_Index_Price'])

video_name = r'C:\Users\Mubeen\Downloads\test_video1.mp4' 
video = imageio.get_reader(video_name)
def delay():
    for i in range (1,1000000):
        i=i+1

def stream(label):

    while True:
        for image in video.iter_data():
            frame_image = ImageTk.PhotoImage(Image.fromarray(image))
            label.config(image=frame_image)
            label.image = frame_image
            delay()
            
        
    
        
        
#def stream(self):
#    
##    self.window = window
##    self.window.title(window_title)
#    self.video_source = 'C:/Users/Admin/Desktop/SMART-CROWD-ANALYZER-master/Updated peoplecounter/Output_Video/cou.avi'
#  
#         # open video source
#    self.vid = tk.MyVideoCapture('C:/Users/Admin/Desktop/SMART-CROWD-ANALYZER-master/Updated peoplecounter/Output_Video/cou.avi')
# 
#         # Create a canvas that can fit the above video source size
#    self.canvas = tk.Canvas(width = self.vid.width, height = self.vid.height)
#    self.canvas.pack()
# 
# 
#    self.window.mainloop()


if __name__ == "__main__":
    
    root = tk.Tk()
    my_label = tk.Label(root)
    my_label.pack()
    thread = threading.Thread(target=stream, args=(my_label,))
    thread.daemon = 1
    thread.start()
	
    root.title('Spy I Smart Predictive Policing')
    root.geometry("600x600")
#    root.Setsheetstyle("background-color = red")
    figure1 = plt.Figure(figsize=(4,4), dpi=100)
    ax1 = figure1.add_subplot(111)
    bar1 = FigureCanvasTkAgg(figure1, root)
    bar1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
    df1 = df1[['Country','GDP_Per_Capita']].groupby('Country').sum()
    df1.plot(kind='bar', legend=True, ax=ax1)
    ax1.set_title('Country Vs. GDP Per Capita')

    figure2 = plt.Figure(figsize=(4,4), dpi=100)
    ax2 = figure2.add_subplot(111)
    line2 = FigureCanvasTkAgg(figure2, root)
    line2.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
    df2 = df2[['Year','Unemployment_Rate']].groupby('Year').sum()
    df2.plot(kind='line', legend=True, ax=ax2, color='r',marker='o', fontsize=10)
    ax2.set_title('Year Vs. Unemployment Rate')

    figure3 = plt.Figure(figsize=(4,4), dpi=100)
    ax3 = figure3.add_subplot(111)
    ax3.scatter(df3['Interest_Rate'],df3['Stock_Index_Price'], color = 'g')
    scatter3 = FigureCanvasTkAgg(figure3, root) 
    scatter3.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
    ax3.legend(['Stock_Index_Price']) 
    ax3.set_xlabel('Interest Rate')
    ax3.set_title('Interest Rate Vs. Stock Index Price')
    
    

#def graph():
#	values = [1, 10, 100]
#	names = ['group_a', 'group_b', 'group_c']
#	plt.figure(figsize=(9, 3))
#	plt.subplot(131)
#	plt.bar(names, values)
#	plt.subplot(132)
#	plt.scatter(names, values)
#	plt.subplot(133)
#	plt.plot(names, values)
#	plt.suptitle('Categorical Plotting')
#	plt.show()
#graphbtn = tk.Button(root, text="Graph",height=5,width=20,bd=10, command=graph)
#graphbtn.pack(pady=10)


    button_exit=tk.Button(root,text="Exit Program",bd=10,command=root.quit)
    button_exit.pack()

    root.mainloop()
