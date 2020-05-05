#Transform jsonl file to npy file.
import pandas as pd
import numpy as np
df = pd.read_json('mytmpfile.jsonl',lines=True, orient='records')
a_sentence=[]
para=[]
for linex_index in range(30):
    a_sentence=[]
    for seq in range(20):
        a_sentence.append( df['features'][linex_index][seq]['layers'][0]['values'] )
    para.append(a_sentence)
output_filename = 'myoutput' #your output file name
np.save('embedding/'+output_filename+'.npy',para)