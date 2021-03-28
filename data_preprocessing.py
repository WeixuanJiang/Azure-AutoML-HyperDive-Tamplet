from azureml.data.dataset_factory import TabularDatasetFactory
import pandas as pd

# your file path to csv
file_path = ''
ds = TabularDatasetFactory.from_delimited_files(file_path)

# a function to do date cleaning here
def clean_data(dataset=ds):
    '''
    write your own code here to do data cleansing
    '''
    return x,y
