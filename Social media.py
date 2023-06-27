#!/usr/bin/env python
# coding: utf-8

# # Clean & Analyze Social Media

# ## Introduction
# 
# Social media has become a ubiquitous part of modern life, with platforms such as Instagram, Twitter, and Facebook serving as essential communication channels. Social media data sets are vast and complex, making analysis a challenging task for businesses and researchers alike. In this project, we explore a simulated social media, for example Tweets, data set to understand trends in likes across different categories.
# 
# ## Prerequisites
# 
# To follow along with this project, you should have a basic understanding of Python programming and data analysis concepts. In addition, you may want to use the following packages in your Python environment:
# 
# - pandas
# - Matplotlib
# - ...
# 
# These packages should already be installed in Coursera's Jupyter Notebook environment, however if you'd like to install additional packages that are not included in this environment or are working off platform you can install additional packages using `!pip install packagename` within a notebook cell such as:
# 
# - `!pip install pandas`
# - `!pip install matplotlib`
# 
# ## Project Scope
# 
# The objective of this project is to analyze tweets (or other social media data) and gain insights into user engagement. We will explore the data set using visualization techniques to understand the distribution of likes across different categories. Finally, we will analyze the data to draw conclusions about the most popular categories and the overall engagement on the platform.
# 
# ## Step 1: Importing Required Libraries
# 
# As the name suggests, the first step is to import all the necessary libraries that will be used in the project. In this case, we need pandas, numpy, matplotlib, seaborn, and random libraries.
# 
# Pandas is a library used for data manipulation and analysis. Numpy is a library used for numerical computations. Matplotlib is a library used for data visualization. Seaborn is a library used for statistical data visualization. Random is a library used to generate random numbers.

# In[7]:


get_ipython().system('pip install pandas')
get_ipython().system('pip install matplotlib')


# In[37]:


get_ipython().system('install seaborn from ')


# In[9]:


get_ipython().system('pip install seaborn')


# In[48]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import random


# Task 2

# In[11]:


categories = ['Food', 'Travel', 'Fashion', 'Fitness', 'Music', 'Culture', 'Family', 'Health']
num_periods = 500 

data_dict = {
    'Date': pd.date_range('2021-01-01', periods=num_periods),
    'Category': [random.choice(categories) for _ in range(num_periods)],
    'Likes': np.random.randint(0, 10000, size=num_periods)
}

print(data_dict)


# Task 3

# In[12]:


df=pd.DataFrame(data_dict)
print(df)


# In[13]:


df.head()


# In[14]:


df.info()


# In[15]:


df.describe()


# In[16]:


df['Category'].value_counts()


# Task 4

# In[17]:


df=df.dropna()
df


# In[19]:


df=df.drop_duplicates()
df


# In[23]:


df['Date']=pd.to_datetime(df['Date'])
df


# In[27]:


df['Likes']=df['Likes'].astype(int)
df


# Task 5

# In[53]:


import seaborn as sns
import matplotlib.pyplot as plt

sns.distplot(df['Likes'])

plt.xlabel('Likes')
plt.ylabel('Frequency')
plt.title('Histogram of Likes')
plt.show()


# In[60]:


sns.boxplot(data=df,y=df['Likes'],x=df['Category'])
plt.xlabel('Category')
plt.ylabel('Likes')
plt.title('Boxplot of Likes by Category')
plt.xticks(Rotation=35)
plt.show()


# In[65]:


Likes_mean=df['Likes'].mean()
Likes_mean


# In[66]:


category_likes_mean = df.groupby('Category')['Likes'].mean()
category_likes_mean


# Task 5 Conclusion

# The above project focused on analyzing social media data using Python and pandas.
# 
# Defined a list of categories for the social media experiment, such as Food, Travel, Fashion, Fitness, Music, Culture, Family, and Health.
# 
# Generated a Python DataFrame with fields 'Date', 'Category', and 'Likes' using random data. The 'Date' field was created using pd.date_range(), the 'Category' field was populated with random choices using random.choice(), and the 'Likes' field was filled with random integers using np.random.randint().
# 
# Explored and analyzed the data by printing the count of each 'Category' element, dropping null values, and removing duplicate data using the DataFrame methods.
# 
# Converted the 'Date' column to a datetime format using pd.to_datetime() to facilitate appropriate display and analysis of the dates.
# 
# Converted the 'Likes' data to integer type using the astype() method to ensure numerical calculations and analysis.
# 
# Visualized the data by creating a histogram plot of the 'Likes' using sns.histplot() or sns.distplot() from the seaborn library.
# 
# Created a boxplot with the x-axis as 'Category' and the y-axis as 'Likes' using sns.boxplot() to examine the distribution and variability of 'Likes' across different categories.
# 
# Calculated and printed the mean of the 'Likes' category using the mean() method on the 'Likes' column.

# In[ ]:




