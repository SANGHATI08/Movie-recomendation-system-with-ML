# -*- coding: utf-8 -*-
"""movie recomondation.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1CHDGhNHE_K2qi7xaYjKPhb_HMWafIq1N

# **Content based movie recomendation system with ML**
Build a content based movie recomendation system which is build with the help of cosine similarity, before that I have convert the textual data to feature vector.
"""

import numpy as np
import pandas as pd
import difflib ##to find the closest match for the movie if the user makes any spelling mistakes
from sklearn.feature_extraction.text import TfidfVectorizer  ##cpnvert the texutal data to feature vector(numerical data)
from sklearn.metrics.pairwise import cosine_similarity #for finding similarity score

"""Data Collection and Pre-Processing"""

df = pd.read_csv('/content/movies.csv', encoding='utf-8')

df.head()

df.shape

df.describe()

from wordcloud import WordCloud
import matplotlib.pyplot as plt

movie_title=[]
for original_title in df.original_title:
    movie_title.append(original_title[0:-7])
movie_title=str(movie_title)

wordcloud_title=WordCloud(width=1500,height=800,background_color='cyan',min_font_size=2,min_word_length=3).generate(movie_title)
plt.figure(figsize=(20,10))
plt.axis('off')
plt.title('WORDCLOUD for Movies title',fontsize=30)
plt.imshow(wordcloud_title)

"""Finding Top 20 movies with highest vote_average"""

df1=df.groupby(['original_title'])[['vote_average']].sum()
high_rated=df1.nlargest(20,'vote_average')
high_rated.head()

plt.figure(figsize=(25,10))
plt.title('Top 20 movies with highest vote_average',fontsize=40)
plt.ylabel('vote_average',fontsize=30)
plt.xticks(fontsize=25,rotation=90)
plt.xlabel('original_title',fontsize=30)
plt.yticks(fontsize=25)
plt.bar(high_rated.index,high_rated['vote_average'],linewidth=3,color=colors)

"""Top 20 movies with highest popularity"""

df2=df.groupby(['original_title'])[['popularity']].sum()
high_rated=df2.nlargest(20,'popularity')
high_rated.head()

plt.figure(figsize=(20,10))
plt.title('Top 20 movies with highest popularity',fontsize=40)
plt.xticks(fontsize=25,rotation=90)
plt.xlabel('original_title',fontsize=30)
plt.yticks(fontsize=25)
plt.bar(high_rated.index,high_rated['popularity'],linewidth=3,color=colors)

"""selecting the relevant features for recommendation"""

selected_features = ['genres','keywords','tagline','cast','director']

"""replacing the null valuess with null string"""

for feature in selected_features:
  df[feature] = df[feature].fillna('')

"""combining all the 5 selected features"""

combined_features = df['genres']+' '+df['keywords']+' '+df['tagline']+' '+df['cast']+' '+df['director']

print(combined_features)

"""converting the text data to feature vectors"""

vectorizer = TfidfVectorizer()
feature_vectors = vectorizer.fit_transform(combined_features)
print(feature_vectors)

"""Cosine Similarity


*getting the similarity scores using cosine similarity*

"""

similarity = cosine_similarity(feature_vectors)
print(similarity)

print(similarity.shape)

"""Getting the movie name from the user"""

movie_name = input(' Enter your favourite movie name : ')

"""creating a list with all the movie names given in the dataset"""

list_of_all_titles = df['title'].tolist()
print(list_of_all_titles)

"""finding the close match for the movie name given by the user"""

find_close_match = difflib.get_close_matches(movie_name, list_of_all_titles)
print(find_close_match)

close_match = find_close_match[0]
print(close_match)

"""finding the index of the movie with title"""

index_of_the_movie = df[df.title == close_match]['index'].values[0]
print(index_of_the_movie)

"""getting a list of similar movies with similarity score

"""

similarity_score = list(enumerate(similarity[index_of_the_movie]))  ##enumerate is used to carry out a loop in a list
print(similarity_score)

len(similarity_score)

"""sorting the movies based on their similarity score"""

sorted_similar_movies = sorted(similarity_score, key = lambda x:x[1], reverse = True)
print(sorted_similar_movies)

"""print the name of similar movies based on the index


"""

print('Movies suggested for you : \n')

i = 1

for movie in sorted_similar_movies:
  index = movie[0]
  title_from_index = df[df.index==index]['title'].values[0]
  if (i<30):
    print(i, '.',title_from_index)
    i+=1

"""Movie Recommendation Sytem"""

movie_name = input(' Enter your favourite movie name : ')

list_of_all_titles = df['title'].tolist()

find_close_match = difflib.get_close_matches(movie_name, list_of_all_titles)

close_match = find_close_match[0]

index_of_the_movie = df[ df.title == close_match]['index'].values[0]

similarity_score = list(enumerate(similarity[index_of_the_movie]))

sorted_similar_movies = sorted(similarity_score, key = lambda x:x[1], reverse = True)

print('Movies suggested for you : \n')

i = 1

for movie in sorted_similar_movies:
  index = movie[0]
  title_from_index = movies_data[movies_data.index==index]['title'].values[0]
  if (i<30):
    print(i, '.',title_from_index)
    i+=1

