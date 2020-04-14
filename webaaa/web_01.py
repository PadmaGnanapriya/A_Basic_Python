# from bs4 import BeautifulSoup
# import requests
#
# # search = input("Search for : ")
# # params ={"q",search}
# r = requests.get("https://www.nlb.lk/results/govisetha")
#
# soup = BeautifulSoup(r.text, "html.parser")
# results = soup.find_all('tr')
# print(results[7:11])
import requests
from bs4 import BeautifulSoup
import csv

r = requests.get("https://www.nlb.lk/results/govisetha")

soup = BeautifulSoup(r.text, "html.parser")
table = soup.find("table")

output_rows = []
for table_row in table.findAll('tr'):
    columns = table_row.findAll('td')
    print(columns)
    output_row = []
    for column in columns:
        output_row.append(column.text)
    output_rows.append(output_row)
   #print(output_rows)

# with open('output.csv', 'wb') as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerows(output_rows)