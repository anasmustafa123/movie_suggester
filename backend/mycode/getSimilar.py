from mycode.fetch_dataframe_from_db import getshowsdataframe, getmoviesdataframe
from joblib import load

def getSimilarMovies(movie_title, n):
    #fetch movies dataframe
    movies = getmoviesdataframe()

    movies_similarity = load("./mycode/movie_sim.pkl")
    title_index =  movies[movies['title'] == movie_title].index[0]
    movies_sorted = sorted(list(enumerate(movies_similarity[title_index])), reverse=True, key = lambda x: x[1])
    L = []
    for i in movies_sorted[1:n]:
        movieposterUrl = movies.iloc[i[0]]["poster_path"]
        if not isinstance(movieposterUrl, str):
            movieposterUrl = "/mmQBX8qeracKZ2uz9zth3L3WKEc.jpg"
        L.append({'title': movies.iloc[i[0]].title,'id': int(movies.iloc[i[0]].id), "poster_path": "https://image.tmdb.org/t/p/w600_and_h900_bestv2"+movieposterUrl})
    return L

def getSimilarShows(show_title, n):
    #fetch shows dataframe
    shows = getshowsdataframe()
    
    shows_similarity = load("./mycode/show_sim.pkl")
    title_index =  shows[shows['title'] == show_title].index[0]
    shows_sorted = sorted(list(enumerate(shows_similarity[title_index])), reverse=True, key = lambda x: x[1])
    L = []
    for i in shows_sorted[1:n]:
        showPosterUrl = shows.iloc[i[0]]["poster_path"]
        if not isinstance(showPosterUrl, str):
            showPosterUrl = "/mmQBX8qeracKZ2uz9zth3L3WKEc.jpg"
        L.append({'title': shows.iloc[i[0]].title,'id': int(shows.iloc[i[0]].id), 'score': int(i[1]), "poster_path": "https://image.tmdb.org/t/p/w600_and_h900_bestv2"+showPosterUrl})
    return L