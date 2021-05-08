import time
from bs4 import BeautifulSoup
from requests import get
from selenium import webdriver
driver = webdriver.Chrome()
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, TimeoutException


driver.get("https://coinmarketcap.com/all/views/all/")
html_soup = BeautifulSoup
time.sleep(2)
tickers = []
coin_names = []
scroll_pause_time = 2
screen_height = driver.execute_script("return window.screen.height;")
i = 1
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
        
html_soup = BeautifulSoup(browser.page_source, 'html.parser')
            ticker = html_soup.find_all('td', class_ = 'cmc-table__cell cmc-table__cell--sortable cmc-table__cell--left cmc-table__cell--sort-by__symbol')
            coin_name = html_soup.find_all('a', class_ = 'cmc-link')
            for x in range(len(ticker)):
                coin_name = coin_name[x]
                ticker = ticker[x]
                coin_name = coin_name.a.text
                ticker = ticker.div.text
                print(ticker)
                tickers.append(ticker)
                coin_names.append(coin_name)