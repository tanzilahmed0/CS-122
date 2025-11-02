import pandas as pd
import re
import string
from textblob import TextBlob
import matplotlib.pyplot as plt
from wordcloud import WordCloud



def extract_hashtags(text):
    if not isinstance(text, str):
        return []
    return re.findall(r'#\w+', text)


def extract_mentions(text):
    if not isinstance(text, str):
        return []
    return re.findall(r'@\w+', text)


def clean_post_content(text):
    if not isinstance(text, str):
        return "No Text"

    # Remove URLs
    text = re.sub(r'http\S+|www.\S+', '', text)
    # Remove mentions and hashtags
    text = re.sub(r'[@#]\w+', '', text)
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    # Remove emojis
    text = re.sub(r'[^\x00-\x7F]+', '', text)
    # Remove extra spaces
    text = re.sub(r'\s+', ' ', text).strip()
    return text


def get_sentiment(text):
    if not isinstance(text, str) or not text.strip():
        return 0.0
    return TextBlob(text).sentiment.polarity


def get_avg_engagement(df):
    """
    Function that accepts a pandas DataFrame that returns a new DataFrame
    showing each user's average likes and shares
    """
    result = df.groupby('user_id', as_index=False)[['likes', 'shares']].mean()
    return result




def main():

    df = pd.read_csv("social_media_posts.csv")

    df['likes'].fillna(df['likes'].median(), inplace=True)
    df['shares'].fillna(df['shares'].mean(), inplace=True)
    df['post_content'].fillna("No Text", inplace=True)
    df['post_date'] = pd.to_datetime(df['post_date'], errors='coerce')

    df['Hashtags'] = df['post_content'].apply(extract_hashtags)
    df['cleaned_post_content'] = df['post_content'].apply(clean_post_content)


    engagement_df = get_avg_engagement(df)
    engagement_df['total_engagement'] = engagement_df['likes'] + engagement_df['shares']
    top_users = engagement_df.sort_values('total_engagement', ascending=False).head(3)
    print("\nTop 3 Users by Engagement:\n", top_users[['user_id', 'total_engagement']])

    all_hashtags = [h for tags in df['Hashtags'] for h in tags]
    top_hashtags = pd.Series(all_hashtags).value_counts().head(5)
    print("\nTop 5 Hashtags:\n", top_hashtags)


    df['sentiment'] = df['cleaned_post_content'].apply(get_sentiment)
    df['sentiment_label'] = df['sentiment'].apply(
        lambda x: 'positive' if x > 0 else ('negative' if x < 0 else 'neutral')
    )

    sentiment_counts = df['sentiment_label'].value_counts()
    avg_sentiment_per_user = df.groupby('user_id')['sentiment'].mean()

    print("\nSentiment Distribution:\n", sentiment_counts)
    print("\nAverage Sentiment per User:\n", avg_sentiment_per_user)

  

    # 1. Word Cloud of hashtags
    if all_hashtags:
        text_for_wc = " ".join(all_hashtags)
        wc = WordCloud(width=800, height=400, background_color="white").generate(text_for_wc)
        wc.to_file("wordcloud.png")

    # 2. Monthly Posts
    df['month'] = df['post_date'].dt.to_period('M')
    monthly_counts = df.groupby('month').size()
    plt.figure(figsize=(8, 4))
    monthly_counts.plot(kind='line', marker='o')
    plt.title('Monthly Posts')
    plt.xlabel('Month')
    plt.ylabel('Number of Posts')
    plt.tight_layout()
    plt.savefig("monthly_posts.png")
    plt.close()

    # 3. Likes vs Shares
    plt.figure(figsize=(6, 6))
    plt.scatter(df['likes'], df['shares'], alpha=0.6)
    plt.title('Likes vs Shares')
    plt.xlabel('Likes')
    plt.ylabel('Shares')
    plt.tight_layout()
    plt.savefig("likes_vs_shares.png")
    plt.close()

    # 4. Average Sentiment per User
    avg_sentiment_per_user.plot(kind='bar', figsize=(8, 4))
    plt.title('Average Sentiment per User')
    plt.xlabel('User ID')
    plt.ylabel('Average Sentiment')
    plt.tight_layout()
    plt.savefig("avg_sentiment_per_user.png")
    plt.close()


if __name__ == "__main__":
    main()
