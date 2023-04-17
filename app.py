from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas
import time

keywords = ["매일 멸균우유", "매일치즈", "매일우유"]

def prepare_browser():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("start-maximized")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option("useAutomationExtension", False)
    driver = webdriver.Chrome(options= chrome_options)
    return driver

def scrape(keyword):
    print (f"->[{keyword}] 검색결과 데이터를 가져오고 있습니다...")

    url = f'https://search.shopping.naver.com/search/all?frm=NVSHMDL&origQuery={keyword}&pagingIndex=1&pagingSize=40&productSet=model&query={keyword}&sort=rel&timestamp=&viewType=list'

    chrome = prepare_browser()
    chrome.get(url)

    wait = WebDriverWait(chrome, 10)
    original_window = chrome.current_window_handle

    assert len(chrome.window_handles) == 1

    chrome.find_element(By.ID, "content").find_element(By.CLASS_NAME, "basicList_link__JLQJf").click()
    wait.until(EC.number_of_windows_to_be(2))
    for window_handle in chrome.window_handles:
        if window_handle != original_window:
            chrome.switch_to.window(window_handle)
            break

    try:
        chrome.find_element(By.CLASS_NAME, "filter_chk_box__wz1oX").click()
        chrome.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
        chrome.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
        time.sleep(1)

        detail_filter = chrome.find_elements(By.CLASS_NAME, "filter_condition_group__h8Gss")
        options = detail_filter[1].find_elements(By.CLASS_NAME, "filter_text__J8EIh")
        for option in options:
            if option.text == '24개':
                option.click()
        time.sleep(1)
    except:
        pass
    
    obj = {
        'market': 'productList_mall_link__TrYxC',
        'title': 'productList_title__R1qZP',
        'price': 'productList_value__B_IxM',
        'delivery': 'productList_delivery__WwSwL',
    }
    markets = chrome.find_elements(By.CLASS_NAME, obj['market'])
    titles = chrome.find_elements(By.CLASS_NAME, obj['title'])
    prices = chrome.find_elements(By.CLASS_NAME, obj['price'])
    deliveries = chrome.find_elements(By.CLASS_NAME, obj['delivery'])
    table = []
    for i in range(len(markets)):
        try:
            img = markets[i].find_element(By.TAG_NAME, "img")
        except:
            img = False
        table.append([img.get_attribute("alt") if img else markets[i].text, titles[i].text, prices[i].text, deliveries[i].text, titles[i].get_attribute("href")])
    
    df = pandas.DataFrame(table, columns=["판매처", "제목", "가격", "배송비", "링크"])
    with pandas.ExcelWriter(f"./{keyword}.xlsx") as writer:
        df.to_excel(writer)

    chrome.quit()

def main():
    for keyword in keywords:
        scrape(keyword)

if __name__ == '__main__':
    main()