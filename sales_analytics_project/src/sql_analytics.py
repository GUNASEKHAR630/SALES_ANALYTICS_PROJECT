import sqlite3
import pandas as pd
conn = sqlite3.connect("data/processed/sales.db")
print(pd.read_sql_query("SELECT product, SUM(sales) as total FROM sales GROUP BY product", conn))
