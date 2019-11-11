Implementation of the paper "Approach to Predicting News ─ A Precise Multi-LSTM Network With BERT"



While predicting news from LTN during 2019 July 20th to August 8th, the accuracy may up to 99%.
The accuracy of experiment is related to the corpus, that is, if one news including many new words, this program may do bad.

	Author: 
		Lana Chen(m073040105@g-mail.nsysu.edu.tw)
		Amanda Huang(amanda10702@gmail.com)
	Advisor:
		Meng-Chang Chen(mcc@iis.sinica.edu.tw)
	Update: Nov.11th,2019
	Target: To predict an unknown news/article from the eight categories(Technology, Finance, Politics, Entertainment, International, Sports, Health, Fashion)
	File description:
		To use this project, you should download the whole package of files and the bert_model.ckpt.data-00000-of-00001,
		and follow the following install instructions.
		You only need to execute two programs--news2E.ipynb and predict.py.
		It's optional for replacinging the context in 'myinput.csv' if you wish to predict your own news.
		
Installation:

	(Request)
	-Tensorflow
	-Numpy
	-json
	-Pandas
	-Keras
	-re
	
	(Optional)
	-collections
	-copy
	-math
	-six
	-shutil
	-unicodedata
	
	(MUST DOWNLOAD FILE)
	"bert_model.ckpt.data-00000-of-00001"
	(It's one of the file inside this folder "chinese_L-12_H-768_A-12"
	from this website: https://github.com/google-research/bert)
	AND PUT IT IN THE FOLDER:
	"Predict_News/chinese_L-12_H-768_A-12/"
	
	OR YOU CAN JUST DOWNLOAD THE WHOLE FOLDER "chinese_L-12_H-768_A-12"
	from this website: https://github.com/google-research/bert)
	

	

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
	|-myinput.csv #it's optional for replacinging the context
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
