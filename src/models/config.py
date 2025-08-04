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
    chrome_driver: str
