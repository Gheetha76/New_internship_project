from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep

class MainWebPage(Page):


    GET_FREE_SUBSCRIPTION = (By.CSS_SELECTOR, '.get-free-period.menu')

    def open_main(self):
          self.driver.get('https://soft.reelly.io/sign-in')
          sleep(3)
          self.driver.refresh()


    def click_subscription(self):
          self.wait_for_element_clickable_click(*self.GET_FREE_SUBSCRIPTION)
          sleep(3)


    def store_original_window(self):
          return self.get_current_window()