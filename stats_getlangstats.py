from api_getrepositories import get_all_repositories
from api_getrepolang import get_language_from_repo
import logging as lg

def get_languages_stats():
    languages_stats = {}
    lg.info("attempting getallrepos!")
    repos = get_all_repositories()
    alllangsize = 0
    for repo in repos:
        reponame = repo['name']
        repolangs = get_language_from_repo(reponame=reponame)
        lg.info("getlanguagefromrepo {reponame}".format(reponame=reponame))

        for repolang in repolangs:
            if repolang == None:
                continue
            
            lg.info("repo found language: {lang}".format(lang=repolang))
            if repolang in languages_stats:
                languages_stats[repolang] += repolangs[repolang]
            else:
                languages_stats[repolang] = repolangs[repolang]
            alllangsize += repolangs[repolang]
    
    langnames = list(languages_stats.keys())
    langsizes = list(languages_stats.values())

    lg.info("ordering by size")
    for _ in range(0, len(langnames)):
        for j in range(0, len(langnames)-1):
            if langsizes[j] < langsizes[j+1]:
                temp = langsizes[j+1]
                langsizes[j+1] = langsizes[j]
                langsizes[j] = temp

                tempname = langnames[j+1]
                langnames[j+1] = langnames[j]
                langnames[j] = tempname
    
    result = {}
    remaininglangsize = alllangsize
    for i in range(0, 8):
        result[langnames[i]] = langsizes[i]
        remaininglangsize -= langsizes[i]
    result['Other'] = remaininglangsize
    lg.info(result['Other'])
    return result
