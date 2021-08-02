import numpy as np
import pandas as pd
import matplotlib
import random
from random import uniform
import matplotlib.pyplot as plt
import time
import os
import sys


def closedFormMultipleLinearRegression(stepn):


    start = time.time()

    if(stepn == 1):
        df=pd.read_csv('ds1.csv', sep=',',header=None)
        y = df.iloc[:,-1].values
        x = df.iloc[:,0:-1].values

        xTranspose = x.transpose()
        xTranspose_DOT_x = np.dot(xTranspose,x)
        firstInverse = np.linalg.inv(xTranspose_DOT_x)
        inverseDOTtranspose = np.dot(firstInverse,xTranspose)
        w = np.dot(inverseDOTtranspose,y)

    elif(stepn == 2):
        df=pd.read_csv('ds2.csv', sep=',',header=None)
        y = df.iloc[:,-1].values
        x = df.iloc[:,0:-1].values
        xTranspose = x.transpose()
        xTranspose_DOT_x = np.dot(xTranspose,x)
        firstInverse = np.linalg.inv(xTranspose_DOT_x)
        inverseDOTtranspose = np.dot(firstInverse,xTranspose)
        w = np.dot(inverseDOTtranspose,y)

    elif(stepn == 3):
        df=pd.read_csv('ds2.csv', sep=',',header=None)
        y = df.iloc[:,-1].values
        x = df.iloc[:,0:-1].values
        xTranspose = x.transpose()
        xTranspose_DOT_x = np.dot(xTranspose,x)

        lambd = 0.6
        lambda_DOT_I = lambd * np.identity(xTranspose_DOT_x.shape[0])
        partA = np.linalg.inv(np.sum([xTranspose_DOT_x , lambda_DOT_I], axis=0))
        regAnswer = np.dot(np.dot(partA,xTranspose),y)

    end = time.time()
    print('Time to complete step',stepn,': ',end - start, 'seconds')
