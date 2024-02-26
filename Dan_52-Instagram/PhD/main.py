
#! OVO RADI ISPOD!!!!!!! 
# import pandas as pd

# # Učitavanje Excel tabele
# file_path = "Dan_52-Instagram/PhD/floristicka_slicnost_50x50.xlsx"
# df = pd.read_excel(file_path)

# # Grupisanje po UTM_50x50 i brojanje različitih Punih Naziva Taksona
# grouped = df.groupby('UTM_50x50')['PunNazivTaksona'].agg(['nunique', 'unique']).reset_index()
# grouped.columns = ['UTM_50x50', 'BrojRazlicitihTaksona', 'JedinstveniTaksoni']

# # Ispisivanje rezultata
# for index, row in grouped.iterrows():
#     print(f"UTM_50x50: {row['UTM_50x50']}")
#     print(f"Broj Različitih Taksona: {row['BrojRazlicitihTaksona']}")
#     print("Jedinstveni Taksoni:")
#     for takson in row['JedinstveniTaksoni']:
#         print(f" - {takson}")
#     print("---------------------------")

# # Čuvanje rezultata u novu Excel datoteku
# grouped.to_excel('rezultati.xlsx', index=False)

import pandas as pd
from scipy.spatial.distance import pdist, squareform
from scipy.cluster.hierarchy import linkage, dendrogram
import seaborn as sns
import matplotlib.pyplot as plt

# Učitavanje Excel tabele
file_path = "Dan_52-Instagram/PhD/floristicka_slicnost_50x50.xlsx"
df = pd.read_excel(file_path)

# Zanemari UTM_10x10 kolonu
df = df.drop(columns=['UTM_10x10'])

# Kreiranje tabele sa brojem pojavljivanja jedinstvenih Punih Naziva Taksona za svaki UTM_50x50
table = df.pivot_table(index='UTM_50x50', columns='PunNazivTaksona', aggfunc='size', fill_value=0)

# Konvertujemo u binarnu matricu
binary_table = (table > 0).astype(int)

# Izračunavanje Jaccard-ovih indeksa sličnosti
jaccard_matrix = pdist(binary_table.values, metric='jaccard')

# Pretvaranje u kvadratnu matricu za dalju obradu
jaccard_square = squareform(jaccard_matrix)

# Klastiranje koristeći UPGMA algoritam
upgma = linkage(jaccard_square, method='average')

# Plotovanje dendrograma
plt.figure(figsize=(10, 7))
dend = dendrogram(upgma, labels=binary_table.index, orientation='right')  # Ovde je dodata orijentacija 'right'
plt.xlabel('Udaljenost')
plt.title('Dendrogram klastiranja po Jaccard-ovom indeksu sličnosti')
plt.tight_layout()
plt.savefig('dendrogram.png')
plt.show()

# Ispis Jaccard-ovih indeksa za kombinacije UTM_50x50 kvadrata
distances = pd.DataFrame(jaccard_square, index=binary_table.index, columns=binary_table.index)
print("Jaccard-ovi indeksi za kombinacije UTM_50x50 kvadrata:")
print(distances)

