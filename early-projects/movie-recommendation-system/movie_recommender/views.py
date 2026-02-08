from django.shortcuts import render
from movie_recommendations.popularity import popularity_recommendations
from movie_recommendations.content import content_based
from movie_recommendations.collaborative import collaborative_filtering
import pandas as pd
import random

def index(request):
    """
    Home page view: displays dynamic content and recommendation form.
    """

    # --- Top 5 popular movies ---
    try:
        top_movies = popularity_recommendations(top_n=5).to_dict(orient="records")
    except Exception as e:
        top_movies = []
        print(f"Error loading popular movies: {e}")

    # --- Random movie suggestion for content-based demo ---
    try:
        movies_df = pd.read_csv("data/movies.csv")
        movies_df['overview'] = movies_df['overview'].fillna('')
        random_movie = random.choice(movies_df['title'].tolist())
    except Exception as e:
        random_movie = ""
        print(f"Error loading movies for content-based suggestion: {e}")

    context = {
        "top_movies": top_movies,
        "random_movie": random_movie,
    }

    return render(request, "movie_recommender/index.html", context)


def results(request):
    """
    Processes recommendation requests and displays results.
    Accepts GET parameters:
      - rec_type: "popularity", "content", or "collaborative"
      - movie_title: for content-based
      - user_id: for collaborative
    """
    rec_type = request.GET.get("rec_type")
    context = {"rec_type": rec_type, "results": []}

    try:
        if rec_type == "popularity":
            context["results"] = popularity_recommendations(top_n=10).to_dict(orient="records")

        elif rec_type == "content":
            movie = request.GET.get("movie_title", "").strip()
            if movie:
                context["results"] = content_based(movie, top_n=5).to_dict(orient="records")
            else:
                context["error"] = "Please enter a movie title for content-based recommendations."

        elif rec_type == "collaborative":
            user_id_str = request.GET.get("user_id", "1").strip()
            if user_id_str.isdigit():
                user_id = int(user_id_str)
                context["results"] = collaborative_filtering(user_id, top_n=5).to_dict(orient="records")
            else:
                context["error"] = "Please enter a valid User ID for collaborative recommendations."
        else:
            context["error"] = "Invalid recommendation type selected."

    except Exception as e:
        context["error"] = str(e)

    return render(request, "movie_recommender/results.html", context)
