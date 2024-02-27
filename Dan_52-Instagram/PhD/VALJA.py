import pandas as pd
from itertools import combinations
from scipy.cluster.hierarchy import dendrogram, linkage
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import os

# Učitavanje Excel tabele
ppath = "Dan_52-Instagram/PhD/floristicka_slicnost_50x50.xlsx"
df = pd.read_excel(ppath)

# Filtriranje tabele po koloni 'UTM_50x50'
filtered_df = df[df['UTM_50x50'].notnull()]

# Izdvajanje jedinstvenih vrednosti 'UTM_50x50'
unique_values = filtered_df['UTM_50x50'].unique()

# Dictionary za čuvanje jedinstvenih 'PunNazivTaksona' za svaku jedinstvenu 'UTM_50x50'
unique_pun_dict = {}

# Iteriranje kroz svaku jedinstvenu vrednost 'UTM_50x50'
for utm_value in unique_values:
    # Filtriranje DataFrame-a za trenutnu 'UTM_50x50' vrednost
    temp_df = filtered_df[filtered_df['UTM_50x50'] == utm_value]
    # Izdvajanje jedinstvenih vrednosti 'PunNazivTaksona' i dodavanje u dictionary
    unique_pun_dict[utm_value] = temp_df['PunNazivTaksona'].unique().tolist()

# Izračunavanje Jaccardovih indeksa za svaki UTM_50x50
jaccard_indices = []
for i, (utm_value1, pun_list1) in enumerate(unique_pun_dict.items()):
    for utm_value2, pun_list2 in list(unique_pun_dict.items())[i+1:]:
        common_items = set(pun_list1).intersection(pun_list2)
        unique_items = set(pun_list1 + pun_list2)
        jaccard_index = len(common_items) / len(unique_items)
        jaccard_indices.append(jaccard_index)

# Napravi dendrogram
Z = linkage(jaccard_indices, method='average')
plt.figure(figsize=(10, 6))
dendrogram(Z, labels=list(unique_pun_dict.keys()), orientation='right')
plt.title('Dendrogram za UTM_50x50')
plt.xlabel('UTM_50x50')
plt.ylabel('Udaljenost')
plt.xticks(rotation=90)
plt.show()

# Napravi heatmapu odnosa svih UTM_50x50 i sačuvaj je kao sliku
matrix = np.zeros((len(unique_values), len(unique_values)))
for i, utm_value1 in enumerate(unique_values):
    for j, utm_value2 in enumerate(unique_values):
        if i != j:
            common_items = set(unique_pun_dict[utm_value1]).intersection(unique_pun_dict[utm_value2])
            unique_items = set(unique_pun_dict[utm_value1] + unique_pun_dict[utm_value2])
            jaccard_index = len(common_items) / len(unique_items)
            matrix[i, j] = jaccard_index

plt.figure(figsize=(10, 8))
sns.heatmap(matrix, annot=True, cmap="YlGnBu", xticklabels=unique_values, yticklabels=unique_values)
plt.title("Heatmapa odnosa svih UTM_50x50")
plt.xlabel("UTM_50x50")
plt.ylabel("UTM_50x50")
plt.show()
