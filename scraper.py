import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
from urllib.parse import urljoin

class BooksScraper:
    def __init__(self, base_url="http://books.toscrape.com/"):
        self.base_url = base_url
        self.books_data = []
    
    def get_rating_value(self, rating_class):
        """Convertir la classe de notation en valeur numérique"""
        ratings = {
            'One': 1,
            'Two': 2,
            'Three': 3,
            'Four': 4,
            'Five': 5
        }
        return ratings.get(rating_class, 0)
    
    def scrape_book_details(self, book_url):
        """Scraper les détails d'un livre spécifique"""
        try:
            response = requests.get(book_url)
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Extraire les informations du tableau produit
            product_info = {}
            table = soup.find('table', class_='table table-striped')
            if table:
                rows = table.find_all('tr')
                for row in rows:
                    th = row.find('th')
                    td = row.find('td')
                    if th and td:
                        product_info[th.text] = td.text
            
            # Description
            description = soup.find('div', id='product_description')
            desc_text = description.find_next('p').text if description else "N/A"
            
            return {
                'upc': product_info.get('UPC', 'N/A'),
                'availability': product_info.get('Availability', 'N/A'),
                'reviews': product_info.get('Number of reviews', '0'),
                'description': desc_text
            }
        except Exception as e:
            print(f"Erreur lors du scraping des détails: {e}")
            return {}
    
    def scrape_page(self, page_url):
        """Scraper une page de livres"""
        try:
            response = requests.get(page_url)
            soup = BeautifulSoup(response.content, 'html.parser')
            
            books = soup.find_all('article', class_='product_pod')
            
            for book in books:
                # Titre
                title = book.h3.a['title']
                
                # Prix
                price_text = book.find('p', class_='price_color').text
                price = float(price_text.replace('£', '').strip())
                
                # Notation
                rating_class = book.find('p', class_='star-rating')['class'][1]
                rating = self.get_rating_value(rating_class)
                
                # Disponibilité
                availability = book.find('p', class_='instock availability')
                in_stock = availability.text.strip() if availability else "N/A"
                
                # URL du livre
                book_link = book.h3.a['href']
                book_url = urljoin(page_url, book_link)
                
                # URL de l'image
                image_tag = book.find('img')
                image_url = urljoin(self.base_url, image_tag['src']) if image_tag else "N/A"
                
                # Scraper les détails supplémentaires
                details = self.scrape_book_details(book_url)
                
                # Ajouter les données
                self.books_data.append({
                    'titre': title,
                    'prix': price,
                    'notation': rating,
                    'disponibilite': in_stock,
                    'url': book_url,
                    'image_url': image_url,
                    'upc': details.get('upc', 'N/A'),
                    'avis': int(details.get('reviews', '0')),
                    'description': details.get('description', 'N/A')
                })
                
                print(f"✓ Scraped: {title}")
            
            return True
        except Exception as e:
            print(f"Erreur lors du scraping de la page: {e}")
            return False
    
    def scrape_all_pages(self, max_pages=None):
        """Scraper toutes les pages du catalogue"""
        page_num = 1
        
        while True:
            if max_pages and page_num > max_pages:
                break
            
            if page_num == 1:
                page_url = self.base_url + "catalogue/page-1.html"
            else:
                page_url = self.base_url + f"catalogue/page-{page_num}.html"
            
            print(f"\n📖 Scraping page {page_num}...")
            
            # Vérifier si la page existe
            response = requests.get(page_url)
            if response.status_code != 200:
                print(f"Page {page_num} n'existe pas. Fin du scraping.")
                break
            
            success = self.scrape_page(page_url)
            if not success:
                break
            
            page_num += 1
            time.sleep(0.5)  # Pause pour ne pas surcharger le serveur
        
        print(f"\n✅ Scraping terminé! {len(self.books_data)} livres collectés.")
    
    def save_to_csv(self, filename='books_data.csv'):
        """Sauvegarder les données dans un fichier CSV"""
        df = pd.DataFrame(self.books_data)
        df.to_csv(filename, index=False, encoding='utf-8-sig')
        print(f"💾 Données sauvegardées dans {filename}")
        return df
    
    def get_dataframe(self):
        """Retourner les données sous forme de DataFrame"""
        return pd.DataFrame(self.books_data)


if __name__ == "__main__":
    # Créer une instance du scraper
    scraper = BooksScraper()
    
    # Scraper toutes les pages (ou limiter avec max_pages=5)
    scraper.scrape_all_pages(max_pages=5)  # Limité à 5 pages pour l'exemple
    
    # Sauvegarder dans un CSV
    df = scraper.save_to_csv('books_data.csv')
    
    # Afficher un aperçu
    print("\n📊 Aperçu des données:")
    print(df.head())
    print(f"\nShape: {df.shape}")