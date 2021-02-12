"""
itc project: data mining.
Asi/Emanuel

Due-Date - 21/2/21
"""

# imports:
import conf
from itertools import count
import requests
from bs4 import BeautifulSoup


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


def main():

    response_list = list()                                      # initialize a new response list
    data_list = list()                                               # initialize a new data list

    for url in conf.url_list:
        response_list.append(get_response(url))
        # f.write(get_response(url))
    for response in response_list:
        data_list.append(get_data_from_response(response))
        # f.write(get_data_from_response(response))
    idx = 1
    for data, url in zip(data_list, conf.url_list):
        with open(f'file{idx}.log', 'w', encoding="utf-8") as f:
            f.write(str(f"the url is {url}:\n\n\n\n================================================================="))
            f.write(str(data.prettify()))
            f.write(str(f"end of file\n\n\n\n======================================================================="))
        idx += 1
    pass


if __name__ == '__main__':
    main()
