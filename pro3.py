import requests
import pandas as pd
from bs4 import BeautifulSoup
#
# with open('teams.csv','r') as f:
#     f.readline()
#     for i in f:
l=[]
url=requests.get("https://www.prokabaddi.com/teams/bengaluru-bulls-profile-1/players")
soup=BeautifulSoup(url.text,'html.parser')
s=soup.find('div',class_='squad-listing swiper-wrapper')
s2=s.find_all('p',class_=('name first-name'))
s3=s.find_all('p',class_="name last-name")
s4=s.find_all('p',class_='squad-category')
s5=s.find_all('p',class_='squad-country')
for i in s2:
    first_name=i.text
    break
    for j in s3:
        last_name=j.text
        break
        for k in s4:
            squad_category=k.text
            break
            for n in s5:
                country=n.text
                l.append({'FIRST NAME':first_name,'LAST NAME':last_name,'SQUAD CATEGORY':squad_category,'COUNTRY':country})
                break
df=pd.DataFrame(l)
df.to_csv('player_details.csv')
      # print(s1)
# for i in read_data:
    # print(i)
# print(read_data)


# print(l)
