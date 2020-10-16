#Given Username as input, it scrapes all the data of that user from twitter
#Drawback : After some tries twitter starts blocking your requests


import GetOldTweets3 as got

tweetCriteria = got.manager.TweetCriteria().setUsername("Barack Obama")\
                                           .setMaxTweets(2)
tweet = got.manager.TweetManager.getTweets(tweetCriteria)
for tweets in tweet:
    print(tweets.username)
    print(tweets.date)
    print(tweets.hashtags)
