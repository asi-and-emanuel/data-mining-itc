
from conf import RANDOM_MULTIPLE, RANDOM_FIX
import json
import time
from selenium import webdriver
from bs4 import BeautifulSoup
from random import random
import re
import os


def get_data_from_url(soup):
    """
    get all the data from the URL soup
    :param soup: soup from html
    :return: dictionary with all data
    """

    # initialize the needed dictionaries to store the data
    etf_data = dict()
    data = dict()
    # finds all charts in soup
    charts = soup.find_all('div', class_="col-md-12 col-sm-12 col-xs-12 no-padding pull-left my15")

    # stores all the data inside lists, then adding them into the dictionaries
    for chart in charts:
        table_row_name = chart.find_all('span', class_="truncate display-inline-b maxw-60")
        table_row_percent = chart.find_all('span', class_="bold pull-right text-right")
        for name, percent in zip(table_row_name, table_row_percent):
            data[name.text] = percent.text
        etf_data[chart.h4.text] = data
        data = dict()

    # finds all summary charts in soup
    summary = soup.find_all('div', class_="generalData col-md-12 no-padding 0 pull-left col-xs-12 col-sm-12")
    new_dict_data = dict()
    for data in summary:

        # finds the name of etf
        name = data.find("h4", class_="w-100 my5")

        # find all other data stores them in lists
        table_row_name2 = data.find_all('label', class_="fund-report-tooltip highlighted-text tooltipstered")
        table_row_percent2 = data.find_all('span')
        new_data = list()
        new_percent = list()
        for data1 in table_row_name2:
            new_data.append(data1.text.replace("\n", ""))
        for data2 in table_row_percent2:
            # pass the fund home and not adding it
            if "Fund Home" in data2.text:
                pass
            else:
                new_percent.append(data2.text)
        # zip the lists into the dictionaries
        for element1, element2 in zip(new_data, new_percent):
            new_dict_data[element1] = element2
        etf_data[name.text] = new_dict_data
        new_dict_data = dict()

    return etf_data


def split_percent_string(my_string):
    """
    splitting the percent string into a float
    :param my_string: full string from file
    :return:  string without %
    """

    output_dict = {}
    all_fields = my_string.split('%')[:-1]
    for my_field in all_fields:
        my_sep = re.search(r"\d", my_field).start()
        my_key, my_value = my_field[:my_sep], my_field[my_sep:]
        my_value = float(my_value) / 100
        output_dict[my_key] = my_value
    return output_dict


def open_url_or_file(url, local_file, is_all_data=False):
    """
    finds if there is a downloaded file or not for the etf sent
    :param url: url for the etf
    :param local_file: if there is local file uses it if not it downloads it
    :param is_all_data:
    :return: soup from file
    """

    # initialize if you want to download the etf list from the start
    download_new_list = False

    # if there is no file for the etf download it and get soup
    if not os.path.isfile(local_file):
        driver = webdriver.Chrome(r'chromedriver.exe')  # Optional argument, if not specified will search path.
        time.sleep(RANDOM_MULTIPLE * random() + RANDOM_FIX)  # Let the user actually see something!
        driver.get(url)
        time.sleep(15)

        # presses the 100 list button to download all of the etf
        if download_new_list:
            element = driver.find_element_by_xpath("//button[@value='100']")
            driver.execute_script("arguments[0].click();", element)

        time.sleep(RANDOM_MULTIPLE * random() + RANDOM_FIX)  # Let the user actually see something!
        soup = BeautifulSoup(driver.page_source, "html.parser")
        with open(local_file, "w", errors="ignore") as file:
            file.write(str(soup))
    # if not reads from HD
    else:
        with open(local_file, "r", errors="ignore") as file:
            soup = BeautifulSoup(file.read(), "html.parser")

    return soup


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
