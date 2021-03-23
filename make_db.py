import sqlite3
import os
import contextlib
import json
import  pprint

mypath = "ETF_raw_data"


only_files = [f for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath, f))]
only_files.remove("all_etf_data.html")
idx = 0


etf_idx = 0
etf_lst = list()
etf_list_data_lst = list()
top_10_countries_lst = list()
top_10_countries_list_data_lst = list()
top_10_sectors_lst = list()
top_10_sectors_list_data_lst = list()
top_10_holdings_lst = list()
top_10_holdings_list_data_lst = list()
summary_data_lst = list()
summary_data_list_data_lst = list()
portfolio_data_lst = list()
portfolio_data_list_data_lst = list()
index_data_lst = list()
index_data_list_data_lst = list()
tradability_data_lst = list()
tradability_data_list_data_lst = list()
performance_statistics_data_lst = list()
performance_statistics_data_list_data_lst = list()
MSCI_ESG_ratings_data_lst = list()
MSCI_ESG_ratings_data_list_data_lst = list()

file_path = 'data.json'


##############################################################################
idx_country = 0
country_list_set = set()
country_list_dict = dict()

with open(file_path) as f:
    data = json.loads(f.read())
    for etf in data:
        if 'Top 10 Countries' in data[etf]:
            for element in data[etf]['Top 10 Countries'].keys():
                country_list_set.add(element)

        else:
            pass
        idx += 1

for val,item in enumerate(sorted(country_list_set)):
    country_list_dict[item] = val

#####################################################################################################
idx = 0
idx_sectors = 0
sectors_list_set = set()
sectors_list_dict = dict()

with open(file_path) as f:
    data = json.loads(f.read())
    for etf in data:
        # print(f"{etf} - {idx}")
        if 'Top 10 Sectors' in data[etf]:
            for element in data[etf]['Top 10 Sectors'].keys():
                sectors_list_set.add(element)
        else:
            pass
        idx += 1

for val,item in enumerate(sorted(sectors_list_set)):
    sectors_list_dict[item] = val
# pprint.pprint(sectors_list_dict)
###################################################################################################

idx = 0
idx_holdings = 0
holdings_list_set = set()
holdings_list_dict = dict()

with open(file_path) as f:
    data = json.loads(f.read())
    for etf in data:
        # print(f"{etf} - {idx}")
        if 'Top 10 Holdings' in data[etf]:
            for element in data[etf]['Top 10 Holdings'].keys():
                holdings_list_set.add(element)
        else:
            pass
        idx += 1

for val,item in enumerate(sorted(holdings_list_set)):
    holdings_list_dict[item] = val

