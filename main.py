#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np


# In[3]:


import seaborn as s
import matplotlib.pyplot as plt


# In[4]:


df = pd.read_csv('project session/Flipkart_Mobiles.csv')
df.head(10)


# In[5]:


df


# # Data Understanding and Exploration:

# In[6]:


df.info()


# In[7]:


colordf=df['Color'].value_counts().head(10)
plt.pie(colordf, labels = colordf.index, autopct = '%1.1f%%')
plt.show()


# In[8]:


df.describe().transpose()


# In[9]:


print('Number of rows is ',df.shape[0],'and number of columns is ', df.shape[1])


# ### different mobile companies in this dataset

# In[10]:


print('the different mobile brands are as follows: \n', df['Brand'].unique())


# In[11]:


print('\n\nThe Number of Mobiles Models that are out for Flipkart Sale: \n\n')
brands = df['Brand'].value_counts()
brands


# ### brands that releases highest numbers of models for sale in flikart

# In[12]:


#plt.pie(brands, labels = df['Brand'].unique())
plt.figure(figsize=(20, 8))
plt.pie(brands, labels=brands.index, autopct='%1.1f%%', startangle=140)
plt.show()


# In[13]:


brands.plot(kind='bar', color='skyblue')
plt.title('Number of Mobile Models by Brand')
plt.xlabel('Brand')
plt.ylabel('Number of Models')
plt.show()


# In[14]:


s.boxplot(df)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# 

# In[ ]:





# ## MOBILE VARIANTS

# ### MEMORY VARIANTS OF THE MOBILE

# In[15]:


memory_var = df['Memory'].value_counts()


# In[16]:


plt.pie(memory_var, labels = memory_var.index)
plt.title('')
plt.show()


# In[17]:


memory_var.plot(kind='bar', color='skyblue')
plt.title('Different Memory Variants of the Mobile')
plt.xlabel('Memory Variants')
plt.ylabel('Number of Models')
plt.show()


# ### STORAGE VARIANTS OF THE MOBILE

# In[18]:


storage_var = df['Storage'].value_counts()
storage_var.plot(kind='bar', color='skyblue')
plt.title('Different Storage Variants of the Mobile')
plt.xlabel('Storage Variants')
plt.ylabel('Number of Models')
plt.show()


# # Different Price range segments for mobiles in India

# In[19]:


Brandslist = df['Brand'].unique().tolist()


# In[20]:


catlist = [900,10000,30000, 60000, 70000, 100000, 200000]


# In[21]:


#cat=pd.cut(df['Selling Price'], bins=catlist, labels=['below 10K','10K-30K','30K-60K','60K-70K','70K-100K','Above 100K'])
df['Price_Category'] = pd.cut(df['Selling Price'], bins=catlist, labels=['below 10K','10K-30K','30K-60K','60K-70K','70K-100K','Above 100K'])
codes = df['Price_Category'].cat.codes


# In[22]:


categorisation = df[['Brand', 'Price_Category']].value_counts()


# In[24]:


categorisation


# In[25]:


categorisation['SAMSUNG']


# In[26]:


#categorisation[categorisation['Price_Category']=='10K-30K']


# In[27]:


categ = pd.DataFrame(categorisation)
categ


# In[47]:


categ = categ.reset_index()
cat=categ[categ['Price_Category']=='10K-30K']
catdf = pd.DataFrame(cat)


# In[48]:


plt.figure(figsize=(10, 8))
plt.pie(catdf['count'], labels=catdf['Brand'],autopct='%1.1f%%', startangle=140)
plt.title('Distribution of Brands in 10K-30K Price Category')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()


# In[49]:


categ = categ.reset_index()
cat=categ[categ['Price_Category']=='60K-70K']
catdf = pd.DataFrame(cat)
catdf
plt.figure(figsize=(10, 8))
plt.pie(catdf['count'], labels=catdf['Brand'],autopct='%1.1f%%', startangle=140)
plt.title('Distribution of Brands for above midrange category')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()


# In[50]:


categ = categ.reset_index()
cat=categ[categ['Price_Category']=='Above 100K']
catdf = pd.DataFrame(cat)
catdf
plt.figure(figsize=(10, 8))
plt.pie(catdf['count'], labels=catdf['Brand'],autopct='%1.1f%%', startangle=140)
plt.title('Distribution of Brands on Premium category')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()


