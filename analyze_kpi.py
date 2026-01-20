"""
Script d'analyse des KPIs business et opérationnels pour Fleetch
Auteur : Idriss Bado
"""
import pandas as pd

# Exemple de structure de données (à remplacer par vos données réelles)
data = {
    'vehicule_id': [1, 2, 3],
    'actif': [True, False, True],
    'revenu': [120000, 0, 95000],
    'immobilisation_jours': [0, 12, 2],
    'couts_operationnels': [30000, 5000, 25000]
}
df = pd.DataFrame(data)

# Calculs de KPIs
nb_vehicules = len(df)
taux_immobilisation = df['immobilisation_jours'].sum() / (nb_vehicules * 30)
revenu_moyen = df['revenu'].mean()
couts_moyens = df['couts_operationnels'].mean()

print(f"Nombre de véhicules : {nb_vehicules}")
print(f"Taux d'immobilisation : {taux_immobilisation:.2%}")
print(f"Revenu moyen par véhicule : {revenu_moyen:.0f} FCFA")
print(f"Coûts opérationnels moyens : {couts_moyens:.0f} FCFA")
