#compare texts based on a similarity measure of cosine similarity
#input: data/*.txt
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
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from scipy.cluster.hierarchy import dendrogram, linkage, fcluster

#variables you need to specify
#directory: folder name which contains comparing texts files(relative)
#workdirectory: work directory where this py file is
directory='data'
workdirectory='C:\\work\\NCDpython'

#other variables
#tmp: used for a temporary folder
#ext: file extension for comparing files
#findfile: used to find files
#targets: used for target file names and sizes
#distance_matrix: used for computing
#corpus: a list which contains comparing file names
#filenames: a list of file names
tmp='tmp'
ext='.txt'
findfile=directory+"\\*"+ext
maxfile=len(glob.glob(findfile))
distance_matrix=[['' for i in range(maxfile)] for j in range(maxfile)]
corpus=['' for i in range(maxfile)]
filenames=['' for i in range(maxfile)]

#change work directory
os.chdir(workdirectory)
#create a temporary folder
os.makedirs(tmp, exist_ok=True)

#get text file names you compare and store them in corpus list
#store filenames in the filenames list as an index
#then process one by one document
i=0
for file in glob.glob(findfile):
    #get a file name
    filenames[i]=file[len(directory)+1:len(file)-len(ext)]
    corpus[i]=open(file,"r").read()
    i += 1

#create a document term matrix and count frequency
count_vectorizer = CountVectorizer()
sparse_matrix = count_vectorizer.fit_transform(corpus)

#transfer the docment term matrix into DataFrame variable
doc_term_matrix = sparse_matrix.todense()
df = pd.DataFrame(doc_term_matrix, 
                  columns=count_vectorizer.get_feature_names(), 
                  index=filenames)

result=pd.DataFrame(cosine_similarity(df,df), 
                  columns=filenames, 
                  index=filenames)

#create a dendrogram
df2=pd.DataFrame(cosine_similarity(df,df))
Z = linkage(df2,method="ward",metric="euclidean")        
dendrogram(Z,labels=filenames,orientation='right')            
