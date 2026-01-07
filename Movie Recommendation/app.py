import streamlit as st
from recommender import recommend

st.set_page_config(page_title="Movie Recommender", layout="centered")

st.title("🎬 Movie Recommendation System")
st.write("Content-Based Movie Recommender using Machine Learning")

movie_name = st.text_input("Enter your favourite movie")

if st.button("Recommend"):
    if movie_name.strip() == "":
        st.warning("Please enter a movie name")
    else:
        recommendations = recommend(movie_name)

        if recommendations:
            st.subheader("Movies suggested for you:")
            for movie in recommendations:
                st.write("👉", movie)
        else:
            st.error("No matching movie found. Try another one!")
