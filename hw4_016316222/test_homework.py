import unittest
import pandas as pd
from social_media_analysis import extract_hashtags,extract_mentions, clean_post_content, get_sentiment, get_avg_engagement

class TestSocialMediaAnalysis(unittest.TestCase):

    def test_clean_post_content(self):
        test_text = "Check this out! @user #cool https://example.com"
        cleaned_text = clean_post_content(test_text)
        extracted_hastags= extract_hashtags(test_text)
        extracted_mentions= extract_mentions(test_text)
        self.assertNotIn("@user", cleaned_text)
        self.assertNotIn("#cool", cleaned_text)
        self.assertNotIn("https", cleaned_text)
        self.assertNotIn("!", cleaned_text)
        self.assertIn("#cool", extracted_hastags)
        self.assertIn("@user", extracted_mentions)

    def test_sentiment_analysis(self):
        test_text = "I love this product!"
        sentiment = get_sentiment(test_text)
        self.assertGreater(sentiment, 0)

    def test_avg_engagement(self):
        # Simulate a small DataFrame for testing
        test_data = {
            'user_id': [1001,1001, 1002, 1003],
            'likes': [120, 305, 95, 200],
            'shares': [50, 405, 30, 75],
        }
        test_df = pd.DataFrame(test_data)
        result = get_avg_engagement(test_df)
        check_against=test_df.groupby('user_id')[['likes', 'shares']].mean()
        self.assertEqual(check_against['likes'].tolist(), result['likes'].tolist())

if __name__ == '__main__':
    unittest.main()
