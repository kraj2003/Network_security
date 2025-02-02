import sys
from pymongo.mongo_client import MongoClient
from Network_security.exception.exception import NetworkSecurityException
# from collections.abc import MutableMapping
import certifi
uri = "mongodb+srv://khushirajpurohit617:<@password>@cluster0.py49u.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client =MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    raise NetworkSecurityException(e,sys)
