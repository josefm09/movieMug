# movieMug
# Movie Recommender System

A movie recommendation system that uses MovieLens dataset and social media profile information to generate personalized movie recommendations.

## Setup

1. Create a virtual environment:

python -m venv venv

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Download the MovieLens dataset and place the files in the `data/` directory:
   - movies.csv
   - ratings.csv
   - tags.csv

4. Create a `.env` file with your API keys:

TWITTER_API_KEY=your_twitter_api_key
TWITTER_API_SECRET=your_twitter_api_secret
FACEBOOK_API_KEY=your_facebook_api_key

5. Run the main script:

```bash
python src/main.py
```

## Usage

Create the directory structure and files as shown above
Download the MovieLens dataset and place it in the data/ directory
Install the requirements
Set up your social media API keys in the .env file
Run the main script
The system will:
Load and process the MovieLens dataset
Collect user preferences from social media
Generate personalized movie recommendations