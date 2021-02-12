"""
itc project: data mining.
Asi/Emanuel

Due-Date - 21/2/21
"""

# imports:
import conf
from itertools import count
import requests

def get_respone(url):
    sequence = count(start=1, step=1)
    response = requests.get(url)
    if response.status_code == 200:
        return f'{next(sequence)} \tOK! {url} is good to go got response code: {response.status_code}\n'
    else:
        return f'{next(sequence)} \tERROR :  NOT OK! {url} got bad response got response code: {response.status_code}\n'


def main():
    with open('stdout.log', 'w', encoding="utf-8") as f:
        for url in conf.url_list:
            f.write(get_respone(url))
    pass


if __name__ == '__main__':

    main()
