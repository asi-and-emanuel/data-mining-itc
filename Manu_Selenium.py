
from conf import RANDOM_MULTIPLE, RANDOM_FIX
import json
import time
from selenium import webdriver
from random import random
from get_data_from_url import get_data_from_url
from open_url_or_file import open_url_or_file
import os


def main():
    # initialize the full dict of etf data
    full_dict = dict()

    # start selenium driver for download
    driver = webdriver.Chrome(r'chromedriver.exe')  # Optional argument, if not specified will search path.

    # sets the urls
    all_etf_url = r'https://www.etf.com/etfanalytics/etf-finder'
    base_url = r'https://www.etf.com/'

    # join data to URL
    path_base_data = os.path.join(os.getcwd(), r'ETF_raw_data', '%s.html' % 'all_etf_data')
    all_etf_data = open_url_or_file(all_etf_url, path_base_data, is_all_data=True)
    time.sleep(10)

    # finds the 100 first endings in the HTML
    first_100 = all_etf_data.find_all('a', 'linkTickerName')

    # for each ETF gets all the data and stores inside the dictionaries
    for current_ETF in first_100:
        current_ETF = current_ETF.text.strip()
        path_base_data = os.path.join(os.getcwd(), r'ETF_raw_data', '%s.html' % current_ETF)
        url_ETF = open_url_or_file(base_url + current_ETF, path_base_data)
        current_ETF_data = open_url_or_file(base_url, path_base_data)
        full_dict[current_ETF] = get_data_from_url(current_ETF_data)

    # dumps all to json file
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(full_dict, f, ensure_ascii=False, indent=4)

    # finds and sets the drivers variables
    if 'driver' in locals() and isinstance(driver, webdriver.chrome.webdriver.WebDriver):
        time.sleep(RANDOM_MULTIPLE * random() + RANDOM_FIX)  # Let the user actually see something!
        driver.quit()


if __name__ == '__main__':
    main()
