import pytest
from src.pages.swag_labs_page import SwagLabsPage


def test_swaglabs_login(page):
    """测试正常登录swaglabs"""
    page_obj = SwagLabsPage(page)
    page_obj.goto()
    page_obj.login("standard_user", "secret_sauce")
    # 断言登录成功后页面url变化
    assert "inventory" in page.url


def test_add_goods_to_cart(page):
    """登录之后把商品加入购物车"""
    page_obj = SwagLabsPage(page)
    page_obj.goto()
    page_obj.login("standard_user", "secret_sauce")
    page_obj.add_product_to_cart()
    page_obj.go_to_cart()
    assert "cart" in page.url
