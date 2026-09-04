import pytest
import allure
from src.enums.User import User
from config.config import PAGE_TIMEOUT


@allure.story("登录功能")
@pytest.mark.regression
def test_login_success(login_page):
    """正向：正常账号登录成功（使用枚举）"""
    login_page.goto_login()
    login_page.login(User.STANDARD_USER, "secret_sauce")
    # 登录成功后跳转inventory页面
    login_page.page.wait_for_url("**/inventory.html", timeout=PAGE_TIMEOUT)


# 参数化异常登录数据集：(用户名,密码,预期错误文案)
login_error_cases = [
    ("", "secret_sauce", "Username is required"),
    ("standard_user", "wrong_password", "Username and password do not match"),
]


@allure.story("登录功能")
@pytest.mark.regression
@pytest.mark.parametrize("username,password,expect_err_msg", login_error_cases)
def test_login_failed_param(login_page, username, password, expect_err_msg):
    """数据驱动：登录异常场景"""
    login_page.goto_login()
    login_page.login(username, password)
    error_msg = login_page.page.locator("[data-test='error']")
    error_msg.wait_for(state="visible", timeout=PAGE_TIMEOUT)
    assert expect_err_msg in error_msg.text_content()
