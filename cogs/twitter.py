import tweepy
from discord.ext import commands


def setup(bot):
    bot.add_cog(BotTwitter(bot))


all_keys = open('ajzt/twitterkey', 'r').read().splitlines()
api_key = all_keys[0]
api_key_secret = all_keys[1]
access_token = all_keys[2]
access_token_secret = all_keys[3]
bearer_token = all_keys[4]

client = tweepy.Client(bearer_token=bearer_token, consumer_key=api_key,
                       consumer_secret=api_key_secret, access_token=access_token,
                       access_token_secret=access_token_secret)


def get_user_id(username):
    """
    Get user id from a username twitter
    """
    print("The screen name is :", username)
    twitter_id = client.get_user(username=username)
    print(f"The Twitter ID is : {twitter_id.data.id}")
    return twitter_id.data.id


def get_username(identifiant):
    """
    Get username from a user id twitter
    """
    twitter_id = client.get_user(id=identifiant)
    return twitter_id.data.name


class BotTwitter(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def last_mention(self, ctx, pseudo):
        """Get last tweet from a twitter account"""
        try:
            tweets = client.get_users_mentions(get_user_id(f"{pseudo}"), tweet_fields=['referenced_tweets',
                                                                                       'in_reply_to_user_id'],
                                               max_results=5)
            tweet_originel = tweets.data[0]['referenced_tweets'][0]['id']
            user_id = tweets.data[0]['in_reply_to_user_id']
            username = get_username(user_id)
            await ctx.send(f"https://twitter.com/{username}/status/{tweet_originel}")
        except:
            await ctx.send("An error has occurred. Please try again !")