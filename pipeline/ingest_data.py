import pandas as pd
from sqlalchemy import create_engine

prefix = "https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/"
url = f"{prefix}yellow_tripdata_2021-01.csv.gz"


dtype = {
    "VendorID": "Int64",
    "passenger_count": "Int64",
    "trip_distance": "float64",
    "RatecodeID": "Int64",
    "store_and_fwd_flag": "string",
    "PULocationID": "Int64",
    "DOLocationID": "Int64",
    "payment_type": "Int64",
    "fare_amount": "float64",
    "extra": "float64",
    "mta_tax": "float64",
    "tip_amount": "float64",
    "tolls_amount": "float64",
    "improvement_surcharge": "float64",
    "total_amount": "float64",
    "congestion_surcharge": "float64"
}

parse_dates = [
    "tpep_pickup_datetime",
    "tpep_dropoff_datetime"
]


df = pd.read_csv(
    url,
    dtype=dtype,
    parse_dates=parse_dates
)


SQLALCHEMY_DB_URL = "postgresql://root:root@localhost:5432/ny_taxi"

engine = create_engine(SQLALCHEMY_DB_URL)

df.head(0).to_sql(name="yellow_taxi_data", con=engine, if_exists="replace")


pd.io.sql.get_schema(df, name="yellow_taxi_data", con=engine)

df_iter = pd.read_csv(
    url,
    dtype=dtype,
    parse_dates=parse_dates,
    iterator=True,
    chunksize=10000
)

for df_chunk in df_iter:
    df_chunk.to_sql(name="yellow_taxi_data",con=engine,if_exists="append")
    print(len(df))

