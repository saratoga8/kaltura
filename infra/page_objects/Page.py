from enum import Enum

from pytest_selenium import driver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver

from infra.page_elements.task import Task


class Filters(Enum):
    COMPLETED = 1
    ACTIVE = 2
    ALL = 3


class Page:
    url = 'https://todomvc.com/examples/vue/dist'
    name = 'Todos page'
    title = 'TodoMVC: Vue'

    def __init__(self, driver: WebDriver):
        self._tasks = []
        self._driver = driver

    @property
    def count_txt(self) -> str:
        return self._driver.find_element(By.CSS_SELECTOR, 'span.todo-count').text

    @property
    def tasks(self) -> list[Task]:
        elements = self._driver.find_elements(By.CSS_SELECTOR, 'ul.todo-list li')
        return list(map(lambda element: Task(element, self._driver), elements))

    def open(self):
        self._driver.get(Page.url)

    def is_open(self) -> bool:
        return self._driver.title == Page.title

    def add_task(self, name: str):
        element = self._driver.find_element(By.CSS_SELECTOR, 'input.new-todo')
        element.send_keys(name)
        element.send_keys(Keys.ENTER)

    def clear_completed(self):
        element = self._driver.find_element(By.CSS_SELECTOR, 'button.clear-completed')
        element.click()

    def filter_by(self, filter_name: str):
        buttons = ('ALL', 'ACTIVE', 'COMPLETED')
        if filter_name in buttons:
            ind = buttons.index(filter_name)
            button = self._driver.find_elements(By.CSS_SELECTOR, 'ul.filters li a')[ind]
            button.click()
        else:
            assert False, f"Unknown filter button {filter_name}"
