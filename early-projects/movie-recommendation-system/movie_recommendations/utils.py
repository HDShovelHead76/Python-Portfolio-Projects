import pandas as pd
import os

BASE_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data")

def load_movies(movies_path=os.path.join(BASE_DIR, "movies.csv")):
    return pd.read_csv(movies_path)

def load_ratings(ratings_path=os.path.join(BASE_DIR, "ratings.csv")):
    return pd.read_csv(ratings_path)
