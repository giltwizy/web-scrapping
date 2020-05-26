###############################################
# program: corona-scrapper.py
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
        '''initialize the class with the url'''
        self.url = url       
    
    def get_data(self):
        '''Makes an http request and download the html data'''
        our_site = requests.get(self.url)

        #get exception if occurs when failed to download the html content
        try:
            our_site.raise_for_status()
        except Exception as e:
            print('There was a problem: %s'%(e))
        s = BeautifulSoup(our_site.text,"html.parser")

        #accessing all tags containing div ="maincounter-number" from the html
        data  = s.find_all("div",class_ = "maincounter-number")

        print("Total Cases: ",data[0].text)
        print("Total Deaths: ",data[1].text)
        print("Total Recoveries: ",data[2].text)

corona_data = Corona_updates("https://www.worldometers.info/coronavirus/")
corona_data.get_data()

