import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# API Keys (store these in .env file)
TWITTER_API_KEY = os.getenv('TWITTER_API_KEY')
TWITTER_API_SECRET = os.getenv('TWITTER_API_SECRET')
FACEBOOK_API_KEY = os.getenv('FACEBOOK_API_KEY')

# Data paths
DATA_DIR = 'data'
MOVIES_FILE = os.path.join(DATA_DIR, 'movies.csv')
RATINGS_FILE = os.path.join(DATA_DIR, 'ratings.csv')
TAGS_FILE = os.path.join(DATA_DIR, 'tags.csv')

# Model parameters
N_RECOMMENDATIONS = 5
SIMILARITY_THRESHOLD = 0.3 