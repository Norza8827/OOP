# OE 3
class SocialMediaAccount:
    def __init__(self, username, password):
        self.username = username
        self.password = password
    
    def login(self):
        print(f"{self.username} has logged in.")
    
    def post(self, content):
        print(f"{self.username} posted: {content}")

class InstagramAccount(SocialMediaAccount):
    def __init__(self, username, password, number_of_followers):
        super().__init__(username, password)
        self.number_of_followers = number_of_followers
    
    def share_story(self, story_content):
        print(f"{self.username} shared a story: {story_content}")
        print(f"Followers who viewed the story: {self.number_of_followers}")

class TwitterAccount(SocialMediaAccount):
    def __init__(self, username, password, number_of_tweets):
        super().__init__(username, password)
        self.number_of_tweets = number_of_tweets
    
    def tweet(self, tweet_content):
        self.number_of_tweets += 1
        print(f"{self.username} tweeted: {tweet_content}")
        print(f"Total Tweets: {self.number_of_tweets}")

insta_account = InstagramAccount("Nicos", "secret", 500)
insta_account.login()
insta_account.post("*some random meme*")
insta_account.share_story("*some random meme, again*")
print()

twitter_account = TwitterAccount("Nicos", "secret", 100)
twitter_account.login()
twitter_account.post("*some random meme*")
twitter_account.tweet("*some random meme, again*")
twitter_account.tweet("*another random meme*")
