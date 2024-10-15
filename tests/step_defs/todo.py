from pytest_bdd import when, then, scenarios, parsers
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

from infra.page_elements.task import Task
from infra.page_objects.Page import Page

scenarios("todo-tasks.feature")


class _TasksNumber(object):
    def __init__(self, number: int):
        self._awaited_num = number

    def __call__(self, driver: WebDriver):
        tasks = Page(driver).tasks
        return len(tasks) == self._awaited_num


@when("user adds a task", target_fixture="name")
def _(page: Page) -> str:
    name = 'Bla'
    page.add_task(name)
    return name


@then("there is a single task")
def _(name: str, chrome_browser: WebDriver):
    wait = WebDriverWait(chrome_browser, 2)
    wait.until(_TasksNumber(1), "There are unexpected tasks")

    page = Page(chrome_browser)
    actual_name = page.tasks[0].name

    assert actual_name == name, "Invalid name of the added task"
    assert page.count_txt == '1 item left', 'Invalid tasks counting'


@when("user adds multiple tasks", target_fixture="names")
def _(page: Page) -> tuple[str, str]:
    names = ('Bla1', 'Bla2')
    [page.add_task(name) for name in names]
    return names


@then("there is a list of tasks")
def _(names: tuple[str, str], chrome_browser: WebDriver):
    page = Page(chrome_browser)
    actual_names = tuple(map(lambda task: task.name, page.tasks))
    assert names == actual_names, "Invalid names of the the added tasks"
    assert page.count_txt == f"{len(actual_names)} items left", 'Invalid tasks counting'


@when("user completes the task", target_fixture="name")
def _(name: str, chrome_browser: WebDriver) -> str:
    page = Page(chrome_browser)
    page.tasks[0].complete()
    return name


@then(parsers.parse("there the completed task"))
def _(name: str, chrome_browser: WebDriver):
    page = Page(chrome_browser)
    assert page.tasks[0].is_completed, f"There is no a completed task"


@when("user deletes the task")
def _(chrome_browser: WebDriver):
    page = Page(chrome_browser)
    page.tasks[0].delete()


@then("there is no tasks")
def _(chrome_browser: WebDriver):
    wait = WebDriverWait(chrome_browser, 2)
    wait.until(_TasksNumber(0), "The task not deleted")


@when(parsers.parse('user adds a task "{name}"'), target_fixture="name")
def _(chrome_browser: WebDriver, name: str):
    page = Page(chrome_browser)
    page.add_task(name)
    return name


@when(parsers.parse('user renames the task to "{new_name}"'))
def _(chrome_browser: WebDriver, new_name: str):
    page = Page(chrome_browser)
    page.tasks[0].rename(new_name)


@then(parsers.parse('there is the task "{name}"'))
def _(chrome_browser: WebDriver, name: str):
    page = Page(chrome_browser)
    assert page.tasks[0].name == name, "The task is not renamed"


@when(parsers.parse('user completes the task "{name}"'))
def _(chrome_browser: WebDriver, name: str):
    page = Page(chrome_browser)
    found: list[Task] = list(filter(lambda task: task.name == name, page.tasks))
    assert found, "There are no tasks"
    assert len(found) == 1, f"There are more than one task with the name {name}"
    found.pop().complete()


@when("user clears all completed tasks")
def _(chrome_browser: WebDriver):
    page = Page(chrome_browser)
    page.clear_completed()


@then("there is no completed tasks")
def _(chrome_browser: WebDriver):
    page = Page(chrome_browser)
    found: list[Task] = list(filter(lambda task: task.is_completed, page.tasks))
    assert len(found) == 0, "There are still completed tasks"


@when(parsers.parse("user filters {filter_name} tasks"))
def _(filter_name: str, chrome_browser: WebDriver):
    page = Page(chrome_browser)
    page.filter_by(filter_name)


@then(parsers.parse("there is the tasks:{tasks}"))
def _(tasks: str, chrome_browser: WebDriver):
    page = Page(chrome_browser)
    expected_tasks = tasks.replace(' ', '').split(',')
    actual_tasks = list(map(lambda task: task.name, page.tasks))
    assert expected_tasks == actual_tasks, 'Invalid list of tasks'

