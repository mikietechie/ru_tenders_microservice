"""..."""

import contextlib
import typing as tp
import time
import random

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException

# from selenium.webdriver.chrome.service import Service

from models.tenders import Tender
from config import config
from utils.scrape_tenders import TenderRowParserUtility
from .tenders import TendersService


class ScraperService:
    """..."""

    def __init__(self, tenders_service: TendersService):
        self.tenders_service = tenders_service
        self.driver: WebDriver | None = None

    def scrape(self):
        """..."""
        # driver = self.driver or webdriver.Chrome(
        #     service=Service(
        #         executable_path=config.chrome_driver,
        #     )
        # )
        pages_count = config.tenders_count // config.tenders_per_page
        driver = webdriver.Remote(
            command_executor=config.chrome_driver,
            options=webdriver.ChromeOptions(),
        )
        tenders: tp.List[Tender] = []
        driver.get(config.rostender_site)
        for page_num in range(2, pages_count):
            time.sleep(random.random() * 5 + 5)
            print(driver.current_url)
            for row_el in driver.find_elements(
                by=By.CSS_SELECTOR,
                value="article.tender-row",
            ):
                with contextlib.suppress(NoSuchElementException):
                    tender = TenderRowParserUtility(row_el=row_el).get_tender()
                    print(tender)
                    tenders.append(tender)
            if page_num != pages_count:
                driver.find_element(
                    by=By.CSS_SELECTOR,
                    value=f'#paginationForm a[href="/extsearch?page={page_num}"]',
                )
            else:
                driver.close()
        self.tenders_service.create_tenders(tenders=tenders)