#####################################################################
with open(file_path) as json_file:
    data = json.loads(json_file.read())
    for etf in data:
        etf_lst.append(etf_idx)
        etf_lst.append(etf)
        etf_list_data_lst .append(etf_lst)
        etf_lst = list()
        if etf in data:
            if 'Top 10 Countries' in data[etf]:
                for element in data[etf]['Top 10 Countries']:
                    top_10_countries_lst.append(etf_idx)
                    top_10_countries_lst.append(country_list_dict[element])
                    top_10_countries_lst.append(element)
                    top_10_countries_lst.append(float(data[etf]['Top 10 Countries'][element][:-1]))
                    top_10_countries_list_data_lst.append(top_10_countries_lst)
                    top_10_countries_lst = list()
            if 'Top 10 Sectors' in data[etf]:
                for element in data[etf]['Top 10 Sectors']:
                    top_10_sectors_lst.append(etf_idx)
                    top_10_sectors_lst.append(sectors_list_dict[element])
                    top_10_sectors_lst.append(element)
                    top_10_sectors_lst.append(float(data[etf]['Top 10 Sectors'][element][:-1]))
                    top_10_sectors_list_data_lst.append(top_10_sectors_lst)
                    top_10_sectors_lst = list()
            if 'Top 10 Holdings' in data[etf]:
                for element in data[etf]['Top 10 Holdings']:
                    top_10_holdings_lst.append(etf_idx)
                    top_10_holdings_lst.append(holdings_list_dict[element])
                    top_10_holdings_lst.append(element)
                    top_10_holdings_lst.append(float(data[etf]['Top 10 Holdings'][element][:-1]))
                    top_10_holdings_list_data_lst.append(top_10_holdings_lst)
                    top_10_holdings_lst = list()
            if 'Summary Data' in data[etf]:
                for element in data[etf]['Summary Data']:
                    summary_data_lst.append(etf_idx)
                    summary_data_lst.append(element)
                    summary_data_lst.append(str(data[etf]['Summary Data'][element]))
                    summary_data_list_data_lst.append(summary_data_lst)
                    summary_data_lst = list()
            if 'Portfolio Data' in data[etf]:
                for element in data[etf]['Portfolio Data']:
                    portfolio_data_lst.append(etf_idx)
                    portfolio_data_lst.append(element)
                    portfolio_data_lst.append(str(data[etf]['Portfolio Data'][element]))
                    portfolio_data_list_data_lst.append(portfolio_data_lst)
                    portfolio_data_lst = list()
            if 'Index Data' in data[etf]:
                for element in data[etf]['Index Data']:
                    index_data_lst.append(etf_idx)
                    index_data_lst.append(element)
                    index_data_lst.append(str(data[etf]['Index Data'][element]))
                    index_data_list_data_lst.append(index_data_lst)
                    index_data_lst = list()
            if 'Tradability' in data[etf]:
                for element in data[etf]['Tradability']:
                    tradability_data_lst.append(etf_idx)
                    tradability_data_lst.append(element)
                    tradability_data_lst.append(str(data[etf]['Tradability'][element]))
                    tradability_data_list_data_lst.append(tradability_data_lst)
                    tradability_data_lst = list()
            if 'Performance Statistics' in data[etf]:
                for element in data[etf]['Performance Statistics']:
                    performance_statistics_data_lst.append(etf_idx)
                    performance_statistics_data_lst.append(element)
                    performance_statistics_data_lst.append(str(data[etf]['Performance Statistics'][element]))
                    performance_statistics_data_list_data_lst.append(performance_statistics_data_lst)
                    performance_statistics_data_lst = list()
            if 'MSCI ESG Ratings' in data[etf]:
                for element in data[etf]['MSCI ESG Ratings']:
                    MSCI_ESG_ratings_data_lst.append(etf_idx)
                    MSCI_ESG_ratings_data_lst.append(element)
                    MSCI_ESG_ratings_data_lst.append(str(data[etf]['MSCI ESG Ratings'][element]))
                    MSCI_ESG_ratings_data_list_data_lst.append(MSCI_ESG_ratings_data_lst)
                    MSCI_ESG_ratings_data_lst = list()
            etf_idx += 1
        else:
            pass


# print(etf_list_data_lst)
# print(top_10_countries_list_data_lst)
# print(top_10_sectors_list_data_lst)
# print(top_10_holdings_list_data_lst)
# print(summary_data_list_data_lst)
# print(portfolio_data_list_data_lst)
# print(index_data_list_data_lst)
# print(tradability_data_list_data_lst)
# print(performance_statistics_data_list_data_lst)
print(MSCI_ESG_ratings_data_list_data_lst)


TEST_DB_FILENAME = 'etf_id.db'

if os.path.exists(TEST_DB_FILENAME):
    print(f'DB already exists:{TEST_DB_FILENAME}')
