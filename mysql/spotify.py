import pandas as pd
import mysql.connector
from sqlalchemy import create_engine
from sqlalchemy import text

## Initialize database connection and cursor
## macOS does not need a password
## other installs use an environment variable:
# password = os.getenv("MYSQL_PASSWORD")

host = "localhost"
user = "root"
password = ""
database = "test" # make sure to create the database in mysql client first
connection_url = "mysql+mysqlconnector://root:@localhost:3306/test"
engine = create_engine(connection_url, echo=True)

with engine.connect() as connection:
    results = connection.execute(text("SHOW DATABASES"));
    for x in results.mappings():
        print(x)
    connection.close()


# Load csv datasets into memory w/ Pandas
songs = pd.read_csv("spotify_songs.csv")
print(songs.head())

# Load panda dataframes into mysql tables
with engine.connect() as connection:
    songs.to_sql("songs", connection) 

# # Testing large dataset
# # TODO: dataset too large, pandas ran out of memory
# playlists = pd.read_csv("spotify_playlists.csv")
# print(playlists.head())
# with engine.connect() as connection:
#     playlists.to_sql("playlists", connection)


# Execute a query
# You don't need the SQL semicolon ; 
with engine.connect() as connection:
    results = connection.execute("SELECT * FROM songs LIMIT 10")
    for x in results.mappings():
        print(x)
    connection.close()

