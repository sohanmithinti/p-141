from flask import Flask, jsonify, request
import csv

all_movies = [] 
with open("movies.csv", encoding= "utf8") as f:
    reader = csv.reader(f)
    data = list(reader) 
    all_movies = data[1:]

liked_movies =  []
not_liked_movies = []
did_not_watch = []

app = Flask(__name__)
if __name__ == "__main__":
    app.run() 

@app.route("/get-movie")
def get_movie():
    return jsonify({
        "data": all_movies[0],
        "status": "success"
    })    