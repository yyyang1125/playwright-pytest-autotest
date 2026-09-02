from playwright.sync_api import Page


class SwagLabsPage:
    def __init__(self, page: Page):
        self.page = page
        self.url = "https://www.saucedemo.com"
        self.username_input = page.locator("#user-name")
        self.password_input = page.locator("#password")
        self.login_btn = page.locator("#login-button")
        self.add_cart_btn = page.locator("[data-test='add-to-cart-sauce-labs-backpack']")
        self.shopping_cart_icon = page.locator(".shopping_cart_link")

    def goto(self):
        self.page.goto(self.url)

    def login(self, username: str, password: str):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_btn.click()

    def add_product_to_cart(self):
        self.add_cart_btn.click()

    def go_to_cart(self):
        self.shopping_cart_icon.click()
