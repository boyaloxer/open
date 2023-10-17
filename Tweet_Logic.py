import tweepy
import openai

# Twitter API credentials
CONSUMER_KEY = 'YOUR_CONSUMER_KEY'
CONSUMER_SECRET = 'YOUR_CONSUMER_SECRET'
ACCESS_TOKEN = 'YOUR_ACCESS_TOKEN'
ACCESS_TOKEN_SECRET = 'YOUR_ACCESS_TOKEN_SECRET'

# Set up Twitter API
auth = tweepy.OAuth1UserHandler(
    consumer_key=CONSUMER_KEY,
    consumer_secret=CONSUMER_SECRET,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_TOKEN_SECRET
)
api = tweepy.API(auth)

# OpenAI credentials
openai.api_key = 'YOUR_OPENAI_API_KEY'

def check_for_fallacies(text):
    response = openai.Completion.create(
        prompt=f"Identify logical fallacies in the following statement: \"{text}\".",
        max_tokens=150
    )
    return response.choices[0].text.strip()

def analyze_tweets(username):
    tweets = api.user_timeline(screen_name=username, count=100, tweet_mode="extended")
    results = {}
    for tweet in tweets:
        text = tweet.full_text
        fallacy = check_for_fallacies(text)
        if fallacy:
            results[text] = fallacy
    return results

if __name__ == '__main__':
    username = "TARGET_USERNAME"
    analysis = analyze_tweets(username)
    for tweet, fallacy in analysis.items():
        print(f"Tweet: {tweet}\nIdentified Fallacy: {fallacy}\n{'-'*50}")

