"""
Module d’analyse prédictive pour immobilisation de flotte VTC
Auteur : Idriss Bado
"""
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

# Charger les données simulées
fleet_df = pd.read_csv('fleet_data_simulated.csv')

# Préparation des features
fleet_df['immobilise'] = fleet_df['immobilisation_jours'] > 0
X = fleet_df[['revenu', 'couts_operationnels']]
y = fleet_df['immobilise']

# Split train/test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Modèle prédictif
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

# Prédictions et rapport
y_pred = clf.predict(X_test)
print(classification_report(y_test, y_pred))

# Exemple : prédire immobilisation pour un nouveau véhicule
sample = pd.DataFrame({'revenu': [100000], 'couts_operationnels': [30000]})
pred = clf.predict(sample)
print(f"Immobilisation prédite : {'Oui' if pred[0] else 'Non'}")
