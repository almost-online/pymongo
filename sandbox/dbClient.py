from pymongo import MongoClient


def get_client() -> MongoClient:
    mongo_url = 'mongodb://root:example@localhost:27017'

    return MongoClient(mongo_url)


client = get_client()
