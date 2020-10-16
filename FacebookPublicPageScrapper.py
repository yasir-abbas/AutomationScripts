#Given Facebook Public page as input it scrapes all posts from that page including all meta information



from facebook_scraper import get_posts


for post in get_posts('Fireeye', pages=3):
    print(post)