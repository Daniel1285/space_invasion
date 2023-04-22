
import pymongo
from pymongo import MongoClient

cluster = MongoClient("")

db = cluster["space"]
collection = db["user"]
