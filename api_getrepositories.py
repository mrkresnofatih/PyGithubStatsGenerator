import json
import os
import requests as req
import logging as lg

def get_repositories(page: int, pagesize: int):
    token = os.getenv("APP_GH_TOKEN")
    queryparams = '?sort=pushed&direction=desc&page={pageNumber}&per_page={per_page}'.format(pageNumber=page, per_page=pagesize)
    url = 'https://api.github.com/user/repos{queryparameters}'.format(queryparameters=queryparams)
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

def get_all_repositories():
    stop = False
    page = 0
    pageSize = 10
    results = []
    while stop == False:
        page += 1
        lg.info("Attempting get repositories page {pg}!".format(pg=page))
        repositories = get_repositories(page, pageSize)
        results.extend(repositories)
        if len(repositories) < pageSize:
            stop = True
    return results

