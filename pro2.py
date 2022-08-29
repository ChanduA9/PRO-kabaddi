import requests
import pandas as pd
from bs4 import BeautifulSoup
l=[]
read_data=pd.read_csv('Details_link.csv',index_col=1)
for i in range(45,57):
    data=read_data.iloc[i]
    l.append(data)
    print(data)
    # req=requests.get(str(data))
    # print(req.text)
df=pd.DataFrame(l)
df.to_csv('teams.csv')
