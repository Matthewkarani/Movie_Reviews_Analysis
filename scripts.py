# Include code to load the different data formats into their respective data frames.
# Create different functions to load different file types.
# Avoid excessive use of loops as it may lead to unneccessary errors.
import sqlite3

import pandas as pd

#load CSV data files
def load_data_from_csv(csv_file_path):
    return pd.read_csv(csv_file_path)

#load TSV Files
def load_data_from_tsv(tsv_file_path):
    return pd.read_csv(tsv_file_path, delimiter='\t')

#Load SQL data files
def create_db_connection(sql_file_path):
    conn = sqlite3.connect(sql_file_path)
    return conn
def load_data_from_sql(conn,querry):
    return pd.read_sql(conn,querry)

