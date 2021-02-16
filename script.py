from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

import requests
import re

print("Nome do Músico")
musico = input()
musico=musico.replace(" ","%20")

#retrieve the search url

urlartista="https://discografiabrasileira.com.br/artista/name/"+musico


r = requests.get(urlartista)
page_source = r.text
page_source = page_source.split('\n')
urls = re.findall('http[s]?://discografiabrasileira.com.br/artista/(?:[0-9])+/(?:[a-zA-Z]|\-)+',str(page_source))

# Remove duplicate  link

res = []
[res.append(x) for x in urls if x not in res]
for value in res:
    #s = requests.get(value)
    #page_source2 = r.text
    #page_source2 = page_source2.split('\n')
    #print(page_source2)

    import dryscrape
    from bs4 import BeautifulSoup

    session = dryscrape.Session()
    session.visit(value)
    response = session.body()
    soup = BeautifulSoup(response)
    print(soup)