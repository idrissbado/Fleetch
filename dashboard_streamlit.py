"""
Dashboard interactif Streamlit pour Fleetch
Visualisation des KPIs, immobilisations, et recommandations
Auteur : Idriss Bado
"""
import streamlit as st
import pandas as pd

# Exemple de données
DATA = {
    'vehicule_id': [1, 2, 3, 4],
    'revenu': [120000, 0, 95000, 110000],
    'immobilisation_jours': [0, 12, 2, 1],
    'score_performance': [120000, 0, 47500, 55000],
    'cause_immobilisation': ['-', 'panne moteur', '-', 'maintenance']
}
df = pd.DataFrame(DATA)

st.title("Fleetch – Dashboard Opérationnel")
st.subheader("KPIs de la flotte VTC")
st.dataframe(df)

st.write("## Visualisation des immobilisations")
st.bar_chart(df.set_index('vehicule_id')['immobilisation_jours'])

st.write("## Recommandations d’action")
for idx, row in df.iterrows():
    if row['score_performance'] < 50000:
        st.warning(f"Véhicule {row['vehicule_id']} : performance faible, intervention recommandée.")
    elif row['immobilisation_jours'] > 5:
        st.info(f"Véhicule {row['vehicule_id']} : immobilisation prolongée, vérifier la cause.")
