from bottle import default_app, route, post, request, template, redirect
import csv
import os
import random

#Path to CSV inside the 'views' folder
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(BASE_DIR, "views", "movielist.csv")

#Function to load movies from CSV
def load_movies():
    movies = []
    try:
        with open(CSV_PATH, newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                movies.append(row)
        
    except FileNotFoundError:
        print(f"CSV file not found at {CSV_PATH}")
    return movies

#Root redirects to /movie
@route('/')
def home():
    return redirect('/movie')

#Show a random movie on /movie
@route('/movie')
def movie():
    movies = load_movies()
    if not movies:
        return "No movies found in CSV! Make sure 'movielist.csv' is in the 'views' folder."
    movie_picked = random.choice(movies)
    return template("indexMovie.html", movie=movie_picked)

#Process form submission
@post('/moviecomp')
def results():
    user_score = request.forms.get("value")
    movieTitle = request.forms.get("movieTitle")
    rotten = request.forms.get("movieRottenScore")
    myscore = request.forms.get("movieMyScore")
    audience = request.forms.get("movieAudience")

    return template("moviecomp.html",
                    user_score=user_score,
                    movieTitle=movieTitle,
                    rotten=rotten,
                    myscore=myscore,
                    audience=audience)

#Web server gateway
application = default_app()

#Start local server if running directly
if __name__ == "__main__":
    from bottle import run
    run(app=application, host='localhost', port=8080, debug=True, reloader=True)
