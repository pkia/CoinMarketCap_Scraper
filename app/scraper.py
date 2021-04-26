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