from playwright.sync_api import Page
from config.config import BASE_URL, PAGE_TIMEOUT


class SwagLabsPage:
    def __init__(self, page: Page):
        self.page = page
        self.url = BASE_URL
        self.username_input = page.locator("#user-name")
        self.password_input = page.locator("#password")
        self.login_btn = page.locator("#login-button")
        self.add_cart_btn = page.locator("[data-test='add-to-cart-sauce-labs-backpack']")
        self.shopping_cart_icon = page.locator(".shopping_cart_link")
        # 购物车页面-结算按钮
        self.checkout_btn = page.locator("[data-test='checkout']")

    def goto(self):
        self.page.goto(self.url)

    def login(self, username: str, password: str):
        self.username_input.wait_for(state="visible",timeout=PAGE_TIMEOUT)
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_btn.click()

    def add_product_to_cart(self):
        """固定添加 Sauce Labs Backpack"""
        self.add_cart_btn.wait_for(state="visible", timeout=PAGE_TIMEOUT)
        self.add_cart_btn.click()

    def add_item_to_cart(self, item_name: str):
        """根据商品名称动态添加商品到购物车，供新结算流程用例调用"""
        item_card = self.page.locator(".inventory_item").filter(has_text=item_name)
        add_btn = item_card.locator("[data-test*='add-to-cart']")
        add_btn.wait_for(state="visible", timeout=PAGE_TIMEOUT)
        add_btn.click()

    def go_to_cart(self):
        """跳转到购物车页面"""
        self.shopping_cart_icon.wait_for(state="visible", timeout=PAGE_TIMEOUT)
        self.shopping_cart_icon.click()

    def remove_item_from_cart(self, item_name: str):
        """根据商品名称移除购物车商品"""
        item_card = self.page.locator(".cart_item").filter(has_text=item_name)
        remove_btn = item_card.locator("[data-test*='remove']")
        remove_btn.wait_for(state="visible", timeout=PAGE_TIMEOUT)
        remove_btn.click()
