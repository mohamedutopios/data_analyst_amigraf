# coding: utf-8

# In[1]:

# activation du mode d'affichage intégré pour matplotlib


# In[2]:

# importation des bibliothèques nécessaires
import os
import subprocess
import stat
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime
sns.set(style="white")


# In[3]:

# chemin absolu jusqu'au dossier parent
abs_path = os.getcwd()
path_array = abs_path.split("/")
path_array = path_array[:len(path_array)-1]
homefolder_path = ""
for i in path_array[1:]:
    homefolder_path = homefolder_path + "/" + i 


# In[4]:

# chemin vers les données nettoyées
clean_data_path = homefolder_path + "/CleanData/CleanedDataSet/cleaned_autos.csv"

# lecture du fichier csv dans un dataframe brut
df = pd.read_csv(clean_data_path,encoding="latin-1")


# ## Prix moyen des véhicules en fonction du type de carburant et du type de boîte de vitesses

# In[9]:

# graphique en barres pour le prix en fonction du type de carburant et du type de boîte de vitesses
fig, ax = plt.subplots(figsize=(8,5))
colors = ["#00e600", "#ff8c1a","#a180cc"]
sns.barplot(x="fuelType", y="price",hue="gearbox", palette="husl",data=df)
ax.set_title("Prix moyen des véhicules par type de carburant et type de boîte de vitesses")
plt.show()


# In[8]:

# enregistrement du graphique
fig.savefig((abs_path + "/Plots/vehicletype-fueltype-price.png"))


# ## Puissance moyenne d'un véhicule en fonction du type de véhicule et du type de boîte de vitesses

# In[18]:

# graphique en barres pour la puissance en fonction du type de véhicule et du type de boîte de vitesses
colors = ["bleu windows", "ambre", "grisâtre", "vert délavé", "violet poussiéreux"]
fig, ax = plt.subplots(figsize=(8,5))
sns.set_palette(sns.xkcd_palette(colors))
sns.barplot(x="vehicleType", y="powerPS",hue="gearbox",data=df)
ax.set_title("Puissance moyenne des véhicules par type de véhicule et type de boîte de vitesses")
plt.show()


# In[19]:

# enregistrement du graphique
fig.savefig((abs_path + "/Plots/vehicletype-fueltype-power.png"))


# In[ ]:


