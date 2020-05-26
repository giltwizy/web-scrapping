###############################################
# program: scrap-corona.py
# author: Gilton Bosco
# version: 1.1
# date: 25 May 2020
###############################################

# requests module handles http requests
# BeautifulSoup parses the html data

import requests
from bs4 import BeautifulSoup

class Corona_updates:
    
    def __init__(self,url):
        self.url = url       
    
    def get_data(self):
        our_site = requests.get(self.url)
        try:
            our_site.raise_for_status()
        except Exception as e:
            print('There was a problem: %s'%(e))
        s = BeautifulSoup(our_site.text,"html.parser")
        data  = s.find_all("div",class_ = "maincounter-number")
        print("Total Cases: ",data[0].text)
        print("Total Deaths: ",data[1].text)
        print("Total Recoveries: ",data[2].text)

corona_data = Corona_updates("https://www.worldometers.info/coronavirus/")
corona_data.get_data()

