#It will all the news regarding certain search query from different blogs and news sites. For further details visit newsapi official documentation

from newsapi import NewsApiClient

# Init
newsapi = NewsApiClient(api_key='a370118eab2c400c9fa646b2728c31ca')

# /v2/top-headlines
top_headlines = newsapi.get_everything(q='Cyber Security',language='en')

print(top_headlines)