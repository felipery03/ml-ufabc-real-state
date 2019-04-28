# ml-ufabc-real-state
Machine Learning Project - creating and studying a real state dataset

Developers:  
	Felipe Rigo Yoshimura  
	Gustavo Zanfelice Dib  
	Lucas Hideki Kimura  
	Paula Keiko Miyashita  

src folder contains all scripts of this project.

The first step is to execute data_generator.py in gendata folder. It will create our study dataset considereing some assumptions adopted about real state. This dataset is saved in "data" folder.

Secondly, executing model_generator.py in genmodel folder will split the dataset in 70/30 run a gridsearch in different random forest models. It 70:30 train-test split pick up the best 

