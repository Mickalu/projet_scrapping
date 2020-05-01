# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 18:59:00 2020

@author: Thomas
"""
import requests
import time
from bs4 import BeautifulSoup
import csv
import json 

number_new_value = 5
dictionary_date_scrapping = {}
dictionary_date_scrapping["date"] = "bitcoin value"

for i in range(0, number_new_value):
    print(i)
    page = requests.get("https://www.boursorama.com/bourse/devises/taux-de-change-bitcoin-euro-BTC-EUR/")
    soup = BeautifulSoup(page.text, 'lxml')
    element = soup.find('span', {'class' : 'c-instrument c-instrument--last'})
    date_now = time.localtime()
    str_date_now = str(date_now[0]) + "-" + str(date_now[1]) + "-" + str(date_now[2]) + "-" + str(date_now[3]) + "-" + str(date_now[4]) + "-" + str(date_now[5])
    
    dictionary_date_scrapping[str_date_now] = element.get_text()
    time.sleep(15)

#au format json
with open("bitcoin_value.json", "w") as json_file:
    json.dump(dictionary_date_scrapping, json_file)

#au format csv
with open("bitcoin_value.csv", "w", newline = "") as csv_file:
    writer = csv.writer(csv_file)
    for key, value in dictionary_date_scrapping.items():
        writer.writerow([key, value])
        


    
    