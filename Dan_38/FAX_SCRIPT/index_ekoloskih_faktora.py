import pandas as pd

# Učitavanje CSV datoteke
df = pd.read_csv("Dan_38/Book1.csv")

# Grupisanje podataka po broju snimka
grouped = df.groupby("Broj_snimka")

# Dictionary za čuvanje rezultata prosečnih vrednosti po snimku za svaki parametar
avg_values = {}

# Iteriranje kroz grupe
for broj_snimka, group in grouped:
    # Izračunavanje prosečnih vrednosti za svaki parametar
    avg_values[broj_snimka] = {}
    for parametar in ['Vlažnost_Kojić1997', 'Kiselost_Kojić1997', 'Azot_Kojić1997', 'Svetlost_Kojić1997', 'Temperatura_Kojić1997']:
        sum_cov_param = (group['Pokrovnost'] * group[parametar]).sum()
        sum_cov = group['Pokrovnost'].sum()
        avg_values[broj_snimka][parametar] = sum_cov_param / sum_cov

# Ispis prosečnih vrednosti za svaki snimak za sve parametre
for broj_snimka, values in avg_values.items():
    print(f"Prosečne vrednosti za snimak broj {broj_snimka}:")
    for parametar, avg_value in values.items():
        print(f"{parametar}: {avg_value}")

# Konvertovanje u DataFrame i čuvanje u CSV i Excel formatu
avg_values_df = pd.DataFrame(avg_values).T

# Promena imena prvog reda (zaglavlja) u DataFrame-u
avg_values_df.columns = ['Vlaznost', 'kiselost', 'azot', 'svetlost', 'temperatura']

# Čuvanje u CSV formatu sa promenjenim zaglavljem
avg_values_df.to_csv("Dan_38/prosecne_vrednosti.csv", header=True, index=True)

# Čuvanje u Excel formatu sa promenjenim zaglavljem
avg_values_df.to_excel("Dan_38/prosecne_vrednosti.xlsx", header=True, index=True)
