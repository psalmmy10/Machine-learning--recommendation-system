import pickle 
import streamlit as st
import numpy as np

st.set_page_config(
    page_title="Book Reommendation App",
) 

st.header('recommendation system using machine learning')
model = pickle.load(open('artifacts/model.pkl', 'rb'))
books_name = pickle.load(open('artifacts/books_name.pkl', 'rb'))
final_data_pair = pickle.load(open('artifacts/final_data_pair.pkl', 'rb'))
books_pivot = pickle.load(open('artifacts/books_pivot.pkl', 'rb'))


def fetch_poster(suggestion):
    books_name = []
    ids_index = []
    poster_url = []
    
    for book_id in suggestion:
        books_name.append(books_pivot.index[book_id])
        
    for name in books_name[0]:
        ids = np.where(final_data_pair['title'] == name)[0][0]
        ids_index.append(ids)
    
    for idx in ids_index:
        url = final_data_pair.iloc[idx]['img_url']
        poster_url.append(url)
        
    return poster_url
        
def recommend_books(book_name):
    book_list = []
    book_id = np.where(books_pivot.index == book_name)[0][0]
    distance, suggestion = model.kneighbors(books_pivot.iloc[book_id,:].values.reshape(1,-1))
    
    poster_url = fetch_poster(suggestion)
    
    for i in range(len(suggestion)):
        books = books_pivot.index[suggestion[i]]
        for j in books:
            book_list.append(j)
            
    return book_list, poster_url

# def a get book function

selected_books = st.selectbox(
    'Type or select a book',
     books_name
)

if st.button('Show recommendation'):
    recommendation_books, poster_url = recommend_books(selected_books)
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        st.text(recommendation_books[1])
        st.image(poster_url[1])
    with col2:
        st.text(recommendation_books[2])
        st.image(poster_url[2])    
    with col3:
        st.text(recommendation_books[3])
        st.image(poster_url[3])    
    with col4:
        st.text(recommendation_books[4])
        st.image(poster_url[4])    
    with col5:
        st.text(recommendation_books[5])
        st.image(poster_url[5])  
        
 
   