"""..."""

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from models.tenders import Tender


class TenderRowParserUtility:
    """
    Tender Row Parser

    Description
    ---
    A utility class for passing a tender row element
    """

    def __init__(self, row_el: WebElement):
        self.row_el = row_el

    def get_tender(self) -> Tender:
        """..."""
        return Tender(
            id=None,
            number=self.get_tender_number(),
            description=self.get_tender_description(),
            link=self.get_tender_link(),
            end_date=self.get_tender_end_date(),
            starting_price=self.get_tender_starting_price(),
            region=self.get_tender_region(),
        )

    def get_tender_number(self) -> str:
        """..."""
        text_el = self.row_el.find_element(
            by=By.CSS_SELECTOR,
            value="span.tender__number",
        )
        text = text_el.text.strip().split(" ")[-1]
        return text

    def get_tender_description(self) -> str:
        """..."""
        text_el = self.row_el.find_element(
            by=By.CSS_SELECTOR,
            value="a.description.tender-info__description.tender-info__link",
        )
        text = text_el.text.strip()
        return text

    def get_tender_link(self) -> str:
        """..."""
        text_el = self.row_el.find_element(
            by=By.CSS_SELECTOR,
            value="a.description.tender-info__description.tender-info__link",
        )
        text = text_el.get_attribute("href")
        return text

    def get_tender_end_date(self) -> str:
        """..."""
        text_el = self.row_el.find_element(
            by=By.CSS_SELECTOR,
            value="div.tender-date-info.tender-date-end.tender__date-end .tender__countdown-text",
        )
        text = text_el.get_attribute("innerText").strip()
        return text

    def get_tender_region(self) -> str:
        """..."""
        text_el = self.row_el.find_element(
            by=By.CSS_SELECTOR,
            value="a.tender__region-link",
        )
        text = text_el.text.strip()
        return text

    def get_tender_starting_price(self) -> str:
        """..."""
        text_el = self.row_el.find_element(
            by=By.CSS_SELECTOR,
            value="div.starting-price__price.starting-price--price",
        )
        text = text_el.text.strip()
        return text
