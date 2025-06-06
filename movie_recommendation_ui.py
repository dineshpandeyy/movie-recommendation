import streamlit as st
import requests
from movie_recommendation import recommend_movies
from dotenv import load_dotenv
import os

load_dotenv()  # take environment variables from .env

# Function to fetch movie details from OMDB API
def fetch_movie_details(movie_name):
    api_key = os.getenv("OMDB_API_KEY")
    url = f"http://www.omdbapi.com/?t={movie_name}&apikey={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None

# Streamlit UI
st.title("Movie Recommendation System")

# Input field for movie name
movie_name = st.text_input("Enter a movie name:")

if movie_name:    
    # Fetch recommendations using your function
    recommendations = recommend_movies(movie_name)
    
    if isinstance(recommendations, str):
        st.error(recommendations)  # Display error message if movie not found
    else:
        st.write("Recommended Movies:")
        for _, row in recommendations.iterrows():
            recommended_movie = row['title']
            # Fetch movie details from OMDB API
            movie_details = fetch_movie_details(recommended_movie)
            if movie_details and movie_details.get('Response') != 'False':
                # Display movie poster and details
                st.image(movie_details.get("Poster", ""), caption=recommended_movie, width=200)
                st.write(f"Title: {movie_details.get('Title', 'N/A')}")
                st.write(f"Year: {movie_details.get('Year', 'N/A')}")
                st.write(f"Plot: {movie_details.get('Plot', 'N/A')}")
                st.write("---")
            else:
                st.write(f"Details for {recommended_movie} not found.")