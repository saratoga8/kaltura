from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from infra.page_elements.element import Element


class Button(Element):
    def __init__(self, root: WebDriver | WebElement, name: str, locator: str, locator_type=By.CSS_SELECTOR):
        super().__init__(root, name, locator, locator_type)

    def click(self):
        self._element.click()
