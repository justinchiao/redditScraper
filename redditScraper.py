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
import numpy as np
import time
import random

start_time = time.time()

#Opens CSV with subreddit names and search words and sorst into subs and words respectively
with open('request.csv', newline='') as f:
    search = list(csv.reader(f))
subs = []
words = []
for i in range(len(search)):
    subs.append(search[i][0])
    words.append(search[i][1])

def listShorten(list):
    newlist =[]
    for i in range(len(list)): 
        if list[i] != '':
            newlist.append(list[i])
    return newlist


def generateURL(subredditName, keywords):
    '''generates search urls for each sub and each search word in request.csv'''

    sort='new' #options are relevance, hot, top, new, comments(most comments)

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

def scrapeResults(urlList,itemTargetCount):
    '''outputs all comment text from URL as a list of strings with only english characters and arabic numbers'''
    urlsCSV=[]
    urls = []
    for i in range(len(urlList)):

        # instantiate options 
        options = webdriver.ChromeOptions() 
        # run browser in headless mode 
        options.headless = True 
        driver = webdriver.Chrome(service=ChromeService( 
	        ChromeDriverManager().install()), options=options) 

        # get the entire website content 
        driver.get(urlList[i])
        #with open('comm.txt', 'w', encoding='utf-8') as f:
            #f.write(driver.page_source)
    
        items = [] 
        # instantiate height of webpage 
        last_height = driver.execute_script('return document.body.scrollHeight') 
 
        # scroll to bottom of webpage 
        while itemTargetCount > len(items): 
            driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
            time.sleep(1)
        
            new_height = driver.execute_script('return document.body.scrollHeight') 
 
            if new_height == last_height: 
                break 
        
            last_height = new_height 
 
	        # select elements by XPath
            elements = driver.find_elements(By.XPATH, "//div[@class='_2i5O0KNpb9tDq0bsNOZB_Q']/div/div/a/div/h3")
            h3_texts = [element.text for element in elements]
            items = h3_texts

        items = items[0:itemTargetCount]
    
        for i in range(len(items)):
            element = driver.find_element(By.LINK_TEXT, items[i])
            urlsCSV = urlsCSV + [[element.get_attribute('href')]]
            urls = urls + [element.get_attribute('href')]

    #removes duplicates
    #urlsCSV = list(set(urlsCSV))
    urls = list(set(urls))
    print(len(urls))
    print(urls)
    #exportResCSV(urlsCSV)
    return urls

def exportResCSV(inputurls):
    rows = inputurls
    # using the savetxt 
    # from the numpy module
    np.savetxt("redditResults.csv", 
           rows,
           delimiter =", ", 
           fmt ='% s')

#reads csv and creates list of links
#with open('redditResults.csv', newline='') as f:
    #redditResults = list(csv.reader(f))
#URLS=[]
#for i in range(len(redditResults)):
    #URLS.append(redditResults[i][0])

def scrapePost(url):
    '''outputs the title and post text from URL as a list of strings with only english characters and arabic numbers '''

    #Pulls page HTML
    page = requests.get(url)

    #creates soup object
    soupPage = BeautifulSoup(page.content, "html.parser")

    #extracting elements
    postTitleHTML = soupPage.find(slot="title")
    postTextHTML = soupPage.find(slot="text-body")

    #ensures title and text have text, discards if not
    if postTitleHTML == None:
        allText = postTextHTML.text.strip()
    elif postTextHTML == None:
        allText = postTitleHTML.text.strip()
    elif postTitleHTML == None and postTitleHTML == None:
        allText = 'XxZzYy'
    else:
        postTitle = postTitleHTML.text.strip()
        postText = postTextHTML.text.strip()
        allText = postTitle + " " + postText[:-10]#removes read more and combines title and text

    return textCleaner(allText)

