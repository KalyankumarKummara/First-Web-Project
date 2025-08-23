import pymongo 
myclient= pymongo.MongoClient("mongodb://localhost:27017")
DB = myclient["Project"]
mycol= DB["BhajanaMandhircol"]