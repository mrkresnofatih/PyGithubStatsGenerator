# PyGithubStatsGenerator

Create Github Stats Generator using Python, Plotly, & Docker.

![my stats](https://github.com/mrkresnofatih/mrkresnofatih/blob/main/generated/pygithubstatsimg.png)

## How to use

1. Generate personal access token [here](https://github.com/settings/tokens).
2. Run:
```yaml
docker run --name pygithubstatsgenerator -e APP_GH_TOKEN=<personal_access_token> -e APP_TARGET_REPONAME=<target_public_repo_that_you_own> ghcr.io/mrkresnofatih/ghcr.io/mrkresnofatih/pyghstatsgenerator:v1.0.2
```
