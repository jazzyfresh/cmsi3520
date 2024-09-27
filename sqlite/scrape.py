## scrape.py:
##   Download the URL
##   Parse the table entries into arrays
##   Create a DataFrame
##   Load into SQLite

import mechanicalsoup
import pandas as pd
import sqlite3



# Download the URL #
url = "https://en.wikipedia.org/wiki/List_of_highest-grossing_films"
browser = mechanicalsoup.StatefulBrowser()
browser.open(url)


# Parse the table entries into arrays #
# table > td
# table > tbody > th

# browser.page.find() # gives first instance of an html element
# browser.page.find_all() # gives all instances
# browser.page.find_all("table", attrs={"class":"wikitable"})

table = browser.page.find("table")
#tbody = table.find("tbody")
# th = tbody.find_all("th")
th = table.find_all("th")
td = table.find_all("td")
td = [value.text.replace("\n", "") for value in td]
titles = [value.text.replace("\n", "") for value in th]
titles = titles[6:]


# Create a DataFrame #
column_names = ["rank", "peak", "world_wide_gross", "year", "ref"]

dictionary = {"title": titles}

# column[0:][::11]
# column[1:][::11]
# column[2:][::11]


for idx, key in enumerate(column_names):
    dictionary[key] = td[idx:][::5]

df = pd.DataFrame(data = dictionary)
print(df.head())
print(df.tail())



# Load into SQLite #
connection = sqlite3.connect("movies.db")
cursor = connection.cursor()
cursor.execute("create table movies (title," + ",".join(column_names) + ")")
for i in range(len(df)):
    cursor.execute("insert into movies values (?,?,?,?,?,?)", df.iloc[i])

connection.commit()

connection.close()

