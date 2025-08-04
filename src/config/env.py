"""..."""

import os

from dotenv import dotenv_values

config = {
    **dotenv_values(".env"),
    **dotenv_values("../.env"),
    **os.environ,
}


DATABASE: str = config.get("DATABASE", "db.sqlite3")
HOST: str = config.get("HOST", "0.0.0.0")
PORT: int = int(config.get("PORT", "8000"))
DEBUG: bool = config.get("DEBUG", "0") == "1"
ROSTENDER_SITE: str = config.get(
    "ROSTENDER_SITE",
    "https://rostender.info/extsearch?page=1",
)
CHROME_DRIVER: str = config.get(
    "CHROME_DRIVER",
    "../chromedriver",
)
