# coding: utf-8

# # Analyse 1

# ## Quelques analyses générales rencontrées lors du nettoyage des données

# In[24]:

# get_ipython().magic('matplotlib inline')

# In[19]:

# importation des bibliothèques requises
import os
import subprocess
import stat
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime
sns.set(style="white")

# In[20]:

# chemin absolu jusqu'au dossier parent
abs_path = os.getcwd()
path_array = abs_path.split("/")
path_array = path_array[:len(path_array)-1]
homefolder_path = ""
for i in path_array[1:]:
    homefolder_path = homefolder_path + "/" + i   

# In[22]:

# chemin vers les données nettoyées
clean_data_path = homefolder_path + "/CleanData/CleanedDataSet/cleaned_autos.csv"

# lecture du csv dans un dataframe brut
df = pd.read_csv(clean_data_path,encoding="latin-1")

# ## Distribution des véhicules basée sur l'année d'enregistrement

# In[64]:

# Distribution des véhicules basée sur l'année d'enregistrement
fig, ax = plt.subplots(figsize=(8,6))
sns.distplot(df["yearOfRegistration"], color="#33cc33",kde=True, ax=ax)
ax.set_title('Distribution des véhicules basée sur l'année d’enregistrement', fontsize= 15)
plt.ylabel("Densité (KDE)", fontsize= 15)
plt.xlabel("Année d'enregistrement", fontsize= 15)
plt.show()

# In[33]:

# sauvegarde du graphique
fig.savefig(abs_path + "/Plots/vehicle-distribution.png")

# ## Variation de la fourchette de prix par type de véhicule

# In[44]:

# Boîte à moustaches pour voir la distribution après avoir retiré les valeurs aberrantes
sns.set_style("whitegrid")
fig, ax = plt.subplots(figsize=(8,6))
sns.boxplot(x="vehicleType", y="price", data=df)
ax.text(5.25,27000,"Boîte à moustaches après retrait des valeurs aberrantes",fontsize=18,color="r",ha="center", va="center")
plt.show()

# In[45]:

# sauvegarde du graphique
fig.savefig(abs_path + "/Plots/price-vehicleType-boxplot.png")

# ## Nombre total de véhicules par type disponibles à la vente sur eBay

# In[53]:

# Graphique en bâtons pour montrer le nombre de véhicules appartenant à chaque type de véhicule
sns.set_style("white")
g = sns.factorplot(x="vehicleType", data=df, kind="count",
                   palette="BuPu", size=6, aspect=1.5)
# pour obtenir les comptes sur le haut des barres
for p in g.ax.patches:
    g.ax.annotate((p.get_height()), (p.get_x()+0.1, p.get_height()+500))

# In[54]:

# sauvegarde du graphique
g.savefig(abs_path + "/Plots/count-vehicleType.png")

# In[ ]:

