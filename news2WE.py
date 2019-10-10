#Author Lana Chen(m073040105@g-mail.nsysu.edu.tw)
#Update: Obt,5th,2019
#Transform news to word embedding, and store them in ./embedding/output.npy

import pandas as pd
import re
from shutil import copyfile
import numpy as np

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
    if len( df_read[j] ) > 0:
        for k in range( len( df_read[j] ) ):
            s+= df_read[j][k]
        for k in range( 50 ):
            s+=' 0'
    df_read[j] = s

#Part3: to use BERT to do word embedding, we transfrom myinput.csv to myinput.txt line by lin,
#transform myinput.txt to mytmpfile.jsonl,
#and at the end output my(word embedding about your news).

input_filename = 'myinput.txt' #your news(input file) name
output_filename = 'myoutput' #your output file name

bertfile =  open(input_filename, "w")
for i in range(30):
    bertfile.writelines(str(df_read[i]))
    bertfile.writelines('\n')
bertfile.close()

#The word embedding information will start as INFO:tensorflow:*** Example ***(it must be seen!!!)
!python ./extract_features.py \
    --input_file=./myinput.txt \
    --output_file=./mytmpfile.jsonl \
    --vocab_file=./chinese_L-12_H-768_A-12/vocab.txt \
    --bert_config_file=./chinese_L-12_H-768_A-12/bert_config.json \
    --init_checkpoint=./chinese_L-12_H-768_A-12/bert_model.ckpt \
    --layers=-1 \
    --max_seq_length=20 \
    --batch_size=8

#Part4: do zero padding on paragraphs whose number of sentences are smaller than 30.
sen_30zero='0'+' 0'*19
if len( df_read ) < 30:
    l=[]
    for j in range( len( df_read ) ):
        l.append( df_read[j] )
    for j in range( 30-len( df_read[i] ) ):
        l.append( sen_30zero )
    df_read[i] = l
    
#Part5: delete sentences that more than 30, and also delete sentences whose words including over 20. 
if len(df_read) > 30:
    df_read = df_read[0:30]
for i in range(30):
    if ( len(df_read[i]) ) > 20:
        df_read[i] = df_read[i][0:20]
        
df = pd.read_json('mytmpfile.jsonl',lines=True, orient='records')
a_sentence=[]
para=[]
for linex_index in range(30):
    a_sentence=[]
    for seq in range(8):
        a_sentence.append( df['features'][linex_index][seq]['layers'][0]['values'] )
    para.append(a_sentence)

np.save('embedding/'+output_filename+'.npy',para)
