import sqlite3
import os
import contextlib
import json
import datetime
import time

import pandas as pd
import requests
from cred_api import API_ADDRESS, TOKEN


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
        for etf_idx, values in enumerate(all_data[field].values()):
            if field in fields_indexed.keys():
                cur_fields.extend([[etf_idx, fields_indexed[field][key], key, value]
                                   for key, value in values.items()])
            else:
                cur_fields.extend([[etf_idx, key, value] for key, value in values.items()])
        all_data_sql[field] = cur_fields

    return all_data, fields_indexed, all_data_sql


def add_market_data_api(ETF_list):
    epoch = datetime.datetime(1970, 1, 1).date()
    date_today = datetime.datetime.now().date()
    date_minus_1y = datetime.date(date_today.year - 1, date_today.month, date_today.day)
    date_end = int((date_today - epoch).total_seconds())
    date_start = int((date_minus_1y - epoch).total_seconds())

    mkt_data_fields = ['date', 'etf', 'valid', 'open', 'high', 'low', 'close', 'volume']
    df = pd.DataFrame(columns=mkt_data_fields)
    for ETF in ETF_list:
        this_request = '%s%s&resolution=D&from=%s&to=%s&token=%s' % (API_ADDRESS, ETF, date_start, date_end, TOKEN)
        r = requests.get(this_request)
        while r.status_code != 200:
            time.sleep(60)
            print('Waiting 60 second because of the API usage...')
            r = requests.get(this_request)
        this_df = pd.DataFrame(r.json())
        this_df['date'] = pd.to_datetime(this_df['t'], unit='s')
        this_df['etf'] = ETF
        this_df = this_df[['date', 'etf', 's', 'o', 'h', 'l', 'c', 'v']]
        this_df.columns = mkt_data_fields
        df = df.append(this_df)
    mkt_data = df.reset_index().to_dict()
    len_df = df.shape[0]
    mkt_data_list = {key: list(v.values()) for key, v in mkt_data.items()}
    mkt_data_sql = [[mkt_data_list[field][x] for field in mkt_data_list if field != 'index'] for x in range(len_df)]

    return df, mkt_data_sql, mkt_data_fields


def create_db():

    my_path = "ETF_raw_data"

    only_files = [f for f in os.listdir(my_path) if os.path.isfile(os.path.join(my_path, f))]
    only_files.remove("all_etf_data.html")

    file_path = 'Data/data.json'
    all_data, fields_indexed, all_data_sql = parse_json(file_path)

    data_fields_json = 'Data/all_tables.json'
    data_fields = parse_json_tables(data_fields_json)
    db_filename = 'Data/etf_id.db'

    if not os.path.isfile(r'Data/market_data.csv'):
        market_data_df, mkt_data_sql, mkt_data_fields = add_market_data_api([x.split('.')[0] for x in only_files])
    else:
        df = pd.read_csv(r'Data/market_data.csv')
        mkt_data = df.reset_index().to_dict()
        len_df = df.shape[0]
        mkt_data_list = {key: list(v.values()) for key, v in mkt_data.items()}
        mkt_data_sql = [[mkt_data_list[field][x] for field in mkt_data_list if field != 'index'] for x in
                        range(len_df)]

    all_data_sql['market_data'] = mkt_data_sql

    if os.path.exists(db_filename):
        # TEMP HACK
        os.remove(db_filename)
        generate_db(db_filename, all_data_sql, data_fields)
        print(f'=============================\n\n\nDB already exists:{db_filename}\n\n\n'
              f'============================='
              f'\n\n\nif you wish to create a new db please delete Data/etf_id.db')
    else:
        generate_db(db_filename, all_data_sql, data_fields)
        print(f"=============================\n\n\nDB created - DB location :{db_filename}\n\n\n"
              f"=============================")
