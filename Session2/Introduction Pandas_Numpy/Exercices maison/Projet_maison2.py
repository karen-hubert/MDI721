#!/usr/bin/env python
# coding: utf-8

# Projet Maison n°2 
# 
# La colonne "geo_shape" comporte des chaines de catactères au format JSON. Elles représentent les formes géométriques des communes qui sont soit des polygones soit composées de plusieurs polygones.
# Utiliser la librairie Python json pour parser la colonne "geo_shape".
# Donner le décompte des valeurs accédées avec la clé "type".
# Donner le décompte des longueurs des listes accédées avec la clé "coordinates".
# Quelle commune est la plus complexe géométriquement ?
# Quelle commune est la seconde la plus complexe géométriquement ?
# Quelles sont les villes qui sont de type "Polygon" mais dont la longueur des listes accédées avec la clé "coordinates" vaut 2 ?
# Pour ces villes vérifier que le premier polygone contient bien le second (enclave). NB : installer la librairie shapely, utiliser la classe Polygon de shapely.geometry. Sur Windows shapely peut nécessiter d'installer la dll "geos_c.dll" dans le répertoire "Library/bin" de votre environnement Python.

# In[89]:


import numpy as np
import pandas as pd

geo = pd.read_csv("correspondance-code-insee-code-postal.csv",
                   sep=';')
geo


# In[90]:


import json 
import shapely


# In[91]:


#Utiliser la librairie Python json pour parser la colonne "geo_shape".

s = geo["geo_shape"]
liste_base = []
for shape in s:
    liste_base.append(json.loads(shape))
    
liste_base


# In[78]:


#Donner le décompte des valeurs accédées avec la clé "type".
#Donner le décompte des longueurs des listes accédées avec la clé "coordinates".

shapes = {}
longueur = {}
tab_longueur = []
type_polygone = []

for item in liste_base:
    for cle, valeur in item.items():
        if cle == "type": 
            if valeur not in shapes:
                shapes[valeur] = 1
            else: 
                shapes[valeur] = shapes[valeur] + 1
            type_polygone.append(valeur)
        else: #i.e. si la clé = "coordinates"

            if (len(valeur[0])) not in longueur: 
                longueur[len(valeur[0])] = 1
            else:
                longueur[len(valeur[0])] = longueur[len(valeur[0])] + 1
            tab_longueur.append(len(valeur[0])) # récupère tous les longueurs 
            
                                
                                
print(shapes)
print(longueur)#longueur se présente sous la forme (longueur de liste, nbr de liste présentant la même longueur)


# In[92]:


def getKey(t):
    return t[0]

sorted(longueur.items(), key = getKey) 
#on remarque donc que la forme géométrique la plus complexes a 486 corrdonnées
#Il faut donc retrouver la Commune qui a pour 486 coordonnées pour sa forme géométrique


# In[93]:


#Quelle commune est la plus complexe géométriquement ?

geo_modif = geo
geo_modif.insert(11,"liste_coordonnées",tab_longueur)
geo_modif.insert(11,"Type",type_polygone)
geo_modif


# In[94]:


index = geo_modif["liste_coordonnées"].idxmax()
print (index)

print("La commune présentant le plus de coordonnées, i.e. la plus complexe est", geo_modif.iloc[index])


# In[95]:


#Quelle commune est la seconde la plus complexe géométriquement ?
#suppression de la ligne du max dans le data frame modifié
geo_modif2 = geo_modif
geo_modif2.drop(index,0, inplace = True)


# In[96]:


index2 = geo_modif2["liste_coordonnées"].idxmax()
print("La seconde commune présentant le plus de coordonnées, i.e. la seconde plus complexe est", geo_modif2.iloc[index2])


# In[107]:


#Quelles sont les villes qui sont de type "Polygon" mais dont la longueur des listes accédées avec la clé "coordinates" vaut 2 ?
geo_modif['liste_coordonnées']==2


# In[110]:


masque = (geo_modif['liste_coordonnées'] ==2)
geo_modif.loc[masque]


# In[ ]:




