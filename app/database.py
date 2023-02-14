from pymongo import mongo_client
import pymongo
from app.config import settings

client = mongo_client.MongoClient(settings.DATABASE_URL)
print('Connected to MongoDB...')

db = client[settings.MONGO_INITDB_DATABASE]
Employee = db.employees
Employee.create_index([("email", pymongo.ASCENDING)], unique=True)
