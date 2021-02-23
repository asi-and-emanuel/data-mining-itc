import re


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
