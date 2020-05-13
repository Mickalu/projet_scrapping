# -*- coding: utf-8 -*-
"""
Created on Thu May  7 23:05:25 2020

@author: Thomas BONGIBAULT, Lucas MICHAELI
"""

### LIBRARIES #################################################################
import requests
from bs4 import BeautifulSoup
import csv
from time import sleep
import datetime
from random import randint

### FUNCTION ##################################################################
def scraping():
    """Function for scraping the bitcoin value on the boursorama website"""

    # Page to scrap and collecting bitcoin value
    page_scrap = requests.get("https://www.boursorama.com/bourse/devises/taux-de-change-bitcoin-euro-BTC-EUR/")
    soup = BeautifulSoup(page_scrap.text, 'lxml')
    bitcoin_value = soup.find('span', {'class' : 'c-instrument c-instrument--last'}).text

    # Collect date
    date_now = str(datetime.datetime.today())[:19]

    # Saving data in the csv file
    with open("bitcoin_value.csv", "a", newline="") as csv_file:
        writer = csv.writer(csv_file, delimiter=";")
        writer.writerow([date_now, bitcoin_value[0]+bitcoin_value[2:]])
    
    sleep(randint(10,15))
    
def delete_data():
    """Delete Data in the csv file"""
    
    with open("bitcoin_value.csv", "w", newline="") as csv_file:
        writer = csv.writer(csv_file, delimiter=";")
        writer.writerow(["date", "bitcoin_value"])    