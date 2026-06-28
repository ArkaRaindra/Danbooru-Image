import requests


# =========================
# DANBOORU SETTINGS
# =========================

TAG = "hirasawa_yui"

LIMIT = 100

API_URL = "https://danbooru.donmai.us/posts.json"



# =========================
# REQUEST
# =========================

headers = {
    "User-Agent": "github-actions-danbooru-gallery/1.0"
}


params = {
    "tags": TAG,
    "limit": LIMIT
}



response = requests.get(
    API_URL,
    params=params,
    headers=headers,
    timeout=30
)



# DEBUG

print("Status:", response.status_code)

print(
    "Response:",
    response.text[:300]
)



if response.status_code != 200:

    raise Exception(
        f"Danbooru error {response.status_code}"
    )



try:

    posts = response.json()


except Exception:

    raise Exception(
        "Response bukan JSON dari Danbooru"
    )



# =========================
# GENERATE README
# =========================


content = f"""
# 🎨 Danbooru Gallery

Tag:

`{TAG}`


Automatically updated.

"""


count = 0



for post in posts:


    image = post.get("file_url")


    if image:


        content += f"""

<img src="{image}" width="300">

"""


        count += 1



# =========================
# SAVE
# =========================


with open(
    "README.md",
    "w",
    encoding="utf-8"
) as f:

    f.write(content)



print(
    f"Generated {count} images"
)
