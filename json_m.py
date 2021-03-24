import json
import os
import pprint
file_path = 'data.json'
mypath = "ETF_raw_data"

only_files = [f for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath, f))]
only_files.remove("all_etf_data.html")
idx = 0

idx_country = 0
country_list_set = set()
country_list_dict = dict()

with open(file_path) as f:
    data = json.loads(f.read())
    for etf in data:
        if str(only_files[idx][:-5]) in data:
            if 'Top 10 Countries' in data[str(only_files[idx][:-5])]:
                for element in data[str(only_files[idx][:-5])]['Top 10 Countries'].keys():
                    country_list_set.add(element)

        else:
            pass
        idx += 1

for val,item in enumerate(sorted(country_list_set)):
    country_list_dict[item] = val

pprint.pprint(country_list_dict)
