from pymongo import MongoClient
import pandas as pd

client = MongoClient('mongodb://localhost:27017/')

db = client['company_db']

employees = db['employees']

print("MongoDB connection established successfully.")

sample_data = [
    {"emp_id":101, "name": "Mukesh","department": "QA"},
    {"emp_id":102, "name": "Ravi","department": "DevOps"},
    {"emp_id":103, "name": "Suresh","department": "Development"},
    {"emp_id":104, "name": "Ramesh","department": "Marketing"}
]

employees.insert_many(sample_data)
print("database and collection created successfully, documents inserted.")

#read data

data = list(employees.find())
print("mongodb records:")
for d in data:
    print(d)

#convert to dataframe
df = pd.DataFrame(data)
print("dataframe created successfully:")
print(df)