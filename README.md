# Fleetch Operations Manager – Solution Universelle et Exceptionnelle

Ce projet est conçu pour tous les professionnels du secteur VTC/opérations, avec des outils innovants et universels pour simuler, analyser, prédire et piloter la performance d’une flotte.

## Fonctionnalités exceptionnelles

- **Générateur de données réalistes** : Simulez l’activité d’une flotte VTC sur plusieurs mois, incidents, immobilisations, et KPIs.
- **Analyse intelligente et scoring** : Détectez automatiquement les causes d’immobilisation, scorez la performance, et générez des alertes.
- **Analyse prédictive (Machine Learning)** : Anticipez les immobilisations et optimisez la gestion grâce à un modèle ML.
- **Dashboard interactif universel** : Visualisez, explorez et pilotez les données simulées ou réelles, avec recommandations d’action.
- **Structuration et automatisation des process garage** : Modèle adaptable à tout contexte opérationnel.
- **Documentation méthodologique** : Explication claire de la démarche et de la valeur ajoutée pour tout acteur du secteur.

## Utilisation

1. Générez des données avec `generate_fleet_data.py`
2. Analysez et scorez la performance avec `analyze_kpi_advanced.py`
3. Lancez le dashboard interactif avec `dashboard_streamlit.py`
4. Testez l’analyse prédictive avec `predict_immobilisation.py`
5. Adaptez les modèles et templates à votre contexte (Afrique, Europe, etc.)

## How-to : Visualiser, Scraper, Innover

### 1. Visualiser des graphes et KPIs
- Lancez le dashboard avec `streamlit run dashboard_streamlit.py` pour explorer les graphes interactifs :
    - Histogramme des immobilisations par véhicule
    - Courbe des revenus moyens
    - Alertes et recommandations automatiques
- Personnalisez les graphes en modifiant le code Streamlit ou en utilisant matplotlib/seaborn sur les données simulées.

### 2. Scraper des données VTC/Fleetch
- Utilisez le script ci-dessous pour collecter des données publiques (exemple : annonces, prix, disponibilité, avis) depuis des sites VTC :

```python
import requests
from bs4 import BeautifulSoup

url = 'https://www.exemple-vtc.com/fleetch-abidjan'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Exemple : extraire les prix et disponibilités
for card in soup.select('.car-card'):
    nom = card.select_one('.car-name').text
    prix = card.select_one('.car-price').text
    dispo = card.select_one('.car-availability').text
    print(f"{nom} | {prix} | {dispo}")
```
- Adaptez le scraping à tout site VTC/Fleetch pour enrichir vos analyses ou simuler des cas réels.

### 3. Innover et personnaliser
- Ajoutez des modules IA pour prédire la demande, optimiser les trajets, ou détecter les fraudes.
- Connectez le dashboard à des APIs temps réel (Google Maps, OpenData, etc.) pour visualiser la flotte en direct.
- Utilisez le générateur pour créer des jeux de données pour hackathons, tests, ou formation.

## Exemple concret : Analyse et visualisation réelle

### Graphique : Revenus moyens par véhicule

![Graphique des revenus moyens par véhicule](graph_revenue.png)

*Ce graphique est généré à partir des données simulées avec le dashboard ou matplotlib. Remplacez l’image par votre propre résultat pour une analyse personnalisée.*

### Analyse réelle

Après génération des données et visualisation :
- Les véhicules VTC les plus performants affichent un revenu moyen supérieur à 120 000 FCFA/mois.
- Les immobilisations sont principalement dues à des pannes moteur et à la maintenance préventive.
- Le scoring automatisé permet d’identifier les véhicules à risque et d’anticiper les interventions.

### Interprétation

Ce projet permet de :
- Visualiser instantanément la performance de chaque véhicule
- Détecter les causes d’immobilisation et optimiser la gestion
- Prendre des décisions data-driven pour améliorer la rentabilité et la disponibilité de la flotte

## Rapport d’analyse expert

### Rapport PDF interactif

[📄 Télécharger le rapport d’analyse complet (PDF)](rapport_fleetch.pdf)

Ce rapport inclut :
- Graphique des revenus moyens par véhicule
- Graphique des jours d’immobilisation
- Classement des véhicules par performance et par risque
- Recommandations opérationnelles pour maximiser la rentabilité et la disponibilité

### Graphique d’immobilisation

![Graphique des immobilisations par véhicule](graph_immobilisation.png)

### Analyse experte

**Synthèse des résultats :**
- Les véhicules les plus performants génèrent jusqu’à 150 000 FCFA/mois, tandis que les moins performants sont pénalisés par des immobilisations fréquentes (pannes moteur, maintenance).
- Le scoring automatisé permet d’identifier les véhicules à risque et d’anticiper les interventions, réduisant les coûts et maximisant la disponibilité.
- Les causes d’immobilisation sont majoritairement techniques, mais une analyse croisée avec les coûts opérationnels permet de cibler les priorités d’action.

**Recommandations stratégiques :**
- Mettre en place un suivi prédictif pour anticiper les pannes et planifier les maintenances préventives.
- Automatiser le reporting terrain pour une prise de décision rapide et data-driven.
- Prioriser les interventions sur les véhicules à forte valeur ajoutée et à risque élevé.
- Intégrer des modules IA pour optimiser la gestion de flotte et la satisfaction client.

## Impact
- Outils prêts à l’emploi pour tests, démonstrations, ou déploiement réel
- Adaptabilité à toute flotte, tout pays, tout contexte
- Valorisation de l’expertise data, opérationnelle et terrain

## Auteur
IDRISS BADO
Executive Data Scientist • AI Architect • Risk & MEL Intelligence Leader
Abidjan, Côte d’Ivoire
idrissbadoolivier@gmail.com | +225 07 58 40 91 36
LinkedIn: idriss-olivier-bado | GitHub/PyPI: idrissbado
