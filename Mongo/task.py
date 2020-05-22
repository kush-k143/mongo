import pandas as pd
from pymongo import MongoClient
client = MongoClient()
db = client.test
table = db.table
df = pd.read_csv("task.csv")
records_ = df.to_dict(orient = 'records')
result = db.table.insert_many(records_)
