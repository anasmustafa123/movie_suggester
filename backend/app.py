from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__, static_folder="../frontend/dist/assets", template_folder='../frontend/dist')

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
