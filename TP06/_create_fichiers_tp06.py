#!/usr/bin/env python
# coding: utf-8

# * création de la liste des fichiers annexes (présents dans un répertoire `_fichiers_`

# In[1]:


import os


# In[2]:


for s in os.listdir():
    if '_fichiers_' in s and os.path.isdir(s):
        s0 = s
        L = os.listdir(s0)
print(L)
f = open(s0 + '.txt', 'w')
for file in L:
    f.write(file + '\n')
f.close()

