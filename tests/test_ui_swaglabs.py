import pytest
from src.pages.swag_labs_page import SwagLabsPage


login_data = [
    ("standard_user", "secret_sauce", True),   #正常账号密码，预期成功
    ("wrong_user", "secret_sauce", False),    #错误用户名，预期失败
    ("", "", False)                           #空账号空密码，预期失败
]


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.parametrize("username,password,expect_success", login_data)
def test_login_param(page, username, password, expect_success):
    """登录场景数据驱动测试"""
    page.goto("https://www.saucedemo.com/")
    page.locator("#user-name").fill(username)
    page.locator("#password").fill(password)
    page.locator("#login-button").click()

    if expect_success:
        assert "/inventory.html" in page.url
    else:
        assert page.locator("[data-test='error']").is_visible()


@pytest.mark.regression
def test_add_goods_to_cart(page):
    """登录之后把商品加入购物车"""
    page_obj = SwagLabsPage(page)
    page_obj.goto()
    page_obj.login("standard_user", "secret_sauce")
    page_obj.add_product_to_cart()
    page_obj.go_to_cart()
    assert "cart" in page.url
