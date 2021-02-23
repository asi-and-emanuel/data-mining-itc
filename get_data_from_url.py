

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
