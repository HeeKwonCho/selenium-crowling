from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
browser = webdriver.Chrome('C:/chromedriver.exe', options=options)

# 구글 지도 접속하기
browser.get("https://www.google.com/maps/")
browser.implicitly_wait(10) # 로딩이 끝날 때까지 10초까지는 기다려줌

searchbox = browser.find_element(By.CSS_SELECTOR, "#gs_lc50")
searchbox.click()

# 검색창에 "카페"입력하기
searchbox = browser.find_element(By.CSS_SELECTOR, "#gs_lc50")
searchbox.send_keys("카페")

# 검색버튼 누르기
searhcbutton = browser.find_element(By.CSS_SELECTOR, "#searchbox-searchbutton")
searhcbutton.click()



