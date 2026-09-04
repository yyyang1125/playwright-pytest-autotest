import allure
import pytest
import requests
from _pytest.fixtures import FixtureRequest, SubRequest
from _pytest.nodes import Item
from playwright.sync_api import Page, Playwright

from src.pages.login_page import LoginPage
from src.pages.swag_labs_page import SwagLabsPage
from src.pages.checkout_page import CheckoutPage


def get_public_ip() -> str:
    """Function to retrieve public IP address."""
    return requests.get(
        "http://checkip.amazonaws.com",
        timeout=40,
    ).text.rstrip()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item: Item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, f"rep_{rep.when}", rep)
    # 只处理call阶段（真正测试函数执行阶段失败）
    if rep.when == "call" and rep.failed:
        # 从用例获取page fixture对象
        page = None
        if "page" in item.fixturenames:
            page = item.funcargs["page"]
        if page:
            allure.attach(
                body=page.url,
                name="URL",
                attachment_type=allure.attachment_type.URI_LIST,
            )
            allure.attach(
                page.screenshot(full_page=True),
                name="Screen shot on failure",
                attachment_type=allure.attachment_type.PNG,
            )
        allure.attach(
            body=get_public_ip(),
            name="public ip address",
            attachment_type=allure.attachment_type.TEXT,
        )


@pytest.fixture(scope="function")
def login_page(page: Page) -> LoginPage:
    return LoginPage(page)


@pytest.fixture(scope="function")
def swag_labs_page(page: Page) -> SwagLabsPage:
    return SwagLabsPage(page)


@pytest.fixture(scope="function")
def checkout_page(page: Page) -> CheckoutPage:
    return CheckoutPage(page)

