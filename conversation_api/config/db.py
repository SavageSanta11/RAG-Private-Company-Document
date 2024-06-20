# from pymongo import MongoClient

from pymongo.mongo_client import MongoClient
import certifi

conn = MongoClient()


MONGO_URI = None # replace with MongoDB URL
conn = MongoClient(MONGO_URI,tlsCAFile=certifi.where())

try:
    conn.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
db = conn.capstonedb
collection_name = db["capstonecollection"]
