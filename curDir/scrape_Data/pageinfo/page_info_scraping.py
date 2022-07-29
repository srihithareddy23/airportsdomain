
from urllib import response
from bs4 import BeautifulSoup
import requests
import pandas as pd

l =[]

def scrape_ids(id,name):
    url =  "https://en.wikipedia.org/w/index.php?title=" + name + "&action=info"
    response = requests.get(url)
    soup = BeautifulSoup(response.text,'html.parser') 
    covers = soup.select('table.wikitable a.extiw')
    for i in covers:
        l.append(id,i.get_text())

    

df = pd.read_excel('wikipedia_links.xlsx')
for i in range(len(df)) : 
    if str(df.iloc[i, 1]) != 'nan':
        scrape_ids(str(df.iloc[i, 0])[30:], str(df.iloc[i, 1]))




