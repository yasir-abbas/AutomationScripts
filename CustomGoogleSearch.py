#This is custom google search api. Give input parameter in query parameter


import requests

# get the API KEY here: https://developers.google.com/custom-search/v1/overview
API_KEY = "AIzaSyBzFGvA5mXIIbMNps5dw5croIiCmJzQvd4"

# get your Search Engine ID on your CSE control panel
SEARCH_ENGINE_ID = "91a91d003fcca445a"

# the search query you want
query = "Ashar Aziz"
# using the first page
page = 1
# constructing the URL
# doc: https://developers.google.com/custom-search/v1/using_rest
# calculating start, (page=2) => (start=11), (page=3) => (start=21)
start = (page - 1) * 10 + 1
url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}&start={start}"

# make the API request
data = requests.get(url).json()

# get the result items
search_items = data.get("items")
# iterate over 10 results found


print(search_items)


