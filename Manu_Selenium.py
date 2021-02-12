

import time
from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome(r'D:\Apps Install\chromedriver.exe')  # Optional argument, if not specified will search path.
driver.get('https://www.etf.com/SPY')
time.sleep(5) # Let the user actually see something!
soup = BeautifulSoup(driver.page_source)
test = soup.find('div', {'id': "totalTop10Holdings2"})
#test = soup.findall("div", {"class": "list-column-count2"})
#search_box = driver.find_element_by_xpath(r'/html/body/div[7]/section/div/div/div[3]/div[1]/div[1]/div[9]/div/div[2]/div')
#search_box = driver.find_element_by_name('totalTop10Holdings2')
#search_box = driver.find_element_by_name('overview')
#search_box.send_keys('ChromeDriver')
#search_box.submit()
time.sleep(5) # Let the user actually see something!
driver.quit()
