import requests


# =========================
# DANBOORU SETTINGS
# =========================

TAG = "hirasawa_yui nude"

LIMIT = 50

API_URL = "https://danbooru.donmai.us/posts.json"



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



if response.status_code != 200:
    raise Exception(
        f"Danbooru error {response.status_code}"
    )



posts = response.json()



# =========================
# README CONTENT
# =========================

content = f"""
# 🎨 Danbooru Gallery

Tag:
`{TAG}`


<div align="center">

<div style="display:flex; flex-wrap:wrap; gap:10px;">

"""


count = 0



for post in posts:


    image = post.get("file_url")


    if image:


        content += f"""
<img src="{image}" width="250">

"""


        count += 1



content += """

</div>

</div>

"""



# =========================
# SAVE README
# =========================

with open(
    "README.md",
    "w",
    encoding="utf-8"
) as file:

    file.write(content)



print(
    f"Generated {count} images"
)
