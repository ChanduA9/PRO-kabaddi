import requests
from bs4 import BeautifulSoup
import pandas as pd

l=[]

url="https://www.prokabaddi.com/teams"
req=requests.get(url) # sendng the requests to url

soup=BeautifulSoup(req.text,'html.parser')
# print(soup)
s=soup.find('div',class_='card-list')
# r=s.find_all('p')
for link in soup.find_all('a'):
    links=link.get('href')
    l.append(links)

df=pd.DataFrame(l)
df.to_csv('Details_link.csv')
