"""..."""

from database import db
from .tenders import TendersService
from .cli import CliService
from .scraper import ScraperService

tenders_service = TendersService(db=db)
scraper_service = ScraperService(tenders_service=tenders_service)
cli_service = CliService(
    tenders_service=tenders_service,
    scraper_service=scraper_service,
)
