from random import randint
from sandbox.dbClient import client
# Number of records to insert
STOP = 5001

# Get or create DB schema
db = client.lorem_ipsum

# Create sample data
names = ['Lorem', 'ipsum', 'dolor', 'sit', 'amet', 'consectetur', 'adipiscing', 'elit', 'Sed', 'rutrum']
text = [
    'Lorem ipsum dolor sit amet, consectetur adipiscing elit.',
    'Sed mollis leo eget turpis sollicitudin, ac luctus lacus dignissim.',
    'Nulla et felis sed nibh pulvinar sodales ut nec eros.',
    'Morbi viverra mi feugiat neque vulputate, in commodo nisi malesuada.'
]
cuisine = ['Pizza', 'Bar Food', 'Fast Food', 'Italian', 'Mexican', 'American', 'Sushi Bar', 'Vegetarian']

# get total documents count
documents = db.reviews.count_documents({})

for x in range(1, STOP):
    lorem_ipsum = {
        'name': names[randint(0, (len(names) - 1))] + ' ' + names[randint(0, (len(names) - 1))] + ': ' + text[
            randint(0, (len(text) - 1))],
        'text': text[randint(0, (len(text) - 1))],
        'rating': randint(1, 5),
        'cuisine': cuisine[randint(0, (len(cuisine) - 1))]
    }
    # Insert lorem_ipsum object directly into MongoDB via isnert_one
    result = db.reviews.insert_one(lorem_ipsum)
    # Print to the console the ObjectID of the new document
    print('Created {0} of 5000 as {1}'.format(x, result.inserted_id))

# Tell us that you are done
print('finished creating {0} business reviews'.format(db.reviews.count_documents({}) - documents))
