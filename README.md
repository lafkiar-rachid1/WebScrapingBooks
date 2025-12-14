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
```

## 📊 Exemple de Données

Le scraper collecte les informations suivantes pour chaque livre :

| Colonne | Description | Exemple |
|---------|-------------|---------|
| titre | Titre du livre | "A Light in the Attic" |
| prix | Prix en livres sterling | 51.77 |
| notation | Note sur 5 étoiles | 3 |
| disponibilite | Statut de disponibilité | "In stock" |
| url | Lien vers la page du livre | http://books.toscrape.com/... |
| image_url | URL de l'image de couverture | http://books.toscrape.com/media/... |
| upc | Code produit universel | a897fe39b1053632 |
| avis | Nombre d'avis | 0 |
| description | Description complète du livre | "It's hard to imagine..." |

## 📈 Analyses Disponibles

Le dashboard offre plusieurs types d'analyses :

- **Distribution des prix** : Identifiez les tendances de prix
- **Répartition des notations** : Comprenez la qualité globale du catalogue
- **Corrélation prix/notation** : Analysez si les livres chers sont mieux notés
- **Tops** : Découvrez les meilleurs livres et les plus chers
- **Statistiques filtrées** : Analyses personnalisées selon vos critères

## ⚙️ Configuration

### Modifier le nombre de pages à scraper

Dans `scraper.py`, ligne finale :
```python
scraper.scrape_all_pages(max_pages=5)  # Changez ce nombre
```

### Personnaliser le délai entre les requêtes

Dans `scraper.py`, méthode `scrape_all_pages()` :
```python
time.sleep(0.5)  # Augmentez pour réduire la charge sur le serveur
```

## 🤝 Contribution

Les contributions sont les bienvenues ! N'hésitez pas à :
1. Fork le projet
2. Créer une branche pour votre fonctionnalité (`git checkout -b feature/AmazingFeature`)
3. Commit vos changements (`git commit -m 'Add some AmazingFeature'`)
4. Push vers la branche (`git push origin feature/AmazingFeature`)
5. Ouvrir une Pull Request

## 📝 Notes

- Le site [Books to Scrape](http://books.toscrape.com/) est un site d'entraînement spécialement conçu pour apprendre le web scraping
- Respectez toujours les délais entre les requêtes pour ne pas surcharger le serveur
- Les données sont à usage éducatif uniquement

## 🐛 Problèmes Connus

- Si le scraping échoue, vérifiez votre connexion internet
- Certaines pages peuvent mettre du temps à charger, soyez patient
- Si le dashboard ne s'affiche pas correctement, essayez de relancer Streamlit

## 📧 Contact

**Rachid LAFKIAR**
- GitHub: [@lafkiar-rachid1](https://github.com/lafkiar-rachid1)

## 📄 License

Ce projet est sous licence MIT - voir le fichier LICENSE pour plus de détails.

## 🙏 Remerciements

- [Books to Scrape](http://books.toscrape.com/) pour fournir un site d'entraînement au web scraping
- La communauté Streamlit pour les excellents outils de visualisation
- Tous les contributeurs qui ont aidé à améliorer ce projet

---

⭐ **Si ce projet vous a été utile, n'hésitez pas à lui donner une étoile !**
