from flask import Flask, render_template, jsonify, request
from mycode.fetch_suggestions import getMovieSuggestion, getShowsSuggestions

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route('/api/get_suggestions/movies', methods=['POST'])
def get_movies_suggestions():
    rdata = request.get_json()
    movie_title = rdata["title"]
    print(movie_title)
    result  = getMovieSuggestion(movie_title)
    print(result)
    return jsonify(result)

@app.route('/api/get_suggestions/shows', methods=['POST'])
def get_shows_suggestions():
    rdata = request.get_json()
    show_title = rdata["title"]
    result  = getMovieSuggestion(show_title)
    return jsonify(result)