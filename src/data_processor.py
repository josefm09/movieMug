import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

class DataProcessor:
    def __init__(self, movies_file, ratings_file, tags_file):
        self.movies_file = movies_file
        self.ratings_file = ratings_file
        self.tags_file = tags_file
        
    def load_data(self):
        """Load and preprocess MovieLens dataset"""
        try:
            self.movies_df = pd.read_csv(self.movies_file)
            self.ratings_df = pd.read_csv(self.ratings_file)
            self.tags_df = pd.read_csv(self.tags_file)
            
            # Basic preprocessing
            self.movies_df['year'] = self.movies_df['title'].str.extract('(\(\d{4}\))').fillna('(0)')
            self.movies_df['year'] = self.movies_df['year'].str.extract('(\d+)').astype(int)
            self.movies_df['title'] = self.movies_df['title'].str.replace('(\(\d{4}\))', '').str.strip()
            
            return True
        except Exception as e:
            print(f"Error loading data: {str(e)}")
            return False
    
    def create_feature_matrix(self):
        """Create feature matrix from movies data"""
        # Create genre features
        genre_features = self.movies_df['genres'].str.get_dummies('|')
        
        # Create tag features
        tfidf = TfidfVectorizer(max_features=1000)
        if not self.tags_df.empty:
            tags_grouped = self.tags_df.groupby('movieId')['tag'].apply(' '.join)
            tag_features = tfidf.fit_transform(tags_grouped)
            tag_features = pd.DataFrame(
                tag_features.toarray(), 
                index=tags_grouped.index,
                columns=tfidf.get_feature_names_out()
            )
        else:
            tag_features = pd.DataFrame()
        
        # Combine features
        self.feature_matrix = pd.concat([genre_features, tag_features], axis=1)
        return self.feature_matrix 