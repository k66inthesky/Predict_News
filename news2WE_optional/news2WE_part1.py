import pandas as pd
import re
from shutil import copyfile
import numpy as np

#read file(It's important that the input file must look like the following: )
df_read= pd.read_csv('myinput.csv') #your news name

#Part1: throw(here as the instruction replace) the trash and split the sentences in each paragraphs.
#PS. You can define "trash" by yourself, e.g. for me, →●▲ are trash.
df_read = df_read.replace(" ","")
df_read = df_read.replace("→","")
df_read = df_read.replace("●","")
df_read = df_read.replace("▲","")
df_read = df_read.replace("◎","")
df_read = df_read.replace("","")
df_read = df_read.replace("","")
df_read = df_read.replace("★","")
df_read = df_read.replace("◆","")
df_read = df_read.replace("☆","")
df_read = df_read.replace("\n","")
df_read = re.split(r'[，。?!,.;；]',df_read['context'][0])

#Part2: do zero padding on words of each sentences no matter the number of it is smaller than 20 or not.
#Here we add 50 words each sentences, and you need to add more than 30 at least.
#(for the reason that tranformimg with BERT can cause problem as "0 0 0" to "000".)
for j in range( len( df_read ) ):
    s=''
    for k in range( len( df_read[j] ) ):
        s+= df_read[j][k]
    for m in range( 30 ):
        s+=' 0'
    df_read[j] = s
    
#Part3: do zero padding on paragraphs no matter whether it's number of sentences are smaller than 30.
sen_30zero='0'+' 0'*30
l=[]
for j in range( len( df_read ) ):
    l.append( df_read[j] )
for j in range( 30-len( df_read ) ):
    l.append( sen_30zero )
df_read = l

#Part5: to use BERT to do word embedding, we transfrom myinput.csv to myinput.txt line by line,
#transform myinput.txt to mytmpfile.jsonl,
#and at the end output my(word embedding about your news).

input_filename = 'myinput.txt' #your news(input file) name

bertfile =  open(input_filename, "w")
for i in range(len(df_read)):
    bertfile.writelines(str(df_read[i]))
    bertfile.writelines('\n')
bertfile.close()
