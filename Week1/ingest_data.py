import pandas as pd
from sqlalchemy import create_engine
from time import time as t
import argparse
import os

def main(params):
    user = params.user
    password = params.password
    host = params.host
    port = params.port
    db = params.db
    table_name = params.table_name
    url = params.url
    csv_name = 'output.csv.gz'  # Keep the original compressed filename

    # Download the compressed CSV file
    os.system(f"wget {url} -O {csv_name}")

    # Create a connection to the database
    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')

    # Read the compressed file in chunks
    df_iterator = pd.read_csv(csv_name, iterator=True, chunksize=100000, compression='gzip')

    df = next(df_iterator)

    # Convert datetime columns
    df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
    df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)

    # Write the first chunk to the database
    df.to_sql(name=table_name, con=engine, if_exists='append')

    # Process the remaining chunks
    while True:
        t_start = t()
        df = next(df_iterator)
        df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
        df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)
        df.to_sql(name=table_name, con=engine, if_exists='append')
        t_end = t()
        print("Inserting a chunk, took %.3f second" % (t_end - t_start))



if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Ingest CSV data to Postgres')

    parser.add_argument('--user', help='user name for postgres')
    parser.add_argument('--password', help='password for postgres')
    parser.add_argument('--host', help='host for postgres')
    parser.add_argument('--port', help='port for postgres')
    parser.add_argument('--db', help='database name for postgres')
    parser.add_argument('--table_name', help='table name where result will be written')
    parser.add_argument('--url', help='url csv file')


    args = parser.parse_args()
    main(args)
