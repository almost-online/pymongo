from pprint import pprint
from sandbox.dbClient import client

db = client.admin
serverStatusResult = db.command("serverStatus")
pprint(serverStatusResult)
