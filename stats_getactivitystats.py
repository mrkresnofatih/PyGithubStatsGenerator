from api_getrepositories import get_repositories
from api_getrepocommits import get_commits_from_repo
from dateutils import get_latest_date_strings_list
from dateutils import get_custom_date_string
import logging as lg

def get_activity_stats():
    activity_stats = {}
    latest_date_strings = get_latest_date_strings_list()
    for datestring in latest_date_strings:
        activity_stats[datestring] = 1

    repos = get_repositories(1, 30)
    lg.info("get30repos successful")
    for repo in repos:
        reponame = repo['name']
        lg.info("attempting get30commitsfromrepo {repo}".format(repo=reponame))
        repocommits = get_commits_from_repo(reponame)

        repolang = repo['language']
        if repolang == None:
            continue

        for commit in repocommits:
            committimestamp = commit['commit']['author']['date'].split("T")[0]
            commitdateindatestring = get_custom_date_string(committimestamp)

            if commitdateindatestring not in latest_date_strings:
                continue
            
            lg.info("commit recorded at {timestmp}".format(timestmp=commitdateindatestring))
            activity_stats[commitdateindatestring] += 1
    return activity_stats

