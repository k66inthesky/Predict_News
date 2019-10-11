Implementaion of "Approach to Predicting News ─ A Precise Multi-LSTM Network With BERT"
	
	Author: Lana Chen(m073040105@g-mail.nsysu.edu.tw)
	Update: Obt,10th,2019
	Target: To predict an unknown news/article to one of the eight categories.
	File description:
		To use this project, you only need to execute two programs--news2E.ipynb and predict.py.

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

Input:
	![image](https://github.com/LanaChen0/Predict_News/blob/master/input.PNG)
	
Output(You can find the answer on the bottom):
	![image](https://github.com/LanaChen0/Predict_News/blob/master/output.PNG)
