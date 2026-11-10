# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 10:32:10 2026

@author: emmba
"""
import numpy as np
from matplotlib import pyplot as pp

A=10 #V/m
a=2 #m
k=0.4 #1/m
dx=0.1
x=np.arange(0,20,dx)

#Part 1
E=A*np.cos(np.pi*x/a)*np.exp(-k*x)

pp.figure()
pp.plot(x,E)
pp.xlabel("Position")
pp.ylabel("Electric Field")
pp.title("Electric Field Along Waveguid")
pp.grid(True)
pp.show()

#Part 2

#Part E: error dx=0.05
dx=0.05
x = np.arange(0,20,dx)
E=A*np.cos(np.pi*x/a)*np.exp(-k*x)

pp.figure()
#part A: Forward Difference
dif_forward = (E[1:]-E[:-1])/dx
pp.plot(x[:-1],dif_forward, 'k-', linewidth=2,label="Forward Difference")

#Part B: Central Difference
dif_central = (E[2:] - E[:-2]) / (2*dx)
pp.plot(x[1:-1],dif_central, 'r--',label="Central Difference")

#Part C: Analytic Derivative
dif_analytic=A*np.exp(-k*x)*(-(np.pi/a)*np.sin(np.pi*x/a)- k*np.cos(np.pi*x/a))
pp.plot(x,dif_analytic,'b:',label="Analytical Derivative")

#Plot Stuff
pp.xlabel("Position x")
pp.ylabel("dE/dx")
pp.title("Numerical Derivatives of Electrical Fields")
pp.legend()
pp.grid(True)
pp.show()

#Part D: error
error_forward=np.abs(dif_forward-dif_analytic[:-1])
error_central=np.abs(dif_central-dif_analytic[1:-1])

pp.figure()
pp.semilogy(x[:-1],error_forward,label="Forward Difference")
pp.semilogy(x[1:-1],error_central,label="Central Difference")

pp.xlabel("Position x")
pp.ylabel("Absolute Error")
pp.title("Absolute Error of Numerical Derivatives")

pp.legend()
pp.grid(True)
pp.show()

#Part 3

import datetime as dt

#importing data
data = np.loadtxt("fismflux20020824.dat", comments="#")

#Extracting Info
times = [ dt.datetime(int(row[0]),int(row[1]),int(row[2]),int(row[3]),int(row[4]),int(row[5]))
         for row in data]

#Getting the 56th bin
bin56=data[:,61]

#Plot stuff
pp.plot(times,bin56)
pp.xlabel("Time")
pp.ylabel("EUV rad")
pp.title("56th Spectrum")
pp.gcf().autofmt_xdate()
pp.grid()
pp.show()