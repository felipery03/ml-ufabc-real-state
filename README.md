# ml-ufabc-real-state
Machine Learning Project - creating and studying a real state dataset

Developers:  
	Felipe Rigo Yoshimura  
	Gustavo Zanfelice Dib  
	Lucas Hideki Kimura  
	Paula Keiko Miyashita  

"src" folder contains all scripts of this project.

The first step is to execute data_generator.py in gendata folder. It will create our study dataset considereing some assumptions adopted about real state. This dataset is saved in "data" folder and contains 100,000 samples.

Secondly, if model_generator.py is executed in genmodel folder, it will split the dataset in 70/30 train test proportion. Using train dataset, it runs a gridsearch in different random forest models with a parameter space showed below:

n_estimators: 3 to 19

max_depth: 1 to 12

bootstrap: True or False
split criterion: Gini


The gridsearch runs a 10-fold cross validation, and based on the best mean validation score accuracy it picks up the best model. Using joblib, genmodel script saves split datasets, best model choosen and grid search setup in "models" folder.

At last, model_analysis.py in evalmodel shows results about the best model. It prints on screen: mean train score & standard error, mean validation score & standard error, test score and feature importance. 

