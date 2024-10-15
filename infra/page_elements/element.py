from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


class Element:
    def __init__(self, root: WebDriver | WebElement, name: str, locator: str, locator_type=By.CSS_SELECTOR):
        self.name = name
        try:
            self._element = root.find_element(locator_type, locator)
        except NoSuchElementException:
            assert False, f"The element '{self.name}' with the locator {locator} not found"

    def get_web_element(self) -> WebElement:
        return self._element
