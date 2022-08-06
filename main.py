from api_getuser import get_user
from stats_getlangstats import get_languages_stats
from stats_getactivitystats import get_activity_stats
from stats_generateimage import generate_stats_image
from api_postfile import post_file
import logging

logging.basicConfig(
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S'
)

get_user()
langstats = get_languages_stats()
activitystats = get_activity_stats()
generate_stats_image(
    langstats=langstats, 
    activitystats=activitystats)

post_file(
    filepath='githubstatsimage.png',
    remotepath='generated/pygithubstatsimg.png'
)

logging.info("Completed!")