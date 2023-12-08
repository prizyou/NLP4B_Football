import requests
import csv
from bs4 import BeautifulSoup

# Instagram-Post-URL
post_url = 'https://www.instagram.com/p/CrQYJ1CIEkboY_8XYMPp8bHM-pKj9b7zPP8KSc0/?img_index=1'

# HTTP-Anfrage an die URL senden
response = requests.get(post_url)

# HTML-Inhalt mit BeautifulSoup analysieren
soup = BeautifulSoup(response.text, 'html.parser')

# Kommentare extrahieren
comments = []
comment_containers = soup.find_all('div', {'class': 'C4VMK'})
for container in comment_containers:
    comment_text = container.find('span').text.strip()
    comments.append({'comment_text': comment_text})

# CSV-Datei schreiben
csv_filename = 'web_scraping/instagram/instagram_comments.csv'
with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['comment_text']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # CSV-Header schreiben
    writer.writeheader()

    # Kommentare in CSV schreiben
    writer.writerows(comments)
