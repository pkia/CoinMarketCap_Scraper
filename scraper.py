#!/usr/bin/python
from datetime import datetime, date
import time
from bs4 import BeautifulSoup
import os
import pandas as pd
from requests import get
from selenium import webdriver
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)
from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementClickInterceptedException
tickers = []
coin_names = []

driver.get("https://coinmarketcap.com/all/views/all/")
html_soup = BeautifulSoup
time.sleep(2)
scroll_pause_time = 2
screen_height = driver.execute_script("return window.screen.height;")
i = 1
coin_exists = False
while True:
    driver.execute_script("window.scrollTo(0, {screen_height}*{i});".format(screen_height=screen_height, i=i))
    i += 1
    time.sleep(scroll_pause_time)
    scroll_height = driver.execute_script("return document.body.scrollHeight;")
    if (screen_height) * i > scroll_height:
        time.sleep(scroll_pause_time)
        try:
            driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/div/div[1]/div/div[3]/button").click()
        except (ElementClickInterceptedException, TimeoutException, NoSuchElementException):
            break
        

html_soup = BeautifulSoup(driver.page_source, 'html.parser')
ticker = html_soup.find_all('td', class_ = 'cmc-table__cell cmc-table__cell--sortable cmc-table__cell--left cmc-table__cell--sort-by__symbol')
coin_name = html_soup.find_all('div', class_ ="sc-1kxikfi-0 fjclfm cmc-table__column-name")
for cur_ticker in ticker:
    c_ticker = cur_ticker.div.text
    tickers.append(c_ticker)
for cur_name in coin_name:
    name = cur_name.a.text
    coin_names.append(name)
    
    
crypto_df = pd.DataFrame({'Coin_name': coin_names, 'ticker': tickers})
crypto_df.to_csv('crypto_scrape.csv')
webdriver.close()
            