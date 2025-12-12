import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from scraper import BooksScraper
import os

# Configuration de la page
st.set_page_config(
    page_title="Books Analytics Dashboard",
    page_icon="",
    layout="wide"
)

# Titre principal
st.title(" Books to Scrape - Dashboard Analytique")

# Sidebar pour les contrôles
st.sidebar.header(" Contrôles")

# Fonction pour charger les données
@st.cache_data
def load_data(csv_file='books_data.csv'):
    if os.path.exists(csv_file):
        return pd.read_csv(csv_file)
    return None

# Option pour scraper ou charger les données
action = st.sidebar.radio(
    "Action:",
    ["Charger données existantes", "Nouveau scraping"]
)

df = None

if action == "Nouveau scraping":
    max_pages = st.sidebar.number_input(
        "Nombre de pages à scraper:",
        min_value=1,
        max_value=50,
        value=5
    )
    
    if st.sidebar.button(" Lancer le scraping"):
        with st.spinner("Scraping en cours..."):
            scraper = BooksScraper()
            scraper.scrape_all_pages(max_pages=max_pages)
            df = scraper.save_to_csv('books_data.csv')
            st.sidebar.success(f" {len(df)} livres scrapés!")
            st.rerun()

else:
    df = load_data()
    if df is None:
        st.warning(" Aucune donnée trouvée. Veuillez d'abord lancer un scraping.")
        st.stop()

