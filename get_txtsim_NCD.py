#compare texts based on a similarity measure of NCD, "normalized compression distance" by Paul M. B. Vitany
#input: data/*.txt - texts yu want to compare
#output: a dendrogram showing how similar each texts are(the more similar, the closer)

import glob
import os
import nltk  
import numpy as np  
import matplotlib.pyplot as plt
import pandas as pd
import random  
import string
import bs4 as bs  
import urllib.request  
import re 
#from docx import Document
from nltk.corpus import stopwords
import heapq
from sklearn import manifold
#from tulip import tlp
#from tulipgui import tlpgui
from scipy.spatial import Delaunay, delaunay_plot_2d, Voronoi, voronoi_plot_2d
import pickle
import csv
import zipfile
import bz2
from scipy.cluster.hierarchy import dendrogram, linkage, fcluster

#variables you need to specify
#directory: folder name which contains comparing texts files(relative)
#workdirectory: work directory where this py file is
directory='data'
workdirectory='C:\\work\\NCDpython'

#other variables
#tmp: used for a temporary folder
#ext: file extension for comparing files
#extt: used for txt file extension
#extz: used for compression file extension
#findfile: used to find files
#targets: used for target file names and sizes
#cx: size of compression file C(x) used for computing
#cy: size of compression file C(y) used for computing
#maxcx: a number of elements of cx
#cxy: size of compression file C(xy) used for computing; x+y->compression file size
#distance_matrix: used for computing
tmp='tmp'
ext='.txt'
extt='.txt'
extz='.bz2'
findfile=directory+"\\*"+ext
targets=[]
cx=[]
cy=[]
maxcx=len(glob.glob(findfile))
cxy= [['' for i in range(maxcx)] for j in range(maxcx)]
distance_matrix=[['' for i in range(maxcx)] for j in range(maxcx)]

#change work directory
os.chdir(workdirectory)
#create a temporary folder
os.makedirs(tmp, exist_ok=True)

#get text file names you compare
#then process one by one document
#compute C(x) 
for file in glob.glob(findfile):
    #get a file name
    f=file[len(directory)+1:len(file)-len(ext)]
    targets.append(f)
    #create a zip file and get the file size->cx
    f2=tmp+"\\"+f+".zip"
    with zipfile.ZipFile(f2, 'w', compression=zipfile.ZIP_BZIP2) as new_zip:
        new_zip.write(file)
    cx.append(os.path.getsize(f2))
#create c(y), which is equals to c(x)
cy=cx
#create a distance matrix
for y in range(len(cy)):
    for x in range(len(cx)):
        #make a file name
        f=targets[x]+targets[y]
        #bind texts
        line=open(directory+"\\"+targets[x]+ext,"r").read()+open(directory+"\\"+targets[y]+ext,"r").read()
        #compress the bound text
        f2=tmp+"\\"+f
        #create a txt file
        with open(f2+extt, mode='w') as f:
            f.write(line)
        #create a compressed file
        with zipfile.ZipFile(f2+extz, 'w', compression=zipfile.ZIP_BZIP2) as new_zip:
            new_zip.write(f2+extt)
        #compute the similarity based on compression rate
        #NCD
        if cx[x] >= cy[y]:
            mincxcy=cy[y]
            maxcxcy=cx[x]
        else:
            mincxcy=cx[x]
            maxcxcy=cy[y]
        cxy[y][x]=os.path.getsize(f2+extz)
        DM=(cxy[y][x]-mincxcy)/maxcxcy
        #store in the distance matrix
        distance_matrix[y][x]=DM
#end of computing

#write in a file, if necessary
#with open("distance_matrix.csv", "w", encoding="Shift_jis") as f:
#    writer = csv.writer(f, lineterminator="\n") 
#    writer.writerows(distance_matrix)
        
#create a dendrogram
df=pd.DataFrame(distance_matrix)
Z = linkage(df,method="ward",metric="euclidean")        
dendrogram(Z,labels=targets,orientation='right')          
 