# 📚 WebScrapingBooks - Books to Scrape Dashboard

Un projet de web scraping et d'analyse de données de livres provenant du site [Books to Scrape](http://books.toscrape.com/), avec un dashboard interactif construit avec Streamlit.

## 🎯 Objectif du Projet

Ce projet permet de :
- Scraper automatiquement les données de livres (titre, prix, notation, disponibilité, etc.)
- Sauvegarder les données dans un fichier CSV
- Visualiser et analyser les données à travers un dashboard interactif
- Explorer les relations entre prix et notations
- Filtrer et télécharger les données

## ✨ Fonctionnalités

### Web Scraper (`scraper.py`)
- ✅ Scraping multi-pages automatique
- ✅ Extraction de données détaillées pour chaque livre :
  - Titre, prix, notation
  - Disponibilité
  - URL du livre et de l'image
  - UPC (Universal Product Code)
  - Nombre d'avis
  - Description complète
- ✅ Sauvegarde automatique en CSV
- ✅ Gestion d'erreurs robuste

### Dashboard Analytique (`dashboard.py`)
- 📊 **Statistiques générales** : nombre de livres, prix moyen, notation moyenne
- 📈 **Visualisations interactives** :
  - Distribution des prix (histogramme et box plot)
  - Répartition des notations (bar chart et pie chart)
  - Analyse de corrélation prix vs notation (scatter plot)
  - Top 10 des livres les mieux notés et les plus chers
- 🖼️ **Galerie de livres** avec images
- 🔍 **Filtrage dynamique** par prix et notation
- 💾 **Export des données filtrées** en CSV

## 🛠️ Technologies Utilisées

- **Python 3.x**
- **Web Scraping** :
  - `requests` - Requêtes HTTP
  - `BeautifulSoup4` - Parsing HTML
- **Data Analysis** :
  - `pandas` - Manipulation de données
- **Visualisation** :
  - `streamlit` - Dashboard interactif
  - `plotly` - Graphiques interactifs
- **Utilities** :
  - `urllib` - Gestion des URLs

## 📋 Prérequis

- Python 3.7 ou supérieur
- pip (gestionnaire de paquets Python)

## 🚀 Installation

1. **Cloner le repository**
```bash
git clone https://github.com/lafkiar-rachid1/WebScrapingBooks.git
cd WebScrapingBooks
```

2. **Créer un environnement virtuel (recommandé)**
```bash
python -m venv venv

# Sur Windows
venv\Scripts\activate

# Sur macOS/Linux
source venv/bin/activate
```

3. **Installer les dépendances**
```bash
pip install -r requirements.txt
```

## 💻 Utilisation

### Option 1 : Scraping uniquement

Pour scraper les données et les sauvegarder en CSV :

```bash
python scraper.py
```

Cela créera un fichier `books_data.csv` avec les données de 5 pages (modifiable dans le code).

### Option 2 : Dashboard interactif

Pour lancer le dashboard Streamlit :

```bash
streamlit run dashboard.py
```

Le dashboard s'ouvrira automatiquement dans votre navigateur par défaut.

### Fonctionnalités du Dashboard

1. **Charger des données existantes** : Utilise le fichier `books_data.csv` existant
2. **Nouveau scraping** : Lance un nouveau scraping avec un nombre de pages personnalisable
3. **Visualisations** : Explorez différents graphiques et analyses
4. **Filtrage** : Filtrez les livres par prix et notation
5. **Export** : Téléchargez les données filtrées en CSV

## 📁 Structure du Projet

```
webScrapingbooks/
│
├── scraper.py              # Script de web scraping
├── dashboard.py            # Application Streamlit
├── books_data.csv          # Données scrapées (généré)
├── requirements.txt        # Dépendances Python
├── README.md              # Ce fichier
│
└── __pycache__/           # Cache Python (ignoré)