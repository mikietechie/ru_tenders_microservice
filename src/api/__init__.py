"""..."""

from fastapi import FastAPI

from config import config
from .routes import tenders_router

app = FastAPI(debug=config.debug)
app.include_router(router=tenders_router)

__all__ = ["app"]
