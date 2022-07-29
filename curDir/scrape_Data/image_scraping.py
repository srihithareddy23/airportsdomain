from bs4 import BeautifulSoup
import requests
import csv


def image_scrape(url):
    try:
        r = requests.get(url)
        soup = BeautifulSoup(r.content,features="lxml")
        covers = soup.select('table.infobox a')
        for cover in covers:
            return(cover['href'])
    except:
        return 'None'


links =[]
with open('wiki_links.csv' , 'r', encoding = 'utf8') as csvfile:

    csv_file_reader = csv.reader(csvfile,delimiter=',')
    for row in csv_file_reader:
        if len(row[-1]) == 0:
            continue
        links.append( { str(row[0]) : str(row[-2])})


    images = []

    fp = open('images.csv', 'w')

    for x in links:
        for key,val in x.items():
            try:
                fp.write(str(key)+ ',' + str(image_scrape(val)) +'\n')
            except:
                continue

