import base64
import json
import requests as req
from api_getrepocommits import get_latest_commit_from_repo, get_commit_tree
import logging as lg
import os


def post_file(filepath: str, remotepath: str):
    lg.info("Starting upload process!")
    with open(filepath, "rb") as imgfile:
        b64offile = base64.b64encode(imgfile.read()).decode('utf-8')

        token = os.getenv("APP_GH_TOKEN")
        gh_username = os.getenv("APP_GH_USERNAME")
        reponame = os.getenv("APP_TARGET_REPONAME")

        filesha = ""
        try:
            latestcommit = get_latest_commit_from_repo(reponame=reponame)
            shaOfTreeLatestCommit = latestcommit['commit']['tree']['sha']

            gittree = get_commit_tree(
                reponame=reponame,
                sha=shaOfTreeLatestCommit
            )

            trees = gittree['tree']
            for node in trees:
                path = node['path']
                if path == remotepath:
                    filesha = node['sha']
                    lg.info('Path {path} exists, will perform update operation'.format(path=remotepath))
        except:
            pass

        url = 'https://api.github.com/repos/{user}/{repo}/contents/{path}'.format(user=gh_username, repo=reponame, path=remotepath)
        headers = {
            "Authorization": 'token {token}'.format(token=token),
            "Accept": "application/vnd.github.v3+json"
        }
        body = {
            "message": "post file {file}".format(file=remotepath),
            "content": b64offile,
            "sha": filesha
        }
        result = req.request(
            method="PUT",
            headers=headers,
            data=json.dumps(body),
            url=url
        )
        parsedresult = json.loads(result.content)
        lg.info("Uploaded! Sha: {newSha}".format(newSha=parsedresult['commit']['sha']))
