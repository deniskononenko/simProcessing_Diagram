# -*- coding: utf-8 -*-
import numpy as np
import matplotlib as ml
import os 

from numpy import array
from scipy.cluster.vq import vq, kmeans, whiten
from numpy import random
from sklearn.cluster import KMeans
from sklearn import metrics
import numpy as np
import matplotlib.pyplot as plt

ids = ['t', 'n', 'b', 'x', 'y', 'z', 'r']
cur = [0.0, 0.2, 0.4, 0.6, 0.8, 1]
tor = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7]
#cur = [0.2, 0.4, 0.6]
#tor = [0.1, 0.2, 0.3]


def findMinEn(adress):            #method of energy read from file
    f = open(adress+'\\'+'helix.sls0300', 'r')
    lines = f.readlines()
    Energy = lines[6][15:]
    #print(Energy)
    return Energy


def findNz(adress):
    nz = []
    mz = []
    f = open('helix.sls0300', 'r')
    lines = f.readlines()
    magn = lines[21:]
    for item in magn:
        splited = item.split(' ')
        mz.append(splited[0])
    #print(len(mz))
    for i in range(2001):
        #print(i)
        if mz[i] == '\n':
            del mz[i]
    
    for i in range(2000):
        mz[i] = float(mz[i])
            
    for j in range(2000):
        nz.append(np.abs((mz[j] - mz[j-1])/2))
    
    sum = 0
    for k in range(2000):
        sum = sum + nz[k]
    Nz = sum/2000
    
    return Nz



dicMinEn = {}
Energy = []
Nz = []


minEn = 100 
d = {} #dictionary of states
#path = str(os.getcwd())
path = str('D:\\1.University\\Nano_Magnetism\\AFM project\\2.Ring_Helix\\Slasi_sim\\2.StartFiles\\TMMC_forDiagram')
#print(path)
#  по всем кривизнам и кручениям перебираем файлы от разных начальных распр.
for k in cur:
    for s in tor:
        os.chdir(path+'\\' + 'k' + str(k) +'s'+ str(s))
        #print(os.getcwd())
        temp = str(os.getcwd())
        for i in ids: # по всем начальным распределениям находим релакс.сост. с мин.ен.
            os.chdir(temp + '\\' + str(i) + '\\')
            E = findMinEn(os.getcwd())
            if float(E) < float(minEn):
                minEn = E
                res = i
                nz = findNz(os.getcwd())
                #print('N=' + str(Nz) +' ' + 'E=' + str(Energy))
                d['k'+ str(k) +'s'+ str(s)] = minEn
                dicMinEn['k'+ str(k) +'s'+ str(s)] = res
                os.chdir('..')
        Energy.append(float(minEn))
        Nz.append(nz)
           # os.chdir('..')
        print('k'+ str(k) +'s'+ str(s) + ' ' + 'min Energy from init. state:'+ str(res))
#print(dicMinEn)
#print(len(d))
print(Energy)
print(Nz)

points = []
points2 = {}
for k in np.arange(0, 1.1, 0.2):
    for s in np.arange(0.1, 0.71, 0.1):
        points.append('k'+str(float(k))+'s'+str(float(s)))	
print(len(points))
print(len(Energy))
print(len(Nz))
for j in np.arange(0, len(points), 1):
	points2[points[j]] =  Energy[j]


# create new plot and data
plt.plot()
X = np.array(list(zip(Energy, Nz))).reshape(len(Energy), 2)
colors = ['b', 'g', 'r']
markers = ['o', 'v', 's']
print(X)
# KMeans algorithm 
K = 3
kmeans_model = KMeans(n_clusters=K).fit(X)
print(kmeans_model.labels_)
print(len(kmeans_model.labels_))
dicEn = {}
#build clusters
plt.plot()
for i, l in enumerate(kmeans_model.labels_):
    plt.plot(Energy[i], Nz[i], color=colors[l], marker=markers[l], ls='None')
    plt.xlabel('E')
    plt.ylabel('Nz')
    #dicEn[str(Energy[i])] = 1
    #print(str(kmeans_model.labels_[i]) + " " + str(Energy[i]))
    dicEn[str(Energy[i])] = kmeans_model.labels_[i]
    plt.xlim([-2,0])
    plt.ylim([-0.5, 1])
plt.show()
print(dicEn)

#build diagram
plt.plot()
for k in np.arange(0, 1.1, 0.2):
    for s in np.arange(0.1, 0.71, 0.1):
#       print(float(k))
#       print(float(s))
        e = points2['k'+str(float(k))+'s'+str(float(s))]
        #print(e)
        if dicEn[str(float(e))] == 0:
            plt.scatter(k, s, color='b', s=50, marker = 'o')
        elif dicEn[str(float(e))] == 1:
            plt.scatter(k, s, color='g', s=50, marker = '>')
        elif dicEn[str(float(e))] == 2:
            plt.scatter(k, s, color='r', s=50, marker = '*') 
        plt.xlabel('curvature')
        plt.ylabel('torsion')
        plt.xlim([-0.1, 1.2])
        plt.ylim([-0.1, 1.2])
plt.show()




