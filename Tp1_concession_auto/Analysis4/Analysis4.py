# Importation des bibliothèques nécessaires
import os  # Module pour interagir avec le système d'exploitation
import pandas as pd  # Bibliothèque pour la manipulation de données
import seaborn as sns  # Bibliothèque pour la visualisation de données statistiques
import matplotlib.pyplot as plt  # Module pour la création de graphiques
sns.set(style="white")  # Configuration du style des graphiques avec un fond blanc

# Chemin absolu jusqu'au dossier parent
abs_path = os.getcwd()  # Obtention du chemin du répertoire de travail actuel
path_array = abs_path.split("/")  # Découpage du chemin absolu en segments
path_array = path_array[:len(path_array)-1]  # Suppression du dernier segment pour remonter d'un niveau dans le chemin
homefolder_path = ""  # Initialisation du chemin du dossier parent
for i in path_array[1:]:  # Reconstruction du chemin du dossier parent
    homefolder_path = homefolder_path + "/" + i 

# Chemin vers les données nettoyées
clean_data_path = homefolder_path + "/CleanData/CleanedDataSet/cleaned_autos.csv"  # Construction du chemin complet vers le fichier de données

# Lecture du fichier CSV dans un dataframe brut
df = pd.read_csv(clean_data_path, encoding="latin-1")  # Lecture du fichier CSV avec l'encodage latin-1

# Préparation des données pour la carte thermique
trial = pd.DataFrame()  # Création d'un DataFrame vide
for b in list(df["brand"].unique()):  # Boucle sur chaque marque unique
    for v in list(df["vehicleType"].unique()):  # Boucle sur chaque type de véhicule unique
        z = df[(df["brand"] == b) & (df["vehicleType"] == v)]["price"].mean()  # Calcul du prix moyen
        new_row = pd.DataFrame({'brand': b, 'vehicleType': v, 'avgPrice': z}, index=[0])  # Création d'une nouvelle ligne avec les données calculées
        trial = pd.concat([trial, new_row], ignore_index=True)  # Ajout de la nouvelle ligne au DataFrame 'trial'

trial["avgPrice"].fillna(0, inplace=True)  # Remplacement des valeurs manquantes par 0 dans la colonne 'avgPrice'
trial["avgPrice"] = trial["avgPrice"].astype(int)  # Conversion de 'avgPrice' en entier

# Création de la carte thermique pour montrer les prix moyens des véhicules par marque et par type
tri = trial.pivot(index="brand", columns="vehicleType", values="avgPrice")  # Pivotement des données pour la visualisation
fig, ax = plt.subplots(figsize=(15,20))  # Création d'une figure et d'un axe pour le graphique avec une taille spécifiée
sns.heatmap(tri, linewidths=1, cmap="YlGnBu", annot=True, ax=ax, fmt="d")  # Création de la carte thermique avec les données pivotées
ax.set_title("Average price of vehicles by vehicle type and brand", fontdict={'size':18})  # Ajout d'un titre au graphique
plt.show()  # Affichage du graphique

# Sauvegarde du graphique
plot_path = abs_path + "/Plots/heatmap-price-brand-vehicleType.png"  # Définition du chemin pour sauvegarder l'image du graphique
os.makedirs(os.path.dirname(plot_path), exist_ok=True)  # Création du répertoire pour le graphique si celui-ci n'existe pas
fig.savefig(plot_path)  # Sauvegarde du graphique dans le fichier
