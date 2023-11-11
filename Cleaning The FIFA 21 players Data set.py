#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np


# In[4]:


data=pd.read_csv(r"C:\Users\hala\Downloads\archive (12).zip")


# In[5]:


data


# ### removing all the white spacess in the Club columns

# In[6]:


data['Club']=data['Club'].str.strip()


# removing the cm using replace
# 

# In[7]:


data['Height'] = data['Height'].str.replace('cm','')


# removing the inch  "  sign

# In[8]:


data['Height']=data["Height"].str.replace('"','')


# create new columns feet(contail the feet number to the right of ') and inch(contail the inch value to the left of ') 

# In[9]:


data["feet"]=data['Height'].str.split("'").str[0].astype(np.float)
data['inch']=data['Height'].str.split("'").str[1].astype(np.float)


# In[10]:


data['inch'].fillna(0,inplace=True)


# convert the feet and inch to CM

# In[11]:


data.loc[data['feet']<10,'feet']*=30.48
data['inch']=data['inch']*2.54


# In[12]:


data['Height']=data['feet']+data['inch']


# In[13]:


data.drop(["feet",'inch'],axis=1,inplace=True)


# remove the g and pound using replace

# In[14]:


data['Weight']=data["Weight"].str.replace('kg','')
data['Weight']=data["Weight"].str.replace('lbs','')


# convert the data type from object to float

# In[15]:


data['Weight']=data["Weight"].astype(np.float)


# and weight above 120 means its in pound there for multiply by 0,45 to chnage to kg

# In[16]:


data.loc[data['Weight']>120,'Weight']*=0.45359237


# In[17]:


data.rename(columns={'Height':'Height_in_cm','Weight':'Weight_in_KG'},inplace=True)


# In[ ]:





# Separating the joined column in to separated month day and year columns

# In[18]:


data["month"]=data['Joined'].str.split(' ').str[0]
data['day']=data['Joined'].str.split(' ').str[1].str.replace(',','')
data["year"]=data['Joined'].str.split(',').str[1].str.replace(' ','')


# 

# renaming the Value Wage and Release Clause

# In[19]:


data.rename(columns={'Value':'Value_in_M','Wage':'Wage_in_K','Release Clause':'Release Clause_in_M'},inplace=True)


# #### removind the strings in the wage_in_k column and change the datat type to float

# In[20]:


data['Wage_in_K']=data['Wage_in_K'].str.replace('€','').str.replace('K','').astype(np.float)


# #### creating two new columns killo ane million to contail the calues in killos and millions 

# In[21]:


data['killo']=np.where(data['Value_in_M'].str.contains('K'),data['Value_in_M'],0)
data['million']=np.where(data['Value_in_M'].str.contains('M'),data['Value_in_M'],0)


# replacing the string and changing the data type to float 

# In[22]:


data['million']=data["million"].str.replace('€','').str.replace('M','').astype(np.float)
data['million'].fillna(0,inplace=True)
data['killo']=data["killo"].str.replace('€','').str.replace('K','').astype(np.float)
data['killo'].fillna(0,inplace=True)


# changing killos to millions and add both columns to find the final columns 

# In[23]:


data['killo']/=1000
data['Value_in_M']=data['million']+data['killo']


# In[ ]:





# ### repeating the same process for the release Clause column

# In[24]:


data['killo']=np.where(data['Release Clause_in_M'].str.contains('K'),data['Release Clause_in_M'],0)
data['million']=np.where(data['Release Clause_in_M'].str.contains('M'),data['Release Clause_in_M'],0)


# In[25]:


data['killo']=data["killo"].str.replace('€','').str.replace('K','').astype(np.float)
data['killo'].fillna(0,inplace=True)
data['million']=data["million"].str.replace('€','').str.replace('M','').astype(np.float)
data['million'].fillna(0,inplace=True)


# In[26]:


data['killo']/=1000
data['Release Clause_in_M']=data['million']+data['killo']


# In[ ]:





# In[27]:


data['Hits'].fillna(0,inplace=True)


# In[28]:


data


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




