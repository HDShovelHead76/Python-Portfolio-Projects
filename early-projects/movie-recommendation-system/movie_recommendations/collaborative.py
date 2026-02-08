import pandas as pd

def collaborative_filtering(user_id, movies_path="data/movies.csv", ratings_path="data/ratings.csv", top_n=5):
    movies = pd.read_csv(movies_path)
    ratings = pd.read_csv(ratings_path)

    # Auto-detect ID columns
    movie_id_col_movies = next((c for c in movies.columns if 'id' in c.lower()), None)
    movie_id_col_ratings = next((c for c in ratings.columns if 'id' in c.lower()), None)

    if not movie_id_col_movies or not movie_id_col_ratings:
        raise ValueError("Could not detect movie ID columns in CSVs.")

    # Simple collaborative filtering: recommend movies the user hasn't rated yet
    user_ratings = ratings[ratings['userId'] == user_id]
    rated_movie_ids = set(user_ratings[movie_id_col_ratings])

    # Recommend top-rated movies not yet rated by user
    avg_ratings = ratings.groupby(movie_id_col_ratings)['rating'].mean().reset_index()
    recommendations = avg_ratings[~avg_ratings[movie_id_col_ratings].isin(rated_movie_ids)]
    merged = pd.merge(recommendations, movies, left_on=movie_id_col_ratings, right_on=movie_id_col_movies)

    top_recs = merged.sort_values("rating", ascending=False).head(top_n)
    return top_recs[['title', 'rating']]
