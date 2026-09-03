import pytest
from src.pages.login_page import LoginPage
from src.pages.swag_labs_page import SwagLabsPage
from src.pages.checkout_page import CheckoutPage

@pytest.mark.smoke
@pytest.mark.regression
def test_complete_checkout_flow(page):
    """完整业务流程：登录-加购商品-结算下单"""
    login_page = LoginPage(page)
    swag_page = SwagLabsPage(page)
    checkout_page = CheckoutPage(page)

    # 1登录
    login_page.goto_login()
    login_page.login("standard_user", "secret_sauce")

    #2 添加商品到购物车
    swag_page.add_item_to_cart("Sauce Labs Backpack")
    #3 跳转购物车
    swag_page.go_to_cart()
    #4 进入结算
    swag_page.checkout_btn.click()
    #5 填写收件信息
    checkout_page.fill_checkout_info("Yang","Yue","210000")
    #6 提交订单
    checkout_page.finish_order()
    #7 断言下单成功
    success_text = checkout_page.get_order_success_text()
    assert success_text == "Thank you for your order!"
