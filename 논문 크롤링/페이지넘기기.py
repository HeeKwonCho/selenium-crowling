from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# 브라우저 생성
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
browser = webdriver.Chrome('C:/chromedriver.exe', options=options)

browser.get("https://www.ncbi.nlm.nih.gov/nlmcatalog?term=currentlyindexed")
browser.implicitly_wait(10) # 로딩이 끝날 때까지 10초까지는 기다려줌

page_bar = browser.find_elements(By.CSS_SELECTOR, "#maincontent > div > div.title_and_pager.bottom > div > h3")[0]
page_bar 

pages = page_bar.find_elements(By.CSS_SELECTOR, "#EntrezSystem2\.PEntrez\.Nlmcatalog\.Nlmcatalog_ResultsPanel\.Entrez_Pager\.Page")
len(pages)

for page in pages :
    print(pages)

page_now = page_bar.find_elements(By.CSS_SELECTOR, "pageno2")[0].text.replace('현재 페이지', '').strip()
page_now


