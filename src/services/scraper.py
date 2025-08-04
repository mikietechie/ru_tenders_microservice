"""..."""

import typing as tp
import time
import random

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.chrome.service import Service as ChromeWebDriverService

from models.tenders import Tender
from config import config
from utils.scrape_tenders import TenderRowParserUtility
from .tenders import TendersService


class ScraperService:
    """..."""

    driver: WebDriver

    def __init__(self, tenders_service: TendersService):
        self.tenders_service = tenders_service

    def scrape(self):
        """..."""
        driver = self.driver or webdriver.Chrome(
            service=ChromeWebDriverService(
                executable_path=config.chrome_driver,
            )
        )
        tenders: tp.List[Tender] = []
        driver.get(config.rostender_site)
        for page_num in range(25):
            time.sleep(random.random() * 5 + 5)
            for row_el in driver.find_elements(
                by=By.CSS_SELECTOR,
                value="article.tender-row",
            ):
                tender = TenderRowParserUtility(row_el=row_el).get_tender()
                tenders.append(tender)
            if page_num != 5:
                driver.find_element(
                    by=By.CSS_SELECTOR,
                    value=f'form#paginationForm a[attr="{page_num}"]',
                )
            else:
                driver.close()
        self.tenders_service.create_tenders(tenders=tenders)
