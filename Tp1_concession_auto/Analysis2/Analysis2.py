# coding: utf-8

# # Analyse 2

# In[7]:

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


# In[6]:

# chemin vers les données nettoyées
clean_data_path = homefolder_path + "/CleanData/CleanedDataSet/cleaned_autos.csv"

# lecture du fichier csv dans un dataframe brut
df = pd.read_csv(clean_data_path,encoding="latin-1")


# ## Nombre de véhicules par marque disponibles à la vente sur eBay

# In[50]:

# Graphique en barres pour montrer le nombre de véhicules appartenant à chaque marque
sns.set_style("whitegrid")
g = sns.factorplot(y="brand", data=df, kind="count",
                   palette="Reds_r", size=7, aspect=1.5)
g.ax.set_title("Nombre de véhicules par marque",fontdict={'size':18})
# pour chaque barre dans le graphique
# g.ax.annotate((largeur de la barre), (position x de la barre, position y de la barre))


# In[51]:

# enregistrement du graphique
g.savefig((abs_path + "/Plots/brand-vehicleCount.png"))


# ## Prix moyen des véhicules en fonction du type de véhicule et du type de boîte de vitesses

# In[62]:

fig, ax = plt.subplots(figsize=(8,5))
colors = ["#00e600", "#ff8c1a","#a180cc"]
sns.barplot(x="vehicleType", y="price",hue="gearbox", palette=colors, data=df)
ax.set_title("Prix moyen des véhicules par type de véhicule et type de boîte de vitesses")
plt.show()


# In[64]:

# enregistrement du graphique
fig.savefig((abs_path + "/Plots/vehicletype-gearbox-price.png"))


# In[ ]:


