from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
# from selenium.common.exceptions import NewConnectionError
import selenium.common.exceptions
from pyhunter import PyHunter
from time import sleep
import time
import csv

#####################
browser = webdriver.Chrome()
hunter = PyHunter('my_hunter_api_key')
#####################

def HuntCheck(websites):
    L = []
    for i in websites:
        EmailCount = hunter.email_count(domain=i, company='none')
        EmailNumber = EmailCount['personal_emails']
        if (EmailNumber > 0):
            L.append("1")
            print("1")
        else:
            L.append("0")
            print("0")
    return L

def scroll():
    for i in range(0, 20):
        try:
            lenOfPage = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
            time.sleep(5)
            browser.find_element_by_xpath("//div[@class='more']").click()
        except NoSuchElementException:
            pass
        print("Scroll numer " + str (i))

    i += 1



def click(x):
    browser.find_element_by_xpath(x).click()
def createToCSV():
    name_list = browser.find_elements_by_xpath("//div[@class='name']")
    names = [x.text for x in name_list]

    angel_link = browser.find_elements_by_xpath("//div[@class='name']//a[@data-type='Startup']")
    angels = [x.get_attribute("href") for x in angel_link]

    location_list = browser.find_elements_by_xpath("//div[@class='column location']//div[@class='value']")
    locations = [x.text for x in location_list]

    market_list = browser.find_elements_by_xpath("//div[@class='column market']//div[@class='value']")
    markets = [x.text for x in market_list]

    website_list = browser.find_elements_by_xpath("//a[@rel=' nofollow noopener noreferrer']")
    websites = [x.get_attribute("href") for x in website_list]

    size_list = browser.find_elements_by_xpath("//div[@class='column company_size']//div[@class='value']")
    sizes = [x.text for x in size_list]

    raised_list = browser.find_elements_by_xpath("//div[@class='column raised']")
    raised = [x.text for x in raised_list]
    emails = HuntCheck(websites)

    with open('lista.csv', 'w', newline='') as f:
        thewriter = csv.writer(f)
        for name, angel, location, market, website, size, money , email in zip(names, angels, locations, markets, websites,sizes, raised, emails):
            thewriter.writerow([name, angel, location, market, website, size, money, email])
def nextToCSV():
    name_list = browser.find_elements_by_xpath("//div[@class='name']")
    names = [x.text for x in name_list]

    angel_link = browser.find_elements_by_xpath("//div[@class='name']//a[@data-type='Startup']")
    angels = [x.get_attribute("href") for x in angel_link]

    location_list = browser.find_elements_by_xpath("//div[@class='column location']//div[@class='value']")
    locations = [x.text for x in location_list]

    market_list = browser.find_elements_by_xpath("//div[@class='column market']//div[@class='value']")
    markets = [x.text for x in market_list]

    website_list = browser.find_elements_by_xpath("//a[@rel=' nofollow noopener noreferrer']")
    websites = [x.get_attribute("href") for x in website_list]

    size_list = browser.find_elements_by_xpath("//div[@class='column company_size']//div[@class='value']")
    sizes = [x.text for x in size_list]

    raised_list = browser.find_elements_by_xpath("//div[@class='column raised']")
    raised = [x.text for x in raised_list]

    emails = HuntCheck(websites)

    with open('lista.csv', 'a', newline='') as f:
        thewriter = csv.writer(f)
        for name, angel, location, market, website, size, money , email in zip(names, angels, locations, markets, websites,sizes, raised, emails):
            thewriter.writerow([name, angel, location, market, website, size, money, email])
def scrollClick(x):
    click(x)
    scroll()

def firstPage():

    browser.get("https://angel.co/companies?tab=claimed&company_types[]=Startup&locations[]=1692-San+Francisco,+CA&markets[]=Enterprise+Software")
    scroll()




firstPage()
createToCSV()
scrollClick(x="//div[@class='column selected signal sortable']")
nextToCSV()
scrollClick(x="//div[@class='column joined sortable']")
nextToCSV()
scrollClick(x="//div[@class='column raised sortable']")
nextToCSV()


