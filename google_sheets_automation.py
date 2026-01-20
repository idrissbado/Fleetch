"""
Exemple d'automatisation Google Sheets pour Fleetch
Auteur : Idriss Bado
"""
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Connexion à Google Sheets (remplacer par vos identifiants et nom de feuille)
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
client = gspread.authorize(creds)

sheet = client.open("Fleetch KPIs").sheet1

# Exemple : ajouter une ligne de KPI
sheet.append_row(["2026-01-20", "Véhicule 1", 120000, 0, 30000])

print("Ligne KPI ajoutée à Google Sheets.")
