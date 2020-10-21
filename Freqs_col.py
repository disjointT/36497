import numpy as np
import pandas as pd
import matplotlib as plt
import sys
import editdistance

#customize the column to evaluate value frequencies
cur_col=str(sys.argv[1])

#output file name (in txt format)
out_file1=sys.argv[2]

attributes=pd.DataFrame(pd.read_csv('/Users/annat/Desktop/STUDY-CMU/CMU 2020 Fall/36497/Data/category_attributes.csv'))
names=attributes[cur_col]
names=[str(x) for x in names]


#implement the map that shows frequency
freq_cur ={}
for line in names:
    if (line in freq_cur):
        freq_cur[line]+=1
    else:
        freq_cur[line]=1


#write out file:
with open (out_file1,"w") as f:
    #total number of distinct values, optional

    #f.write("TOTAL VALUES:%s"%len(freq_cur)+"\n")
    #f.write("==================================="+"\n")
    for x in freq_cur:
        #threshold for top values, optional
        #if (freq_cur[x]>2000):
            f.write("{word} : {count}".format(word=x,count=freq_cur[x])+"\n")
            #f.write("_____________________________________________________________________"+"\n")
