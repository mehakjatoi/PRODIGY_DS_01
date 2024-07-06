#!/usr/bin/env python
# coding: utf-8

# In[39]:


import matplotlib.pyplot as plt
import pandas as pd
df=pd.read_csv("C:/Users/Wahab/Downloads/WorldBank_Population/API_SP.POP.TOTL_DS2_en_csv_v2_269358.csv",skiprows=4)
df.drop(["Indicator Name","Indicator Code","Country Code"],axis="columns",inplace=True)
# df.drop_duplicate() 
df.drop_duplicates(subset="Country Name")


# In[44]:


df.head()


# In[45]:


df.info()


# In[46]:


df.describe()


# In[10]:


plt.hist(df["1960"],bins=10,edgecolor="black",label='1960')
plt.title("Population distribution in 1960")
plt.xlabel("Population")
plt.ylabel("Frequency")
plt.legend(loc='upper right')
plt.show()


# In[3]:


plt.hist(df["2023"],bins=10,edgecolor="black",label='2023')
plt.title("Population distribution in 2023")
plt.xlabel("Population")
plt.ylabel("Frequency")
plt.legend(loc='upper right')
plt.show()


# In[11]:


plt.hist([df['1960'], df['1970'], df['1980'],df['1990'],df['2000'],df['2010'],df['2020']],bins=5,edgecolor="black",label=['1960','1970','1980','1990', '2000','2010', '2020'], alpha=0.7)
# counts, bins, patches = plt.hist(df['1970'], bins=10, edgecolor='black')
plt.title("Population Growth Trends from 1960 to 2020")
plt.xlabel("Population")
plt.ylabel("Frequency")
plt.legend(loc='upper right')
# bin_centers = 0.5 * (bins[:-1] + bins[1:])
# plt.xticks(bin_centers, [f'{int(b)}' for b in bins[:-1]], rotation=45)
plt.show()



# In[5]:


df['Population Change (1960-2023)'] = df['2023'] - df['1960']
# Plot histogram of absolute population changes 
plt.hist(df['Population Change (1960-2023)'], bins=10, edgecolor='black')
plt.xlabel('Population Change (1960-2023)')
plt.ylabel('Frequency')
plt.title('Distribution of Absolute Population Changes (1960-2023)')
plt.show()


# In[50]:


years=df.columns[1:-1]
total_population_per_years=df[years].sum()
plt.figure(figsize=(25,25))
plt.barh(years,total_population_per_years,)
plt.xlabel("Population",size=30,color='red')
plt.ylabel("Years",size=30,color='red')
plt.title("Population Over the Years",size=30,color='red')
plt.show()


# In[51]:


df_sorted = df.sort_values(by='2020', ascending=False).head(10)
countries = df_sorted['Country Name']
population_2020 = df_sorted['2020']

# Plotting the bar chart
plt.figure(figsize=(10, 6))
plt.bar(countries, population_2020, color='skyblue')
plt.xlabel('Countries')
plt.ylabel('Population in 2020')
plt.title('Top 10 Most Populous Countries of 2020')
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.tight_layout()

plt.show()


# In[52]:


df_sorted_des=df.sort_values(by='2020',ascending=True).head(10)
countries =df_sorted_des['Country Name']
population =df_sorted_des['2020']
plt.figure(figsize=(10, 6))
plt.bar(countries,population,color='skyblue')
plt.title("Top Ten least Populated Countries of 2020")
plt.xlabel("Countries")
plt.ylabel("Population in 2020")
plt.xticks(rotation=45)
plt.show()


# In[ ]:




