#!/usr/bin/env python
# coding: utf-8

import re
import requests
from BeautifulSoup import BeautifulSoup

response = requests.get('https://www.daydeal.ch')
soup = BeautifulSoup(response.content)

title = soup.find("h1", {"class":"meta-first-line"}).getText()
subtitle = soup.find("span", {"class":"meta-second-line"}).getText()

price = soup.find("span", {"class":"price"}).getText()
originalprice = soup.find("div", {"class":"originalPrice"}).getText()
originalprice = re.sub('[\D+]', '', originalprice)
percentage = soup.find("span", {"class":"percentage"}).getText()

print "Heutiger Daydeal: "+title+" "+subtitle
print u"Für CHF "+price+" anstatt CHF "+originalprice+".-"
print "Noch "+percentage+u"% verfügbar"
