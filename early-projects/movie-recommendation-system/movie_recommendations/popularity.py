import pandas as pd

def popularity_recommendations(movies_path="data/movies.csv", ratings_path="data/ratings.csv", top_n=10):
    movies = pd.read_csv(movies_path)
    ratings = pd.read_csv(ratings_path)

    # Auto-detect ID columns
    movie_id_col_movies = next((c for c in movies.columns if 'id' in c.lower()), None)
    movie_id_col_ratings = next((c for c in ratings.columns if 'id' in c.lower()), None)

    if not movie_id_col_movies or not movie_id_col_ratings:
        raise ValueError("Could not detect movie ID columns in CSVs.")

    popularity = ratings.groupby(movie_id_col_ratings).size().reset_index(name="rating_count")
    merged = pd.merge(popularity, movies, left_on=movie_id_col_ratings, right_on=movie_id_col_movies)
    top_movies = merged.sort_values("rating_count", ascending=False).head(top_n)

    return top_movies[["title", "rating_count"]]
