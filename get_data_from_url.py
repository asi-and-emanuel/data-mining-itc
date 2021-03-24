import time
import re


def remove_leading_etf_name(field, etf):
    """
    This function removes the leading etf symbol from the field:
    eg: spy Top 10 Countries => Top 10 Countries
    This will be useful when we will compare the fields of several ETF's, that will now have the exact same field
    :param field: the original field
    :param etf: the etf symbol
    :return: the field without the leading etf symbol, useless since it's already in the etf data
    """
    if len(field) < 5:
        return field
    first_space = field.find(' ')
    if field.split(' ')[0] == etf:
        return field[first_space + 1:].replace(' [View All]', '').rstrip()
    return field.replace(' [View All]', '').rstrip()


def format_numbers(field):
    """
    This function takes a string as input and convert it to the relevant number format
    It is disabled for now (return the field) but we need to complete it at a further stage
    :param field: a field which is potentially a number
    :return: the number value of the field if the field was detected as a number
    """
    # return field
    if field[-1] == '%':
        return round(float(field[:-1]) / 100, 4)

    if field[0] == '$':
        if field[-1] == 'B':
            return int(float(field[1:-1]) * 1_000_000_000)
        if field[-1] == 'M':
            return int(float(field[1:-1]) * 1_000_000)
        if field[-1] == 'K':
            return int(float(field[1:-1]) * 1_000)
        return float(field[1:])

    if field.count(r'/') == 2:
        return time.strftime('%Y/%m/%d', time.strptime(field, '%m/%d/%y'))

    if field.replace(',', '').isdigit():
        return int(field.replace(',', ''))

    if field.replace('.', '', 1).isdigit():
        return float(field)

    return field


def get_data_from_url(soup, current_ETF):
    """
    get all the data from the URL soup
    :param soup: soup from html
    :param current_ETF: the current ETF to process
    :return: dictionary with all data
    """

    # initialize the needed dictionaries to store the data
    etf_data = dict()
    # finds all charts in soup
    charts = soup.find_all('div', class_="col-md-12 col-sm-12 col-xs-12 no-padding pull-left my15")

    # stores all the data inside lists, then adding them into the dictionaries
    for chart in charts:
        data = dict()
        table_row_name = chart.find_all('span', class_="truncate display-inline-b maxw-60")
        table_row_percent = chart.find_all('span', class_="bold pull-right text-right")
        for name, percent in zip(table_row_name, table_row_percent):
            data[name.text] = format_numbers(percent.text)
        etf_data[remove_leading_etf_name(chart.h4.text, current_ETF)] = data

    # finds all summary charts in soup
    summary = soup.find_all('div', class_="generalData col-md-12 no-padding 0 pull-left col-xs-12 col-sm-12")
    for data in summary:

        # finds the name of etf
        name = data.find("h4", class_="w-100 my5")

        # find all other data stores them in lists
        table_row_name2 = iter(data.find_all('label', class_="fund-report-tooltip highlighted-text tooltipstered"))
        table_row_percent2 = iter(data.find_all('span'))
        new_dict_data = dict()
        while True:
            try:
                cur_field, cur_data = next(table_row_name2).text.strip(), next(table_row_percent2).text.strip()
                if "Fund Home" in cur_data:
                    continue
                elif cur_field == 'Max. Premium / Discount (12 Mo)':
                    new_dict_data[cur_field] = format_numbers(cur_data.split(r' / ')[0])
                    new_dict_data[cur_field.replace('Max.', 'Min.')] = format_numbers(cur_data.split(r' / ')[1])
                elif cur_field == 'MSCI ESG Rating':
                    temp = re.findall(r'MSCI_ESG_(.+).jpg', next(iter(data.find_all('figure'))).contents[1].attrs['src'])
                    new_dict_data[cur_field] = format_numbers(temp[0])
                    cur_field = next(table_row_name2).text.strip()
                    new_dict_data[cur_field + ' (out of 10)'] = format_numbers(cur_data.split(r' / ')[0])
                else:
                    new_dict_data[cur_field] = format_numbers(cur_data)
            except StopIteration:
                break
        etf_data[remove_leading_etf_name(name.text, current_ETF)] = new_dict_data

    return etf_data
