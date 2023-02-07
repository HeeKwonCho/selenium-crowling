from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

search_url = "https://game.naver.com/esports/schedule/lck?date=2022-09"

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
browser = webdriver.Chrome('C:/chromedriver.exe', options=options)
browser.get(search_url)

browser.implicitly_wait(2)

schedules = browser.find_elements(By.CSS_SELECTOR, "#civ > div > div > div > div").text

for sechedule in schedules:
    date = browser.find_elements(By.CSS_SELECTOR, "#civ > div > div > div > div > div:nth-child(2) > div.list_wrap__3zIxG > div:nth-child(2)")
    information = browser.find_elements(By.CSS_SELECTOR, "#civ > div > div > div > div > div:nth-child(2) > div.list_wrap__3zIxG > div:nth-child(2) > ul")

    print(date, information)

