#!/usr/bin/env python
# coding: utf-8

import re
import requests
from bs4 import BeautifulSoup

response = requests.get('https://www.daydeal.ch')
soup = BeautifulSoup(response.content, 'html.parser')

title = soup.find('h1', {'class': ['product-description__title1']}).get_text()
subtitle = soup.find('h2', {'class': ['product-description__title2']}).get_text()
print("Heutiger Daydeal: "+title+" "+subtitle)

price = soup.find('h2', {'class': ['product-pricing__prices-new-price']}).get_text()
originalprice = soup.find('strong', {'class': 'product-pricing__prices-old-price'}).get_text(strip=True)
print("Für "+price+" "+ originalprice)

percentage = soup.find('strong', {'class': 'product-progress__availability'}).get_text()
print("Noch "+percentage+"% verfügbar")
