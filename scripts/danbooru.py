import requests


# =========================
# DANBOORU SETTINGS
# =========================

TAG = "hirasawa_yui"

LIMIT = 100

API_URL = "https://danbooru.donmai.us/posts.json"



# =========================
# GET POSTS
# =========================

params = {
    "tags": TAG,
    "limit": LIMIT
}


response = requests.get(
    API_URL,
    params=params
)


posts = response.json()



# =========================
# CREATE README
# =========================

content = f"""

# 🎨 Danbooru Gallery

Tag:
`{TAG}`


Automatically updated using Danbooru API.


"""


for post in posts:


    image = post.get("file_url")


    if image:


        content += f"""

<img src="{image}" width="300">


"""



# =========================
# WRITE README
# =========================

with open(
    "README.md",
    "w",
    encoding="utf-8"
) as file:


    file.write(content)



print(
    f"Generated {len(posts)} images"
)
