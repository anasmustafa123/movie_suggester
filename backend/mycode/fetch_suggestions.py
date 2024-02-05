from pymongo import MongoClient
import re

def getMovieSuggestion(search_string):
    # MongoDB connection details
    uri = "mongodb+srv://anasmuostafa:anasanas123A@cluster0.zex5zoj.mongodb.net/?retryWrites=true&w=majority"

    # Connect to MongoDB
    client = MongoClient(uri)

    # Specify the database and collection names
    database_name = "predections"
    collection_name = "movies"

    # Access the specified database and collection
    db = client[database_name]
    collection = db[collection_name]


    # Create a regex pattern for a case-insensitive search
    regex_pattern = re.compile(f".*{re.escape(search_string)}.*", re.IGNORECASE)

    # Use the regex pattern to find movies with titles similar to the search string
    query = {"title": {"$regex": regex_pattern}}
    matching_movies = collection.find(query)
    
    L = []
    count = 0
    # Print the matching movies
    for movie in matching_movies:
        if(count < 7):
            L.append(movie['title'])
            count += 1

    # Close the MongoDB connection
    client.close()
    
    return L

def getShowsSuggestions(search_string):
    # MongoDB connection details
    uri = "mongodb+srv://anasmuostafa:anasanas123A@cluster0.zex5zoj.mongodb.net/?retryWrites=true&w=majority"

    # Connect to MongoDB
    client = MongoClient(uri)

    # Specify the database and collection names
    database_name = "predections"
    collection_name = "tvshows"

    # Access the specified database and collection
    db = client[database_name]
    collection = db[collection_name]


    # Create a regex pattern for a case-insensitive search
    regex_pattern = re.compile(f".*{re.escape(search_string)}.*", re.IGNORECASE)

    # Use the regex pattern to find movies with titles similar to the search string
    query = {"title": {"$regex": regex_pattern}}
    matching_shows = collection.find(query)

    L = []
    count = 0
    # Print the matching movies
    for show in matching_shows:
        if(count < 7):
            L.append(show['title'])
            count += 1

    # Close the MongoDB connection
    client.close()
    
    return L

