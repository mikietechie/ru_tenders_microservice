""" """

from pydantic import BaseModel


class Config(BaseModel):
    """
    Description:
    ---

    System Config Object
    """

    database: str
    host: str
    port: int
    debug: bool
    rostender_site: str
    tenders_per_page: int
    tenders_count: int
    chrome_driver: str
