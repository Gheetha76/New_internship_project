# from pages.best_seller_page import Bestsellerpage
# from pages.blog import Blog
# from pages.not_found_page import NotFoundPage
# from pages.term_and_condition_page import TermAndConditionPage
# from pages.main_page import MainPage
# from pages.header import Header
# from pages.search_result_page import SearchResultPage
# from pages.sign_in_page import SignInPage
from pages.login_page import LoginPage
from pages.main_web_page import MainWebPage
from pages.free_subscription_page import SubscriptionPage


class Application:

    def __init__(self, driver: object) -> object:
        # self.best_seller_page = Bestsellerpage(driver)
        # self.blog = Blog(driver)
        # self.main_page = MainPage(driver)
        # self.not_found_page = NotFoundPage(driver)
        # self.term_and_condition_page = TermAndConditionPage(driver)
        # self.header = Header(driver)
        # self.search_result_page = SearchResultPage(driver)
        # self.sign_in_page = SignInPage(driver)
        self.login_page = LoginPage(driver)
        self.main_web_page = MainWebPage(driver)
        self.free_subscription_page = SubscriptionPage(driver)
