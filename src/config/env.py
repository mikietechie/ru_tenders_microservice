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
ROSTENDERS_PER_PAGE: int = int(config.get("ROSTENDERS_PER_PAGE", "20"))
TENDERS_COUNT: int = int(config.get("TENDERS_COUNT", "100"))
CHROME_DRIVER: str = config.get(
    "SELENIUM_CHROME_URI",
    "http://localhost:4444",
)
