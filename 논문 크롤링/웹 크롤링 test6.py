from webbrowser import Chrome
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# 크롬 드라이버 자동 업데이트
from webdriver_manager.chrome import ChromeDriverManager

import time
import pyautogui
import pyperclip


# 브라우저 꺼짐 방지
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# 불필요한 에러 메시지 없애기
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

service = Service(executable_path=ChromeDriverManager().install())
browser = webdriver.Chrome(service=service)

# 웹페이지 주소 이동
browser.maximize_window() # 화면 최대화
browser.get("https://pubmed.ncbi.nlm.nih.gov/?term=covid-19")
browser.implicitly_wait(10) # 웹페이지가 로딩 될때까지 5초는 기다림

# 스크롤 전 높이
before_h = browser.execute_script("return window.scrollY")

# 무한 스크롤
while True:
    # 맨 아래로 스크롤을 내린다.
    browser.find_element(By.CSS_SELECTOR, "body").send_keys(Keys.END)

    # 스크롤 사이 페이지 로딩 시간
    time.sleep(2)

    # 스크롤 후 높이
    after_h = browser.execute_script("return window.scrollY")

    if after_h == before_h:
        break
    before_h = after_h

# 논문 정보 div
contents = browser.find_elements(By.CSS_SELECTOR, ".full-docsum")

for content in contents:
    title = content.find_element(By.CSS_SELECTOR, ".docsum-title").text
    docsum_pmid = content.find_element(By.CSS_SELECTOR, ".docsum-pmid").text
    docsum_authors_full_authors = content.find_element(By.CSS_SELECTOR, "docsum_authors_full_authors").text

    print(title, docsum_pmid, docsum_authors_full_authors)
