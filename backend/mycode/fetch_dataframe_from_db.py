from pymongo import MongoClient
import pandas as pd 


def getmoviesdataframe():
    # MongoDB connection details
    uri = "mongodb+srv://anasmuostafa:anasanas123A@cluster0.zex5zoj.mongodb.net/?retryWrites=true&w=majority"
    database_name = "predections"

    # Connect to MongoDB
    client = MongoClient(uri)

    # Access the specified database
    db = client[database_name]

    # Specify the collection names
    movies_collection = db['movies']

    # Fetch data from 'movies' collection
    movies_df = pd.DataFrame(movies_collection.find())

    # Close the MongoDB connection
    client.close()

    return movies_df
    
def getshowsdataframe():
    # MongoDB connection details
    uri = "mongodb+srv://anasmuostafa:anasanas123A@cluster0.zex5zoj.mongodb.net/?retryWrites=true&w=majority"
    database_name = "predections"

    # Connect to MongoDB
    client = MongoClient(uri)

    # Access the specified database
    db = client[database_name]

    # Specify the collection names
    shows_collection = db['tvshows']
    # Fetch data from 'shows' collection
    shows_df = pd.DataFrame(shows_collection.find())
    # Close the MongoDB connection
    client.close()

    return shows_df

