# Description: Movie recommendation engine (Content based)

import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load data from csv
df = pd.read_csv('movie_dataset.csv')
# print(df.head(3))

# view shape of data
# print(df.shape)

features = ['keywords', 'cast', 'genres', 'director']

# filter based on columns
# print(df[features].head(3))

# clean data and process it
for feature in features:
    df[feature] = df[feature].fillna('')  # fill with empty string

# Function that creates a single string


def combine_features(row):
    return row['keywords'] + " " + row['cast'] + " " + row['genres'] + " " + row['director']


df["combined_features"] = df.apply(combine_features, axis=1)

# print(df['combined_features'].head(3))

# create matrix/vector from combined combined features column
count_matrix = CountVectorizer().fit_transform(df['combined_features'])
# print(count_matrix.toarray())

# Get the cosine similarity from the matrix count
cosine_sim = cosine_similarity(count_matrix)
# print(cosine_sim)

# helper function to get title from index


def get_title_from_index(index):
    return df[df.index == index]["title"].values[0]

# function to get index from title


def get_index_from_title(title):
    return df[df.title == title]["index"].values[0]


movie_user_likes = 'Robin Hood'

# get movie index
m_index = get_index_from_title(movie_user_likes)

# find similar movies
similar_movies = list(enumerate(cosine_sim[m_index]))

# sort the list
sorted_movies = sorted(similar_movies, key=lambda x: x[1], reverse=True)[1:]

# print(sorted_movies)

i = 0
print('My top movies similar to %s are: ' % movie_user_likes)

for item in sorted_movies:
    print(get_title_from_index(item[0]))
    # title = get_title_from_index(item[0])
    # score = sorted_movies[i][1]
    # movie_data = 'Movie Title: ' + title + " Similarity score: " + str(score)
    i = i + 1
    if i >= 10:
        break

i=0
for i in range( len(sorted_movies)):
    print('Movie title:',get_title_from_index(sorted_movies[i][0]), ', Similarity Score: ', sorted_movies[i][1] )
    i=i+1
    if i>=10:
        break
