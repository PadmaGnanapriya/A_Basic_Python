import bs4
import matplotlib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from jedi.refactoring import inline

from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "http://www.hubertiming.com/results/2017GPTR10K"
html = urlopen(url)

soup = BeautifulSoup(html, "html.parser")
type(soup)
bs4.BeautifulSoup

text = soup.get_text()


rows = soup.find_all('tr')
for row in rows:
    row_td = row.find_all('td')
print(row_td)
type(row_td)
str_cells = str(row_td)
cleantext = BeautifulSoup(str_cells, "html.parser").get_text()
print(cleantext)