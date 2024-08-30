import mechanicalsoup
import pandas as pd
import sqlite3

# scrape.py:
# Download the URL
# Parse the table entries into arrays
# Create a DataFrame
# Load into SQLite


# Download the URL #
url = "https://en.wikipedia.org/wiki/Comparison_of_Linux_distributions"
browser = mechanicalsoup.StatefulBrowser()
browser.open(url)


# Parse the table entries into arrays #
th = browser.page.find_all("th", attrs={"class": "table-rh"})
distribution = [value.text.replace("\n", "") for value in th]
# print(distribution.index("Zorin OS"))
distribution = distribution[:98]
# print(distribution)

td = browser.page.find_all("td")
columns = [value.text.replace("\n", "") for value in td]
# print(columns)
# print(columns.index("AlmaLinux Foundation"))
# print(columns.index("Binary blobs"))

columns = columns[6:1084]
print(columns)


# Create a DataFrame #
column_names = ["Founder",
                "Maintainer",
                "Initial_Release_Year",
                "Current_Stable_Version", 
                "Security_Updates", 
                "Release_Date", 
                "System_Distribution_Commitment", 
                "Forked_From", 
                "Target_Audience", 
                "Cost", 
                "Status"]

# column[0:][::11]
# column[1:][::11]
# column[2:][::11]

dictionary = {"Distribution": distribution}

for idx, key in enumerate(column_names):
    dictionary[key] = columns[idx:][::11]

df = pd.DataFrame(data = dictionary)
print(df.head())
print(df.tail())


# Load into SQLite #
connection = sqlite3.connect("distro.db")
cursor = connection.cursor()
cursor.execute("create table linux (Distribution, " + ",".join(column_names) + ")")
for i in range(len(df)):
    cursor.execute("insert into linux values (?,?,?,?,?,?,?,?,?,?,?,?)", df.iloc[i])

connection.commit()

connection.close()

