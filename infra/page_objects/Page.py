from pytest_selenium import driver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver

from infra.page_elements.button import Button
from infra.page_elements.task import Task
from infra.page_elements.text_field import TextField


class Page:
    url = 'https://todomvc.com/examples/vue/dist'
    name = 'Todos page'
    title = 'TodoMVC: Vue'

    def __init__(self, driver: WebDriver):
        self.__tasks = []
        self.__driver = driver

    @property
    def count_txt(self) -> str:
        return TextField(self.__driver, 'Count label', 'span.todo-count').get_text()

    @property
    def tasks(self) -> list[Task]:
        elements = self.__driver.find_elements(By.CSS_SELECTOR, 'ul.todo-list li')
        return list(map(lambda element: Task(element, self.__driver), elements))

    def open(self):
        self.__driver.get(Page.url)

    def is_open(self) -> bool:
        return self.__driver.title == Page.title

    def add_task(self, name: str):
        TextField(self.__driver, 'Adding task', 'input.new-todo').type_in(name)

    def clear_completed(self):
        Button(self.__driver, 'Clear completed', 'button.clear-completed').click()

    def filter_by(self, filter_name: str):
        buttons = ('ALL', 'ACTIVE', 'COMPLETED')
        if filter_name in buttons:
            ind = buttons.index(filter_name)
            button = self.__driver.find_elements(By.CSS_SELECTOR, 'ul.filters li a')[ind]
            button.click()
        else:
            assert False, f"Unknown filter button {filter_name}"
