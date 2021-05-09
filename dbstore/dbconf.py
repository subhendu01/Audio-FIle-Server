from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

database_name = client["PROJECT-TEST"]

file_store = database_name["DATA_STORE"]