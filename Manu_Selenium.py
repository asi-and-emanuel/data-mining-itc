
from conf import RANDOM_MULTIPLE, RANDOM_FIX
import time
from selenium import webdriver
from bs4 import BeautifulSoup
from random import random
import re
import os


def split_percent_string(my_string):
    output_dict = {}
    all_fields = my_string.split('%')[:-1]
    for my_field in all_fields:
        my_sep = re.search(r"\d", my_field).start()
        my_key, my_value = my_field[:my_sep], my_field[my_sep:]
        my_value = float(my_value) / 100
        output_dict[my_key] = my_value
    return output_dict


def open_url_or_file(url, local_file, is_all_data=False):
    if not os.path.isfile(local_file):
        driver = webdriver.Chrome(r'chromedriver.exe')  # Optional argument, if not specified will search path.
        time.sleep(RANDOM_MULTIPLE * random() + RANDOM_FIX) # Let the user actually see something!
        driver.get(url)
        time.sleep(15)
        element = driver.find_element_by_xpath("//button[@value='100']")
        driver.execute_script("arguments[0].click();", element)
        time.sleep(RANDOM_MULTIPLE * random() + RANDOM_FIX) # Let the user actually see something!
        soup = BeautifulSoup(driver.page_source, "html.parser")
        with open(local_file, "w", encoding='utf-8') as file:
            file.write(str(soup))
    else:
        with open(local_file, "r") as file:
            soup = BeautifulSoup(file.read(), "html.parser")
    return soup


def main():
    driver = webdriver.Chrome(r'chromedriver.exe')  # Optional argument, if not specified will search path.
    all_etf_url = r'https://www.etf.com/etfanalytics/etf-finder'
    base_url = r'https://www.etf.com/'
    path_base_data = os.path.join(os.getcwd(), r'ETF_raw_data', '%s.html' % 'all_etf_data')
    all_etf_data = open_url_or_file(all_etf_url, path_base_data, is_all_data=True)
    time.sleep(10)

    first_100 = all_etf_data.find_all('a', 'linkTickerName')



    for current_ETF in first_100:
        current_ETF = current_ETF.text.strip()
        path_base_data = os.path.join(os.getcwd(), r'ETF_raw_data', '%s.html' % current_ETF)
        url_ETF = open_url_or_file(base_url + current_ETF, path_base_data)
        current_ETF_data = open_url_or_file(base_url, path_base_data)
        test1 = current_ETF_data.find_all('div', {'id': "totalTop10Holdings2"})
        countries = split_percent_string(test1[0].text)
        sectors = split_percent_string(test1[1].text)
        stocks = split_percent_string(test1[2].text)
        print(countries)
        print(sectors)
        print(stocks)

    if 'driver' in locals() and isinstance(driver, webdriver.chrome.webdriver.WebDriver):
        time.sleep(RANDOM_MULTIPLE * random() + RANDOM_FIX) # Let the user actually see something!
        driver.quit()


if __name__ == '__main__':
    main()
