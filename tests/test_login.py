import pytest
import allure


@allure.story("登录功能")
@pytest.mark.regression
def test_login_success(login_page):
    """正向：正常账号登录成功"""
    login_page.goto_login()
    login_page.login("standard_user", "secret_sauce")
    # 登录成功后跳转inventory页面
    login_page.page.wait_for_url("**/inventory.html", timeout=8000)


@allure.story("登录功能")
@pytest.mark.regression
def test_login_wrong_password(login_page):
    """反向：密码错误，校验错误提示"""
    login_page.goto_login()
    login_page.login("standard_user", "wrong_password")
    # 获取错误提示元素
    error_msg = login_page.page.locator("[data-test='error']")
    error_msg.wait_for(state="visible", timeout=8000)
    assert "Username and password do not match" in error_msg.text_content()


@allure.story("登录功能")
@pytest.mark.regression
def test_login_empty_username(login_page):
    """反向：用户名为空，校验错误提示"""
    login_page.goto_login()
    login_page.login("", "secret_sauce")
    error_msg = login_page.page.locator("[data-test='error']")
    error_msg.wait_for(state="visible", timeout=8000)
    assert "Username is required" in error_msg.text_content()
