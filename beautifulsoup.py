import requests
from bs4 import BeautifulSoup

url = "https://www.worldometers.info/coronavirus/"
our_site = requests.get(url)
try:
    our_site.raise_for_status()
except Exception as e:
    print('There was a problem: %s'%(e))

s = BeautifulSoup(our_site.text,"html.parser")
data  = s.find_all("div",class_ = "maincounter-number")


print("Total Cases: ",data[0].text)
print("Total Deaths: ",data[1].text)
print("Total Recoveries: ",data[2].text)
