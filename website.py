import streamlit as st
import pandas as pd
import numpy as np
import requests
import pickle
st.title('Movie Recommendation System')



similarity=pickle.load(open('similarity_matrix.pkl','rb'))
movies_dict=pickle.load(open('movies_dict.pkl','rb'))
movies=pd.DataFrame(movies_dict)
selected_movie=st.selectbox('Enter your choice',movies['title'].values)

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])
    top_five = movie_list[1:6]
    recommended_movie = []
    for i in top_five:
        movie_id=i[0]
        recommended_movie.append(movies.iloc[i[0]].title)
    return recommended_movie

if st.button('Recommend'):
    recommendations = recommend(selected_movie)
    for i in recommendations:
        st.write(i)
