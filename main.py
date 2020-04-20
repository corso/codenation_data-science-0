#!/usr/bin/env python
# coding: utf-8

# # Desafio 1
# 
# Para esse desafio, vamos trabalhar com o data set [Black Friday](https://www.kaggle.com/mehdidag/black-friday), que reúne dados sobre transações de compras em uma loja de varejo.
# 
# Vamos utilizá-lo para praticar a exploração de data sets utilizando pandas. Você pode fazer toda análise neste mesmo notebook, mas as resposta devem estar nos locais indicados.
# 
# > Obs.: Por favor, não modifique o nome das funções de resposta.

# ## _Set up_ da análise

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


black_friday = pd.read_csv("black_friday.csv")


# ## Inicie sua análise a partir daqui

# In[3]:


black_friday.head()


# ## Questão 1
# 
# Quantas observações e quantas colunas há no dataset? Responda no formato de uma tuple `(n_observacoes, n_colunas)`.

# In[6]:


def q1():
    return black_friday.shape    
    pass


# ## Questão 2
# 
# Há quantas mulheres com idade entre 26 e 35 anos no dataset? Responda como um único escalar.

# In[7]:


def q2():
    df_q2 = black_friday.groupby('Age')['Gender'].value_counts()
    return int(df_q2['26-35']['F'])
    pass


# ## Questão 3
# 
# Quantos usuários únicos há no dataset? Responda como um único escalar.

# In[64]:


def q3():
    return int(black_friday['User_ID'].nunique())
    pass


# ## Questão 4
# 
# Quantos tipos de dados diferentes existem no dataset? Responda como um único escalar.

# In[9]:


def q4():
    return black_friday.dtypes.nunique()
    pass


# ## Questão 5
# 
# Qual porcentagem dos registros possui ao menos um valor null (`None`, `ǸaN` etc)? Responda como um único escalar entre 0 e 1.

# In[61]:


def q5():
    total = black_friday.any(axis=1).sum() 
    nullLines = black_friday.isnull().any(axis=1).sum()
    return float(nullLines / total)
    pass


# ## Questão 6
# 
# Quantos valores null existem na variável (coluna) com o maior número de null? Responda como um único escalar.

# In[62]:


def q6():
    maxNulls = 0
    # percorre cada coluna do DF, comparando se a qtd de valores nulos é maior que o max encontrado ate entao
    for i in black_friday.columns:
        rowSum = black_friday[i].isnull().sum()
        if (maxNulls < rowSum):
            maxNulls = rowSum
    return int(maxNulls)
    pass


# ## Questão 7
# 
# Qual o valor mais frequente (sem contar nulls) em `Product_Category_3`? Responda como um único escalar.

# In[65]:


def q7():
    # retorna um Pandas Series ordenada pelo valor mais recorrente
    count = black_friday['Product_Category_3'].value_counts()
    return count.first_valid_index()
    pass


# ## Questão 8
# 
# Qual a nova média da variável (coluna) `Purchase` após sua normalização? Responda como um único escalar.

# In[66]:


def q8():
    column = black_friday['Purchase']
    normalized = (column - min(column)) / (max(column) - min(column))
    return normalized.mean()
    pass


# ## Questão 9
# 
# Quantas ocorrências entre -1 e 1 inclusive existem da variáel `Purchase` após sua padronização? Responda como um único escalar.

# In[67]:


def q9():
    column = black_friday['Purchase']
    standardized = (column - column.mean()) / column.std()
    df_standard = pd.DataFrame(standardized.sort_values())
    return len(df_standard.query('Purchase >= -1 and Purchase <= 1'))
    pass


# ## Questão 10
# 
# Podemos afirmar que se uma observação é null em `Product_Category_2` ela também o é em `Product_Category_3`? Responda com um bool (`True`, `False`).

# In[97]:


def q10():
    dfpc = pd.DataFrame({'Product_Category_2':black_friday.Product_Category_2.isnull(), 
                         'Product_Category_3':black_friday.Product_Category_3.isnull()})
    count_pc2 = len(dfpc.query('Product_Category_2 == True'))
    count_both = len(dfpc.query('Product_Category_2 == True and Product_Category_3 == True'))
    return bool(count_pc2 == count_both)
    pass

