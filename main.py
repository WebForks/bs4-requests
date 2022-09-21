import requests #https://requests.readthedocs.io/en/latest/
import selenium #https://selenium-python.readthedocs.io/installation.html
from bs4 import BeautifulSoup #https://www.crummy.com/software/BeautifulSoup/bs4/doc/
import wget #https://pypi.org/project/wget/
import time
import urllib.request
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver


#https://stackoverflow.com/questions/53404285/cant-download-image-off-pixiv-with-scraper-python-3-selenium-beautifulsoup4-urll
def login(browser):
    print("c")
    Log_In = browser.find_element(By.CLASS_NAME, 'signup-form__submit--login')
    Log_In.click()
    print("d")
    Username = browser.find_element(By.XPATH,'/html/body/div[2]/div/div[3]/div[1]/div[2]/div/div/div/form/fieldset[1]/label/input') #https://selenium-python.readthedocs.io/locating-elements.html
    Username.send_keys('pixiv username/email') #input username
    Password = browser.find_element(By.XPATH, '/html/body/div[2]/div/div[3]/div[1]/div[2]/div/div/div/form/fieldset[2]/label/input')
    Password.send_keys('pixiv password') #input password
    Login = browser.find_element(By.XPATH, '/html/body/div[2]/div/div[3]/div[1]/div[2]/div/div/div/form/button')
    print("e")
    Login.click()

#https://stackoverflow.com/questions/70804909/how-to-correctly-find-elements-by-class-name-on-python-selenium-related (use this)
def search(tags, browser):
    time.sleep(10)
    searchbox = browser.find_element(By.CSS_SELECTOR, ".sc-5ki62n-4.eOTMOA")
    searchbox.send_keys(tags)
    searchbox.send_keys(Keys.ENTER)
    time.sleep(10)
    popularity = browser.find_element(By.CSS_SELECTOR, ".sc-rkvk44-2.bSKUcn")
    popularity.click()
    time.sleep(10)
    popularity_with_all = browser.find_element(By.CSS_SELECTOR, ".sc-1o8nozx-7.imOciH")
    popularity_with_all.click()
    time.sleep(10)
    print("g")
    Illustrations_only = browser.find_element(By.CSS_SELECTOR, ".sc-1mycqam-1.hIfEPv")
    Illustrations_only.click()


def main():
    tags = input("Enter tags: ")
    tags = str(tags)
    print(tags)
    url = "https://www.pixiv.net/"
    service = Service(r'Path to geckodriver') #path to geckodriver.exe
    options = webdriver.FirefoxOptions()
    options.add_argument('--disable-blink-features=AutomationControlled')
    browser = webdriver.Firefox(service=service, options=options)
    print("a")
    browser.get(url)
    print("b")
    login(browser)
    print("f")
    search(tags, browser)

main()