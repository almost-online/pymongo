from random import randint
from sandbox.dbClient import client

# Number of records to insert
STOP = 5001

# Get or create DB schema
db = client.lorem_ipsum

# init x for latest use
x = 0
random_record = list(db.reviews.aggregate([{"$sample": {"size": 1}}]))
record_id = random_record[0]["_id"]

for x in range(1, STOP):
    # Insert lorem_ipsum object directly into MongoDB via isnert_one
    result = db.reviews.update_one({"_id": record_id}, {"$inc": {"rating": 1}})
    # Print to the console the ObjectID of the new document
    print('Updated {0} of 5000 as {1}'.format(x, result.raw_result["n"]))

last_record = db.reviews.find_one({"_id": record_id})

# Tell us that you are done
print('finished updating {0} times'.format(int(last_record["rating"]) - int(random_record[0]["rating"])))
