"""
Initial exploratory data analysis of features in dataset

Returns:
    histotarget: histograms that display the value distribution among the target variable to see how many casualties are confirmed terrorists

    histoage: histograms that visualize distribution of casualty ages at death among the age variable to learn more about who the IDF is neutralizing

    histomethods: histograms that display the value distribution among method variable to see how the IDF neutralized their targets

    astable: table that displays casualty coount per terrorist organization through airstrikes to see how organizations are being impacted by airstrikes 

    offensehisto: histograms that visualize distribution of values among the offenses variable to display casualties' acts of terror committed  

    historegion: histograms that display the distribution of regions in which the casualties were executed among the region feature to see mainly where the IDF is catching terrorists

"""

import numpy as np 
import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt 

class EDA:
    def __init__(self, dfpath):
        self.df = pd.read_csv(dfpath)
        """ Read terrorsim datasetwith pandas and creating dataframe object

        Args:
            self(series): original dataframe to be analyzed
            dfpath(str): name of csv file in which dataset is contained

        Returns:
            Pandas dataframe of terrorism data

        """

    def histotarget(self):
        """ Read terrorsim datasetwith pandas and creating dataframe object

        Args:
            self(series): original dataframe to be analyzed
            dfpath(str): name of csv file in which dataset is contained

        Returns:
            Pandas dataframe of terrorism data

        """
        fig, axes = plt.subplots(nrows =1, ncols=2)
        mathistotarg = self.df['terrorist'].hist(ax = axes[0])
        snshistotarg = sns.histplot(self.df['terrorist'], ax = axes[1])
        axes[0].set_title('Matplotlib Distribution of target')
        axes[1].set_title('Seaborn Distribution of target')
        plt.tight_layout()
        return plt.show()
    
    def histoage(self):
        """ Read terrorsim datasetwith pandas and creating dataframe object

        Args:
            self(series): original dataframe to be analyzed
            dfpath(str): name of csv file in which dataset is contained

        Returns:
            Pandas dataframe of terrorism data

        """
        fig, axes = plt.subplots(nrows = 1, ncols = 2, figsize =(12,10))
        plthistoage = self.df['age'].hist(ax = axes[0])
        snshistoage = sns.histplot(self.df['age'], ax = axes[1])
        axes[0].set_title('Matplotlib distribution of casualty age')
        axes[1].set_title('Seaborn distribution of casulty age')
        return plt.show()
    
    def histomethods(self):
        """ Read terrorsim datasetwith pandas and creating dataframe object

        Args:
            self(series): original dataframe to be analyzed
            dfpath(str): name of csv file in which dataset is contained

        Returns:
            Pandas dataframe of terrorism data

        """
        fig, axes = plt.subplots(nrows=1, ncols=2, figsize = (12,10))
        mathistomethod = self.df['method'].hist(ax = axes[0])
        snshistomethod = sns.histplot(self.df['method'], ax = axes[1])
        axes[0].set_title('Matplotlib Distribution of Method')
        axes[1].set_title('Seaborn Distribution of Method')
        return plt.show()
    
    def astable(self):
        """ Read terrorsim datasetwith pandas and creating dataframe object

        Args:
            self(series): original dataframe to be analyzed
            dfpath(str): name of csv file in which dataset is contained

        Returns:
            Pandas dataframe of terrorism data

        """
        airstrikedf = self.df[self.df['method'] == 'Airstrike']
        airstrikedf = airstrikedf.groupby('affiliation').agg(casualties = ('name', 'count')).reset_index()
        return airstrikedf 
    
    def offensehisto(self): 
        """ Read terrorsim datasetwith pandas and creating dataframe object

        Args:
            self(series): original dataframe to be analyzed
            dfpath(str): name of csv file in which dataset is contained

        Returns:
            Pandas dataframe of terrorism data

        """
        fig, axes = plt.subplots(nrows=1, ncols=2, figsize = (12,10))
        matoffhisto = self.df['offenses'].hist(ax = axes[0])
        snsoffhisto = sns.histplot(self.df['offenses'], ax = axes[1])
        axes[0].set_title('Matplotlib distribution of casualty offenses')
        axes[1].set_title('Seaborn distribution of casualty offenses')
        return plt.show()
    
    
    def historegion(self): 
        """ Read terrorsim datasetwith pandas and creating dataframe object

        Args:
            self(series): original dataframe to be analyzed
            dfpath(str): name of csv file in which dataset is contained

        Returns:
            Pandas dataframe of terrorism data

        """
        fig, axes = plt.subplots(nrows = 1, ncols = 2, figsize =(12,10))
        plthistoreg = self.df['region'].hist(ax = axes[0])
        snshistoreg = sns.histplot(self.df['region'], ax = axes[1])
        axes[0].set_title('Matplotlib distiribution of regions')
        axes[1].set_title('Seaborn distribution of regions')
        return plt.show()


