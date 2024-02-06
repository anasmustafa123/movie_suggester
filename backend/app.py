from flask import Flask, render_template, jsonify, request
from mycode.fetch_suggestions import getMovieSuggestion, getShowsSuggestions
from mycode.getSimilar import getSimilarMovies, getSimilarShows
from flask_cors import CORS

app = Flask(__name__)

# Enable CORS for requests from 
CORS(app, resources={r"/*": {"origins": "https://movie-suggester-dun.vercel.app"}})

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/api/autocomplete_movies', methods=['POST'])
def get_movies_suggestions():
    try:
        rdata = request.get_json()
        movie_title = rdata["title"]
        print("Received query:", movie_title)
        result = getMovieSuggestion(movie_title)
        print("Generated suggestions:", result)
        return jsonify(result)
    except Exception as e:
        print("Error:", e)
        return jsonify([])


@app.route('/api/autocomplete_shows', methods=['POST'])
def get_shows_suggestions():
    rdata = request.get_json()
    show_title = rdata["title"]
    result  = getShowsSuggestions(show_title)
    return jsonify(result)


@app.route('/api/similar_movies', methods=['POST'])
def get_similar_movies():
    try:
        rdata = request.get_json()
        movie_title = rdata["title"]
        n = rdata['n']
        print("Received query:", movie_title)
        result = getSimilarMovies(movie_title, n)
        print("Generated suggestions:", result)
        return jsonify(result)
    except Exception as e:
        print("Error:", e)
        return jsonify([])


@app.route('/api/similar_shows', methods=['POST'])
def get_similar_shows():
    try:
        rdata = request.get_json()
        show_title = rdata["title"]
        n = rdata['n']
        result  = getSimilarShows(show_title, n)
        return jsonify(result)
    except Exception as e:
        print('Error: ', e)
        return jsonify([])

