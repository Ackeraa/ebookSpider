from urllib.request import urlopen
from urllib.request import urlretrieve 
from urllib.request import Request
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import requests
import re

class pdfDriveSpider:

    def __init__(self):
        self.books = []
        self.baseUrl = "https://www.pdfdrive.com"
        self.headers = {
            "content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "DNT": "1",
            "Origin": "https://www.premierleague.com",
            "Referer": "https://www.premierleague.com/players",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
        }

    def craw(self, keywords):
        self.books = []
        html = urlopen(self.baseUrl + "/search?q=" + keywords + "&pagecount=&pubyear=&searchin=&em=")
        bsObj = BeautifulSoup(html, features = "lxml")
        bookDivList = bsObj.find("", {"class": "files-new"}).find("ul").findAll("li")
        order = 0 
        for bookDiv in bookDivList:
            order += 1
            name = bookDiv.find("h2").get_text()
            link = bookDiv.find("", {"class": "file-right"}).find("a")["href"]
            html1 = urlopen(self.baseUrl + link)
            bsObj1 = BeautifulSoup(html1, features = "lxml")
            bookDiv1 = bsObj1.find("", {"class": "ebook-main"})
            if bookDiv1.find("", {"class": "ebook-author"}).find("a") != None: 
                author = bookDiv1.find("", {"class": "ebook-author"}).find("a").get_text()
            else:
                author = "None"

            fileType = "pdf"
            size = bookDiv1.find("", {"class": "ebook-file-info"}).findAll("", {"class": "info-green"})[2].get_text()
            link = bookDiv1.find("", {"id": "download-button"}).find("a")["href"]
            book = {"order": str(order), "name": name, "link": link, "author": author, "type": fileType, "size": size, "from": "pdfDrive"}
            self.books.append(book)
            if order >= 10:
                break
        return self.books

    def download(self, bookLink):

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-gpu')
        client = webdriver.Chrome(chrome_options=chrome_options, executable_path='tools/chromedriver')
        print("Opening...\n")
        client.get(self.baseUrl + bookLink)

        print("Waiting for response...\n")
        wait = WebDriverWait(client, 150)
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "text-center")))

        print("Geting data...\n")
        html = client.page_source
        bsObj = BeautifulSoup(html, features = "lxml")
        downloadLink = self.baseUrl + bsObj.find("", {"class": "text-center"}).find("a")['href']
        client.quit()
        return downloadLink

if __name__ == '__main__':

    spider = pdfDriveSpider()
    spider.craw("Network")
    urlretrieve(Spider.download(Spider.books[0]["link"]), "a.pdf")

