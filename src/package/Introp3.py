"""introduction to variables in terrorism dataset for project 1 of DAV5400

Returns:
    shape: shape of dataset 
    nullstypes: sum of null values among attributes and data types in the dataset 
    numdesc: creates a list of the numerical variables in the dataset and prints a description of numerical variables in the dataset
"""
import numpy as np 
import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt 

class intro: 
    def __init__(self, dfpath):
        """ Read terrorsim datasetwith pandas and creating dataframe object

        Args:
            self(series): original dataframe to be analyzed
            dfpath(str): name of csv file in which dataset is contained

        Returns:
            Pandas dataframe of terrorism data

        """
        self.df = pd.read_csv(dfpath)
    
    def shape(self):
        """ Read terrorsim datasetwith pandas and creating dataframe object

        Args:
            self(series): original dataframe to be analyzed
            dfpath(str): name of csv file in which dataset is contained

        Returns:
            Pandas dataframe of terrorism data

        """
        shape = self.df.shape
        return shape

    def nullstypes(self):
        """ Read terrorsim datasetwith pandas and creating dataframe object

        Args:
            self(series): original dataframe to be analyzed
            dfpath(str): name of csv file in which dataset is contained

        Returns:
            Pandas dataframe of terrorism data

        """
        nulls = self.df.isnull().sum()
        types = self.df.dtypes
        return types, nulls
    
    def numdesc(self):
        """ Read terrorsim datasetwith pandas and creating dataframe object

        Args:
            self(series): original dataframe to be analyzed
            dfpath(str): name of csv file in which dataset is contained

        Returns:
            Pandas dataframe of terrorism data

        """
        num_var = [i for i in self.df.select_dtypes(exclude = object) if i != 'terrorist' and i != 'date']
        return self.df[num_var].describe().transpose()
    
    
