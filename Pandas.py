#!/usr/bin/env python
# coding: utf-8

# #### Pandas
# 
# Vamos analisar a performance de estudantes usando o Pandas.

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


df = pd.read_csv('StudentsPerformance.csv')


# In[3]:


df


# In[4]:


type(df)


# In[5]:


# 5 primeiras linhas
df.head()


# In[6]:


# 5 últimas linhas
df.tail()


# In[7]:


# quantidade de linhas e colunas
df.shape


# In[8]:


df.columns


# In[9]:


df.duplicated()


# In[10]:


# verifica linhas duplicadas
df.duplicated().sum()


# In[11]:


df.info()


# In[12]:


# verifica existência de NaN
df.isna().sum()


# In[13]:


# sumário estatístico
df.describe()


# In[14]:


# sumário estatístico - inclusive para as variáveis categóricas
df.describe(include = 'all')


# In[15]:


# quantidade de valores únicos em cada coluna
df.nunique()


# In[16]:


# valores únicos
df['parental level of education'].unique()


# In[17]:


# frequência entre os gêneros
df.gender.value_counts()


# In[18]:


provas = ['math score', 'reading score', 'writing score']


# In[19]:


df


# In[20]:


df.sort_values(['math score']).reset_index(drop = True)


# In[21]:


# ordena o dataset
df = df.sort_values(by = provas, ascending = False).reset_index(drop = True)


# In[22]:


df


# In[23]:


# coluna com a média das provas
df['mean'] = df[provas].mean(axis = 1)


# In[24]:


df.head()


# In[25]:


# consulta
df.query('(gender == "male") & (`test preparation course` == "none") & (`math score` >= 70)')


# In[26]:


df[(df.gender == 'male') & (df['test preparation course'] == 'none') & (df['math score'] >= 70)]


# In[27]:


df.loc[(df.gender == 'male') & (df['test preparation course'] == 'none') & (df['math score'] >= 70)]


# In[28]:


# agrupamento - agrupa os dados por gênero e obtém estatísticas descritivas
df.groupby(by = 'gender')[provas].agg([np.mean, np.median]).T

