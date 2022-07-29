from urllib import response
from bs4 import BeautifulSoup
import requests
import csv
from time import sleep
def fetchData(id,link,all_data):
    wiki_url = link
    table_id = "infobox vcard"

    response = requests.get(wiki_url)
    soup = BeautifulSoup(response.text,'html.parser')

    box = soup.find('table',attrs={'class' : table_id})
    
    keys,vals = [],[]
    try:
        for x in box.findAll('th',attrs={'class': 'infobox-label'}):
            keys.append(x.text) 

        for x in box.findAll('td',attrs={'class': 'infobox-data'}):
            vals.append(x.text.encode('utf8'))
        d = {'Airport Type'.lower() : None,'Owner/Operator'.lower() : None, 'Serves'.lower() : None, 'Opened'.lower() : None, 'Hub for'.lower() : None,'Passengers'.lower() : None, "Cargo tonnage".lower():None ,'Aircraft movements'.lower() : None, 'Land Area'.lower(): None,'Owner'.lower() : None,'Operator'.lower(): None}
        for i in range(len(keys)):
            if keys[i].lower() in d:
                try:
                    d[keys[i].lower()] = vals[i].decode('ISO-8859-1').replace('\n','| ')
                    print(d[keys[i].lower()])
                except:
                    continue

        all_data.append({id:d})
    except:
        return

links =[]
all_data = []
with open('Indian.csv' , 'r', encoding = 'utf8') as csvfile:

    csv_file_reader = csv.reader(csvfile,delimiter=',')
    cnt=0
    

    for row in csv_file_reader:
        if cnt == 0:
            header = row
        else:
            if len(row[-2]) == 0:
                continue
            try:
                links.append( { int(row[0]) : row[-2]})
            except:
                continue
        cnt+=1

for dts in links :
    for key,link in dts.items():
        fetchData(key,link,all_data)


fp = open('wiki-data.csv','w')
fp.write('id ,' + 'Airport Type ,'.lower() + 'Owner/Operator ,'.lower() + 'Serves ,'.lower() + 'Opened ,'.lower() + 'Hub for ,'.lower() + 'Passengers ,'.lower() + "Cargo tonnage".lower() +'Aircraft movements ,'.lower() + 'Land Area ,'.lower() + 'Owner ,'.lower() + 'Operator ,'.lower()+ '\n')


for x in all_data:
    for key,val in x.items():
        s = str(key) + ','
        for k,v in val.items():
            if v != None:
                s += str(v.replace(',',' ')) + ','
            else:
                s += ','
        s+='\n'
        try:
            print(s)
        except:
            continue

