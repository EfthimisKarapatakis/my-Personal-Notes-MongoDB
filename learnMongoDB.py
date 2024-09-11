import pymongo

# Create a database:

myClient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myClient["mydatabase"]

# Check if database exists:
"""
# Return a list of your system's databases:
print(myClient.list_database_names())
# Or you can check a specific database by name:
dblist = myClient.list_database_names()
if "mydatabase" in dblist:
    print("The database exists.")
"""

# Create a collection(table):

mycol = mydb["customers"]

# Check if a database exists:
"""
# Return a list of all collections in your database:
print(mydb.list_collection_names())
# Or you can check a specific collection by name:
collist = mydb.list_collection_names()
if "customers" in collist:
    print("The collection exists.")
"""

# Insert into collection:
"""
mydict = { "name": "John", "address": "Highway 37" }
x = mycol.insert_one(mydict)
"""

# Return the _id Field:
"""
mydict = { "name": "Peter", "address": "Lowstreet 27" }
x = mycol.insert_one(mydict)
print(x.inserted_id)
"""

# Insert Multiple Documents:
"""
mylist = [
    { "name": "Amy", "address": "Apple st 652"},
    { "name": "Hannah", "address": "Mountain 21"},
    { "name": "Michael", "address": "Valley 345"},
    { "name": "Sandy", "address": "Ocean blvd 2"},
    { "name": "Betty", "address": "Green Grass 1"},
    { "name": "Richard", "address": "Sky st 331"},
    { "name": "Susan", "address": "One way 98"},
    { "name": "Vicky", "address": "Yellow Garden 2"},
    { "name": "Ben", "address": "Park Lane 38"},
    { "name": "William", "address": "Central st 954"},
    { "name": "Chuck", "address": "Main Road 989"},
    { "name": "Viola", "address": "Sideway 1633"}
    ]
x = mycol.insert_many(mylist)
#print list of the _id values of the inserted documents:
print(x.inserted_ids)
"""

# Insert Multiple Documents, with Specified IDs:
"""
mylist = [
    { "_id": 1, "name": "John", "address": "Highway 37"},
    { "_id": 2, "name": "Peter", "address": "Lowstreet 27"},
    { "_id": 3, "name": "Amy", "address": "Apple st 652"},
    { "_id": 4, "name": "Hannah", "address": "Mountain 21"},
    { "_id": 5, "name": "Michael", "address": "Valley 345"},
    { "_id": 6, "name": "Sandy", "address": "Ocean blvd 2"},
    { "_id": 7, "name": "Betty", "address": "Green Grass 1"},
    { "_id": 8, "name": "Richard", "address": "Sky st 331"},
    { "_id": 9, "name": "Susan", "address": "One way 98"},
    { "_id": 10, "name": "Vicky", "address": "Yellow Garden 2"},
    { "_id": 11, "name": "Ben", "address": "Park Lane 38"},
    { "_id": 12, "name": "William", "address": "Central st 954"},
    { "_id": 13, "name": "Chuck", "address": "Main Road 989"},
    { "_id": 14, "name": "Viola", "address": "Sideway 1633"}
]
x = mycol.insert_many(mylist)
#print list of the _id values of the inserted documents:
print(x.inserted_ids)
"""

# Select data from a collection:
"""
# For one:
x = mycol.find_one()
print(x)
# For all:
for x in mycol.find():
    print(x)
"""

# Return Only Some Fields:
"""
for x in mycol.find({},{ "_id": 0, "name": 1, "address": 1 }):  # only name and address
    print(x)
# Or :
for x in mycol.find({},{ "address": 0 }):   #everything except address
    print(x)
# 0 False 1 True
"""

# Filter the results:
"""
myquery = { "address": "Park Lane 38" }
mydoc = mycol.find(myquery)
for x in mydoc:
    print(x)
"""

# Advanced query:
"""
myquery = { "address": { "$gt": "S" } } # The "address" field starts with the letter "S" or higher.
mydoc = mycol.find(myquery)
for x in mydoc:
    print(x)
"""

# Filter With Regular Expressions:
"""
myquery = { "address": { "$regex": "^S" } } # The "address" field starts with the letter "S".
mydoc = mycol.find(myquery)
for x in mydoc:
    print(x)
"""

# Sort the Result:
"""
mydoc = mycol.find().sort("name")
# sort("name", 1) #ascending
# sort("name", -1) #descending
for x in mydoc:
    print(x)
"""

# Delete Document:
"""
myquery = { "address": "Mountain 21" }
mycol.delete_one(myquery)
"""

# Delete multiple documents:
"""
myquery = { "address": {"$regex": "^S"} }   # The "address" field starts with the letter "S".
x = mycol.delete_many(myquery)
print(x.deleted_count, " documents deleted.")
"""

# Delete all the documents:
"""
x = mycol.delete_many({})
print(x.deleted_count, " documents deleted.")
"""

# Delete collections:
"""
mycol.drop()
"""

# Update Collection:
"""
myquery = { "address": "Valley 345" }
newvalues = { "$set": { "address": "Canyon 123" } }
mycol.update_one(myquery, newvalues)
#print "customers" after the update:
for x in mycol.find():
    print(x)
"""

# Update many: 
"""
myquery = { "address": { "$regex": "^S" } }
newvalues = { "$set": { "name": "Minnie" } }
x = mycol.update_many(myquery, newvalues)
print(x.modified_count, "documents updated.")
"""

# Limit the Result:
"""
myresult = mycol.find().limit(5)
#print the result:
for x in myresult:
    print(x)
"""
