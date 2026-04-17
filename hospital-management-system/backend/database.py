from pymongo import MongoClient

client = MongoClient("mongodb+srv://naveenkumar:XJ99AGOx8SV14YtZ@cluster0.pligakl.mongodb.net/hospital?retryWrites=true&w=majority")
db = client["hospital"]
