from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from infra.page_elements.button import Button
from infra.page_elements.element import Element
from infra.page_elements.text_field import TextField


class Task:
    def __init__(self, root: WebElement, driver: WebDriver):
        self.__root = root
        self.__driver = driver

    @property
    def name(self) -> str:
        return TextField(self.__root, 'Name', 'label', By.TAG_NAME).get_text()

    def complete(self):
        Button(self.__driver, 'Complete', 'input[type="checkbox"]').click()

    @property
    def is_completed(self):
        return self.__root.get_attribute('class') == 'completed'

    def delete(self):
        button = Button(self.__root, 'X', 'button.destroy').get_web_element()
        ActionChains(self.__driver).move_to_element(self.__root).click(button).perform()

    def rename(self, name: str):
        label = Element(self.__root, 'Task Label', 'label', By.TAG_NAME).get_web_element()
        ActionChains(self.__driver).double_click(label).perform()
        txt_field = TextField(self.__root, 'Edit name', "edit-todo-input", By.ID)
        txt_field.get_web_element().send_keys(Keys.CONTROL, 'A')
        txt_field.type_in(name)
