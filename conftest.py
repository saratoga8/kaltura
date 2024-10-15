import os

from pytest_bdd import given

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager

from infra.page_objects.Page import Page


def get_driver() -> WebDriver:
    run_in_container = bool(os.getenv('IN_CONTAINER', False))

    options = webdriver.ChromeOptions()
    options.arguments.extend(["--headless=new", "--no-sandbox", "--disable-setuid-sandbox"])

    if run_in_container:
        return webdriver.Chrome(options=options)
    else:
        return webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


@pytest.fixture()
def chrome_browser() -> WebDriver:
    driver = get_driver()
    driver.implicitly_wait(10)
    yield driver
    driver.save_screenshot('/tmp/error.png')
    driver.quit()


@given("user is at the tasks page", target_fixture="page")
def _(chrome_browser: WebDriver) -> Page:
    page = Page(chrome_browser)
    page.open()
    assert page.is_open(), "User is not on the page"
    return page
