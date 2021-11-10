import sys
import os
from bs4 import BeautifulSoup
import requests
import lxml

# extract url from terminal call

rootURL = sys.argv[1]
headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
}

# should ask about the details of the website, the username & password
# HTML id's

# should implement a max-url number to visit, -n <num>

# should implement a max depth to go down the website, -d <depth>

# should implement a toggle for javascript files default off, -j to turn on

foundURLs = {}
serverfiles = {}

num = 100

def recursiveCrawl(rootURL,  parentURL, num):
    try:
        req = requests.get(rootURL,headers, timeout=5)
        soup = BeautifulSoup(req.content, 'html.parser')
    except:
        return

    num -= 1

    if num == 0:
        return

    allHREF = soup.find_all(href=True)

    if len(allHREF) == 0:
        return

    for a in allHREF:

        url = a['href']

        urlList = []
        
        if url[0] == '/' or url[:5] != 'https':
            if parentURL[len(parentURL)-1] == '/':
                parentURL = parentURL[:-1]
            else:
                url = parentURL + url

        # inserts all hrefs into urls dict
        if url in foundURLs:
            donothing = "true"
        else:
            if (os.path.splitext(url)[1] == '.php' or os.path.splitext(url)[1] == '.xhtml' or os.path.splitext(url)[1] == '.html' or os.path.splitext(url)[1] == ''):
                print(url)
                foundURLs[url] = 1
                urlList.append(url)

        # elif url not in serverfiles:
        #     if (os.path.splitext(url)[1] == '.php' or os.path.splitext(url)[1] == '.html' or os.path.splitext(url)[1] == ''):
        #         serverfiles[url] = 1
        
        for link in urlList:
            print (link)
            recursiveCrawl(link, rootURL, num)

recursiveCrawl(rootURL, rootURL, 3)

print(foundURLs)
str = "https://123"
print(str[:5])

