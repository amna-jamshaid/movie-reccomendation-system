# as I am working in virtal envirnment so first have to download libraries

import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    response= requests.get('https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US'.format(movie_id))
#copied the url of API KEY
    data= response.json()
    return "http://image.tmdb.org/t/p/w500/" + data['poster_path']  # complete poster path

def suggest(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    gap = resemblance[movie_index]
    movies_list = sorted(list(enumerate(gap)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies=[]
    recommended_movies_poster = []
    for i in movies_list:
        # now to fetch poster
        movie_id=movies.iloc[i[0]].	movie_id # get poster from API

        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_poster.append(fetch_poster(movie_id))
    return recommended_movies,recommended_movies_poster

movies_dict =pickle.load(open('movie_dict.pkl','rb'))
#movies = movies_dict['title'].values
movies=pd.DataFrame(movies_dict)

resemblance=pickle.load(open('resemblance.pkl','rb'))

st.title('Movie Recommendation System')

selected_movie_name = st.selectbox(
'TYPE THE NAME OF MOVIE',
    movies['title'].values)

if st.button('Recommend'):
    names,posters=suggest(selected_movie_name)

    col1, col2, col3, col4, col5 =st.beta_columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])

    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:
        st.text(names[2])
        st.image(posters[2])

    with col4:
        st.text(names[3])
        st.image(posters[3])

    with col5:
        st.text(names[4])
        st.image(posters[4])


