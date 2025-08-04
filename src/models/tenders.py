"""
Tender Data Transfer Objects
"""

from __future__ import annotations
import typing as tp

from pydantic import BaseModel


type TenderRow = tp.Tuple[
    tp.Optional[int],
    str,
    str,
    str,
    str,
    str,
    str,
    str,
]


class Tender(BaseModel):
    """
    Description:
    ---

    Tender data model with the following fields
    """

    id: tp.Optional[int]
    number: str
    link: str
    description: str
    end_date: str
    starting_price: str
    region: str

    @staticmethod
    def get_tender_from_row(row: TenderRow) -> Tender:
        """..."""
        return Tender(
            id=row[0],
            number=row[1],
            link=row[2],
            description=row[3],
            end_date=row[4],
            starting_price=row[5],
            region=row[6],
        )

    def get_tender_as_row(self) -> TenderRow:
        """..."""
        return (
            self.id,
            self.number,
            self.link,
            self.description,
            self.end_date,
            self.starting_price,
            self.region,
        )
