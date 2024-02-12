import csv
from tmdbv3api import TMDb, TV, Discover

tmdb = TMDb()
tv = TV()
tmdb.api_key = 0#add your api key here from tmdb  

# Create an instance of the Discover class
discover = Discover()

def save_allpages_tocsv():
    with open('tvshows_df_last.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["id", "title","poster_path" ,"overview", "actors", "directors", "writers", "genres", "tag"])
        for pagenum in range(1, 500):
            print('done page')
            tvshows = movies_on_page(pagenum)
            writer.writerows(tvshows)

def movies_on_page(page_num):
    tvshows_data = discover.discover_tv_shows({'page': page_num})["results"]
    totalL = []

    for tvshow_data in tvshows_data:
        L = []
        tvshow_id = tvshow_data["id"]
        tvshows_overview = tvshow_data['overview']
        details = tv.details(tvshow_id)

        actors, directors, writers = get_cast(details)
        genres = get_genres(details)
        if(tvshow_id):
            L.extend([tvshow_id, tvshow_data["name"],tvshow_data["poster_path"], tvshows_overview.split(), actors, directors, writers, genres, actors + directors + writers + genres])
        totalL.append(L)

    return totalL

def get_genres(tvshows_details):
    genres = tvshows_details.genres

    return [genre.name.replace(" ", "") for genre in genres]

def get_cast(tvshows_details):
    cast = tvshows_details['credits']["cast"]
    crews = tvshows_details['credits']["crew"]

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
