"""
itc project: data mining.
Asi/Emanuel

Due-Date - 21/2/21
"""

# imports:
import conf
from itertools import count
import requests
import time
import pprint
from bs4 import BeautifulSoup
from selenium import webdriver

def get_data_from_response(response):
    try:
        return BeautifulSoup(response.text, 'lxml')
    except AttributeError:
        return f'url defected'


def get_response(url):
    sequence = count(start=1, step=1)
    response = requests.get(url)
    if response.status_code == 200:
        print(f'{next(sequence)} \tOK! {url} is good to go got response code: {response.status_code}\n')
        return response
    else:
        print(f'{next(sequence)} \tERROR :  NOT OK! {url} got bad response got response code: {response.status_code}\n')
        return response

def get_data_from_url(url):
    driver = webdriver.Chrome(
        r'chromedriver.exe')  # Optional argument, if not specified will search path.
    etf_data = dict()
    data = dict()

    driver.get(url)
    # time.sleep(2)  # Let the user actually see something!
    soup = BeautifulSoup(driver.page_source)
    name = soup.find("h1", class_="etf pull-left w-100")
    charts = soup.find_all('div', class_="col-md-12 col-sm-12 col-xs-12 no-padding pull-left my15")
    for chart in charts:
        table_row_name = chart.find_all('span', class_="truncate display-inline-b maxw-60")
        table_row_percent = chart.find_all('span', class_="bold pull-right text-right")

        for name, percent in zip(table_row_name, table_row_percent):
            data[name.text] = percent.text

        etf_data[chart.h4.text] = data
        data = dict()

    summary = soup.find_all('div', class_="generalData col-md-12 no-padding 0 pull-left col-xs-12 col-sm-12")
    idx = 1
    new_dict_data = dict()
    for data in summary:
        name = data.find("h4", class_="w-100 my5")

        table_row_name2 = data.find_all('label', class_="fund-report-tooltip highlighted-text tooltipstered")
        table_row_percent2 = data.find_all('span')
        new_data = list()
        new_percent = list()
        for data1 in table_row_name2:
            new_data.append(data1.text.replace("\n", ""))
        for data2 in table_row_percent2:
            if "Fund Home" in data2.text:
                pass
            else:
                new_percent.append(data2.text)

        for element1, element2 in zip(new_data,new_percent):
            new_dict_data[element1] = element2
        etf_data[name.text] = new_dict_data

        new_dict_data = dict()

        idx += 1
    # time.sleep(2)  # Let the user actually see something!
    driver.quit()
    return etf_data


def main():
    id = 1
    full_dict = dict()
    for url in conf.url_list:
        full_dict[url] = get_data_from_url(url)
        id += 1

    pprint.pprint(full_dict)


if __name__ == '__main__':
    main()
