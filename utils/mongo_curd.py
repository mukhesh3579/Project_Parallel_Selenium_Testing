from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')

print("MongoDB connection established successfully.")
db = client['company_db']

#create a collection
employees = db['employees']

# Insert a document into the collection
employee= {
    "name": "Ravi",
    "salary": 30000
}

employees.insert_one(employee)
print("database and collection created successfully, document inserted.")
print("read operation started**")

all_employees = employees.find()
for emp in all_employees:
    print(emp)

employees.update_one({"name": "Mukesh"}, {"$set": {"salary": 35000}})
print("update operation completed successfully.")

print("delete operation started**")
employees.delete_one({"name": "Mukesh"})
print("delete operation completed successfully.")

client.close()


