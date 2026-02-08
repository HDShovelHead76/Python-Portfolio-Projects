import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

def content_based(movie_title, movies_path="data/movies.csv", top_n=5):
    movies = pd.read_csv(movies_path)

    # Fill missing overviews
    movies['overview'] = movies['overview'].fillna('')

    # Compute TF-IDF matrix
    tfidf = TfidfVectorizer(stop_words="english")
    tfidf_matrix = tfidf.fit_transform(movies['overview'])

    # Compute cosine similarity
    cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
    indices = pd.Series(movies.index, index=movies['title']).drop_duplicates()

    if movie_title not in indices:
        raise ValueError(f"Movie '{movie_title}' not found in dataset.")

    idx = indices[movie_title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:top_n + 1]

    movie_indices = [i[0] for i in sim_scores]
    return movies.iloc[movie_indices][['title', 'overview']]
