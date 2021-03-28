import argparse
import os
import numpy as np
from sklearn.metrics import mean_squared_error
# import your ml model here 
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import pandas as pd
from azureml.core.run import Run
from azureml.data.dataset_factory import TabularDatasetFactory
from data_preprocessing import clean_data
run = Run.get_context()

# get the cleaned data
x,y = clean_data()
# split the dataset
xtrain,xtest,ytrain,ytest = train_test_split(x,y,test_size=0.2,random_state=1)

# create machine learning model
def main():
    # Add arguments to script for HyperDrive
    parser = argparser.ArgumentParser()
    parser.add_argument('--criterion',type=string,default='gini',help='The function to measure the quality of a split. Supported criteria are “gini” for the Gini impurity and “entropy” for the information gain.')
    parser.add_argument('--max_depth',type=integer,default=None,help='The maximum depth of the tree.')
    parser.add_argument('--min_samples_split',type=int,default=2,help='he minimum number of samples required to split an internal node')
    parser.add_argument('--min_samples_leaf',type=int,default=1,help='The minimum number of samples required to be at a leaf node')

    args = parser.parse_args()
    run.log('Criterion: ',args.criterion)
    run.log('max_depth: ', args.max_depth)
    run.log('min_samples_split: ', args.min_samples_split)
    run.log('min_samples_leaf: ', min_samples_leaf)

    # create your model here
    model = DecisionTreeClassifier(criterion=args.criterion,
                                   max_depth=args.max_depth,
                                   min_samples_split=args.min_samples_split,
                                   min_samples_leaf=min_samples_leaf,
                                   random_state=1).fit(xtrain,ytrain)

    accuracy = model.score(xtest,ytest)
    mse = mean_squared_error(ytest,model.predict(xtest))
    run.log('Accuracy',np.float(accuracy))
    run.log('mse', np.float(mse))

if __name__ == '__main__':
    main()