import subprocess
import mysql.connector


username = 'root'
password = 'Liri19012012'
database = 'Data/etf_id.db'
sql_dump_name = 'etf_id.sql'

with open(sql_dump_name, 'w') as f:
    f.write('CREATE SCHEMA `etf_id` ;\n')
    f.write('USE etf_id;')
    f.write('\n')
    proc = subprocess.Popen('sqlite3 Data/etf_id.db .dump', stdout=subprocess.PIPE)
    output = proc.stdout.read()
    f.write(output.decode())

with open(sql_dump_name, "r") as f:
    lines = f.readlines()

with open(sql_dump_name, "w") as f:
    for line in lines:
        if 'PRAGMA' in line.strip("\n") or \
                'BEGIN TRANSACTION' in line.strip("\n") or \
                line.strip("\n") == '':
            pass
        else:
            f.write(line)

my_db = mysql.connector.connect(host='127.0.0.1', user='root', passwd='Liri19012012')
cur = my_db.cursor()
for line in open(sql_dump_name):
    cur.execute(line)
