"""Inferences and insight from data analysis of terrorismp1.csv dataset 

Returns:
    rolestable: a table that aggregates offenses by role to see more into who the IDF is neutralizing and the significance of their contribution to terror
    orgcount: a table that aggregates offenses by terrorist organization to see which organizations have been targeted or clashed most with IDF forces
    snsbar: Seaborn bar graph visualization of the orgscount object
    pltbar: Matplotlib bar graph visualizaton of the orgscount object

"""

import numpy as np 
import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt 

class INF:
    def __init__(self, dfpath):
        """ Read terrorsim datasetwith pandas and creating dataframe object

        Args:
            self(series): original dataframe to be analyzed
            dfpath(str): name of csv file in which dataset is contained

        Returns:
            Pandas dataframe of terrorism data

        """
        self.df = pd.read_csv('terrorismp3.csv')

    def rolestable(self):
        """ Aggregate casualty count, average committed offenses, and average age by role within terrorist organizations

        Args:
            self(series): original dataframe to be analyzed
       

        Returns:
            Table displaying aggregated data calculating casualties per role within terrorist organizations, average offenses committed by casualties in that organization, and average age of casualties belonging to each organization. 

        """
        rolesinfo = self.df[self.df['terrorist'] == 1].groupby('role').agg(rolecount = ('role', 'count'), offensesavg = ('offenses', 'mean'), avage = ('age', 'mean')).reset_index()
        return rolesinfo

    def orgcount(self):
        """ Aggregate casualty count, total committed offenses, and average age by role within terrorist organizations

        Args:
            self(series): original dataframe to be analyzed
       

        Returns:
            Table displaying aggregated data calculating casualties per role within terrorist organizations, total offenses committed by casualties in that organization, and average age of casualties belonging to each organization. 

        
        """
        orgscount = self.df[self.df['terrorist'] == 1].groupby('affiliation').agg(totaloffenses =('offenses', 'count'), avage = ('age', 'mean')).reset_index()
        return orgscount 
    
    def snsbar(self):
        """ Plot seaborn bar chart displaying total offenses committed by each terrorist organization
            Uses aggregated data returned from orgscount

        Args:
            self(series): original dataframe to be analyzed


        Returns:
            seaborn bar chart displaying total offenses committed by each terrorist organization
 

        """
        orgscount = self.df[self.df['terrorist'] == 1].groupby('affiliation').agg(totaloffenses =('offenses', 'count'), avage = ('age', 'mean')).reset_index()
        fig, ax = plt.subplots(figsize = (16,6))
        sns.barplot(x = 'affiliation', y = 'totaloffenses', data = orgscount)
        return plt.show()
    
    def pltbar(self):
        """ Plot matplotlib bar chart displaying total offenses committed by each terrorist organization
            Uses aggregated data returned from orgscount
        Args:
            self(series): original dataframe to be analyzed


        Returns:
            matplotlib bar chart displaying total offenses committed by each terrorist organization
 

        """
        orgscount = self.df[self.df['terrorist'] == 1].groupby('affiliation').agg(totaloffenses =('offenses', 'count'), avage = ('age', 'mean')).reset_index()
        fig, ax = plt.subplots(figsize = (16,6))
        ax.bar(orgscount['affiliation'], orgscount['totaloffenses'])
        ax.set_title('PLT Total Offenses by Affiliation')
        ax.set_xlabel('Affiliation')
        ax.set_ylabel('Total Offenses')
