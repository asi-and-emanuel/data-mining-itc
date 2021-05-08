# DATA MINING - ITC PROJECT
(by: Asi Sheratzki / Emmanuel Berdugo)<br /><br />
Data mining project ITC - on retrieving raw data and parsing data from URL<br />
Our sub topic is - stock exchange site "ETF.com".

# OUT LINE
Our project is based on the ETF site that have a lot of raw data on the the stocks ETF.<br />
there are many ETF's they are a group af stocks that have many characteristics. <br />

updated 8/5/2021:<br />
this is etf.com data scraper it will download all data from 100 top links in etf.com<br />

optional arguments:<br />

  -h, --help        show this help message and exit <br />
  -d, --download    delete all eft *.html data and download new data this make take a while <br />
  -l, --list        delete etf.com list data and download new 100 top list<br />
  -s, --show        show the etf.com after downloading list<br />
  -sc, --savecsv    save the etf to data.json file<br />
  -sj, --savejson   save the etf to data.csv file<br />
  -sql, --sqldb     save the etf to sql.db file<br />
  -ddb, --del_DB    Deletes the data base Data/etf_id.db in order to create the new one with -sql<br />
  -vs, --verbose_s  increase output verbosity to screen<br />
  -vl, --verbose_l  increase output verbosity to log<br />


# the data collected
### for every eft we will collect the data submitted bellow in a sql database

###FOR EXAMPLE: <br />

The ETF **"SPY"** is stated as : **"SPDR S&P 500 ETF Trust"**<br />

####it has many stock its made of: <br />
* Apple Inc.<br />
* Microsoft Corporation<br />
* Amazon.com, Inc.<br />
* Tesla Inc<br />
* Facebook, Inc. Class A<br />
* Alphabet Inc. Class A<br />
* Alphabet Inc. Class C<br />

and many more (actually 500 of them)<br />

#### URL FOR PARSING

if we will take the url: https://www.etf.com/SPY#overview <br />
we will be able to see it has a lot of data inside:<br />
#### characteristics 

**Name**: SPYSPDR S&P 500 ETF Trust<br />
**Grade:** A<br />
**Score:** 94<br />
**ETF.com segment:** (Equity(U.S.(Large Cap)))<br />
**Popular SPY Comparisons:** SPY vs QQQ, SPY vs DIA, SPY vs IVV, SPY vs VTI, SPY vs VOO<br />
**Related ETF Channels:** U.S., Equity, Large Cap, Broad-based, North America, Vanilla, S&P 500<br />

#### SPY Summary Data
|NAME                       |       DATA                    |
|---------------------------|-------------------------------|
|   IssuerState             |       Street Global Advisors  |
|   Brand                   |       SPDR                    |
|   Inception Date          |       01/22/93                |
|   Legal Structure         |       Unit Investment Trust   |
|   Expense Ratio           |       0.09%                   |
|   Assets Under Management |       $329.13B                |
|   Average Daily $ Volume  |       $20.67B                 |
|   Average Spread          |       (%)0.00%                |
|   Competing ETFs          |       QQQ, DIA                |

#### SPY Portfolio Data
|NAME                       |DATA       |
|---------------------------|-----------|
|Weighted Average Market Cap| $472.77B  |
|Price / Earnings Ratio     | 37.91     |
|Price / Book Ratio         | 4.13      |
|Distribution Yield         | 1.47%     |
|Next Ex-Dividend Date      | N/A       |
|Number of Holdings         |498        |

#### SPY Index Data 
|NAME                       |DATA       |
|---------------------------|-----------|
|Index Tracked |S&P 500|
|Index Weighting Methodology |Market Cap|
|Index Selection Methodology |Market Cap|
|Segment Benchmark |MSCI USA Large Cap Index|

#### SPY vs Peers Comparison
|NAME                       |DATA1       |DATA1       |
|---------------------------|------------|------------|
| |SPY| QQQ
Brand|SPDR|Invesco|
Expense Ratio|0.09%|0.20%|
YTD Return|3.29%|5.26%|
AUM|$334.36B|$159.96B|
Number of Holdings|506|103|
Avg. Spread ($)|$0.01$|0.02$|
Average Daily $ Volume|$20.67B|$8.38B|
#### or data as charts
#### SPY Top 10 Countries
|NAME  |DATA1       |
|---------------|------------|
|United States|100.00%|
|Canada|0.00%|

