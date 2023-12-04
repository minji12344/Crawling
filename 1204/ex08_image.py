# 스크래핑과 크롤링 차이 - 이미지 검색

from selenium import webdriver
from bs4 import BeautifulSoup
import time

def fn_soup(res):
    soup = BeautifulSoup(res, 'lxml')
    images = soup.find_all('div', attrs={'class': 'isv-r PNCib ViTmJb BUooTd'})
    for idx, image in enumerate(images):
        title = image.find('div', attrs={'class':'zbRPDe M2qv4b P4HtKe'}).get_text()
        print(idx + 1, ':', title)

options = webdriver.ChromeOptions()
# options.headless = True # 구글창으로 열기
options.add_argument('headless') # 구글창으로 열지않고 크롤링
options.add_argument('window-size=1900x1080')

browser = webdriver.Chrome(options=options)
browser.maximize_window()
url = 'https://www.google.com/search?q=%EC%86%A1%EC%A4%91%EA%B8%B0&sca_esv=587611622&tbm=isch&sxsrf=AM9HkKmXyQyk7CmKcPWQM3VLT5HzsfxSdw:1701677484196&source=lnms&sa=X&sqi=2&ved=2ahUKEwizxt7PqvWCAxWNslYBHYnGBMMQ_AUoAnoECAIQBA&biw=1397&bih=784&dpr=1'

browser.get(url)

# 이전 스크롤 높이
prev_height = browser.execute_script('return document.body.scrollHeight')
print('이전 높이 : ', prev_height)

while True:
    browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    time.sleep(2)
    curr_height = browser.execute_script('return document.body.scrollHeight')
    if prev_height == curr_height:
        break
    prev_height = curr_height

# print(prev_height)

res = browser.page_source
fn_soup(res)
time.sleep(10)
