import csv
links =[]
with open('wiki_links.csv' , 'r', encoding = 'utf8') as csvfile:

    csv_file_reader = csv.reader(csvfile,delimiter=',')
    cnt=0
    

    for row in csv_file_reader:
        if cnt == 0:
            header = row
            print(header[-2])
        else:
            try:
                links.append( { int(row[0]) : row[-2]})
            except:
                continue
        cnt+=1