#### SPY Top 10 Sectors
|NAME  |DATA1       |
|---------------|------------|
|Technology      |33.46%|
|Consumer Cyclicals|15.90%|
|Healthcare|13.30%|
|Financials|12.60%|
|Industrials|9.19%|
|Consumer Non-Cyclicals|6.27%|
|Utilities|2.73%|
|Basic Materials|2.52%|
|Energy|2.30%|
|Telecommunications Services|1.73%|

#### and also open close chart for last year<br />

# SETUP<br />

see erd in files:<br />
erd.pdf

check the video in :<br />

https://www.youtube.com/watch?v=S_AZxyuh7N4

for setup we will need to download the "chromedriver" for our chrome browser.<br />
there is one in the directory but best to update chrome and web driver from this sites below: <br />
if you need to download chrome download here : <br />

https://www.google.com/chrome

to download the correct chrome driver find the version in chrome.<br />
download the corresponding driver from here: 

https://chromedriver.chromium.org/downloads

after downloading paste in the same folder.<br />
you can follow this link for explanation from you tube explaning how to download the chromedriver:<br />

https://www.youtube.com/watch?v=dz59GsdvUF8

after you downloaded it paste it in root folder.<br />
you don't have to use since all relevant already downloaded as html file to the system.<br />


# Requirements<br />

requests>=2.24.0<br />
selenium>=3.141.0<br />
beautifulsoup4>=4.9.1<br />
pandas>=1.0.5<br />

in order to install them paste and run :br />

"pip install -r requirements.txt"

# How it works <br />

Simply run the "main_script.py" script with the relevant sub-fix .<br />
When running the program we can either download all the etf pages from the web <br />
or read from hard drive.<br />

We build a method of random wait between operations in order not to be detected<br />
as a robot by the website, that does not allow scraping...<br />

For the same reason, we pre downloaded the pages once and keep them <br />
rather than downloading the pages each time...<br />

#### OPTIONS AND EXPLANATION<br />

you can show a list all of the downloaded html files simply by running main_script.py with: <br />
  -s, --show        show the etf.com after downloading list<br />
simply write in the command line : <br />
"python.exe  main_script.py  -s"<br />

verbose log and on screen : <br />
you can toggle between Verbose log on screen and to log file by selecting :<br />


  -vs, --verbose_s  increase output verbosity to screen<br />
simply write in the command line : <br />
"python.exe main_script.py  -s -vs"<br />


  -vl, --verbose_l  increase output verbosity to log file "log.log":<br />
simply write in the command line : <br />
"python.exe main_script.py  -s -vl"<br />

##### in order to delete all data and download new data from site:

simply write in the command line : <br />
"python.exe  main_script.py  -l"<br />
in order to refresh the 100 top etf list
  
simply write in the command line : <br />
"python.exe  main_script.py  -d"<br />
in order to refresh all data after deleting the list delete all data - this may take some time

simply write in the command line : <br />
"python.exe  main_script.py  -sj"<br />
in order to dump all data to json file - this file will be the data that will produce the DB.<br />

after downloading all the new data from scratch and making a data.json.file you will need to make a new DB: <br />
for that you will need to do some things: <br />

first: <br />
go to the site : <br />
https://finnhub.io<br />

register and get a token. <br />
place the token inside "cred_api.py" under : TOKEN = r'INSERT TOKEN HERE'<br />

now run this to delete the old DB (or just delete : \\Data\etf_id.db)<br />
  -ddb, --del_DB    Deletes the data base Data/etf_id.db<br />
simply write in the command line : <br />
"python.exe  main_script.py  -ddb"<br />

then use -sql to create a db file for SQLite3<br />
simply write in the command line : <br />
"python.exe  main_script.py  -sql"<br />

it will create a new DB - now you can query db file with SQLite3.<br />

on the other hand if you want to use MYSQL<br />
use the conf.py to enter host, user, pass for the server and run:<br />

MY_SQL_HOST = 'host ip'<br />
MY_SQL_USER = 'my sql user name'<br />
MY_SQL_PASS = 'my sql password'<br />

simply write in the command line : <br />
"python.exe  main_script.py  -mysql"<br />

it will create a new mysql DB - now you can query db file with MYSQL.<br />

there is en erd.pdf file in the folder in order to grasp the DB.

#Contributing<br />

Feel Free<br />
