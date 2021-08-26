from pymongo import MongoClient
import os

config = {
    "host": os.environ["MONGO_HOST"],
    "port": int(os.environ["MONGO_PORT"])
}

client = MongoClient(**config)
conn = client.botgame
