import tweepy
from sentiment import sentiment

consumer_key = "Cc2c5Q9juFjp71PYd8Y220sao"
consumer_secret = "Id2JRDjI1xmLzXiDmTecW55Knh2KXOUSr8yRJ6PrUrmIUI5a5f"
access_token = "1381210768008388617-ghTiHPyb7w3FzsEc6GLoE1K2fg0mmO"
access_token_secret = "xPLWB9Bd4zfRd1iArg7jRqQYdIw4LixXGwyWp628R7gZ0"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


def choose(tag):
    if(tag == "lasttweet"):
        out = get_latest_tweet()

    elif(tag == "recenttweet"):
        out = keyword_search()    

    return out

def get_latest_tweet():
    cursor = tweepy.Cursor(api.user_timeline, id = 'JustinTrudeau', tweet_mode = "extended").items(1)
    for i in cursor:
        out = "Hmm, lets see...My most recent tweet says: \n\n\"" + str(i.full_text) + "\" \n\nIt got " + str(i.favorite_count) + " likes and " + str(i.retweet_count) + " retweets..."
        if i.favorite_count > 500:
            out += "\nI guess the people seemed to like it!"
        elif i.favorite_count < 500:
            out += "\nLooks like people didn't seem to agree..."
        elif i.retweet_count > 50:
            out += "\nSeems like it's generating quite a buzz!"
        else:
            out += "\nI think this was just posted. Give people time to react!"
        return out

def keyword_search():
    cursor = tweepy.Cursor(api.search, q = 'Trudeau', tweet_mode = "extended").items(20)
    for i in cursor:
        if "RT" not in i.full_text:
            out = "User " + str(i.user.screen_name) + " says:\n\n\"" + str(i.full_text) + "\"\n\n"
            s = sentiment(i.full_text)
            sent = s.sentiment_analysis()
            out += str(s.sentimentNumber(sent))
            return out         