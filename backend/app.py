from flask import Flask, jsonify, request
from flask_executor import Executor
from mycode.getSimilar import getSimilarMovies, getSimilarShows

app = Flask(__name__)
executor = Executor(app)

@app.route('/api/similar_movies', methods=['POST'])
def get_similar_movies():
    try:
        rdata = request.get_json()
        movie_title = rdata["title"]
        n = rdata['n']

        # Execute the getSimilarMovies function asynchronously
        future = executor.submit(getSimilarMovies, movie_title, n)

        # Return an immediate response to the client
        return jsonify({'message': 'Task started successfully.'}), 202

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/similar_shows', methods=['POST'])
def get_similar_shows():
    try:
        rdata = request.get_json()
        show_title = rdata["title"]
        n = rdata['n']

        # Execute the getSimilarShows function asynchronously
        future = executor.submit(getSimilarShows, show_title, n)

        # Return an immediate response to the client
        return jsonify({'message': 'Task started successfully.'}), 202

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
