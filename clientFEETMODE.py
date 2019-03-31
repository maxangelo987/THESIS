#!/usr/bin/python               # This is client.py file #IKADUHA MODAGAN
import socket                   # Import socket module
import math

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

import os
import time
import serial
from time import gmtime, strftime
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

import tkSimpleDialog
import Tkinter as tk
import tkMessageBox


from time import sleep
from datetime import datetime

#import plotly.plotly as py
import pandas as pd




s = socket.socket()             # Create a socket object
host = "192.168.1.3"        # Get local machine name, ip address sa ? server
port = 1234
# Reserve a port for your service.


print 'Connecting to ', host, port
s.connect((host, port))


file = open("C:\Users\userPC\Desktop\data_log3.csv", "a")

i=0
if os.stat("C:\Users\userPC\Desktop\data_log3.csv").st_size == 0:
        file.write("Time,X,Y,Z,Message\n")

root = tk.Tk()
root.withdraw()
name = tkSimpleDialog.askstring("Name","Enter Patient's Name")
room = tkSimpleDialog.askstring("Room No.","Enter Patient's Room No.")

n = 0
t = []
td=0
points = ''
r = 1000


yorigin = 130
xorigin = -22
zorigin = 160

count = 0
count1 = 0
count2 = 0
count3 = 0
count4 = 0
while n<r:
        n += 1
        msg = 'OK'
        s.send(msg)
      #  s.send(name)
       # name = s.recv(1024)
        msg = s.recv(1024)
   #     print name
        print 'SERVER >> ', msg
        # create the K-means classifier
        text = msg
      #  tkMessageBox.showinfo("Welcome", message)
        message = 'Inactive'
     
        
       # tkMessageBox.showinfo("Message", message)
        # array of observations
        Type  = text.split(',')  
        x = Type[0]
        x = x.split('X=')
        x = x[1]
        xx = int(x)

        y = Type[1]
        y = y.split(' Y=')
        y = y[1]
        yy = int(y)
       
        z = Type[2]
        z = z.split(' Z=')
        z = z[1]
        zz = int(z)
        
        m=(xx**2)+(yy**2)+(zz**2)
        m=m**0.5
        m1=m*-1
        print ' '
        print m
       # print m1
        #if yy<yorigin+40 and xx<xorigin-50:
               # 

        if xx>=xorigin-60 and xx<=xorigin+50:

                if m>211:
                        count1 = 0
                        count2 = 0
                        count3 = 0
                        count4 = 0
                        count += 1
                        if count == 3:
                                root = tk.Tk()
                                root.withdraw()
                                message = 'Call a nurse.'
                                tkMessageBox.showinfo(name + room, message)
                                count = 0
                                time.sleep(1) 
                      
                if m<211:
                                message = 'Inactive feet'
        if xx<xorigin-60:

            if m>200 and m<215:
                        count = 0
                        count1 = 0
                        count3 = 0
                        count4 = 0
                        count2 += 1
                        if count2 == 3:
                                root = tk.Tk()
                                root.withdraw()
                                message = 'On/Off lights.'
                                tkMessageBox.showinfo(name + room, message)
                                count2 = 0
                                time.sleep(1)
            if m>215:
                        count = 0
                        count1 = 0
                        count2 = 0
                        count4 = 0
                        count3 += 1
                        if count3==3:
                                root = tk.Tk()
                                root.withdraw()
                                message = 'Adjust the bed.'
                                tkMessageBox.showinfo(name + room, message)
                                count3 = 0
                                time.sleep(1)                                

        if xx>xorigin+50:

                if m>200 and m<223:
                        count = 0
                        count3 = 0
                        count2 = 0
                        count4 = 0
                        count1 += 1
                        if count1==3:
                                root = tk.Tk()
                                root.withdraw()
                                message = 'I want to eat.'
                                tkMessageBox.showinfo(name + room, message)
                                count1 = 0
                                time.sleep(1)
                if m>223:
                        count = 0
                        count1 = 0
                        count2 = 0
                        count3 = 0
                        count4 += 1
                        if count4==3:
                                root = tk.Tk()
                                root.withdraw()
                                message = 'I feel pain.'
                                tkMessageBox.showinfo(name + room, message)
                                count4 = 0
                                time.sleep(1)
                    

 
        


        print msg +' Message: '+message
  #   tkMessageBox.showinfo("Message", message)
        
        if n<r:
                points = points+ x + ', '+ y +', '+ z+', '
        else:
                points = points+ x + ', '+ y +', '+ z

        file.write(strftime("%a %d %b %Y %H:%M:%S +0800", gmtime())+","+x.rstrip()+","+y.rstrip()+","+z.rstrip()+','+message+"\n")
        print 'Data Logging in ' + strftime("%a %d %b %Y %H:%M:%S +0800", gmtime())
        file.flush()
        


print("Enter 9 Element in Square Matrix")
print ''
pointi = map(int,filter(None,points.split(","))) # Converting strings to 1d array


td=0
a = [x[:] for x in [[0] * 3] * r] # Declaring 2D Array in Python
for i in range(0, r):
    for j in range(0, 3):
        a[i][j] = pointi[td]
        td=td+1


print a