# # Apple vs Samsung 

# In[34]:


df_samsung=df[df['Brand']=='SAMSUNG'][['Model','Memory','Storage','Selling Price']]


# In[35]:


Memorlst = ['8 GB','6 GB','4 GB','3 GB','2GB','1 GB']


# In[36]:


samsung_limitedMem = df_samsung[df_samsung['Memory'].isin(Memorlst)]
sams_Mem=samsung_limitedMem['Memory'].value_counts()


# In[37]:


plt.pie(sams_Mem,labels = sams_Mem.index, autopct = '%1.1f%%', startangle=140)
plt.title('samsung memory variants counts')
plt.show()


# In[ ]:





# In[38]:


storlst=['64 GB', '128 GB', '256 GB', '512 GB', '1 TB', '16 GB', '32 GB']


# In[39]:


sams_limstorage=df_samsung[df_samsung['Storage'].isin(storlst)]
sams_storage = sams_limstorage['Storage'].value_counts()


# In[40]:


plt.pie(sams_storage,labels = sams_storage.index, autopct = '%1.1f%%', startangle=140)
plt.title('samsung storage variants counts')
plt.show()


# In[ ]:





# In[41]:


df_apple = df[df['Brand']=='Apple'][['Model','Memory','Storage','Selling Price']]


# In[ ]:





# In[42]:


apple_mem= df_apple['Memory'].value_counts()


# In[43]:


plt.pie(apple_mem,labels = apple_mem.index, autopct = '%1.1f%%', startangle=140)
plt.title('apple memory variants counts')
plt.show()


# In[44]:


apple_storage =df_apple['Storage'].value_counts()


# In[45]:


plt.pie(apple_storage,labels = apple_storage.index, autopct = '%1.1f%%', startangle=140)
plt.title('apple storage variants counts')
plt.show()


# In[ ]:





# # Are higher rated mobiles always premium or expensive?

# In[ ]:


ratingDf=pd.DataFrame(df[df['Rating']>= 4.7])
ratingDf


# In[ ]:


ratings=ratingDf['Price_Category'].value_counts()


# In[ ]:


plt.pie(ratings, labels = ratings.index, autopct = '%1.1f%%')
plt.title('price categories with respect to ratings >= 4.7')
plt.show()


# In[ ]:


ratingDf=pd.DataFrame(df[df['Rating']>= 4.5])
ratings2=ratingDf['Price_Category'].value_counts()


# In[ ]:


plt.pie(ratings2, labels = ratings2.index, autopct = '%1.1f%%')
plt.title('price categories with respect to ratings >= 4.5')
plt.show() 


# In[ ]:





# # Does a brand have better than 4 ratings for all its products?

# In[57]:


brand_to_check = 'Google Pixel'

# Filter the DataFrame for the selected brand
brand_df = df[df['Brand'] == brand_to_check]

# Check if all ratings are greater than 4
all_ratings_greater_than_4 = (brand_df['Rating'] > 4.0).all()

# Print the result
if all_ratings_greater_than_4:
    print(f"{brand_to_check} has a rating of better than 4 for all its products.")
else:
    print(f"{brand_to_check} does not have a rating of better than 4 for all its products.")


# In[ ]:


#IQOO
# google pixel


# ## IQOO and Google Pixel has ratings of above 4.0 for all its models released 

# In[ ]:





# In[55]:


total_model_counts = df.groupby('Brand')['Model'].count().reset_index()
total_model_counts.columns = ['Brand', 'Total Models released']

# Filter the DataFrame to include only models with ratings greater than 4.0
filtered_df = df[df['Rating'] > 4.0]

# Calculate the count of models with rating > 4.0 for each brand
rating_above_4_counts = filtered_df.groupby('Brand')['Model'].count().reset_index()
rating_above_4_counts.columns = ['Brand', 'Models with Rating > 4.0']

# Merge the two DataFrames
result_df = pd.merge(total_model_counts, rating_above_4_counts, on='Brand', how='left')

# Fill NaN values with 0 for brands with no models above 4.0 rating
result_df['Models with Rating > 4.0'] = result_df['Models with Rating > 4.0'].fillna(0).astype(int)


# In[56]:


result_df


# In[ ]:




