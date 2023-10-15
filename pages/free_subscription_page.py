from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep


class SubscriptionPage(Page):


    FOUR_STEPS_CONNECT_COMPANY = (By.CSS_SELECTOR, '.step-text')
    SUBSCRIPTION_PLANS = (By.CSS_SELECTOR, '.step-button.margin-bottom-8.w-button')


    def open_new_page(self):
        self.driver.get('https://soft.reelly.io/book-presentation')
        sleep(3)
        self.refresh()


    def open_new_window(self, window_id):
        self.switch_to_window(window_id)


    def get_text_list(self):
        self.get_text(*self.FOUR_STEPS_CONNECT_COMPANY)


    def verify_subscription_plans_clickable(self):
          self.click(*self.SUBSCRIPTION_PLANS)
          sleep(3)