# Afficher les données si disponibles
if df is not None and not df.empty:
    
    # Statistiques globales
    st.header(" Statistiques Générales")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Nombre total de livres", len(df))
    
    with col2:
        st.metric("Prix moyen", f"£{df['prix'].mean():.2f}")
    
    with col3:
        st.metric("Notation moyenne", f"{df['notation'].mean():.2f}/5")
    
    with col4:
        st.metric("Prix maximum", f"£{df['prix'].max():.2f}")
    
    # Graphiques
    st.header(" Visualisations")
    
    tab1, tab2, tab3, tab4 = st.tabs([
        "Distribution des prix",
        "Notations",
        "Prix vs Notation",
        "Top livres"
    ])
    
    with tab1:
        col1, col2 = st.columns(2)
        
        with col1:
            # Histogramme des prix
            fig_hist = px.histogram(
                df,
                x='prix',
                nbins=30,
                title="Distribution des prix des livres",
                labels={'prix': 'Prix (£)', 'count': 'Nombre de livres'},
                color_discrete_sequence=['#1f77b4']
            )
            fig_hist.update_layout(showlegend=False)
            st.plotly_chart(fig_hist, use_container_width=True)
        
        with col2:
            # Box plot des prix
            fig_box = px.box(
                df,
                y='prix',
                title="Répartition des prix (Box Plot)",
                labels={'prix': 'Prix (£)'},
                color_discrete_sequence=['#ff7f0e']
            )
            st.plotly_chart(fig_box, use_container_width=True)
    
    with tab2:
        col1, col2 = st.columns(2)
        
        with col1:
            # Distribution des notations
            rating_counts = df['notation'].value_counts().sort_index()
            fig_ratings = px.bar(
                x=rating_counts.index,
                y=rating_counts.values,
                title="Distribution des notations",
                labels={'x': 'Notation (étoiles)', 'y': 'Nombre de livres'},
                color=rating_counts.values,
                color_continuous_scale='Viridis'
            )
            fig_ratings.update_layout(showlegend=False)
            st.plotly_chart(fig_ratings, use_container_width=True)
        
        with col2:
            # Pie chart des notations
            fig_pie = px.pie(
                values=rating_counts.values,
                names=rating_counts.index,
                title="Répartition des notations (%)",
                hole=0.4
            )
            st.plotly_chart(fig_pie, use_container_width=True)
    
    with tab3:
        # Scatter plot prix vs notation
        fig_scatter = px.scatter(
            df,
            x='notation',
            y='prix',
            title="Relation entre Prix et Notation",
            labels={'notation': 'Notation (étoiles)', 'prix': 'Prix (£)'},
            color='notation',
            size='prix',
            hover_data=['titre'],
            color_continuous_scale='RdYlGn'
        )
        st.plotly_chart(fig_scatter, use_container_width=True)
        
        # Calculer la corrélation
        correlation = df['prix'].corr(df['notation'])
        st.info(f" Coefficient de corrélation: {correlation:.3f}")
    
    with tab4:
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader(" Top 10 - Livres les mieux notés")
            top_rated = df.nlargest(10, 'notation')[['titre', 'notation', 'prix']]
            top_rated.index = range(1, len(top_rated) + 1)
            st.dataframe(top_rated, use_container_width=True)
        
        with col2:
            st.subheader(" Top 10 - Livres les plus chers")
            top_expensive = df.nlargest(10, 'prix')[['titre', 'prix', 'notation']]
            top_expensive.index = range(1, len(top_expensive) + 1)
            st.dataframe(top_expensive, use_container_width=True)
    
    # Section d'affichage des livres avec images
    st.header("  Galerie de livres")
    
    # Sélectionner le nombre de livres à afficher
    num_books_display = st.slider("Nombre de livres à afficher", 5, 50, 20)
    
    # Vérifier si la colonne image_url existe
    if 'image_url' in df.columns:
        display_books = df.head(num_books_display)
        
        # Afficher les livres en grille
        cols_per_row = 5
        for i in range(0, len(display_books), cols_per_row):
            cols = st.columns(cols_per_row)
            for j, col in enumerate(cols):
                idx = i + j
                if idx < len(display_books):
                    book = display_books.iloc[idx]
                    with col:
                        # Afficher l'image
                        if book['image_url'] != "N/A":
                            st.image(book['image_url'], use_container_width=True)
                        else:
                            st.write(" Image non disponible")
                        
                        # Titre (tronqué)
                        title_short = book['titre'][:30] + "..." if len(book['titre']) > 30 else book['titre']
                        st.markdown(f"**{title_short}**")
                        
                        # Prix et notation
                        st.write(f" £{book['prix']:.2f}")
                        st.write(f" {book['notation']}/5")
    else:
        st.warning(" Les images ne sont pas disponibles. Veuillez relancer le scraping pour obtenir les URLs des images.")
    
    # Section de filtrage
    st.header(" Explorer les données")
    
    col1, col2 = st.columns(2)
    
    with col1:
        price_range = st.slider(
            "Filtrer par prix (£)",
            float(df['prix'].min()),
            float(df['prix'].max()),
            (float(df['prix'].min()), float(df['prix'].max()))
        )
    
    with col2:
        rating_filter = st.multiselect(
            "Filtrer par notation",
            options=sorted(df['notation'].unique()),
            default=sorted(df['notation'].unique())
        )
    
    # Appliquer les filtres
    filtered_df = df[
        (df['prix'] >= price_range[0]) & 
        (df['prix'] <= price_range[1]) & 
        (df['notation'].isin(rating_filter))
    ]
    
    st.subheader(f" Résultats filtrés: {len(filtered_df)} livres")
    
    # Afficher le tableau filtré
    if 'image_url' in filtered_df.columns:
        display_df = filtered_df[['titre', 'prix', 'notation', 'disponibilite', 'image_url']].copy()
        display_df.columns = ['Titre', 'Prix (£)', 'Notation', 'Disponibilité', 'Image URL']
    else:
        display_df = filtered_df[['titre', 'prix', 'notation', 'disponibilite']].copy()
        display_df.columns = ['Titre', 'Prix (£)', 'Notation', 'Disponibilité']
    
    st.dataframe(
        display_df,
        use_container_width=True,
        height=400
    )
    
    # Bouton de téléchargement
    csv = filtered_df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label=" Télécharger les données filtrées (CSV)",
        data=csv,
        file_name="books_filtered.csv",
        mime="text/csv"
    )
    
    # Statistiques sur les données filtrées
    st.subheader(" Statistiques des données filtrées")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Prix moyen", f"£{filtered_df['prix'].mean():.2f}")
    
    with col2:
        st.metric("Notation moyenne", f"{filtered_df['notation'].mean():.2f}/5")
    
    with col3:
        st.metric("Prix médian", f"£{filtered_df['prix'].median():.2f}")

else:
    st.info(" Utilisez la barre latérale pour charger ou scraper des données.")
