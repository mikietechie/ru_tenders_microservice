"""..."""

from models.config import Config
from . import env


config = Config(
    database=env.DATABASE,
    host=env.HOST,
    port=env.PORT,
    debug=env.DEBUG,
    rostender_site=env.ROSTENDER_SITE,
    chrome_driver=env.CHROME_DRIVER,
    tenders_per_page=env.ROSTENDERS_PER_PAGE,
    tenders_count=env.TENDERS_COUNT,
)

__all__ = ["config"]
