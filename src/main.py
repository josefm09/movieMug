import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config.config import *
from src.data_processor import DataProcessor
from src.social_media_processor import SocialMediaProcessor
from src.recommender import MovieRecommender

def main():
    # Initialize processors
    data_processor = DataProcessor(
        movies_file=MOVIES_FILE,
        ratings_file=RATINGS_FILE,
        tags_file=TAGS_FILE
    )
    
    social_processor = SocialMediaProcessor(
        twitter_api_key=TWITTER_API_KEY,
        twitter_api_secret=TWITTER_API_SECRET,
        facebook_api_key=FACEBOOK_API_KEY
    )
    
    # Initialize recommender
    recommender = MovieRecommender(data_processor)
    
    # Example usage
    twitter_username = "example_user"
    facebook_id = "example_id"
    
    # Get social profile
    user_profile = social_processor.get_social_profile(
        twitter_username=twitter_username,
        facebook_id=facebook_id
    )
    
    # Get recommendations
    recommendations = recommender.get_recommendations(
        user_preferences=user_profile,
        n_recommendations=N_RECOMMENDATIONS
    )
    
    # Print recommendations
    print("\nRecommended movies:")
    for i, rec in enumerate(recommendations, 1):
        print(f"\n{i}. {rec['title']} ({rec['year']})")
        print(f"   Genres: {rec['genres']}")
        print(f"   Similarity Score: {rec['similarity_score']:.2f}")

if __name__ == "__main__":
    main() 