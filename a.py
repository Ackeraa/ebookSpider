from urllib.request import urlopen
from io import BytesIO
from bs4 import BeautifulSoup
import re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def google_driver(url):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-gpu')
    client = webdriver.Chrome(chrome_options=chrome_options, executable_path='tools/chromedriver')
    print("Opening...")
    client.get(url)

    print("Waiting for response...")
    wait = WebDriverWait(client, 150)
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "text-center")))

    print("Geting data...")
    html = client.page_source
    bsObj = BeautifulSoup(html, features = "lxml")
    baseUrl = "https://www.pdfdrive.com"
    downloadLink = baseUrl + bsObj.find("", {"class": "text-center"}).find("a")['href']

    print(downloadLink)
    client.quit()
    pass
 
google_driver('https://www.pdfdrive.com/nmap-network-scanning-the-official-nmap-project-guide-to-network-discovery-and-security-scanning-d188101047.html')

