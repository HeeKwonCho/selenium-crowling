from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import csv

# 브라우저 생성
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
browser = webdriver.Chrome('C:/chromedriver.exe', options=options)

browser.get("https://www.ncbi.nlm.nih.gov/nlmcatalog?term=currentlyindexed")
browser.implicitly_wait(10) # 로딩이 끝날 때까지 10초까지는 기다려줌

# 논문 정보 div
contents = browser.find_elements(By.CSS_SELECTOR, "#maincontent > div")

for content in contents:
    title = content.find_element(By.CSS_SELECTOR, "#maincontent > div > div:nth-child(5) > div:nth-child(1) > div.rslt > p").text
    supp = content.find_element(By.CSS_SELECTOR, "#maincontent > div > div:nth-child(5) > div:nth-child(1) > div.rslt > div.supp").text
    resc = content.find_element(By.CSS_SELECTOR, "#maincontent > div > div:nth-child(5) > div:nth-child(1) > div.rslt > div.aux > div").text

    print(title,supp,resc)

   


