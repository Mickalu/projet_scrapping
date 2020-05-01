# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 18:59:00 2020

@author: Thomas
"""

import requests
from bs4 import BeautifulSoup

page = requests.get("https://www.boursorama.com/bourse/devises/taux-de-change-bitcoin-euro-BTC-EUR/")

soup = BeautifulSoup(page.text, 'lxml')

element = soup.find('span', {'class' : 'c-instrument c-instrument--last'})
print(element.text)