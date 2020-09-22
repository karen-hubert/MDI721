#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 19:55:38 2020

@author: KarenHubert
"""

from collections import deque 
from math import pi

# Tutoriel Python 
#Exercices 

#Chapitre 3

def Fibonacci(n):
    a=0
    b=1 
    # possibilité d'avoir une affectation multiple
    # a,b =0,1
    while a < n:
        print(a)
        a,b = b,a+b


def autreFibonacci():
    a,b = 0,1
    while a<1000:
        print(a, end=",")
        a,b = b, a+b


def main_chapitre3():
    
    #n = int(input("entier pour Fibonacci ? "))
    #Fibonacci(n)
    
    autreFibonacci()
   

#Chapitre 4 

def identification_integer():
    x = int(input("Please enter an integer: "))
    if x<0:
        print ("x est en entier relatif")
    elif x ==0:
        print("zero")
    elif x ==1:
        print("single")
    else: 
        print("more")
        

def boucle_for(liste_l):
    for i in liste_l:
        print (i,len(i))


def fonction_range(n):
    print("range(10):")
    print(range(10))
    
    
    print("impression de range (n))")
    for i in range (n):
        # la fonction range va de 0 à n-1
        print(i)
    
    print("impression de range (5,10)")
    for i in range(5,10):
        print(i)
        
        
    print("impression de range (0,100,10)")
    for i in range(0,100,10):
        print(i)
        
    print("impression de range (-10,-100,-30)")
    for i in range(-10,-100,-30):
        print(i)


def autre_range(n):
    #correspond à 0+1+2+ ... + n-1 + n 
    print(sum(range(n))) 
    #donne une liste partant de 0 à n-1
    print(list(range(n)))


def impression_index_liste(liste_l):
    for i in range(len(liste_l)):
        print(i,liste_l[i])


def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)

def f(a, L=[]):
    L.append(a)
    return L

def f2(a, L=None):
    if L is None:
        L=[]
    L.append(a)
    return L


def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")


def cheeseshop(kind, *arguments, **keywords):
    print("--Do you have any", kind, " ?")
    print ("--I'm sorry, we're all out of ", kind)
    for arg in arguments:
        print(arg)
    print ("-"* 40)
    for kw in keywords:
        print(kw,":", keywords[kw])
        
    #Ici Python garantit l'ordre d'affichage des arguments rentrés.
    
    
#Les arguments peuvent être passés à une fonction Python par position ou par mot-clé

# exemple de définition de fonction 

#def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
#où / et * sont facultatifs. 

#S'ils sont utilisés, ces symboles indiquent par quel type de paramètre 
#un argument peut être transmis à la fonction : position seule, position ou mot-clé, et mot-clé seul. 
#Les paramètres par mot-clé sont aussi appelés paramètres nommés.

#Si / et * ne sont pas présents dans la définition de fonction, 
#les arguments peuvent être passés à une fonction par position ou par mot-clé.

#attention en python 3.7, nous n'avons les arguments position/nommés
        

 
def standard_arg(arg):
    print(arg)

# def pos_only_arg(arg,/):
#    #print(arg)

# def kwd_only_arg(*, arg):
#     print(arg)

# def combined_example(pos_only, /, standard, *, kwd_only):
#     print(pos_only, standard, kwd_only)   


#Liste d'arguments arbitraires 
    #Une fonction peut être appelée avec un nombre arbitraire darguments 
    
def concat(*args, sep = "/ "):
    for arg in  args:
        print (arg + sep)


def creation_liste(start, stop):
    return list (range(start, stop))


def creation_liste2(args):
    return list (range(*args))

#fonction anonyme
def make_incrementor(n):
    return lambda x: x+n

def my_function():
    """
    Returns
    ------
    None.
    Cette fonction ne fait absolument rien... 
    Mais permet de comprendre comment afficher la documentation /commentaire la décrivant
    """
    pass

def exemple_annotation(ham: str, egg: str = "eggs")-> str: 
    #avec en argument uniquement ham et egg => les annotations ne sont pas renvoyées. 
    pass
    

def main_chapitre4():
    pass
    
    #identification_integer()
    
    #words = ['chat','chien', 'oiseau','tortue']
    #boucle_for(words)
    #impression_index_liste(words)
    
    #n = int(input("entier?"))
    #autre_range(n)
    #fonction_range(n)
   
    #ask_ok("Do you want to quit? ", 5, "Only yes or no")
    
    #print(f(1))
    #print(f(2))
    #print(f(3))
    
    #print(f2(5))
    #L = f2(5)
    #print(f2(1))
    #print(f2(1, L))
    
    #print ("parrot 1")
    #parrot(1000)
    #print ("parrot 2")
    #parrot(voltage =1000)
    #print ("parrot 3")
    #parrot(voltage =10000,action = "HEYHEY")
    #print ("parrot 4")
    #parrot('A million', 'bereft of life', 'jump')
    #print ("parrot 5")
    #parrot('a thousand', state = "pushing up the daisies")
    #d = {"voltage" : "four million", "state": "Wisconsin", "action":"VROOM"}
    #parrot(*d)
    #print("-----")
    #parrot(**d)
    
    #cheeseshop("Limberger", "it is very funny, sir", "It is very very funy, sir", shopseeker = "Michael Palin", slient = "John Clesse", sketch ="Cheese Shop Sketch")
    #cheeseshop("Compté", "1", "2", "3", "4","5", shopseeker = "K", client = "A", sketch ="R", test = "essai", test2 = "E", test3 = "N")  

    #concat("terre","mars", "pluton")
    
    #print(creation_liste(1,10))
    #print(creation_liste2([1,10]))
    
    #fonction anonyme
     # f = make_incrementor(10)
     # print(f(0))
     # print(f(1))
     
     # f= make_incrementor(42)
     # print(f(3))
     
     # pairs = [(1,'one'), (2,'two'),(3,'three'),(4,'four')]
     # pairs.sort(key = lambda pair:pair[1])
     # print (pairs)
    
    #documentation d'une fonction
    # print("activation de la fonction: ma fonction")
    # my_function()
    # print("fini, et ne fait rien")
    
    # print(my_function.__doc__)
    
    #annotation d'une fonction 
    # print("annotation de la fonction exemple_annotation", exemple_annotation.__annotations__)


    
#Chapitre 5: structure de données 
#Compléménts sur les listes 

    
# =============================================================================
# Les différentes fonctions pour les listes 
# 
#     L.append(x) : pour ajouter un élément à la fin d'une liste 
#     
#     L.extend(iterable) : étend la liste en y ajoutant tous les éléments de l'iterable
#     
#     L.insert (i,x) : insère x à la position i i.e. L.insert(0,x) revient à inclure x au début de la liste
#     L.insert(len(L), x) est équivalent à L.append(x)
#     
#     L.remove(x) : supprime de la liste le premier élément dont la valeur est x
#     
#     L.pop(i): enlève de la liste l'élément situé à la position indiquée et renvoie la valeur en retour
#     L.pop(): enlève le dernier élément de la liste et le renvoie. 
#     
#     L.index(x) qui renvoie la position du premier élément de la liste dont la valeur est x
#     L.index(x, start, stop) on peut limiter la recherche à un sous ensemble de la liste, on commence la recherche à l'éléméent positionné à l'indice start.
#     La recherche se termine à l'indice stop.
#     
#     L.clear() : pour supprimer tous les éléments de la liste
#     
#     L.count(x): renvoie le nombre d'éléments ayant pour valeur x'
#     
#     L.sort(key = non, reverse = false) : ordonne les éléments dans la liste 
#     
#     L.reverse(): inverse l'ordre des éléments dans la liste'
#     
#     L.copy(): renvoie une copie superficielle de la liste
#     
# 
#     => Utilisation des listes comme des piles où le dernier élément ajouté et le premier récupéré 
#     LIFO //last in first out
#     utilisation de L.append pour rajouter un élément et de L.pop pour le retirer
# 
# 
#     => Utilisation des listes comme des files où le premier élément ajouté est le premier sorti
#         FIFO // first in first out
#         Les listes sont peu efficaces pour réaliser ce type de traitement
#         Possibilité d'utiliser la classe deque 
#         from collection import deque'
# ===================================================

def comprendre_deque():
    queue = deque(["Eric", "Emmanuel", "Gauthier"])
    queue.append("Olivier")
    queue.append("Sebastien")
    print(queue.popleft())
    print(queue.popleft())
    print(queue)
    
#comprendre_deque()
    
def liste_exemple(): 
    squares = []
    for x in range(10):
        squares.append(x ** 2)
    return squares
# autre façon de le faire
# squares = list(map(lambda x : x ** 2, range(10)))
# squares = [x ** 2 for x in range(10)]


#print(liste_exemple())

#print([(x,y) for x in [1,2,3] for y in [3,1,4] if x !=y])

def equivalence1 ():
    l =[]
    for x in [1,2,3]:
        for y in [3,1,4]: 
            if x!=y:
                l.append((x,y))
    return l

#print(equivalence1())

def liste2():
    vec = [-5,-4,-3,-2,-1,0,1,2,3,4,5]
    l=[]
    for i in vec :
        l.append(i**2)
    
    print(l)
    print([x for x in vec if x>0])
    print([abs(x) for x in vec])
    print([str(round(pi, i)) for i in range (1,10)])
    

#liste2()
    
def listes_imbriquées():
    matrix  = [[1,2,3,4,5],[6,7,8,9, 10],[11,12,13,14,15]]
    print (matrix)
    matrix2 = [[row[i] for row in matrix] for i in range(4)]
    print(matrix2)
    
    transpose = []
    for i in range (len(matrix)):
        transpose.append([row[i]for row in matrix])
    print (transpose)

#listes_imbriquées()

def comprehension_tuple(): 
    """
    pour comprendre les tuples ou n-uplets
    """
    t = (12345 , 54321, 'karen', 'hugo')
    print (t)

#comprehension_tuple()


def comprehension_ensemble():  
    basket = {'apple', 'orange', 'apple'}
    basket2 = {'pomme', 'pêche', 'abricot'}
    print (basket)
    print('orange' in basket2)
    basket3 = set('lambrequin')
    print(basket3)

#comprehension_ensemble()  
    
def comprehension_dico(): 
    # un dictionnaire dpit être pris comme un ensemble de clé/valeur. 
    #suppression d'une clé valeur avec del
    knights = {'gallahad': 'the pure', 'robin': 'the brave'}
    for k, v in knights.items():
        print(k, v)
        
    for i, v in enumerate(['tic', 'tac', 'toe']):
        print(i, v)
        
        
    questions = ['name', 'quest', 'favorite color']
    answers = ['lancelot', 'the holy grail', 'blue']
    for q, a in zip(questions, answers):
        print('What is your {0}?  It is {1}.'.format(q, a))
        
    for i in reversed(range(1, 10, 2)):
        print(i)
        
    basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
    for f in sorted(set(basket)):
        print(f)
    
comprehension_dico()