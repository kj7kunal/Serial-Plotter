# -*- coding: utf-8 -*-
"""
Created on Sat Dec 24 20:38:39 2016

@author: Kunal
"""
import serial
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
#from matplotlib import style
import time

ser = serial.Serial('/dev/ttyACM0', 9600)
ser.close()
ser.open()
time.sleep(1)

x=range(0,50)
dataline = ser.readline()
yval = [int(s) for s in dataline.split(' ')]
n = len(yval)
y = [[0]*50 for _ in range(n)]	#because list is mutable 

#style.use('fivethirtyeight')
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.set_title('Pitch vs time')
ax.grid(True)
ax.set_ylabel('Pitch')
ax.set_xlabel('time')

lines=[]
for index in range(n):
    lobj = ax.plot([],[])[0] 
    lines.append(lobj)

def init():
    for line in lines:
        line.set_data([],[])
    return lines

def update(i):
    global n
    del x[0]    
    x.append(x[len(x)-1]+1)
    dataline = ser.readline()
    time.sleep(0.01)
    yval = [int(s) for s in dataline.split(' ')]
    
    for j in range(n):
        del y[j][0]
        y[j].append(yval[j])
        lines[j].set_data(x,y[j])

    plt.ylim([np.min(y)-10,np.max(y)+10])
    plt.xlim([x[0],x[len(x)-1]])
    plt.draw()

    return lines,
    
            
try:
    anim = animation.FuncAnimation(fig,update,init_func=init,interval=20)
    # show plot
    plt.show() 
except ValueError:
    ser.close()
except KeyboardInterrupt:
    ser.close()


