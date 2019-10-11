#Author Lana Chen(m073040105@g-mail.nsysu.edu.tw)
#Update: Obt,10th,2019
#Target: Predict a news to one of the eight categories
import numpy as np
from keras.models import load_model

def findMax(y):
    max = y[0] # default
    maxloc = 0 # default
    for i in range(8):
        if y[i] > max:
            max = y[i]
            maxloc = i
    if maxloc == 0:
        print("\n=====techonology=====\n")
    elif maxloc == 1:
        print("\n=====health=====\n")
    elif maxloc == 2:
        print("\n=====fashion=====\n")
    elif maxloc == 3:
        print("\n=====politics=====\n")
    elif maxloc == 4:
        print("\n=====finance=====\n")
    elif maxloc == 5:
        print("\n=====sports=====\n")
    elif maxloc == 6:
        print("\n=====entertainment=====\n")
    elif maxloc == 7:
        print("\n=====international=====\n")

#read model
model = load_model('our_model.h5')

#read weight of model
model.load_weights('our_model_weight.h5')

#read the news
output_filename = 'myoutput' # you can change the file name to your own file name
X_test = np.load('embedding/'+output_filename+'.npy')

#predict the news to one of the eight categories
X_test = X_test.reshape(1,600,768)
y_test = model.predict(X_test)

#print the category of the target news
y = y_test[0]
findMax(y)