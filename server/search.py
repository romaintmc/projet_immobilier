import pandas as pd

def villes(PATH):
    df = pd.read_csv(PATH, low_memory=False, sep=',')
    return df['Ville'].unique().tolist()

def quartier(ville, PATH):
    df = pd.read_csv(PATH, low_memory=False, sep=',')
    ville_quartier = df[df['Ville'] == ville]
    return ville_quartier['Quartier'].unique().tolist()

def prix(ville, quartier, PATH):
    df = pd.read_csv(PATH, low_memory=False, sep=',')
    prix_df = df[(df['Ville'] == ville) & (df['Quartier'] == quartier)]
    if prix_df.empty:
        return None
    return prix_df['Prix'].mean()
