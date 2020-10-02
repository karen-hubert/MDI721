#!/usr/bin/env python
# coding: utf-8

# Projet Maison n°2
# 
# La colonne "geo_shape" comporte des chaines de catactères au format JSON. Elles représentent les formes géométriques des communes qui sont soit des polygones soit composées de plusieurs polygones. Utiliser la librairie Python json pour parser la colonne "geo_shape". Donner le décompte des valeurs accédées avec la clé "type". Donner le décompte des longueurs des listes accédées avec la clé "coordinates". Quelle commune est la plus complexe géométriquement ? Quelle commune est la seconde la plus complexe géométriquement ? Quelles sont les villes qui sont de type "Polygon" mais dont la longueur des listes accédées avec la clé "coordinates" vaut 2 ? Pour ces villes vérifier que le premier polygone contient bien le second (enclave). NB : installer la librairie shapely, utiliser la classe Polygon de shapely.geometry. Sur Windows shapely peut nécessiter d'installer la dll "geos_c.dll" dans le répertoire "Library/bin" de votre environnement Python.

# In[46]:


import numpy as np
import pandas as pd

geo = pd.read_csv("correspondance-code-insee-code-postal.csv",
                   sep=';')
geo


# In[47]:


import json 
#Possibilité de créer une nouvelle colonne à partir de la même sémantique
geo_modif = geo
geo_modif["Parse_json"] = geo_modif["geo_shape"].apply(json.loads)
geo_modif


# Utiliser la librairie Python json pour parser la colonne "geo_shape". Donner le décompte des valeurs accédées avec la clé "type". Donner le décompte des longueurs des listes accédées avec la clé "coordinates".

# In[48]:


geo_modif["coordonnées"] = geo_modif["Parse_json"].apply(lambda x : x["coordinates"]).str.len()
geo_modif["Type"] = geo_modif["Parse_json"].apply(lambda x : x["type"])
geo_modif["Polygone"] = geo_modif["Parse_json"].apply(lambda x : x["coordinates"])


# In[49]:


geo_modif


# In[50]:


#décompte des valeurs accédées avec la clé "type"
geo_modif['Type'].value_counts()


# In[51]:


#décompte des longueurs des listes 
geo_modif['coordonnées'].value_counts()


# Quelle commune est la plus complexe géométriquement ? 

# In[52]:


index = geo_modif["coordonnées"].idxmax()
print("La commune présentant le plus de coordonnées, i.e. la plus complexe est", geo_modif.iloc[index])


# In[53]:


#Quelle commune est la seconde la plus complexe géométriquement ?
#suppression de la ligne du max dans le data frame modifié
geo_modif2 = geo_modif
geo_modif2.drop(index,0, inplace = True)
geo_modif2


# Quelle commune est la seconde la plus complexe géométriquement ? 

# In[54]:


#Quelles sont les villes qui sont de type "Polygon" mais dont la longueur des listes accédées avec la clé "coordinates" vaut 2 ?
index2 = geo_modif2["coordonnées"].idxmax()
print("La seconde commune présentant le plus de coordonnées, i.e. la seconde plus complexe est", geo_modif2.iloc[index2])


# Quelles sont les villes qui sont de type "Polygon" mais dont la longueur des listes accédées avec la clé "coordinates" vaut 2 ? 

# In[55]:


masque = (geo_modif['coordonnées'] ==2)
masque


# In[56]:


# s est la série de commune définie comme polygone et dont la longueur des coordonnées= 2
s = geo_modif.loc[(geo_modif['coordonnées'] ==2) & (geo_modif['Type']=='Polygon'),:]
s


# In[57]:


print(len(s)) # les villes qui sont Polygones et dont la longueur de la liste ==2 sont au nombre de 10


# Pour ces villes vérifier que le premier polygone contient bien le second (enclave). NB : installer la librairie shapely, utiliser la classe Polygon de shapely.geometry. 

# In[58]:


from shapely.geometry import Polygon, shape, Point

def change_lliste_listetuple(liste): 
    liste_tuple = []
    for i in liste: 
        liste_tuple.append(tuple(i))
    return liste_tuple

def isInPolygone(polygone,liste_points):
    trigger = True
    for point in liste_points:
        if (polygone.contains(Point(point))!= True):
            return false 
            break
    return True #si retourne True alors tous les points appartiennent au Polynome



liste_bool = []


for form in s["Polygone"]:
    new_liste0 = change_lliste_listetuple(form[0])
    new_liste1 = change_lliste_listetuple(form[1]) 
    polygone1 = Polygon(new_liste0)
    trigger = isInPolygone(polygone1,new_liste1)
    liste_bool.append(trigger)


s.insert(21,'is_in_Polygon',liste_bool)


# In[59]:


print(s.shape)
s


# In[60]:


liste_bool_test = []
for form in s["Polygone"]:
    new_liste0 = change_lliste_listetuple(form[0])
    new_liste1 = change_lliste_listetuple(form[1]) 
    polygone1 = Polygon(new_liste0)
    polygone2 = Polygon(new_liste1)
    liste_bool_test.append(polygone1.contains(polygone2))


s.insert(22,'is_in_Polygon_2',liste_bool_test)


# On voit dans les deux colonnes de fins, les résultats des tests 
# is_in_Polygon vérifiant si tous les points sont à l'intérieur du polygone
# is_in_Polygon2 vérifiant si le second polygone est inclus dans le premier polygone

# In[61]:


s


# In[ ]:




