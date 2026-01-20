"""
Dashboard interactif Streamlit pour Fleetch
Visualisation des KPIs, immobilisations, et recommandations
Auteur : Idriss Bado
"""
import streamlit as st
import pandas as pd
import os

st.title("Fleetch – Dashboard Opérationnel Universel")

# Charger les données simulées si disponibles
if os.path.exists('fleet_data_simulated.csv'):
    df = pd.read_csv('fleet_data_simulated.csv')
    st.success(f"Données simulées chargées : {len(df)} lignes")
    st.dataframe(df.head(50))
    st.write("## Visualisation des immobilisations par véhicule")
    immobilisation_sum = df.groupby('vehicule_id')['immobilisation_jours'].sum()
    st.bar_chart(immobilisation_sum)
    st.write("## Revenus moyens par véhicule")
    revenu_mean = df.groupby('vehicule_id')['revenu'].mean()
    st.line_chart(revenu_mean)
else:
    st.warning("Aucune donnée simulée trouvée. Veuillez générer les données avec generate_fleet_data.py.")

st.write("## Recommandations d’action universelles")
st.markdown("- Identifier les véhicules à faible performance pour intervention proactive\n- Utiliser l’analyse prédictive pour anticiper les immobilisations\n- Automatiser le reporting et le suivi terrain pour toute flotte VTC\n- Adapter le modèle à tout contexte opérationnel (Afrique, Europe, etc.)")
