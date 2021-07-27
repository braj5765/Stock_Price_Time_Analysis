#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[3]:


##now we will define list of all companies whose data we want to analyse in a list
company_list=['AAPL_data.csv','GOOG_data.csv','MSFT_data.csv','AMZN_data.csv']
path=r'C:\Users\brajk\Desktop\Data Analytics Projects\Project 2- Stock Price analysis\individual_stocks_5yr'
all_data=pd.DataFrame()  ##this dataframe to store all csv files in a single one
for file in company_list:
    current_df=pd.read_csv(path+'/'+file)
    all_data=pd.concat([all_data,current_df])


# In[4]:


all_data.head()


# ### Analyse closing price of all stocks

# In[8]:


all_data['date']=pd.to_datetime(all_data['date'])


# In[9]:


tech_list=all_data['Name'].unique() #unique company list for iteration


# In[10]:


##now we will plot for all companies individually
plt.figure(figsize=(20,12))
for i,company in enumerate(tech_list,1):
    plt.subplot(2,2,i)
    df=all_data[all_data['Name']==company]
    plt.plot(df['date'],df['close'])
    plt.xticks(rotation='vertical')
    plt.title(company)


# ### Analyze the total volume of stock being traded each day

# In[12]:


import plotly.express as px


# In[13]:


for company in tech_list:
    df=all_data[all_data['Name']==company]
    fig=px.line(df,x='date',y='volume',title=company)
    fig.show()


# ### Analyze daily price change in stock

# In[17]:


## add a column of % return to the dataframe
all_data['1day % return']=((all_data['close']-all_data['open'])/all_data['close'])*100


# In[18]:


all_data.head()


# In[19]:


##plot it using plotly
plt.figure(figsize=(20,12))
for i,company in enumerate(tech_list,1):
    plt.subplot(2,2,i)
    df=all_data[all_data['Name']==company]
    plt.plot(df['date'],df['1day % return'])
    plt.title(company)


# In[20]:


##plot using matplotlib
plt.figure(figsize=(20,12))
for i,company in enumerate(tech_list,1):
    plt.subplot(2,2,i)
    df=all_data[all_data['Name']==company]
    df['1day % return'].plot()
    plt.title(company)


# In[23]:


# plot for particular date duration only
plt.figure(figsize=(20,15))
for i,company in enumerate(tech_list,1):
    plt.subplot(2,2,i)
    df=all_data[all_data['Name']==company]
    df.set_index('date')['2016-01-01':'2016-03-31']['1day % return'].plot()
    plt.xticks(rotation='vertical')
    plt.title(company)


# ### Analyse monthly mean of close feature

# In[4]:


df=pd.read_csv(r'C:\Users\brajk\Desktop\Data Analytics Projects\Project 2- Stock Price analysis\individual_stocks_5yr/AAPL_data.csv')


# In[5]:


df.dtypes


# In[6]:


##we will change data type of date column
df['date']=pd.to_datetime(df['date'])


# In[7]:


df.set_index('date',inplace=True)


# In[8]:


df.head()


# In[11]:


## now we will resample the close column on monthly basis and calculate its mean and plot it
df['close'].resample('M').mean().plot()


# In[12]:


df['close'].resample('Y').mean().plot(kind='bar')


# ### Analyse whether the stock prices of these companies(apple,amazon,google,microsoft) are correlated or not

# In[16]:


#we will read data of these 4 companies in separate data frames
aapl=pd.read_csv(r'C:\Users\brajk\Desktop\Data Analytics Projects\Project 2- Stock Price analysis\individual_stocks_5yr/AAPL_data.csv')
aapl.head()


# In[17]:


amzn=pd.read_csv(r'C:\Users\brajk\Desktop\Data Analytics Projects\Project 2- Stock Price analysis\individual_stocks_5yr/AMZN_data.csv')
amzn.head()


# In[18]:


msft=pd.read_csv(r'C:\Users\brajk\Desktop\Data Analytics Projects\Project 2- Stock Price analysis\individual_stocks_5yr/MSFT_data.csv')
msft.head()


# In[19]:


goog=pd.read_csv(r'C:\Users\brajk\Desktop\Data Analytics Projects\Project 2- Stock Price analysis\individual_stocks_5yr/GOOG_data.csv')
goog.head()


# In[20]:


## we will make a new dataframe having just CLOSE data of 4 companies
close=pd.DataFrame()
close['aapl']=aapl['close']
close['amzn']=amzn['close']
close['msft']=msft['close']
close['goog']=goog['close']
close.head()


# In[21]:


import seaborn as sns


# In[22]:


## we will plot correlation data
sns.pairplot(data=close)


# In[23]:


sns.heatmap(close.corr(),annot=True)


# ### Analyse daily return of each stock & how they are co-related

# In[24]:


## first we will create a new dataframe for the needed data and then add columns to it
data=pd.DataFrame()
data['aapl_change']=((aapl['close']-aapl['open'])/aapl['close'])*100
data['amzn_change']=((amzn['close']-amzn['open'])/amzn['close'])*100
data['goog_change']=((goog['close']-goog['open'])/goog['close'])*100
data['msft_change']=((msft['close']-msft['open'])/msft['close'])*100
data.head()


# In[25]:


## now again we will plot correlated data like earlier
sns.pairplot(data=data)


# In[26]:


sns.heatmap(data.corr(),annot=True)


# ### Value at Risk Analysis for Tech Companies

# In[32]:


## distribution plot of change data 
sns.distplot(data['aapl_change'])


# In[33]:


data['aapl_change'].std()
#68% of entire data


# In[34]:


data['aapl_change'].std()*2
#95% of entire data


# In[35]:


data['aapl_change'].std()*3
#99.7% of entire data


# In[36]:


data.describe().T


# In[ ]:




