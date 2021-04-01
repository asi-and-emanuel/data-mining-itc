import sqlite3
import os
import contextlib
import json


def generate_db(path_to_file, data, data_dict):
    with contextlib.closing(sqlite3.connect(path_to_file)) as con:  # auto-closes
        with con:  # auto-commits
            cur = con.cursor()

            for table in data:
                table_name = '_'.join(table.lower().split())
                data_k = data_dict[table_name].keys()
                exec_command = 'CREATE TABLE %s (%s)' % (table_name, ', '.join(['%s %s' % (k, v) for k, v in
                                                                                data_dict[table_name].items()]))
                add_command = 'INSERT INTO %s (%s) VALUES (%s)' % (table_name, ', '.join(map(str, data_k)),
                                                                   ', '.join(['?'] * len(data_k)))

                cur.execute(exec_command)
                for entry in data[table]:
                    cur.execute(add_command, entry)
                con.commit()


def parse_json_tables(json_file):
    with open(json_file) as f:
        data = json.loads(f.read())
    return data


def parse_json(json_file):
    """
    This function inputs the path to a json_file, opens it and create from it 3 dictionaries:
    all_data - fields_indexed - all_data_sql
    :param json_file: the path to a json_file to parse
    :return: all_data: a dict containing all the fields and the relevant values from each ETF
    fields_indexed: a dict containing 3 dicts, one for each of the 3 common fields:
    Top 10 Countries, Top 10 Sectors and Top 10 Holdings
    Each one of these 3 dicts contains all the existing fields and a running reference number
    all_data_sql: a dict containing all the fields and the relevant values from each ETF,
    but with one line for each data
    """
    with open(json_file) as f:
        data = json.loads(f.read())

    all_fields = data['SPY'].keys()
    top_10_fields = ['Top 10 Countries', 'Top 10 Sectors', 'Top 10 Holdings']

    all_data = dict()
    all_data['ETF ID'] = {k: v for k, v in enumerate(data.keys())}
    for field in all_fields:
        all_data[field] = {k: v[field] if field in v else {'Null': 1.0} for k, v in data.items()}

    fields_indexed = dict()
    for field in top_10_fields:
        fields_indexed[field] = {v: k for k, v in enumerate(sorted(
            set([val for sublist in (list(all_data[field][k].keys()) for k in all_data[field].keys())
                 for val in sublist if val != 'Null'])))}
        fields_indexed[field]['Null'] = 9999

    all_data_sql = dict()
    all_data_sql['ETF ID'] = [[k, v] for k, v in enumerate(data.keys())]
    for field in all_fields:
        cur_fields = list()
        for etf_idx, (etf_name, values) in enumerate(all_data[field].items()):
            if field in fields_indexed.keys():
                cur_fields.extend([[etf_idx, etf_name, fields_indexed[field][key], key, value]
                                   for key, value in values.items()])
            else:
                cur_fields.extend([[etf_idx, etf_name, key, value] for key, value in values.items()])
        all_data_sql[field] = cur_fields

    return all_data, fields_indexed, all_data_sql


def create_db():

    my_path = "ETF_raw_data"

    only_files = [f for f in os.listdir(my_path) if os.path.isfile(os.path.join(my_path, f))]
    only_files.remove("all_etf_data.html")

    file_path = 'Data/data.json'
    all_data, fields_indexed, all_data_sql = parse_json(file_path)

    data_fields_json = 'Data/all_tables.json'
    data_fields = parse_json_tables(data_fields_json)
    db_filename = 'Data/etf_id.db'

    if os.path.exists(db_filename):
        print(f'DB already exists:{db_filename}')
    else:
        generate_db(db_filename, all_data_sql, data_fields)
        print("DB created")

    # with contextlib.closing(sqlite3.connect(db_filename)) as con: # auto-closes
    #     cur = con.cursor()
    #     cur.execute('SELECT * FROM msci_esg_ratings LIMIT 10')
    #     result = cur.fetchall()
    #
    # print(result)
