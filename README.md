# get_txtsim
These Python codes compare text files by using similarity measure. Currently it includes "normalized compression distance"(NCD), 
"Compression-based  Dissimilarity Measure"(CDM) and cosine similarity.The results will be illustrated as a dendrogram so that 
you can see how similar each text is.

For running the codes, create a folder and put the codes in the folder as follows:

1. prepare for a data folder\n\n
appication folder\n
   |--data folder\n\n
Place python apps (.py) in the application folder. Create a data folder in the application folder and put your text files there.

2. prepare for data
All the data should be plain texts. The file names are used for showing each file as item name in a dendrogram, so name them
as you can see which file is which easily.

3. run a Python code
Run a Python code. For example,
py get_txtsim_NCD.py
Then it computes the similarity and show the result.

I used these codes for analyzing students' collaborative writings in an English teaching class.
Yet this is for general use. Try checking the similarity measure as you like.
