import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=f588570312d19e221efd488d61fdb695'.format(movie_id))
    data =  response.json()
    return 'http://image.tmdb.org/t/p/w500/' + data['poster_path']


movie_dict = pickle.load(open('movies_dict.pkl','rb'))
movies = pd.DataFrame(movie_dict)
similarity = pickle.load(open('similarity.pkl','rb'))


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distance = similarity[movie_index]
    five_movies = sorted(list(enumerate(distance)),reverse= True , key = lambda x:x[1])[1:6]

    names = []
    poster = []
    for i in five_movies:
        movie_id = movies.iloc[i[0]].id

        names.append(movies.iloc[i[0]].title)
        # poster.append(fetch_poster(movie_id))
    return names


st.title('Movies Recommender System')

selected_movie_name = st.selectbox('Select your movies here',movies['title'].values)
if st.button('Recommend'):
    recommendation = recommend(selected_movie_name)
    for i in recommendation:
        st.write(i)
    # names , poster = recommend(selected_movie_name)
    # import streamlit as st

    # col1, col2, col3 ,col4 ,col5= st.columns(5)

    # with col1:
    #     st.text(names[0])
    #     st.image(poster[0])

    # with col2:
    #     st.text(names[1])
    #     st.image(poster[1])

    # with col3:
    #     st.text(names[2])
    #     st.image(poster[2])

    # with col4:
    #     st.text(names[3])
    #     st.image(poster[3])

    # with col5:
    #     st.text(names[4])
    #     st.image(poster[4])