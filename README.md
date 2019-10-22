Implementation of the paper "Approach to Predicting News ─ A Precise Multi-LSTM Network With BERT"
	
	Author: Lana Chen(m073040105@g-mail.nsysu.edu.tw)
	Update: Obt,22th,2019
	Target: To predict an unknown news/article to one of the eight categories.
	File description:
		To use this project, you should download the whole package of files,
		and you only need to execute two programs--news2E.ipynb and predict.py.
		It's optional for replacinging the context in 'myinput.csv' if you wish to predict your own news.
		
Installation:
	
	-Tensorflow
	-Numpy
	-json
	-Pandas
	-Keras
	-collections
	-copy
	-math
	-re
	-six
	-
	

Notice:
	
	*input:
		
		CHINESE ONLY!!!
		
		Should be like the example'myinput.csv':
			two rows: 
				-context
				-your news // It can be any size, but 30*20 words per paragraph may be better.

File:

	|-chinese_L-12_H-768_A-12
	|-embedding
		|-myoutput.npy
	|-news2E.ipynb #turn your input news(myinput.csv) into mytmpfile.jsonl and myoutput.npy(located at ./embedding/)
	|-predict.py #predict the last output to one of the eight categories 
	|-extract_features.py
	|-modeling.py
	|-myinput.csv
	|-mytmpfile.jsonl
	|-optimization.py
	|-our_model.h5 # it had already been trained with 28,768 corpus
	|-our_model_weight.h5 # it had already been trained with 28,768 corpus
	|-tokenization.py

Input(input will be a table/dataframe with only one row):
	![image](https://github.com/LanaChen0/Predict_News/blob/master/input.PNG)
	
Output(You can find the answer on the bottom):
	![image](https://github.com/LanaChen0/Predict_News/blob/master/output.PNG)
	
If you have any questions, please feel free to ask;)
