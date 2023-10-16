import pandas as pd
import sqlite3

df = pd.read_csv("amazon_laptop_prices_v01.csv")
print(df.head())
print(df.tail())



connection = sqlite3.connect("laptops.db")
cursor = connection.cursor()
cursor.execute("DROP TABLE IF EXISTS laptops")
# create table

df.to_sql("laptops", connection)

connection.close()

# load data into the table

