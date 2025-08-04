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
)

__all__ = ["config"]
