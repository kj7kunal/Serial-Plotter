# -*- coding: utf-8 -*-
"""
@author: Kunal
"""
import serial
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time

x=range(0,50)
y = [[0]*50 for _ in range(2)]	#because list is mutable 
yval = [0, 0]

ser = serial.Serial('/dev/ttyACM0', 9600)
ser.close()
ser.open()


fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.set_title('Pitch vs time')
ax.grid(True)
ax.set_ylabel('Pitch')
ax.set_xlabel('time')
lines=[]
clr = ["red","cyan"]
for index in range(2):
    lobj = ax.plot([],[],lw=2,color=clr[index])[0]
    lines.append(lobj)
def init():
    for line in lines:
        line.set_data([],[])
    return lines


def update(i):
    del x[0]    
    x.append(x[len(x)-1]+1)
    dataline = ser.readline()
    time.sleep(0.05)
    yval = [int(s) for s in dataline.split(' ')]
    
    for j in range(2):
        del y[j][0]
        y[j].append(yval[j])
        lines[j].set_data(x,y[j])

    print yval, y

    plt.ylim([np.min(y)-10,np.max(y)+10])
    plt.xlim([x[0],x[len(x)-1]])
    plt.draw()
    time.sleep(0.05)

    return lines,

try:
    anim = animation.FuncAnimation(fig,update,init_func=init,interval=50)
    # show plot
    plt.show() 
except ValueError:
    print "boooo"
    ser.close()
except KeyboardInterrupt:
    ser.close()


