# DATA MINING - ITC PROJECT
Data mining project ITC - on retrieving raw data and parsing data from URL<br />
Our sub topic is - stock exchange site "ETF.com".

# OUT LINE
Our project is based on the ETF site that have a lot of raw data on the the stocks ETF.<br />
there are many ETF's they are a group af stocks that have many characteristics. <br />

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


#### And a lot more data<br />

# SETUP<br />

for setup we will need to download the "chromedriver" for our chrome browser.<br />

if you need to download chrome download here : https://www.google.com/chrome<br />
to download the correct chrome driver find the version in chrome.<br />
download the corresponding driver from here: https://chromedriver.chromium.org/downloads<br />

after downloading paste in the same folder.<br />

# Requirements<br />

requests>=2.24.0<br />
selenium>=3.141.0<br />
beautifulsoup4>=4.9.1<br />

# How it works <br />

when running the program we can either download all the etf from the web <br />
or read from hard drive.<br />

## if we want to load from hard drive:<br />
set value "download_new_list = False" <br />
in function "open_url_or_file".<br />
program will run from files in ETF_raw_data<br />

## if we want to load from hard and refresh some etf data:<br />
delete etf data from ETF_raw_data - program will download it fresh.<br />
set value "download_new_list = False"<br /> 
in function "open_url_or_file".<br />
program will download them.<br />

## if we want to fresh list top-100 etf and new etf data:<br />
delete etf data from ETF_raw_data - program will download it fresh.<br />
set value "download_new_list = True" <br />
in function "open_url_or_file".<br />

run program once to download all data.<br />

# output<br />

output is in json file "data.json"<br />

#Contributing

Feel Free
