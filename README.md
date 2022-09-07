# Download Data from Google Trends

1. This repository contains the code for downloading the data from Google Trends. The search term, country and time frame can be specified. Also, a directory name should be given to the code so it will save the csv file into the specified directory.

2. I spent around half an hour for searching how to get the data from Google Trends and an hour for creating the script.

3. I tried web scraping but found that there were easier ways to download it using the library pytrends.

4. The library pytrends provides easy and fast way of downloading the data of a search term from Google Trends. 

5. In order to use this code, open up your terminal. Clone the repository and install the necessary packages (pandas and pytrends). From the root of the repository, run the following command:

```
python src/trends.py --keyword="bitcoin" --geo="CA" --timefram="today 5-y" --dir="data"
```
