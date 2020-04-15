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
from _csv import writer

import requests
from bs4 import BeautifulSoup
import csv

def append_list_as_row(file_name, list_of_elem):
    # Open file in append mode
    with open(file_name, 'a+', newline='') as write_obj:
        # Create a writer object from csv module
        csv_writer = writer(write_obj)
        # Add contents of list as last row in the csv file
        csv_writer.writerow(list_of_elem)


r = requests.get("https://www.nlb.lk/results/govisetha")

soup = BeautifulSoup(r.text, "html.parser")
table = soup.find("table")
file = open("copy.txt", "w")
output_rows = []
for table_row in table.findAll('tr'):
    columns = table_row.findAll('td')
    string_col=str(columns)
    row_contents = [string_col]

    # Append a list as new line to an old csv file
    append_list_as_row('output.csv', row_contents)

   # print(table_row.findAll('b'))
   # print(table_row.findAll('li'))
   #  file.write(columns)
    # c = csv.writer(open('dbdump01.csv', 'wb'))
    # for x in result:
    #     c.writerow(x)

    output_row = []
    for column in columns:
        output_row.append(column.text)
    output_rows.append(output_row)
   #print(output_rows)

# with open('output.csv', 'wb') as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerows(output_rows)