"""..."""

import typing as tp

import pandas as pd

from utils.constants import TENDER_ROW_COLUMNS
from .tenders import TendersService
from .scraper import ScraperService


class CliService:
    """..."""

    def __init__(
        self,
        tenders_service: TendersService,
        scraper_service: ScraperService,
    ):
        """..."""
        self.tenders_service = tenders_service
        self.scraper_service = scraper_service

    def handle(self, args: tp.List[str]):
        """..."""
        args_num = len(args)
        arg0 = args[0]
        if arg0 == "scrape":
            self.handle_scrape()
            return
        if arg0 == "--max":
            assert args_num >= 2
            limit = int(args[1])
            csv_file: str | None = None
            if args_num == 4:
                csv_file = args[3]
            self.handle_query(
                limit=limit,
                csv_file=csv_file,
            )
            return
        print("Command not found")

    def handle_scrape(self):
        """..."""
        self.scraper_service.scrape()

    def handle_query(
        self,
        limit: int,
        csv_file: str | None = None,
    ):
        """..."""
        tenders = self.tenders_service.find_tenders(limit)
        df = pd.DataFrame(
            [t.get_tender_as_row() for t in tenders],
            columns=TENDER_ROW_COLUMNS,
        )
        if csv_file:
            df.to_csv(csv_file)
        else:
            print(df)
