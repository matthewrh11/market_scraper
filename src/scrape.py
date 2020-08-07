import bs4
import time
from selenium import webdriver
from bs4 import BeautifulSoup


def get_price(page):
    soup = BeautifulSoup(page, 'lxml')

    price = soup.find('div', 
        {'class':'tv-symbol-price-quote__value js-symbol-last'}).find('span').text
        
    return price

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
options.add_argument('--headless')
driver = webdriver.Chrome("G:\Projects\driver\chromedriver.exe", chrome_options=options)

# symbol = raw_input("Enter the stock symbol you are interested in: \n")
# exchange = raw_input("Enter the market this stock is traded on: \n")

symbol = 'SONA'
exchange = 'CSE'

url = "https://www.tradingview.com/symbols/{}-{}/".format(exchange, symbol)

while True:
    driver.get(url)
    price = get_price(driver.page_source)
    print ("\n \n The current price of {} on the {} is ${} a share. \n \n".format(symbol, exchange, price))
    time.sleep(15)