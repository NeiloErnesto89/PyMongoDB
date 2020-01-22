import pymongo
import os

MONGODB_URI = os.getenv("MONGO_URI")
DBS_NAME = "myTestDB" #caps lock needed !
COLLECTION_NAME = "myFirstMDB"

def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is connected!")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e
        
conn = mongo_connect(MONGODB_URI)

coll = conn[DBS_NAME][COLLECTION_NAME]

"""
new_docs = [{'first': 'terry', 'last': 'pratt', 'dob': '25/02/1948', 'gender': 'm', 'hair_colour': 'bald', 'occupation': 'writer', 'nationality': 'english'}, {'first': 'george', 'last': 'martin', 'dob': '17/09/1950', 'gender': 'm', 'hair_colour': 'white', 'occupation': 'writer', 'nationality': 'american'}]


coll.insert_many(new_docs)
"""

coll.update_many({'nationality': 'american'}, {'$set': {'hair_colour': 'maroon'}}) 

documents = coll.find({'nationality': 'american'})# keep to iterate and print everything to screen

for doc in documents:
    print(doc)