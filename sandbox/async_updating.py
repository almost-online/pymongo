import asyncio
from sandbox.dbClient import client
from sandbox.dbClient import get_client

# Get or create DB schema
db = client.lorem_ipsum

# Number of records to insert
STOP = 5000

# init x for latest use
x = 0
random_record = list(db.reviews.aggregate([{"$sample": {"size": 1}}]))
record_id = random_record[0]["_id"]


async def update_rating(x, id):
    # Insert lorem_ipsum object directly into MongoDB via update_one
    result = db.reviews.update_one({"_id": id},
                                   {
                                       "$inc": {"rating": 1},
                                       "$currentDate": {"operation.date." + str(x): {"$type": "timestamp"}}
                                   })
    # Print to the console the ObjectID of the new document
    print('Updated thread {0} of 5000 as +{1} (API call went through: {2})'.format(x, result.modified_count,
                                                                                   result.acknowledged))


loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait([update_rating(x, record_id) for x in range(0, STOP)]))

last_record = db.reviews.find_one({"_id": record_id})

# Tell us that you are done
print('finished updating {0} times'.format(int(last_record["rating"]) - int(random_record[0]["rating"])))

print('Final record', last_record)
