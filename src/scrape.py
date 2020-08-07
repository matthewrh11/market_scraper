import bs4
import requests
from bs4 import BeautifulSoup

symbol = input("Enter the stock symbol you are interested in: \n")
exchange = input("Enter the market this stock is traded on: \n")

print(symbol, exchange)