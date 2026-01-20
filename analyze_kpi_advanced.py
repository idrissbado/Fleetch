"""
Analyse intelligente des KPIs pour Fleetch
Détection automatique des causes d’immobilisation et scoring de performance
Auteur : Idriss Bado
"""
import pandas as pd
import numpy as np

# Exemple de données (à remplacer par vos exports réels)
data = {
    'vehicule_id': [1, 2, 3, 4],
    'actif': [True, False, True, True],
    'revenu': [120000, 0, 95000, 110000],
    'immobilisation_jours': [0, 12, 2, 1],
    'cause_immobilisation': ['-', 'panne moteur', '-', 'maintenance']
}
df = pd.DataFrame(data)

# Scoring de performance
score = (df['revenu'] / (df['immobilisation_jours'] + 1)).apply(lambda x: min(x, 100000))
df['score_performance'] = score

# Détection automatique des causes majeures d’immobilisation
immobilisations = df[df['immobilisation_jours'] > 0]
causes = immobilisations['cause_immobilisation'].value_counts()

print("--- Analyse KPI Fleetch ---")
print(df[['vehicule_id', 'revenu', 'immobilisation_jours', 'score_performance']])
print("\nPrincipales causes d’immobilisation :")
print(causes)

if any(df['score_performance'] < 50000):
    print("\nAlerte : Certains véhicules ont une performance faible, intervention recommandée !")
