from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


class Task:
    def __init__(self, root: WebElement, driver: WebDriver):
        self._root = root
        self._driver = driver

    @property
    def name(self) -> str:
        return self._root.find_element(By.TAG_NAME, 'label').text

    def complete(self):
        element = self._root.find_element(By.CSS_SELECTOR, 'input[type="checkbox"]')
        element.click()

    @property
    def is_completed(self):
        return self._root.get_attribute('class') == 'completed'

    def delete(self):
        element = self._root.find_element(By.CSS_SELECTOR, 'button.destroy')
        ActionChains(self._driver).move_to_element(self._root).click(element).perform()

    def rename(self, name: str):
        label = self._root.find_element(By.TAG_NAME, 'label')
        ActionChains(self._driver).double_click(label).perform()
        element = self._root.find_element(By.ID, "edit-todo-input")
        element.send_keys(Keys.CONTROL, 'A')
        element.send_keys(name)
        element.send_keys(Keys.ENTER)
