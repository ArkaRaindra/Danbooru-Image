import requests


TAG = "hirasawa_yui"

API = "https://danbooru.donmai.us/posts.json"


params = {
    "tags": TAG,
    "limit": 50
}


data = requests.get(API, params=params).json()


markdown = f"""
# Hirasawa Yui Gallery

Generated automatically from Danbooru.

"""


for post in data:

    url = post.get("file_url")

    if url:

        markdown += f"""
<img src="{url}" width="300">

"""


with open("README.md", "w", encoding="utf-8") as f:
    f.write(markdown)


print("README updated")
