#!/usr/bin/env python
# coding: utf-8

# ## Pandas
# 
# ### Instructions
# 
# This assignment will be done completely inside this Jupyter notebook with answers placed in the cell provided.
# 
# All python imports that are needed shown.
# 
# Follow all the instructions in this notebook to complete these tasks.    
# 
# Make sure the CSV data files is in the same folder as this notebook - alumni.csv, groceries.csv

# In[1]:


# Imports needed to complete this assignment


# ### Question 1 :  Import CSV file (1 Mark)
# 
# 
# Write code to load the alumni csv dataset into a Pandas DataFrame called 'alumni'.
# 

# In[5]:


import pandas as pd
alumni = pd.read_csv('alumni.csv')


# ### Question 2 :  Understand the data set (5 Marks)
# 
# Use the following pandas commands to understand the data set: a) head, b) tail, c) dtypes, d) info, e) describe 

# In[7]:


alumni.head()


# In[8]:


alumni.tail()


# In[11]:


alumni.dtypes


# In[10]:


alumni.info()


# In[6]:


alumni.describe()


# ### Question 3 :  Cleaning the data set - part A (3 Marks)
# 
# a) Use clean_currency method below to strip out commas and dollar signs from Savings ($) column and put into a new column called 'Savings'.

# In[30]:


def clean_currency(curr):
    return float(curr.replace(",", "").replace("$", ""))

clean_currency("$66,000")


# In[47]:


import pandas as pd
alumni = pd.read_csv('alumni.csv')
def clean_currency(curr):
    return float(curr.replace(",", "").replace("$", ""))
alumni['Savings ($)'] = alumni['Savings ($)'].apply(clean_currency).astype('float')

alumni.rename(columns={'Savings ($)': 'Savings'}, inplace=True)


# b) Uncomment 'alumni.dtypes.Savings' to check that the type change has occurred

# In[48]:


alumni['Savings'].dtype


# ### Question 4 :  Cleaning the data set - part B (5 Marks)
# 
# a) Run the 'alumni["Gender"].value_counts()' to see the incorrect 'M' fields that need to be converted to 'Male'

# In[28]:


alumni["Gender"].value_counts()


# b) Now use a '.str.replace' on the 'Gender' column to covert the incorrect 'M' fields. Hint: We must use ^...$ to restrict the pattern to match the whole string. 

# In[52]:


alumni['Gender'].str.replace('^M$', 'Male', regex=True)


# In[54]:


alumni["Gender"].value_counts()


# c) That didn't the set alumni["Gender"] column however. You will need to update the column when using the replace command 'alumni["Gender"]=<replace command>', show how this is done below

# In[57]:


alumni["Gender"]= alumni['Gender'].str.replace('^M$', 'Male', regex=True)
alumni["Gender"].value_counts()


# d) You can set it directly by using the df.loc command, show how this can be done by using the 'df.loc[row_indexer,col_indexer] = value' command to convert the 'M' to 'Male'

# In[60]:


alumni.loc[alumni['Gender'] == 'M', 'Gender'] = 'Male'


# e) Now run the 'value_counts' for Gender again to see the correct columns - 'Male' and 'Female' 

# In[62]:


alumni["Gender"].value_counts()


# ### Question 5 :  Working with the data set (4)
# 
# a) get the median, b) mean and c) standard deviation for the 'Salary' column

# In[63]:


median = alumni['Salary'].median()

print(median)


# In[65]:


mean = alumni['Salary'].mean()

print(mean)


# In[78]:


std_dev = alumni['Salary'].std()

print(std_dev)


# d) identify which alumni paid more than $15000 in fees, using the 'Fee' column

# In[76]:


paid_above_15000 = alumni[alumni["Fee"] >15000]

paid_above_15000.head(5)


# ### Question 6 :  Visualise the data set (4 Marks)
# 
# a) Using the 'Diploma Type' column, plot a bar chart and show its value counts.

# In[79]:


#a) (1)
alumni['Diploma Type'].value_counts().plot(kind='bar')


# b) Now create a box plot comparison between 'Savings' and 'Salary' columns

# In[80]:


#b) (1)
box = alumni.boxplot(column=['Savings', 'Salary'])


# c) Generate a histogram with the 'Salary' column and use 12 bins.

# In[87]:


#c) (1)
import matplotlib.pyplot as plt
plt.hist('Salary', bins=12)
plt.xlabel('Salary')
plt.ylabel('Count')
plt.title('Salary')
plt.show()


# d) Generate a scatter plot comparing 'Salary' and 'Savings' columns.

# In[89]:


#d) (1)
alumni.plot.scatter(x='Salary', y='Savings')


# ### Question 7 :  Contingency Table (2 Marks)
# 
# Using both the 'Martial Status' and 'Defaulted' create a contingency table. Hint: crosstab

# In[97]:


# Q7 (2)
pd.crosstab(alumni['Marital Status'], alumni['Defaulted'])


# In[ ]:




