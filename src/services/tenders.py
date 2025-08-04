"""
...
"""

import typing as tp

from database.database import Database
from models.tenders import Tender


class TendersService:
    """..."""

    def __init__(self, db: Database):
        self.db = db

    def create_tenders(self, tenders: tp.List[Tender]) -> int:
        """..."""
        self.db.insert_tenders([t.get_tender_as_row()[1:] for t in tenders])
        self.db.commit()

    def find_tenders(self, limit: int, offset: int = 0) -> tp.List[Tender]:
        """..."""
        rows = self.db.select_tenders(limit=limit, offset=offset)
        return [Tender.get_tender_from_row(row=row) for row in rows]

    def count_tenders(self) -> int:
        """..."""
        return self.db.count_tenders()
