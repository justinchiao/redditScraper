import requests
import string
import re
import csv
from bs4 import BeautifulSoup
import selenium
from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.chrome.service import Service as ChromeService 
from webdriver_manager.chrome import ChromeDriverManager 
import time 
import numpy as np

with open('request.csv', newline='') as f:
    search = list(csv.reader(f))
subs = []
words = []
for i in range(len(search)):
    subs.append(search[i][0])
    words.append(search[i][1])

sort='new' #options are relevance, hot, top, new, comments(most comments)

def listShorten(list):
    newlist =[]
    for i in range(len(list)): 
        if list[i] != '':
            newlist.append(list[i])
    return newlist


def generateURL(subredditName, keywords):
    SEARCHCSV = []
    SEARCH = []

    subs = listShorten(subredditName)
    words = listShorten(keywords)
    formatted = []
    for i in range(len(words)):
        formatted = formatted + [words[i].replace(" ", "%20" )]
    #print(formatted)

    for i in range(len(subs)):
        for k in range(len(words)):
            SEARCHCSV = SEARCHCSV + [['https://www.reddit.com/' + subs[i] + '/search/?q=' + formatted[k] + '&restrict_sr=1&sort=' + sort]]
            SEARCH = SEARCH + ['https://www.reddit.com/' + subs[i] + '/search/?q=' + formatted[k] + '&restrict_sr=1&sort=' + sort]
    exportSearchCSV(SEARCHCSV)
    return SEARCH

def exportSearchCSV(urls):
    rows = urls
    # using the savetxt
    # from the numpy module
    np.savetxt("searches.csv", 
           rows,
           delimiter =", ", 
           fmt ='% s')


#https://www.reddit.com/r/androidapps/search/?q=photo%20apps&restrict_sr=1&sort=new
#https://www.reddit.com/(subreddit(r/name))/search/?q=(search%20words)&restrict_sr=1&sort=new
