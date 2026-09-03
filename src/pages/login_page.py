from typing import Union
import allure
from playwright.sync_api import Page
from src.enums.User import User

@allure.severity(allure.severity_level.CRITICAL)
@allure.story("Login page behavior")
class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        # sauce demo 使用 data‑test，不是标准 data‑testid，不能用 get_by_test_id
        self.user_name_field = page.locator("[data-test='username']")
        self.password_field = page.locator("[data-test='password']")
        self.login_button = page.locator("[data-test='login-button']")
        self.error_message = page.locator("[data-test='error']")

    @allure.step("Navigate to login page")
    def goto_login(self):
        """跳转到登录页面"""
        self.page.goto("https://www.saucedemo.com/", timeout=15000)
        self.page.wait_for_load_state("networkidle")
        print(f"DEBUG 当前页面url: {self.page.url}")

    @allure.step("Login with username {username} and password {password}")
    def login(self, username: Union[User, str], password: str):
        self.user_name_field.wait_for(state="visible", timeout=8000)
        if hasattr(username, "value"):
            self.user_name_field.fill(username.value)
        else:
            self.user_name_field.fill(username)
        self.password_field.fill(password)
        self.login_button.click()
