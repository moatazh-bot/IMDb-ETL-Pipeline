import pandas as pd
import requests
from bs4 import BeautifulSoup
import sqlite3
from datetime import datetime


URL = 'https://web.archive.org/web/20230531010141/https://www.imdb.com/chart/top/'


def extract(url):
    page = requests.get(url).text
    data = BeautifulSoup(page, 'html.parser')


    tables = data.find_all('tbody')
    rows = tables[0].find_all('tr')


    df = pd.DataFrame(columns=["Rank", "Movie_Name", "Year", "Rating"])
    count = 0

    for row in rows:
        if count >= 50:
            break

        cols = row.find_all('td')
        if len(cols) >= 4:

            rank = cols[0].text.strip()
            name = cols[1].text.strip()
            year = cols[2].text.strip()
            rating = cols[3].text.strip()

            data_dict = {
                "Rank": [rank],
                "Movie_Name": [name],
                "Year": [year],
                "Rating": [rating]
            }

            new_row = pd.DataFrame(data_dict)
            df = pd.concat([df, new_row], ignore_index=True)

            count += 1

    return df

def transform(df):
    df["year"] = df["Year"].str.replace('(','',regex=False)
    df["year"] = df["year"].str.replace(')','',regex=False)
    df["year"]=pd.to_numeric(df["year"])
    return df

def load_to_csv(df, path):
    df.to_csv(path, index=False)

def load_to_db(df, conn, table):
    df.to_sql(table, conn, if_exists='replace', index=False)

def log_progress(message):
    timestamp_format = '%Y-%b-%d-%H:%M:%S'
    now = datetime.now()
    timestamp = now.strftime(timestamp_format)
    with open("logs/etl_project_log.txt", "a") as f:
        f.write(f"{timestamp} : {message}\n")


log_progress("ETL Started")

log_progress("data extraction started")

df = extract(URL)

log_progress("data extraction finished, data transformation started")

df = transform(df)

log_progress("data transformation  finished, data loading started")

path= 'data/top_films.csv'

conn = sqlite3.connect('data/top_films.db')

load_to_csv(df, path)

log_progress("data loading finished")

load_to_db(df, conn, 'top_films',if_exists='replace')

log_progress("ETL Finished")

print(df)
