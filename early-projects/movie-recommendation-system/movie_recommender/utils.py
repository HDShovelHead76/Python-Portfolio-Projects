# movie_recommender/utils.py
import pandas as pd

def load_movies(movies_path="data/movies.csv"):
    return pd.read_csv(movies_path)

def load_ratings(ratings_path="data/ratings.csv"):
    return pd.read_csv(ratings_path)