else:
    with contextlib.closing(sqlite3.connect(TEST_DB_FILENAME)) as con: # auto-closes
        with con: # auto-commits
            cur = con.cursor()
            cur.execute(
                '''CREATE TABLE etf_id (
                    etf_id INT PRIMARY KEY,
                    etf_name VARCHAR)'''
            )
            for i in etf_list_data_lst:
                # print(str(i[0]), str(i[1]), str(i[2]), str(i[3]), str(i[4]), str(i[5]), str(i[6]) )
                cur.execute(
                    "INSERT INTO etf_id (etf_id, etf_name) VALUES (?, ?)",
                    [i[0], i[1]]
                )
                if idx % 100 == 0:
                    con.commit()

            cur.execute(
                '''CREATE TABLE top_10_countries (
                    etf_id INT,
                    country_id INT,
                    country_name VARCHAR,
                    country_percent FLOAT)'''
            )
            for i in top_10_countries_list_data_lst:
                cur.execute(
                    "INSERT INTO top_10_countries (etf_id, country_id, country_name, country_percent)"
                    " VALUES (?, ?, ?, ?)",
                    [i[0], i[1], i[2], i[3]]
                )
                if idx % 100 == 0:
                    con.commit()

            cur.execute(
                '''CREATE TABLE top_10_sectors (
                    etf_id INT,
                    sector_id INT,
                    sector_name VARCHAR,
                    sector_percent FLOAT)'''
            )
            for i in top_10_sectors_list_data_lst:
                cur.execute(
                    "INSERT INTO top_10_sectors (etf_id, sector_id, sector_name, sector_percent)"
                    " VALUES (?, ?, ?, ?)",
                    [i[0], i[1], i[2], i[3]]
                )
                if idx % 100 == 0:
                    con.commit()

            cur.execute(
                '''CREATE TABLE top_10_holdings (
                    etf_id INT,
                    holdings_id INT,
                    holdings_name VARCHAR,
                    holdings_percent FLOAT)'''
            )
            for i in top_10_holdings_list_data_lst:
                cur.execute(
                    "INSERT INTO top_10_holdings (etf_id, holdings_id, holdings_name, holdings_percent)"
                    " VALUES (?, ?, ?, ?)",
                    [i[0], i[1], i[2], i[3]]
                )
                if idx % 100 == 0:
                    con.commit()

            cur.execute(
                '''CREATE TABLE summary_data (
                    etf_id INT,
                    data_name VARCHAR,
                    data VARCHAR)'''
            )
            for i in summary_data_list_data_lst:
                cur.execute(
                    "INSERT INTO summary_data (etf_id, data_name, data)"
                    " VALUES (?, ?, ?)",
                    [i[0], i[1], i[2]]
                )
                if idx % 100 == 0:
                    con.commit()

            cur.execute(
                '''CREATE TABLE portfolio_data (
                    etf_id INT,
                    portfolio_data_name VARCHAR,
                    data VARCHAR)'''
            )
            for i in portfolio_data_list_data_lst:
                cur.execute(
                    "INSERT INTO portfolio_data (etf_id, portfolio_data_name, data)"
                    " VALUES (?, ?, ?)",
                    [i[0], i[1], i[2]]
                )
                if idx % 100 == 0:
                    con.commit()

            cur.execute(
                '''CREATE TABLE index_data (
                    etf_id INT,
                    index_data_name VARCHAR,
                    data VARCHAR)'''
            )
            for i in index_data_list_data_lst:
                cur.execute(
                    "INSERT INTO index_data (etf_id, index_data_name, data)"
                    " VALUES (?, ?, ?)",
                    [i[0], i[1], i[2]]
                )
                if idx % 100 == 0:
                    con.commit()

            cur.execute(
                '''CREATE TABLE tradability_data (
                    etf_id INT,
                    tradability_data_name VARCHAR,
                    data VARCHAR)'''
            )
            for i in tradability_data_list_data_lst:
                cur.execute(
                    "INSERT INTO tradability_data (etf_id, tradability_data_name, data)"
                    " VALUES (?, ?, ?)",
                    [i[0], i[1], i[2]]
                )
                if idx % 100 == 0:
                    con.commit()

            cur.execute(
                '''CREATE TABLE performance_statistics_data (
                    etf_id INT,
                    performance_statistics_data_name VARCHAR,
                    data VARCHAR)'''
            )
            for i in performance_statistics_data_list_data_lst:
                cur.execute(
                    "INSERT INTO performance_statistics_data (etf_id, performance_statistics_data_name, data)"
                    " VALUES (?, ?, ?)",
                    [i[0], i[1], i[2]]
                )
                if idx % 100 == 0:
                    con.commit()

            cur.execute(
                '''CREATE TABLE MSCI_data (
                    etf_id INT,
                    MSCI_data_name VARCHAR,
                    data VARCHAR)'''
            )
            for i in MSCI_ESG_ratings_data_list_data_lst:
                cur.execute(
                    "INSERT INTO MSCI_data (etf_id, MSCI_data_name, data)"
                    " VALUES (?, ?, ?)",
                    [i[0], i[1], i[2]]
                )
                if idx % 100 == 0:
                    con.commit()

with contextlib.closing(sqlite3.connect(TEST_DB_FILENAME)) as con: # auto-closes
    cur = con.cursor()
    cur.execute('SELECT * FROM MSCI_data LIMIT 10')
    result = cur.fetchall()

print(result)