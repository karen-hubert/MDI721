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

# In[127]:


import numpy as np
import pandas as pd

geo = pd.read_csv("correspondance-code-insee-code-postal.csv",
                   sep=';')
geo


# Utiliser la librairie Python json pour parser la colonne "geo_shape". 

# In[128]:


import json 
import shapely


# In[129]:


#Utiliser la librairie Python json pour parser la colonne "geo_shape".

s = geo["geo_shape"]
liste_base = []
for shape in s:
    liste_base.append(json.loads(shape))
    
liste_base


# Donner le décompte des valeurs accédées avec la clé "type". Donner le décompte des longueurs des listes accédées avec la clé "coordinates". 

# In[130]:


#Donner le décompte des valeurs accédées avec la clé "type".
#Donner le décompte des longueurs des listes accédées avec la clé "coordinates".

shapes = {}
longueur = {}
tab_longueur = []
type_polygone = []
tab_coordonnees = []

for item in liste_base:
    for cle, valeur in item.items():
        if cle == "type": 
            if valeur not in shapes:
                shapes[valeur] = 1
            else: 
                shapes[valeur] = shapes[valeur] + 1
            type_polygone.append(valeur)
        else: #i.e. si la clé = "coordinates"
            cpt = len(valeur)
            if (cpt) not in longueur: 
                longueur[cpt] = 1
            else:
                longueur[cpt] = longueur[cpt] + 1
            tab_longueur.append(cpt) # récupère tous les longueurs 
            tab_coordonnees.append(valeur)
                                
                                
print(shapes)
print(longueur)#longueur se présente sous la forme (longueur de liste, nbr de liste présentant la même longueur)


# In[131]:


def getKey(t):
    return t[0]

sorted(longueur.items(), key = getKey) 
#on remarque donc que la forme géométrique la plus complexes a 486 corrdonnées
#Il faut donc retrouver la Commune qui a pour 486 coordonnées pour sa forme géométrique


# In[132]:


#Quelle commune est la plus complexe géométriquement ?

geo_modif = geo
geo_modif.insert(11,"liste_coordonnées",tab_longueur)
geo_modif.insert(11,"Type",type_polygone)
geo_modif.insert(12,"Coordonnées",tab_coordonnees)
geo_modif


# In[133]:


index = geo_modif["liste_coordonnées"].idxmax()
print (index)

print("La commune présentant le plus de coordonnées, i.e. la plus complexe est", geo_modif.iloc[index])


# Quelle commune est la plus complexe géométriquement ? Quelle commune est la seconde la plus complexe géométriquement ? 

# In[134]:


#Quelle commune est la seconde la plus complexe géométriquement ?
#suppression de la ligne du max dans le data frame modifié
geo_modif2 = geo_modif
geo_modif2.drop(index,0, inplace = True)


# In[135]:


index2 = geo_modif2["liste_coordonnées"].idxmax()
print("La seconde commune présentant le plus de coordonnées, i.e. la seconde plus complexe est", geo_modif2.iloc[index2])


# Quelles sont les villes qui sont de type "Polygon" mais dont la longueur des listes accédées avec la clé "coordinates" vaut 2 ? 

# In[136]:


#Quelles sont les villes qui sont de type "Polygon" mais dont la longueur des listes accédées avec la clé "coordinates" vaut 2 ?
geo_modif['liste_coordonnées']==2 ## communes dont la longueur est égale à 2


# In[137]:


# s est la série de commune définie comme polygone et dont la longueur des coordonnées= 2
s = geo_modif.loc[(geo_modif['liste_coordonnées'] ==2) & (geo_modif['Type']=='Polygon'),:]
s


# Pour ces villes vérifier que le premier polygone contient bien le second (enclave). NB : installer la librairie shapely, utiliser la classe Polygon de shapely.geometry. Sur Windows shapely peut nécessiter d'installer la dll "geos_c.dll" dans le répertoire "Library/bin" de votre environnement Python.

# In[138]:


import shapely.geometry


# In[139]:


#exemple de tracage du d'un polygone
from shapely.geometry import shape

form = shape(json.loads('{"type": "Polygon", "coordinates": [[[0.671852008023359, 43.268343740258835], [0.658909106290094, 43.26408629331833], [0.650936412043327, 43.26784594351563], [0.631954762438815, 43.267341506214635], [0.614599943106533, 43.27783114666891], [0.615325237745429, 43.28054704401019], [0.618933377058037, 43.290418241139854], [0.632703603053863, 43.29290769140922], [0.635725394813344, 43.29913861652718], [0.606810974957096, 43.31088599158548], [0.611653374530417, 43.315673021192005], [0.64425277303335, 43.312392395723855], [0.656250024142831, 43.317414027217886], [0.686254891306201, 43.30042113215234], [0.679800800221225, 43.285046628685656], [0.690880497530084, 43.27968634836884], [0.671852008023359, 43.268343740258835]]]}'
                ))
form


# In[140]:


s


# In[195]:


def change_lliste_listetuple(liste): 
    liste_tuple = []
    for i in liste: 
        liste_tuple.append(tuple(i))
    return liste_tuple
        
def isInPolygone(polygone,liste_points):
    trigger = True
    for point in liste_points:
        if (polygone1.contains(Point(point))!= True):
            return false 
            break
    return True #si retourne True alors tous les points appartiennent au Polynome

from shapely.geometry import Polygon


liste_bool = []
    
for form in s['Coordonnées']:
        #print (type (form))
        #print(len(form),"en entier")
        #print(form)
        #print(len(form[0]), "premier élément")
        #print(form[0])
        #print(len(form[1]), "premier élément")
        #print(form[1])
        #print(tuple(form[0]))
  
        new_liste0 = change_lliste_listetuple(form[0])
        new_liste1 = change_lliste_listetuple(form[1])
        #print(new_liste0)
        polygone1 = Polygon(new_liste0)
        trigger = isInPolygone(polygone1,new_liste1)
        liste_bool.append(trigger)
          
liste_bool # toutes les communes sont enclavées. 


# In[ ]:




