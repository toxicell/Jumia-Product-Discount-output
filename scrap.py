from bs4 import BeautifulSoup
import requests
import json
from urllib.parse import urljoin



url = 'https://www.jumia.ma/'
page = requests.get(url)


url = 'https://www.jumia.ma/'
page = requests.get(url)

soup = BeautifulSoup(page.text, 'html.parser')

articles = soup.find_all('article')

prod_disc = []

for article in articles:
    prod = {}

    name_element = article.find(class_='name')
    if name_element:
        prod['name'] = name_element.get_text(strip=True)

    price_element = article.find(class_='prc')
    if price_element:
        prod['price'] = price_element.get_text(strip=True)

    discount_element = article.find(class_='bdg _dsct')
    if discount_element:
        prod['discount'] = discount_element.get_text(strip=True)
    else:
        continue

    href_element = article.find('a')
    if href_element:
        href = href_element['href']
        full_url = urljoin(url, href)
        prod['href'] = full_url


    prod_disc.append(prod)

formatted_output = json.dumps(prod_disc, indent=4)

print(formatted_output)
