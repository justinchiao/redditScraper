## What it does
This program will take a list of subreddits and a list of words and search each word in each subreddit. I will then take the top n results, sort method and n set by user, and scrape the post and comment text. User can set a maximum number of comments to scrape. Last, a word frequency list will be output.

## Requirements:
1. requests
2. selenium
3. webdriver manager
4. numpy
5. BeautifulSoup

copy these to install each package
pip install requests
pip install selenium
pip install selenium webdriver-manager
pip install numpy
pip install beautifulsoup4

## How to use:
1. Edit request.csv to gather desired results. column 1 is the list of subreddits to crawl, column 2 is the words that will be searched in each subreddit 
2. Number of search results and maximum number of comments can be set in main()
3. Sort method can be set in generateURL() in variable named sort
4. run redditScraper.py
5. This is currently not very efficient so please be patient