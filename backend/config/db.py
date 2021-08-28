from pymongo import MongoClient
import os

config = {
    "host": os.environ["MONGO_HOST"],
    "port": int(os.getenv("MONGO_PORT", default=27017))
}

client = MongoClient(**config)
conn = client.botgame
