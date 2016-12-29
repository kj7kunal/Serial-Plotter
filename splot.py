# -*- coding: utf-8 -*-
"""
Created on Sat Dec 24 20:38:39 2016

@author: Kunal
"""
import serial
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time

x=range(0,50)
y = [0] * 50


ser = serial.Serial('/dev/ttyACM0', 9600)
ser.close()
ser.open()


fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.set_title('Pitch vs time')
ax.grid(True)
ax.set_ylabel('Pitch')
ax.set_xlabel('time')
plt.ylim([np.min(y)-10,np.max(y)+10])
line, = plt.plot(y)


def update(i):
    x.append(x[len(x)-1]+1)
    y.append(int(ser.readline()))
    del y[0]
    del x[0]
    plt.ylim([np.min(y)-10,np.max(y)+10])
    plt.xlim([x[0],x[len(x)-1]])
    line.set_xdata(x)
    line.set_ydata(y)
    plt.draw()
    time.sleep(0.05)
    
    
    
plt.ion()


            
try:
    data = ser.readline()
    anim = animation.FuncAnimation(fig, update,interval=10)
    # show plot
    plt.show() 
except ValueError:
    print "boooo"
    ser.close()
except KeyboardInterrupt:
    ser.close()


