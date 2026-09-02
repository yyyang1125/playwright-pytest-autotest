import allure
import pytest
import requests
from _pytest.fixtures import FixtureRequest, SubRequest
from _pytest.nodes import Item
# from axe_playwright_python.sync_playwright import Axe
from playwright.sync_api import Page, Playwright
# ========== 注释axe相关导入，不再使用axe无障碍审计 ==========
# from src.utilities.axe_helper import AxeHelper
# from src.utilities.constants import Constants


# ========== 【重要】注释掉原业务自动跳转fixture，我们自己测试脚本里手动写page.goto ==========
# @pytest.fixture(scope="function", autouse=True)
# def goto(page: Page, request: SubRequest):
#     """Fixture to navigate to the base URL based on the user.
#     If the 'storage_state' is set in 'browser_context_args', it navigates to the inventory page,
#     otherwise, it navigates to the login page.
#     Args:
#         page (Page): Playwright page object.
#         request (SubRequest): Pytest request object to get the 'browser_context_args' fixture value.
#             If 'browser_context_args' is set to a user parameter (e.g., 'standard_user'),
#             the navigation is determined based on the user.
#     Example:
#         @pytest.mark.parametrize('browser_context_args', ["standard_user"], indirect=True)
#     """
#     if request.getfixturevalue("browser_context_args").get("storage_state"):
#         page.goto("/inventory.html")
#     else:
#         page.goto("")


# ========== axe_playwright fixture 整个注释，不再使用 ==========
# @pytest.fixture(scope="session")
# def axe_playwright():
#     """Fixture to provide an instance of AxeHelper with Axe initialized.
#     This fixture has a session scope, meaning it will be created once per test session
#     and shared across all tests.
#     Returns:
#         AxeHelper: An instance of AxeHelper with Axe initialized.
#     """
#     return AxeHelper(Axe())


@pytest.fixture(scope="function")
def browser_context_args(browser_context_args: dict) -> dict:
    """This fixture allows setting browser context arguments for Playwright."""
    context_args = {
        **browser_context_args,
        "no_viewport": True,
        # "user_agent": Constants.AUTOMATION_USER_AGENT, # 依赖Constants，注释
        "permissions": ["geolocation", "microphone", "camera", "clipboard-read", "clipboard-write"],
    }
    return context_args


@pytest.fixture(scope="session")
def browser_type_launch_args(browser_type_launch_args: dict, playwright: Playwright) -> dict:
    """Fixture to set browser launch arguments."""
    playwright.selectors.set_test_id_attribute("data-test")
    return {
        **browser_type_launch_args,
        "headless": False,
        "args": [
            "--start-maximized",
            "--allow-file-access-from-files",
            "--use-fake-device-for-media-stream",
            "--use-fake-ui-for-media-stream",
            "--hide-scrollbars",
            "--disable-features=IsolateOrigins,site-per-process,VizDisplayCompositor,SidePanelPinning,OptimizationGuideModelDownloading,OptimizationHintsFetching,OptimizationTargetPrediction,OptimizationHints",
            "--disable-popup-blocking",
            "--disable-search-engine-choice-screen",
            "--disable-infobars",
            "--disable-dev-shm-usage",
            "--disable-notifications",
            "--disable-blink-features=AutomationControlled",
        ],
    }


def get_public_ip() -> str:
    """Function to retrieve public IP address."""
    return requests.get(
        "http://checkip.amazonaws.com",
        timeout=40,
    ).text.rstrip()


@pytest.fixture(autouse=True)
def attach_playwright_results(page: Page, request: FixtureRequest):
    """Fixture to perform teardown actions and attach results to Allure report
    on failure.
    Args:
        page (Page): Playwright page object.
        request: Pytest request object.
    """
    yield
    if request.node.rep_call.failed:
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


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item: Item):
    """Hook implementation to generate test report for each test phase."""
    outcome = yield
    rep = outcome.get_result()
    setattr(item, f"rep_{rep.when}", rep)
