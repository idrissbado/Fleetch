"""
Générateur de données réalistes pour flotte VTC Fleetch
Auteur : Idriss Bado
"""
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# Paramètres de simulation
N_VEHICULES = 50
N_JOURS = 90
start_date = datetime(2025, 10, 1)

vehicules = [f"VTC-{i+1:03d}" for i in range(N_VEHICULES)]
data = []

for v in vehicules:
    immobilisation_total = 0
    for j in range(N_JOURS):
        date = start_date + timedelta(days=j)
        actif = random.choices([True, False], weights=[0.95, 0.05])[0]
        immobilisation = 0 if actif else random.randint(1, 5)
        revenu = random.randint(80000, 150000) if actif else 0
        couts = random.randint(20000, 40000)
        cause = '-' if actif else random.choice(['panne moteur', 'accident', 'maintenance', 'pneu crevé'])
        data.append({
            'date': date.strftime('%Y-%m-%d'),
            'vehicule_id': v,
            'actif': actif,
            'revenu': revenu,
            'immobilisation_jours': immobilisation,
            'cause_immobilisation': cause,
            'couts_operationnels': couts
        })

# Export CSV
fleet_df = pd.DataFrame(data)
fleet_df.to_csv('fleet_data_simulated.csv', index=False)
print(f"Données simulées générées : {len(fleet_df)} lignes, {N_VEHICULES} véhicules sur {N_JOURS} jours.")
