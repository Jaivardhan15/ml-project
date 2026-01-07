import pandas as pd
import difflib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load dataset
movies_data = pd.read_csv("movies.csv")

# Features used for recommendation (same as notebook)
selected_features = ['genres', 'keywords', 'tagline', 'cast', 'director']

# Fill missing values
for feature in selected_features:
    movies_data[feature] = movies_data[feature].fillna('')

# Combine all features
combined_features = (
    movies_data['genres'] + ' ' +
    movies_data['keywords'] + ' ' +
    movies_data['tagline'] + ' ' +
    movies_data['cast'] + ' ' +
    movies_data['director']
)

# Convert text to vectors
vectorizer = TfidfVectorizer()
feature_vectors = vectorizer.fit_transform(combined_features)

# Cosine similarity
similarity = cosine_similarity(feature_vectors)

def recommend(movie_name, n=10):
    list_of_all_titles = movies_data['title'].tolist()

    # Find closest matching movie name
    close_match = difflib.get_close_matches(movie_name, list_of_all_titles)

    if not close_match:
        return []

    close_match = close_match[0]

    index_of_movie = movies_data[movies_data.title == close_match]['index'].values[0]

    similarity_scores = list(enumerate(similarity[index_of_movie]))

    sorted_movies = sorted(similarity_scores, key=lambda x: x[1], reverse=True)

    recommended_movies = []

    for i in range(1, n + 1):
        index = sorted_movies[i][0]
        title = movies_data[movies_data.index == index]['title'].values[0]
        recommended_movies.append(title)

    return recommended_movies
