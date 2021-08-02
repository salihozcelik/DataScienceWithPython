import numpy as np
import pandas as pd
import matplotlib
import random
from random import uniform
import matplotlib.pyplot as plt
import time
import os
import sys


def Perceptron(stepn):

    data = []

    if(stepn == 1):
        inputNo = 50
    if(stepn == 2):
        inputNo = 100
    if(stepn == 3):
        inputNo = 5000

    for i in range(inputNo):
        x = uniform(0,1)
        y = uniform(-3,3)
        if( y < (-3*x) + 1  ):
            color = 'red'
            data.append((1,x,y,color,0))
        elif ( y > (-3*x) + 1  ):
            color = 'blue'
            data.append((1,x,y,color,1))
    for point in data:
        plt.plot(point[1],point[2],color = point[3], marker = 'o' if point[4]==0 else 'x' )

    w = [0,1,1]
    missIter = []

    for i in range(len(data)):
        if(data[i][4]==1 and w[0]*data[i][0] + w[1]*data[i][1]+  w[2]*data[i][2] < 0):
            missIter.append(i)
        elif(data[i][4]==0 and w[0]*data[i][0]+w[1]*data[i][1]+w[2]*data[i][2] >= 0):
            missIter.append(i)

    totalStep = 0
    while  len(missIter) != 0 :
        totalStep = totalStep + 1
        i = random.choice(missIter)
        if((data[i][4] == 1) and (w[0]*data[i][0] + w[1]*data[i][1] + w[2]*data[i][2] < 0) ):
            w[0] = w[0] + data[i][0]
            w[1] = w[1] + data[i][1]
            w[2] = w[2] + data[i][2]
        if((data[i][4] == 0) and (w[0]*data[i][0] + w[1]*data[i][1] + w[2]*data[i][2] >= 0) ):
            w[0] = w[0] - data[i][0]
            w[1] = w[1] - data[i][1]
            w[2] = w[2] - data[i][2]

        missIter = []
        for i in range(len(data)):
            if(data[i][4]==1 and w[0]*data[i][0] + w[1]*data[i][1]+  w[2]*data[i][2] < 0):
                missIter.append(i)
            elif(data[i][4]==0 and w[0]*data[i][0]+w[1]*data[i][1]+w[2]*data[i][2] >= 0):
                missIter.append(i)
    print('Total Step : ' , totalStep)

    x = np.linspace(0,1,100)
    y = (-w[1]/w[2])*x+(-w[0]/w[2])
    for point in data:
        plt.plot(point[1],point[2],color = point[3], marker = 'o' if point[4]==0 else 'x' )
    plt.xlabel('x')
    plt.ylabel('y')
    plt.plot(x, -3*x+1, label='y=2x+1', color="green")
    plt.plot(x, y, color="purple")

    figString = "part1_step{}.png".format(stepn)
    plt.savefig(figString)
