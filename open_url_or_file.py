from conf import RANDOM_MULTIPLE, RANDOM_FIX
import time
from selenium import webdriver
from bs4 import BeautifulSoup
from random import random
import os


def open_url_or_file(url, local_file, is_all_data=False, download_new_list = False):
    """
    finds if there is a downloaded file or not for the etf sent
    :param url: url for the etf
    :param local_file: if there is local file uses it if not it downloads it
    :param is_all_data:
    :param download_new_list: for getting new list set to true
    :return: soup from file
    """

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