#broken rn
def scrapeComments(url,itemTargetCount):
    '''outputs all comment text from URL as a list of strings with only english characters and arabic numbers'''
    username = "SufficientDemand3270"
    password = "HoRZrm00LT"
    time.sleep(random.randint(5,10))

    # instantiate options 
    options = webdriver.ChromeOptions() 
    # run browser in headless mode 
    options.headless = True
    # instantiate driver 
    driver = webdriver.Chrome(service=ChromeService( 
	    ChromeDriverManager().install()), options=options) 
    # get the entire website content 
    driver.get(url)
    with open('comm.html', 'w', encoding='utf-8') as f:
        f.write(driver.page_source)

    #login
    originalWindow = driver.current_window_handle
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[1])
    driver.get('https://www.reddit.com/login/')

    #driver.find_element(By.ID,'login-button').click()
    #loginButton = driver.find_element(By.ID,'login-button')
    #driver.execute_script("arguments[0].click();", loginButton)
    time.sleep(2)
    with open('comm.html', 'w', encoding='utf-8') as f:
        f.write(driver.page_source)
    driver.find_element(By.ID,'loginUsername').send_keys(username)
    driver.find_element(By.ID,'loginPassword').send_keys(password)
    #login = driver.find_element(By.CLASS_NAME,'AnimatedForm__submitButton m-full-width m-modalUpdate ')
    with open('comm.html', 'w', encoding='utf-8') as f:
        f.write(driver.page_source)
    driver.find_element(By.TAG_NAME,'button').click()
    driver.switch_to.window(originalWindow)
    time.sleep(1)
    driver.refresh()

    # create list of strings from list of elements
    comments = [] 
    # instantiate height of webpage 
    last_height = driver.execute_script('return document.body.scrollHeight') 
    # set target count 

    while itemTargetCount > len(comments): 
        # scroll to bottom of webpage

        driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        time.sleep(0.5)
        
        new_height = driver.execute_script('return document.body.scrollHeight') 
        #print('lastheight =', last_height)
        #print('newheight =', new_height)
        
        if new_height == last_height: 
            #print('scroll fail')
            break
        
        last_height = new_height

	    # select elements by ID
        elements = driver.find_elements(By.CLASS_NAME, "_1qeIAgB0cPwnLhDF9XSiJM")
        comments = [element.text for element in elements]
    


    #DONT TOUCH
    comments = comments[0:itemTargetCount]
    print(len(comments))
    print(comments)
    #process every string in list of strings
    cleanComments=[]
    for i in range(len(comments)):
        cleanComments = cleanComments + textCleaner(comments[i])
    #print(cleanComments)
    driver.close()
    return cleanComments

#possible improvement to account for contractions
#with open('contractions.csv', newline='') as c:
    #contractions = list(csv.reader(c))

def textCleaner(inputString):
    '''returns list of one word strings without any extra spaces, line breaks, or special characters.'''

    #remove punctuation and conver to all lowercase
    noPunc = inputString.translate(str.maketrans('', '', string.punctuation)).lower()

    #removes extra spaces and line breaks
    res = ""
    res2 = ""
    for i in range(len(noPunc)):
        if (noPunc[i] == " " and noPunc[i-1] == " " ) or ord(noPunc[i]) == 10:
            pass
        else:
            res += noPunc[i]
    for i in range(len(res)):
        if (res[i] == " " and res[i-1] == " ") or ord(res[i]) == 10:
            pass
        else:
            res2 += res[i]    
    
    #remove emojis/special char
    wordList = makeList(res2)
    for i in range(len(wordList)):
        if not wordList[i].isalnum():
            newWord=""
            for k in range(len(wordList[i])):
                if wordList[i][k].isalnum():
                    newWord = newWord + wordList[i][k]
            wordList[i] = newWord
    return wordList


def makeList(string):
    return list(string.split(" "))

count = {} #{word,frequency}
def counter(url,coms):
    '''Stores frequency of every word in the main post and comments in dictionary count'''
    allWords = scrapePost(url) + scrapeComments(url,coms)
    for i in range(len(allWords)):
        if allWords[i] in count: #if this word has already been encountered add one to its dictionary value
            count[allWords[i]] = count[allWords[i]] + 1
        else: #if this is the first time this word has been encountered, create dictionary item with word as key and value equal to one
            count[allWords[i]] = 1

def countAllPages(list,coms):
    '''Iterates counter on all URLS in list'''
    for i in range(len(list)):
        counter(list[i],coms)

def filterDict():
    '''filters dictionary to only include desired keywords'''
    pass

def exportCSV(dict):
    '''exports dict as CSV'''

    with open('wordFrequency.csv', 'w', newline='', encoding = 'utf-8') as csvfile:
        header_key = ['word', 'freq']
        new_val = csv.DictWriter(csvfile, fieldnames=header_key)

        new_val.writeheader()
        for new_k in dict:
            new_val.writerow({'word': new_k, 'freq': dict[new_k]})

def main():
    #creates list of search urls
    searchURLS = generateURL(subs,words)

    #creates list with numResults posts per search url
    numResults = 10
    URLS = scrapeResults(searchURLS,numResults)
    #creates list with numComments comments per post
    numComments = 30

    countAllPages(URLS,numComments)
    #filterDict(count)
    exportCSV(count)
    print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == "__main__":
    main()



