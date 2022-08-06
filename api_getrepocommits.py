import json
import requests as req
import os

def get_commits_from_repo(reponame: str):
    token = os.getenv("APP_GH_TOKEN")
    gh_username = os.getenv("APP_GH_USERNAME")
    url = 'https://api.github.com/repos/{username}/{reponame}/commits'.format(username=gh_username, reponame=reponame)
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

def get_latest_commit_from_repo(reponame: str):
    commits = get_commits_from_repo(reponame=reponame)
    return commits[0]

def get_commit_tree(reponame: str, sha: str):
    token = os.getenv("APP_GH_TOKEN")
    gh_username = os.getenv("APP_GH_USERNAME")

    url = 'https://api.github.com/repos/{username}/{repo}/git/trees/{sha}?recursive=0'.format(username=gh_username, repo=reponame, sha=sha)
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