# Import necessary libraries
import pandas as pd
import sqlite3

# Read CSV files into dataframes
df1 = pd.read_csv("file1.csv")
df2 = pd.read_csv("file2.csv")
df3 = pd.read_csv("file3.csv")
df4 = pd.read_csv("file4.csv")
df5 = pd.read_csv("file5.csv")
df6 = pd.read_csv("file6.csv")


# Write dataframes to SQLite database
with sqlite3.connect("netflix.db") as conn:
    df1.to_sql("rawTiles", conn, if_exists="replace")
    df2.to_sql("rawCredits", conn, if_exists="replace")
    df3.to_sql("bestShowYear", conn, if_exists="replace")
    df4.to_sql("bestMovieYear", conn, if_exists="replace")
    df5.to_sql("bestMovies", conn, if_exists="replace")
    df6.to_sql("bestShows", conn, if_exists="replace")


# Create combined table in database
query = """
    CREATE TABLE combined_table AS
        SELECT *
        FROM rawTiles
"""

with sqlite3.connect("netflix.db") as conn:
    conn.execute(query)
