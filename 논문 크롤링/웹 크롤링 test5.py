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
browser.get("https://www.naver.com")
browser.implicitly_wait(10) # 웹페이지가 로딩 될때까지 5초는 기다림

# 쇼핑 메뉴 클릭
browser.find_element(By.CSS_SELECTOR, "a.nav.shop").click()
time.sleep(2)

# 검색창 클릭
search = browser.find_element(By.CSS_SELECTOR, "input._searchInput_search_text_3CUDs")
search.click()

# 검색어 입력
search.send_keys("아이폰13")
search.send_keys(Keys.ENTER)


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

# 상품 정보 div
items = browser.find_elements(By.CSS_SELECTOR, ".basicList_item__0T9JD")

for item in items:
    name = item.find_element(By.CSS_SELECTOR, ".basicList_title__VfX3c").text
    price = item.find_element(By.CSS_SELECTOR, ".basicList_price_area__K7DDT").text
    link = item.find_element(By.CSS_SELECTOR, ".basicList_title__VfX3c > a").get_attribute('href')
    
    print(name, price, link)