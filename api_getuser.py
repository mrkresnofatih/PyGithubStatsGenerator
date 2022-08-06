import json
import requests as req
import logging as lg
import os

def get_user():
    token = os.getenv("APP_GH_TOKEN")
    result = req.request(
        method="GET", 
        url="https://api.github.com/user",
        headers={
            "Authorization": 'token {ghtoken}'.format(ghtoken=token)
        })
    parsedresult = json.loads(result.content)
    loginusername = parsedresult['login']
    os.environ["APP_GH_USERNAME"] = loginusername
    lg.info("Logged in as {user}".format(user=loginusername))