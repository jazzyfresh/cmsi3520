import pandas as pd
import sqlite3

# read csv file into memory using pandas
df = pd.read_csv("amazon_laptop_prices_v01.csv")
print(df.head())
print(df.tail())

# connect to sqlite database
# this connects to an exiting file or creates a new file
connection = sqlite3.connect("laptops.db")
cursor = connection.cursor()

# load data into the table
df.to_sql("laptops", connection)

connection.close()

