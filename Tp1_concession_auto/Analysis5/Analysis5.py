# coding: utf-8

# # Analyse 5

# In[1]:

# activation du mode d'affichage intégré pour matplotlib


# In[6]:

# importation des bibliothèques nécessaires
import os
import sys
import subprocess
import stat
import glob
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


# In[9]:

# concaténation des fichiers de la même marque
search_term = str(sys.argv[1])
# search_term = "audi"
path = homefolder_path + "/CleanData/DataForAnalysis/" + search_term # utilisez votre chemin
allFiles = glob.glob(path + "/*.csv")
frame = pd.DataFrame()
list_ = []
for file_ in allFiles:
    df = pd.read_csv(file_,index_col=None, header=0)
    list_.append(df)
frame = pd.concat(list_)


# In[15]:

frame.head(2)


# In[28]:

# couleurs = ["#47d147", "#ff8c1a","#a180cc"]
colors = ["bleu windows", "ambre", "grisâtre", "vert délavé", "violet poussiéreux"]
fig, ax = plt.subplots(figsize=(8,5))
sns.set_palette(sns.xkcd_palette(colors))
sns.stripplot(x="vehicleType", y="NoOfDaysOnline", hue="gearbox", split=True, data=frame, size=8, alpha=0.5, jitter=True)
ax.set_title("Nombre de jours qu'une annonce reste en ligne avant que les véhicules de la marque " + search_term + " soient vendus")
plt.show()


# In[27]:

# enregistrement du graphique
fig.savefig((abs_path + "/Plots/vehicletype-NoOfDaysOnline.png"))


# In[ ]:


