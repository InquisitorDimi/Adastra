import pandas as pd
import logging
import json

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

df = pd.read_csv("movies_metadata.csv")

class MovieAnalysis:

  #  A class to perform various operations on a movie dataset.

    def __init__(self, csv_path):
       
        # Initialize the MovieAnalysis class with the path to the CSV file.
        # param csv_file: Path to the CSV file containing the movie dataset.
        self.csv_file = csv_path
        self.df = None

    def load_dataset(self):
        # Load the dataset from the CSV file into a pandas DataFrame.
        
        try:
            self.df = pd.read_csv(self.csv_file)
            logging.info("Dataset loaded successfully.")
        except Exception as e:
            logging.error(f"Error loading dataset: {e}")
            raise

    def unique_movies_count(self):
        
        # Print the number of unique movies in the dataset.
        
        try:
            unique_movies = self.df['title'].nunique()
            logging.info(f"Number of unique movies: {unique_movies}")
            return unique_movies
        except Exception as e:
            logging.error(f"Error calculating unique movies: {e}")
            raise

    def average_rating(self):
       # Print the average rating of all the movies.
        
        try:
            avg_rating = self.df['vote_average'].mean()
            logging.info(f"Average rating of all movies: {avg_rating}")
            return avg_rating
        except Exception as e:
            logging.error(f"Error calculating average rating: {e}")
            raise

    def top_5_highest_rated_movies(self):
       # Print the top 5 highest rated movies.
        
        try:
            top_5_movies = self.df.nlargest(5, 'vote_average')[['title', 'vote_average']]
            logging.info("Top 5 highest rated movies:")
            logging.info(top_5_movies)
            return top_5_movies
        except Exception as e:
            logging.error(f"Error fetching top 5 highest rated movies: {e}")
            raise

    def movies_released_each_year(self):

       # Print the number of movies released each year.
        try:
            movies_per_year = self.df['release_date'].value_counts().sort_index()
            logging.info("Number of movies released each year:")
            logging.info(movies_per_year)
            return movies_per_year
        except Exception as e:
            logging.error(f"Error calculating movies released each year: {e}")
            raise

    def movies_per_genre(self):
    
       # Print the number of movies in each genre.
        try:
            genre_counts = self.df['genres'].value_counts()
            logging.info("Number of movies in each genres:")
            logging.info(genre_counts)
            return genre_counts
        except Exception as e:
            logging.error(f"Error calculating movies in each genre: {e}")
            raise

    def save_to_json(self, json_file):
       # Save the dataset to a JSON file.
       # param json_file: Path to the JSON file where the dataset will be saved.
        try:
            self.df.to_json(json_file, orient='records', lines=True)
            logging.info(f"Dataset saved to JSON file: {json_file}")
        except Exception as e:
            logging.error(f"Error saving dataset to JSON: {e}")
            raise

def main():
    csv_path = 'movies_metadata.csv'
    json_path = 'output_movies_metadata.json'

    movie_dataset = MovieAnalysis(csv_path)
    movie_dataset.load_dataset()
    movie_dataset.unique_movies_count()
    movie_dataset.average_rating()
    movie_dataset.top_5_highest_rated_movies()
    movie_dataset.movies_released_each_year()
    movie_dataset.movies_per_genre()
    movie_dataset.save_to_json(json_path)

if __name__ == "__main__":
    main() 

quit
