from pymongo import MongoClient


def get_client() -> MongoClient:
    mongo_url = 'mongodb://root:example@localhost:27017'

    client = MongoClient(mongo_url)
    return client


client = get_client()
