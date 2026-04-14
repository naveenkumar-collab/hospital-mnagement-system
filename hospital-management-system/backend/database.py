from pymongo import MongoClient

MONGO_DETAILS = "mongodb://localhost:27017"
client = MongoClient(MONGO_DETAILS)
db = client.hospital_db

def get_db():
    yield db
