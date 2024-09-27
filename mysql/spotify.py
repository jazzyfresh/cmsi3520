import pandas as pd
import mysql.connector
import pymysql

## Initialize database connection and cursor
## macOS does not need a password
## other installs use password="your_password"

# password = os.getenv("MYSQL_PASSWORD")
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    # password=password,
    database="spotify"
)

engine = create_engine("mysql+pymysql://root:" + password + "@localhost/spotify")


# cursor = connection.cursor()


## Load csv datasets into memory w/ Pandas
songs = pd.read_csv("spotify_songs.csv")
# playlists = pd.read_csv("spotify_playlists.csv")

## Load panda dataframes into mysql tables
songs.to_sql("songs ", connection, if_exists="replace", index=False) 
# df.to_sql("playlists", connection, if_exists="replace", index=False) 



# ## Execute a query
# ## You don't need the SQL semicolon ; 
# cursor.execute("SELECT * FROM songs LIMIT 10")
#
# ## Fetch all results
# results = cursor.fetchall()
#
# ## Print the results
# for x in results:
#   print(x)

connection.close()
