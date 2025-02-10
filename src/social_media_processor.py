import tweepy
import facebook
from typing import Dict, List

class SocialMediaProcessor:
    def __init__(self, twitter_api_key: str, twitter_api_secret: str, facebook_api_key: str):
        self.twitter_api = self._init_twitter(twitter_api_key, twitter_api_secret)
        self.facebook_api = self._init_facebook(facebook_api_key)
    
    def _init_twitter(self, api_key: str, api_secret: str):
        """Initialize Twitter API client"""
        try:
            auth = tweepy.OAuthHandler(api_key, api_secret)
            return tweepy.API(auth)
        except Exception as e:
            print(f"Error initializing Twitter API: {str(e)}")
            return None
    
    def _init_facebook(self, api_key: str):
        """Initialize Facebook API client"""
        try:
            return facebook.GraphAPI(api_key)
        except Exception as e:
            print(f"Error initializing Facebook API: {str(e)}")
            return None
    
    def get_social_profile(self, twitter_username: str = None, facebook_id: str = None) -> Dict:
        """Collect user data from social media profiles"""
        profile_data = {
            'interests': [],
            'keywords': [],
            'demographics': {}
        }
        
        if twitter_username and self.twitter_api:
            twitter_data = self._get_twitter_data(twitter_username)
            profile_data['interests'].extend(twitter_data.get('interests', []))
            profile_data['keywords'].extend(twitter_data.get('keywords', []))
        
        if facebook_id and self.facebook_api:
            facebook_data = self._get_facebook_data(facebook_id)
            profile_data['interests'].extend(facebook_data.get('interests', []))
            profile_data['demographics'].update(facebook_data.get('demographics', {}))
        
        return profile_data
    
    def _get_twitter_data(self, username: str) -> Dict:
        """Extract relevant data from Twitter profile"""
        try:
            user = self.twitter_api.get_user(screen_name=username)
            tweets = self.twitter_api.user_timeline(screen_name=username, count=100)
            
            return {
                'interests': self._extract_interests_from_bio(user.description),
                'keywords': self._extract_keywords_from_tweets(tweets)
            }
        except Exception as e:
            print(f"Error getting Twitter data: {str(e)}")
            return {}
    
    def _get_facebook_data(self, user_id: str) -> Dict:
        """Extract relevant data from Facebook profile"""
        try:
            user = self.facebook_api.get_object(user_id)
            likes = self.facebook_api.get_connections(user_id, 'likes')
            
            return {
                'interests': self._extract_facebook_likes(likes),
                'demographics': self._extract_demographics(user)
            }
        except Exception as e:
            print(f"Error getting Facebook data: {str(e)}")
            return {} 