# IoT_Assn4
Iot Assignment 4  

assn4_normalize_combined.py:  
This program trains the model from all the samples present in three datasets and then find out cross validation accuracy.  
You can change the cross validation number using -v option in svm_train method.  

Command to execute assn4_normalize_combined.py:  
python assn4_normalize_combined.py <datatest1.csv> <datatest2.csv> <datatest3.csv>   
Example:  

python assn4_normalize_combined.py datatest1.csv datatest2.csv datatest3.csv  

*Note: This will generate a output file in libsvm format which will have all the samples.  

assn4_nomalize_70_30.py:  
This program trains the model by selecting 70% random samples and test on remaining. You can change the percentage of samples  
to be used to train the model  by modifying the variable TRAINDATA_PERCENT.  
It tells you the accuracy of the model after testing on remaining samples.  

Command to execute assn4_normalize_70_30.py:  
python assn4_normalize_combined.py <datatest1.csv> <datatest2.csv> <datatest3.csv>  
Example:  

python assn4_normalize_combined.py datatest1.csv datatest2.csv datatest3.csv  

*Note: This will generate two output files, both in libsvm format. One is for training data and other is testing data.
