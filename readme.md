## What it does
This program will take a list of subreddits and a list of words and search each word in each subreddit. I will then take the top n results, sort method and n set by user, and scrape the post and comment text. User can set a maximum number of comments to scrape. Last, word frequency lists and wordcloud will be output.

## Requirements:
1. requests
2. selenium
3. webdriver manager
4. numpy
5. BeautifulSoup
6. pandas
7. matplotlib
8. pillow
9. wordcloud

copy these to install each package <br>
pip install requests <br>
pip install selenium <br>
pip install selenium webdriver-manager <br>
pip install numpy <br>
pip install beautifulsoup4 <br>
pip install pillow <br>
pip install matplotlib <br>
pip install wordcloud <br>

## How to use:
only files you need are redditScraper.py, request.csv, and noiseWords.csv. The others will be written by the program

1. Edit request.csv to gather desired results. column 1 is the list of subreddits to crawl, column 2 is the words that will be searched in each subreddit 
2. Number of search results can be set in main()
3. Sort method can be set in generateURL() in variable named sort
4. noiseWords.csv can be edited to remove unwanted words
5. wordCloud function has wordcloud size and color settings
6. run redditScraper.py
7. This is currently not very efficient so please be patient