import requests
import string
import re
import csv
from bs4 import BeautifulSoup


#reads csv and creates list of links
with open('redditResults.csv', newline='') as f:
    redditResults = list(csv.reader(f))
URLS=[]
for i in range(len(redditResults)):
    URLS.append(redditResults[i][0])

def scrapePost(url):
    '''outputs the title and post text from URL as a single string continuous string with only english characters and arabic numbers '''

    #Pulls page HTML
    page = requests.get(url)

    #creates soup object
    soupPage = BeautifulSoup(page.content, "html.parser")

    #extracting text
    postTitleHTML = soupPage.find(slot="title")
    postTextHTML = soupPage.find(slot="text-body")
    postTitle = postTitleHTML.text.strip()
    postText = postTextHTML.text.strip()
    allText = postTitle + " " +postText[:-22]#removes read more and combines title and text

    #remove punctuation and conver to all lowercase
    noPunc = allText.translate(str.maketrans('', '', string.punctuation)).lower()
    
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
                    newWord=newWord + wordList[i][k]
            wordList[i] = newWord
            
    cleanPost=wordList
    return cleanPost #list of words
    


def scrapeComments():
    print("i can't read script")

def makeList(string):
    return list(string.split(" "))



count = {} #{word,frequency}
def counter(url):
    '''Stores frequency of every word in the main post and comments in dictionary count'''
    allWords = scrapePost(url)# + scrapeComments(url)
    for i in range(len(allWords)):
        if allWords[i] in count: #if this word has already been encountered add one to its dictionary value
            count[allWords[i]] = count[allWords[i]] + 1
        else: #if this is the first time this word has been encountered, create dictionary item with word as key and value equal to one
            count[allWords[i]] = 1

def countAllPages(list):
    '''Iterates counter on all URLS in list'''
    for i in range(len(list)):
        counter(list[i])

def filterDict():
    pass

def exportCSV(dict):
    '''exports dict as CSV'''

    with open('wordFrequency.csv', 'w', newline='') as csvfile:
        header_key = ['word', 'freq']
        new_val = csv.DictWriter(csvfile, fieldnames=header_key)

        new_val.writeheader()
        for new_k in dict:
            new_val.writerow({'word': new_k, 'freq': dict[new_k]})

def main():
    countAllPages(URLS)
    #filterDict(count)

    print(count)
    exportCSV(count)

if __name__ == "__main__":
    main()

    




