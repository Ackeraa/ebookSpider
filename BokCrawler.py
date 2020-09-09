from urllib.request import urlopen
from urllib.request import urlretrieve 
from bs4 import BeautifulSoup
import requests
import re

class BokCrawler:
    
    def __init__(self):
        self.books = []
        self.baseUrl = "https://b-ok.global"
    def craw(self, keywords):
        self.books = []
        limit = 1
        for page in range(1, limit + 1):
            html = urlopen(self.baseUrl + "/s/" + keywords + "?page=" + str(page))
            bsObj = BeautifulSoup(html, features = "lxml")
            bookDivList = bsObj.findAll("", {"class": "resItemBox"})

            order = 0 
            for bookDiv in bookDivList:
                order += 1
                name = bookDiv.find("h3").find("a").get_text()
                link = bookDiv.find("h3").find("a")["href"]
                author = bookDiv.find("", {"class": "authors"}).find("a").get_text()
                type_and_size = bookDiv.find("", {"class": "bookProperty property__file"}).find("", {"class" : "property_value"}).get_text().split(',')
                fileType = type_and_size[0]
                size = type_and_size[1]
                book = {"order": str(order), "name": name, "link": link, "author": author, "type": fileType, "size": size, "from": "bok"}
                self.books.append(book)
        return self.books

    def download(self, bookLink):
        html = urlopen(self.baseUrl + bookLink)
        bsObj = BeautifulSoup(html, features = "lxml")
        downloadLink = self.baseUrl + bsObj.find("a", {"class": "btn btn-primary dlButton addDownloadedBook"})['href']
        return downloadLink
        #urlretrieve(downloadLink, "a.pdf")

if __name__ == '__main__':
    bokCrawler = BokCrawler()
    bokCrawler.craw('Network')
    bokCrawler.download(bokCrawler.books[0]['link'])