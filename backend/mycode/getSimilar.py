from mycode.fetch_dataframe_from_db import getshowsdataframe, getmoviesdataframe
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def getSimilarMovies(movie_title, n):
    #fetch movies dataframe
    movies = getmoviesdataframe()
    
    # calculating movie similarities
    cv_movie = CountVectorizer(max_features=movies.shape[0])
    movies_vector = cv_movie.fit_transform(movies['tag']).toarray()
    movies_similarity = cosine_similarity(movies_vector)
    
    title_index =  movies[movies['title'] == movie_title].index[0]
    movies_sorted = sorted(list(enumerate(movies_similarity[title_index])), reverse=True, key = lambda x: x[1])
    L = []
    for i in movies_sorted[1:n]:
        L.append({'title': movies.iloc[i[0]].title,'id': int(movies.iloc[i[0]].id), "poster_path": "https://image.tmdb.org/t/p/w600_and_h900_bestv2"+movies.iloc[i[0]]["poster_path"]})
    return L

def getSimilarShows(show_title, n):
    #fetch shows dataframe
    shows = getshowsdataframe()
    
    # calculating shows similarities
    cv_show = CountVectorizer(max_features=shows.shape[0],stop_words='english')
    shows_vector = cv_show.fit_transform(shows['tag']).toarray()
    shows_similarity = cosine_similarity(shows_vector)
    
    title_index =  shows[shows['title'] == show_title].index[0]
    shows_sorted = sorted(list(enumerate(shows_similarity[title_index])), reverse=True, key = lambda x: x[1])
    L = []
    for i in shows_sorted[1:n]:
        L.append({'title': shows.iloc[i[0]].title,'id': int(shows.iloc[i[0]].id), 'score': int(i[1]), "poster_path": "https://image.tmdb.org/t/p/w600_and_h900_bestv2"+shows.iloc[i[0]]["poster_path"]})
    return L

""" starttime = time.time()
getSimilarShows("Sherlock", 10)
endtime = time.time()

print("time taken "+ str(endtime - starttime)+" seconds") """