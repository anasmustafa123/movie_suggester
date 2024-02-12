import csv
from tmdbv3api import TMDb, Movie, Discover

tmdb = TMDb()
tmdb.api_key = 0#add your api key here from tmdb  
movie = Movie()

# Create an instance of the Discover class
discover = Discover()

def save_allpages_tocsv():
    with open('movies_df_last.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["id", "title","poster_path", "actors", "directors", "writers", "genres", "keywords", "tag"])
        for pagenum in range(1, 500):
            print('done page')
            movies = movies_on_page(pagenum)
            writer.writerows(movies)

def movies_on_page(page_num):
    movies_data = discover.discover_movies({'page': page_num})["results"]
    totalL = []

    for movie_data in movies_data:
        L = []
        movie_id = movie_data["id"]
        details = movie.details(movie_id)

        actors, directors, writers = get_cast(details)
        genres = get_genres(details)
        keywords = get_keywords(details)

        L.extend([movie_id, movie_data["title"],movie_data["poster_path"] , actors, directors, writers, genres, keywords, actors + directors + writers + genres + keywords])
        totalL.append(L)

    return totalL

def get_genres(movie_details):
    genres = movie_details.genres

    return [genre.name.replace(" ", "") for genre in genres]

def get_keywords(movie_details):
    keywords = movie_details.keywords["keywords"]

    return [keyword.name.replace(" ", "") for keyword in keywords]

def get_cast(movie_details):
    cast = movie_details.casts.cast
    crews = movie_details.casts.crew

    A, D, W = [], [], []
    count = 0

    for actor in cast:
        if count < 3 and actor.known_for_department == "Acting":
            A.append(actor.name.replace(" ", ""))
            count += 1
        else:
            break
    for crew in crews:    
        if crew.known_for_department == "Directing":
            D.append(crew.name.replace(" ", ""))
        elif crew.known_for_department == "Writing":
            W.append(crew.name.replace(" ", ""))
    
    return A, D, W


save_allpages_tocsv()
