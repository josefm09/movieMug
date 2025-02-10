import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from typing import List, Dict

class MovieRecommender:
    def __init__(self, data_processor):
        self.data_processor = data_processor
        self.feature_matrix = None
        self.initialize_recommender()
    
    def initialize_recommender(self):
        """Initialize the recommendation system"""
        if self.data_processor.load_data():
            self.feature_matrix = self.data_processor.create_feature_matrix()
    
    def get_recommendations(self, user_preferences: Dict, n_recommendations: int = 5) -> List[Dict]:
        """Generate movie recommendations based on user preferences"""
        if self.feature_matrix is None:
            return []
        
        # Create user profile vector
        user_vector = self._create_user_vector(user_preferences)
        
        # Calculate similarities
        similarities = cosine_similarity([user_vector], self.feature_matrix.values)[0]
        
        # Get top N recommendations
        top_indices = similarities.argsort()[-n_recommendations:][::-1]
        
        # Prepare recommendations
        recommendations = []
        for idx in top_indices:
            movie = self.data_processor.movies_df.iloc[idx]
            recommendations.append({
                'movie_id': movie.name,
                'title': movie['title'],
                'genres': movie['genres'],
                'year': movie['year'],
                'similarity_score': similarities[idx]
            })
        
        return recommendations
    
    def _create_user_vector(self, preferences: Dict) -> np.ndarray:
        """Create user preference vector"""
        user_vector = np.zeros(len(self.feature_matrix.columns))
        
        # Map preferences to features
        for interest in preferences.get('interests', []):
            if interest in self.feature_matrix.columns:
                user_vector[self.feature_matrix.columns.get_loc(interest)] = 1
        
        for keyword in preferences.get('keywords', []):
            if keyword in self.feature_matrix.columns:
                user_vector[self.feature_matrix.columns.get_loc(keyword)] = 1
        
        return user_vector 