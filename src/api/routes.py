"""..."""

import typing as tp

from fastapi.routing import APIRouter

from models.tenders import Tender
from services import tenders_service


tenders_router = APIRouter(prefix="/tenders", tags=["Tenders"])


@tenders_router.get("/")
def read_tenders() -> tp.List[Tender]:
    """..."""
    return tenders_service.find_tenders(limit=100)


@tenders_router.get("/count")
def count_tenders() -> int:
    """..."""
    return tenders_service.count_tenders()
