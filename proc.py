# -*- coding: utf-8 -*-
import numpy as np
import matplotlib as ml
import os 

from numpy import array
from scipy.cluster.vq import vq, kmeans, whiten
from numpy import random


ids = ['t', 'n', 'b', 'x', 'y', 'z', 'r']
cur = [0.005, 0.2, 0.4, 0.6, 0.8, 1]
tor = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7]
def findMinEn(adress):            #method of energy read from file
    f = open(adress+'\\'+'helix.sls0300', 'r')
    lines = f.readlines()
    Energy = lines[6][15:]
    #print(Energy)
    return Energy

dicMinEn = {}

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
           #print(os.getcwd())
           #print(i)
           E = findMinEn(os.getcwd())
           if float(E) < float(minEn):
               minEn = E
               res = i
               d['k'+ str(k) +'s'+ str(s)] = minEn
               dicMinEn['k'+ str(k) +'s'+ str(s)] = res
               os.chdir('..')
        print('k'+ str(k) +'s'+ str(s) + ' ' + 'min Energy from init. state:'+ str(res))
#print(dicMinEn)
#print(len(d))