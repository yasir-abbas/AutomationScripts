#Searches for all the tweets containing specific hashtag given as input

from twitter_scraper import get_tweets,Profile,get_trends

for tweet in get_tweets('#twitter', pages=1):
    print(tweet['text'])

# profile = Profile("Shah Rukh Khan")
# print(profile.location)

# print(get_trends())