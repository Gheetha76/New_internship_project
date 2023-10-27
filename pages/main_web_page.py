from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep

class MainWebPage(Page):

    MENU_BUTTON = (By.XPATH, '//div[text()="Menu"][@class="mobile-top-menu"]')
    GET_FREE_SUBSCRIPTION = (By.CSS_SELECTOR, '.get-free-period.menu')
    CONNECT_THE_COMPANY_BUTTON = (By.XPATH, '/html/body/div[3]/div[2]/a[1]/div')

    def open_main(self):
          self.driver.get('https://soft.reelly.io/sign-in')
          sleep(3)
          self.driver.refresh()


    def click_subscription(self):
          self.wait_for_element_clickable_click(*self.MENU_BUTTON)



    def store_original_window(self):
          return self.get_current_window()

    def click_connect_the_company(self):
        self.wait_for_element_clickable_click(*self.CONNECT_THE_COMPANY_BUTTON)