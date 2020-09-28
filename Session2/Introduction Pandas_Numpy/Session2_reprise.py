#!/usr/bin/env python
# coding: utf-8

# Reprise de la session 2
# 

# In[2]:


import numpy as np
import pandas as pd

#utilisation de read
geo = pd.read_csv("correspondance-code-insee-code-postal.csv", sep = ";", usecols = range(11))


# In[2]:


geo


# In[3]:


s = geo["Altitude Moyenne"]


# In[4]:


s


# In[5]:


s.unique()


# In[6]:


geo["Département"].value_counts()


# In[9]:


geo["Statut"].value_counts()


# In[10]:


geo["Commune"].value_counts().head(10)


# In[15]:


l = geo["Commune"].str.len()
min = l.min() 
min


# In[14]:


max = l.max()
max


# In[16]:


s = geo["Superficie"]
s.apply(np.sqrt)


# In[17]:


def rayon(x):
    rayon = np.sqrt(x/np.pi)
    return rayon

s2 = s.apply(rayon)
s2


# In[19]:


geo.reset_index().set_index("Commune").index.is_unique


# In[20]:


geo.set_index('Code INSEE')


# In[28]:


s = geo["Commune"]
s


# In[29]:


s.iloc[200]


# In[30]:


masque = s.str.startswith('A')
s.loc[masque]


# In[31]:


s.loc[s.str.startswith('B')]


# In[36]:


s.loc[(s.str.startswith('B'))]


# In[37]:


s.loc[(s.str.startswith('Z'))]


# In[38]:


s.loc[s.str.startswith('Y') & s.str.endswith('Y')]


# In[39]:


s.loc[s.str.contains('SOUS')]


# Exercice 1
# 
# Combien de valeurs différentes comporte la colonne "Altitude Moyenne" ?
# Pour quelle altitude inférieure à 1000 mètres n'y a-t-il aucune commune ?

# In[40]:


geo["Altitude Moyenne"].value_counts()


# In[3]:


l = geo["Altitude Moyenne"]
for i in range(1000):
    if i not in l: 
        print(i)


# Exercice 2
# Donner le décompte des différents statuts des communes.
# Quels sont les 10 noms de communes les plus fréquents ?
# En français, le nom de famille le plus fréquent est Martin, mais quel est le nom de commune le plus fréquent ?

# In[50]:


statuts = geo["Statut"]
statuts
statuts.value_counts()


# In[52]:


geo["Commune"].value_counts()
geo["Commune"].value_counts().head(10)


# In[53]:


geo["Commune"].value_counts().head(1)
geo["Commune"].value_counts().index[0]


# Exercice 3
# Calculez le minimum et le maximum des longueurs des noms des communes.
# Donnez le décompte des longueurs de noms des communes.
# Quelle est la commune dont le nom est le plus long ?

# In[56]:


geo["Commune"].str.len()


# In[57]:


(geo["Commune"].str.len()).min()


# In[6]:


(geo["Commune"].str.len()).max()


# In[8]:


#Quelle est la commune dont le nom est le plus long ?
s = geo["Commune"]
for commune in s: 
    if len(commune) == 45:
        print(commune)


# DataFrame

# In[59]:


type(geo)


# In[60]:


geo.shape


# In[61]:


len(geo)


# In[62]:


geo.size


# In[63]:


geo.index


# In[64]:


geo.info()


# In[65]:


geo.head()


# In[67]:


geo1  = geo.set_index("Code INSEE")
geo1


# In[68]:


geo.index


# Exercice
# Effectuez un reset_index() puis modifiez l'index en utilisant la colonne 'Commune'.
# Testez l'unicité de l'index. Expliquez.
# 

# In[69]:


geo.index.is_unique


# In[71]:


geo = geo.set_index('Code INSEE')
geo


# In[72]:


geo.index.is_unique


# In[73]:


geo


# In[80]:


geo.reset_index()

