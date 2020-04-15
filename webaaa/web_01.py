import requests
from bs4 import BeautifulSoup
import pandas as pd

search = input("Search for : ")
params = {"q", search}
r = requests.get("https://www.nlb.lk/results/" + search)

# r = requests.get("https://www.nlb.lk/results/govisetha")

soup = BeautifulSoup(r.text, "html.parser")
table = soup.find("table")
file = open("copy.txt", "w")
output_rows = []
for table_row in table.findAll('tr'):
    columns = table_row.findAll('td')
    num_set = table_row.findAll("li", {"class": "Number-2"})
    string_col = str(columns)
    row_contents = [string_col]
    loto_num = BeautifulSoup(str(num_set), "html.parser").get_text()
    loto_index = str(row_contents)[int(str(row_contents).find('<b>')) + 3:int(str(row_contents).find('</b>'))]
    loto_date = str(row_contents)[int(str(row_contents).find('<br/>')) + 5:int(str(row_contents).find('</td>'))]
    loto_letr = str(row_contents)[
                int(str(row_contents).find('Letter">')) + 8:int(str(row_contents).find('Letter">')) + 9]
    f = open('helloworld.txt', 'a+')
    padma_dic = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12,
                 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23,
                 'X': 24, 'Y': 25, 'Z': 26}
    loto_letr_num = padma_dic.get(loto_letr)
    lot_day = str(row_contents)[int(str(row_contents).find('<br/>')) + 5:int(str(row_contents).find(' '))] #Thursday
    lot_mon = str(row_contents)[int(str(row_contents).find(' '))+1:int(str(row_contents).find(', ')) - 3]
    d03 = str(row_contents)[int(str(row_contents).find(', '))-2 :int(str(row_contents).find(', '))]
    padma_dic2 = {'Sunday': 1, 'Monday': 2, 'Tuesday': 3, 'Wednesday': 4, 'Thursday': 5, 'Friday': 6, 'Saturday': 7}
    padma_dic3 = {'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6, 'July': 7, 'August': 8, 'September': 9, 'October': 10, 'November': 11, 'December': 12}
    d01 = padma_dic2.get(lot_day)
    d02 = padma_dic3.get(lot_mon)

    kk = ''
    if len(loto_num) > 9:
        kk = loto_index +', ' + str(loto_letr_num) + ', \'' + loto_letr + '\', ' + loto_num[1:-1] + ', \'' + loto_date[:-6] + '\',' + loto_date[-5:]+', '+str(d01)+', '+str(d02)+', '+str(d03)
        f = open('helloworld.txt', 'a+')
        if len(kk) > 2:
            if kk not in f:
                f.write(kk)
                f.write('\n')
    print(kk)
    f.close()

read_file = pd.read_csv(r'helloworld.txt')
read_file.to_csv(r'outputs.csv', index=None)
