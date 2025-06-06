# Movie Recommendation System

A content-based movie recommendation system that suggests similar movies based on movie content analysis. The system uses natural language processing and machine learning techniques to provide personalized movie recommendations.

## Live Demo

Try the application online: [Movie Recommendation System](https://findmovie.streamlit.app/)

## Features

- Content-based movie recommendations using TF-IDF and cosine similarity
- Movie details and posters fetched from OMDB API
- Interactive web interface built with Streamlit
- Text preprocessing and analysis of movie content
- Word cloud visualization of movie content

## Prerequisites

- Python 3.x
- Required Python packages
  - numpy
  - pandas
  - scikit-learn
  - matplotlib
  - wordcloud
  - nltk
  - streamlit
  - requests
  - python-dotenv

## Setup

1. Clone the repository
2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```
3. Create a `.env` file in the root directory and add your OMDB API key:
   ```
   OMDB_API_KEY=your_api_key_here
   ```
4. Download the required NLTK data:
   ```python
   import nltk
   nltk.download('punkt')
   nltk.download('stopwords')
   ```

## Usage

1. Run the Streamlit application:
   ```bash
   streamlit run movie_recommendation_ui.py
   ```
2. Open your web browser and navigate to the provided local URL (typically http://localhost:8501)
3. Enter a movie name in the input field
4. View the recommended movies with their details and posters

## How It Works

1. The system uses a dataset of movies with information about genres, keywords, overview, and director
2. Text preprocessing is applied to clean and normalize the movie content
3. TF-IDF vectorization converts the text data into numerical features
4. Cosine similarity is used to find similar movies based on content
5. The web interface fetches additional movie details from OMDB API
6. Results are displayed with movie posters and information

## Project Structure

- `movie_recommendation.py`: Core recommendation system implementation
- `movie_recommendation_ui.py`: Streamlit web interface
- `movies.csv`: Movie dataset
- `.env`: Environment variables (API keys)

## Note

Make sure to keep your OMDB API key secure and never commit it to version control. The API key should be stored in the `.env` file. 