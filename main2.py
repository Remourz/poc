import tweepy
import random
import time

consumer_key = "IVeKWKmESrTnz53xTc0hyw20n"
consumer_secret = "F591A6eBeeka5HHBNCu2sv6RNuKd6Nd5STwCisZes5KrpeAImD"
access_token = "990012327956238337-sWhlWEsPZ8fqQut5n0uiZSc2e9szjvq"
access_token_secret = "seRFfywxBnSYZxBsahSjZFyW62zdlaboF5BjxJ8muKbPs"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

query = "#NFTGiveaways Drop"
walletAdress = "0x9E1bAf2FB1C5cB6cF9ED1F28ef5a5597b28b3ee8" #change this to your wallet adress
replies = [
    "broooof!\n",
    "Ya!\n",
    "cool\n",
    "nice\n",
    "Amazing!\n",
    "Lets get lucky!\n",
    "gg!\n",
    "Welp\n",
    "Lets go!!!\n",
    "Woop\n",
    "Thanks\n",
    "Welp go!\n"

]


friendsList = api.get_friend_ids(screen_name="elonmusk", count=3) #set your screen name
friends = []

print("Getting the friends list. Please wait...\n")
for i in range(0, 3):
    friend = api.get_user(user_id=friendsList[i])
    friends.append(friend.screen_name)

tagList = []

for tweet in tweepy.Cursor(api.search_tweets, q=query, count=100, lang="en", tweet_mode="extended").items():
    try:
        tweet.retweeted_status
    except AttributeError:
        print(f"Tweet found. Tweet ID: {tweet.id}")
        s = tweet.full_text
        words = s.split()
        tagFound = False
        for word in words:
            if word.find("tag") != -1 or word.find("Tag") != -1 or word.find("TAG") != -1:
                tagFound = True
        if tagFound == False:
            try:
                reply = random.choice(replies) + walletAdress
                api.update_status(status=reply, in_reply_to_status_id=tweet.id, auto_populate_reply_metadata=True)
                print("Wallet adress succesfully dropped.")
            except Exception as e:
                print(e)
            try:
                api.create_favorite(tweet.id)
                print("Tweet liked.")
            except Exception as e:
                print(e)
            try:
                api.create_friendship(screen_name=tweet.user.screen_name)
                print("Followed user.")
            except Exception as e:
                print(e)
            #following everyone tagged into the post
            tweetSplit2 = tweet.full_text.split()
            users = []
            for user in tweetSplit2:
                if user.find("@") != -1:
                    users.append(user)
            if len(users) > 0:
                users_NonDuplicates = list(dict.fromkeys(users))
                for name in users_NonDuplicates:
                    try:
                        api.create_friendship(screen_name=name)
                        print(f"Succesfully followed {name}.")
                    except Exception as e:
                        print(e)
            #following everyone tagged into the post
            try:
                api.retweet(tweet.id)
                print("Tweet has been retweeted successfully.")
            except Exception as e:
                print(e)
            timer = random.randint(300, 600) #set the timer to a random value between X and Y seconds
            print(f"All tasks are done for this tweet. Sleeping for {timer} seconds.\n")
            time.sleep(timer)
