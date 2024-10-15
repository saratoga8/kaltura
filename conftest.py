import os

from pytest_bdd import given

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager

from infra.page_objects.Page import Page


def _get_headed_driver() -> WebDriver:
    headless = bool(os.getenv('HEADLESS', False))
    service = ChromeService(ChromeDriverManager().install())
    return webdriver.Chrome(service=service, options=_get_chrome_opts() if headless else None)


def _get_chrome_opts() -> Options:
    options = webdriver.ChromeOptions()
    options.arguments.extend(["--headless=new", "--no-sandbox", "--disable-setuid-sandbox"])
    return options


def _get_driver() -> WebDriver:
    run_in_container = bool(os.getenv('IN_CONTAINER', False))
    return webdriver.Chrome(options=_get_chrome_opts()) if run_in_container else _get_headed_driver()


@pytest.fixture()
def chrome_browser() -> WebDriver:
    driver = _get_driver()
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
