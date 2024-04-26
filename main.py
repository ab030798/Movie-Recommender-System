import streamlit as st
import pickle
import pandas as pd
import numpy as np
import requests
from bokeh.models.widgets import Div
import color

st.markdown(color.page_bg_img, unsafe_allow_html=True)


def poster_fetch(id):
    res= requests.get('https://api.themoviedb.org/3/movie/{}?api_key=3db8a7d5f9a060ef7e399048f5177774&language=en-US'.format(id))
    data=res.json()
    return "https://image.tmdb.org/t/p/original/" + data['poster_path']

def recomonded(movie):
    movie_index= movies[movies['title']==movie].index[0]
    dist= cosine_vec[movie_index]
    mv_list=sorted(list(enumerate(dist)),reverse=True,key=lambda x: x[1])[1:6]
    recomonded_movies=[]
    recomnonded_poster=[]
    for i in mv_list:
        movie_id= movies.iloc[i[0]].movie_id
        recomonded_movies.append(movies['title'][i[0]])
        recomnonded_poster.append(poster_fetch(movie_id))
    return recomonded_movies,recomnonded_poster

cosine_vec=pickle.load(open('cosine_vec.pkl','rb'))
    
    

movies_dict= pickle.load(open('movies_dict.pkl','rb'))
movies= pd.DataFrame(movies_dict)
movies_list= movies['title'].values;
st.title("Movie Recommender System")
selected_movies = st.selectbox(
'How would you like to be contacted?',
(movies_list))

if st.button('Recommend',):
    recommended_movie_names,recommended_movie_poster=recomonded(selected_movies)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_poster[0])
        #url = 'https://www.uphe.com/movies/8-mile'
        

        
        
        
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_poster[1])

    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_poster[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_poster[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_poster[4])


recommended_movie_names,recommended_movie_poster=recomonded(selected_movies)


