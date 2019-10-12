import pymongo


def connect(name, connection=False):
    """
    Connects to Mongo Database
    Keyword Arguments:
    name -- name of database collection to open
    connection -- return pymongo connection - True or False
    """
    client = pymongo.MongoClient("mongodb://database:27017")
    db = client['CarpeNoctum']
    collection = db[name]

    if connection is True:

        return collection, client, pymongo

    return collection, client


def disconnect(client):
    """
    Disconnects from the Mongo Database
    Keyword Arguments:
    client -- Database connection to disconnect
    """
    client.close()
