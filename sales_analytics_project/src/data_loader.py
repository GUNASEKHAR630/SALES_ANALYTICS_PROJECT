import pandas as pd
import sqlite3
def load_data(): 
    df = pd.read_csv("data/raw/sales_data.csv")
    df["date"] = pd.to_datetime(df["date"])
    return df
def create_db(df):
    conn = sqlite3.connect("data/processed/sales.db")
    df.to_sql("sales", conn, if_exists="replace", index=False)
    print("DB created")
if __name__ == "__main__":
    df = load_data()
    create_db(df)
