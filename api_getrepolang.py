import json
import os
import requests as req

def get_language_from_repo(reponame: str):
    token = os.getenv("APP_GH_TOKEN")
    gh_username = os.getenv("APP_GH_USERNAME")

    url = 'https://api.github.com/repos/{username}/{reponame}/languages'.format(username=gh_username, reponame=reponame)
    headers = {
        "Authorization": 'token {ghtoken}'.format(ghtoken=token)
    }

    result = req.request(
        method="GET",
        url=url,
        headers=headers
    )
    parsedresult = json.loads(result.content)
    return parsedresult