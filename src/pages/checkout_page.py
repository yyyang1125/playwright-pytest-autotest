from playwright.sync_api import Page

class CheckoutPage:
    def __init__(self, page: Page):
        self.page = page
        # 结算第一步：填写用户信息
        self.first_name_input = page.locator("[data-test='firstName']")
        self.last_name_input = page.locator("[data-test='lastName']")
        self.postal_code_input = page.locator("[data-test='postalCode']")
        self.continue_btn = page.locator("[data-test='continue']")

        # 第二步：订单概览，完成订单
        self.finish_btn = page.locator("[data-test='finish']")
        self.order_complete_title = page.locator("[data-test='complete-header']")

    def fill_checkout_info(self, first_name: str, last_name: str, postal_code: str):
        """填写结算收件人信息"""
        self.first_name_input.wait_for(state="visible", timeout=8000)
        self.first_name_input.fill(first_name)
        self.last_name_input.fill(last_name)
        self.postal_code_input.fill(postal_code)
        self.continue_btn.click()

    def finish_order(self):
        """确认提交订单"""
        self.finish_btn.wait_for(state="visible", timeout=8000)
        self.finish_btn.click()

    def get_order_success_text(self) -> str:
        """获取订单成功标题文本"""
        self.order_complete_title.wait_for(state="visible", timeout=8000)
        return self.order_complete_title.text_content()
