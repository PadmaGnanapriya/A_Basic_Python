import requests
from bs4 import BeautifulSoup
import pandas as pd

search = input("Search for : ")
params ={"q", search}
r = requests.get("https://www.nlb.lk/results/"+search)


#r = requests.get("https://www.nlb.lk/results/govisetha")

soup = BeautifulSoup(r.text, "html.parser")
table = soup.find("table")
file = open("copy.txt", "w")
output_rows = []
for table_row in table.findAll('tr'):
    columns = table_row.findAll('td')
    num_set=table_row.findAll("li", {"class": "Number-2"})
    string_col=str(columns)
    row_contents = [string_col]
    loto_num = BeautifulSoup(str(num_set), "html.parser").get_text()
    loto_index=str(row_contents)[int(str(row_contents).find('<b>'))+3:int(str(row_contents).find('</b>'))]
    loto_date=str(row_contents)[int(str(row_contents).find('<br/>'))+5:int(str(row_contents).find('</td>'))]
    loto_letr=str(row_contents)[int(str(row_contents).find('Letter">'))+8:int(str(row_contents).find('Letter">'))+9]
    f = open('helloworld.txt', 'a+')
    kk=''
    if len(loto_num)>9:
        kk=loto_index+', \''+loto_letr+'\', '+loto_num[1:-1]+', \''+loto_date[:-6]+'\','+loto_date[-5:]
        f = open('helloworld.txt', 'a+')
        if len(kk)>2:
            if kk not in f:
                f.write(kk)
                f.write('\n')
    print(kk)
    f.close()


read_file = pd.read_csv(r'helloworld.txt')
read_file.to_csv(r'outputs.csv', index=None)






