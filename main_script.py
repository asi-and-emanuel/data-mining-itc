from conf import RANDOM_MULTIPLE, RANDOM_FIX
import json
import time
from selenium import webdriver
from random import random
from get_data_from_url import get_data_from_url
from open_url_or_file import open_url_or_file
from create_db import create_db
import os
import re
import pandas as pd
import argparse


parser = argparse.ArgumentParser(description="this is etf.com data scraper it will download all data from 100 top "
                                             "links in etf.com")
group = parser.add_mutually_exclusive_group()
group.add_argument('-d', '--download', action="store_true", help='delete all eft *.html data and '
                                                                 'download new data this make take a while')
group.add_argument('-l', '--list', action="store_true", help='delete etf.com list data and download new '
                                                             '100 top list')
group.add_argument('-s', '--show', action="store_true", help='show the etf.com after downloading list')
group.add_argument('-sc', '--savecsv', action="store_true", help='save the etf to data.json file')
group.add_argument('-sj', '--savejson', action="store_true", help='save the etf to data.csv file')
group.add_argument('-sql', '--sqldb', action="store_true", help='save the etf to sql.db file')
group.add_argument('-ddb', '--del_DB', action="store_true", help='Deletes the data base Data/etf_id.db in order to'
                                                                 ' create the new one with -sql')
args = parser.parse_args()


def main():
    # initialize the full dict of etf data
    full_dict = dict()

    # sets the urls
    all_etf_url = r'https://www.etf.com/etfanalytics/etf-finder'
    base_url = r'https://www.etf.com/'
    mypath = "ETF_raw_data"
    only_files = [f for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath, f))]

    if args.download:
        only_files.remove("all_etf_data.html")
        for i in only_files:
            os.remove(str(mypath) + '/' + str(i))


    if args.list:
        os.remove("ETF_raw_data/all_etf_data.html")

    print_idx = 1
    if args.show:
        for i in only_files:
            print(f"downloaded etf {print_idx} is : {i}")
            print_idx += 1
        exit()

    if args.del_DB:
        os.remove("Data/etf_id.db")
        exit()

    # dumps all to json file
    if args.savejson:
        with open('Data/data.json', 'w', encoding='utf-8') as f:
            json.dump(full_dict, f, ensure_ascii=False, indent=4)

    if args.savecsv:
        if os.path.isfile("Data/data.csv"):
            os.remove("Data/data.csv")
        data = pd.DataFrame(full_dict)
        data = data.fillna("-")
        data.to_csv("Data/data.csv")

    if args.sqldb:
        create_db()

    # start selenium driver for download
    # Optional argument, if not specified will search path.
    driver = webdriver.Chrome(r'chromedriver.exe')

    # join data to URL
    path_base_data = os.path.join(os.getcwd(), r'ETF_raw_data', '%s.html' % 'all_etf_data')
    all_etf_data = open_url_or_file(all_etf_url, path_base_data, is_all_data=True, download_new_list=True)
    #time.sleep(10)

    # finds the 100 first endings in the HTML
    first_100 = all_etf_data.find_all('a', 'linkTickerName')

    # for each ETF gets all the data and stores inside the dictionaries
    for current_ETF in first_100:
        current_ETF = current_ETF.text.strip()
        path_base_data = os.path.join(os.getcwd(), r'ETF_raw_data', '%s.html' % current_ETF)
        url_ETF = open_url_or_file(base_url + current_ETF, path_base_data)
        current_ETF_data = open_url_or_file(base_url, path_base_data)
        full_dict[current_ETF] = get_data_from_url(current_ETF_data, current_ETF)

    # finds and sets the drivers variables
    if 'driver' in locals() and isinstance(driver, webdriver.chrome.webdriver.WebDriver):
        time.sleep(RANDOM_MULTIPLE * random() + RANDOM_FIX)  # Let the user actually see something!
        driver.quit()


if __name__ == '__main__':
    main()
