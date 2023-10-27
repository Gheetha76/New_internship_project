from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


# FREE_SUBSCRIPTION = (By.XPATH, "// div[@class='get-free-period menu']")
FOUR_STEPS_CONNECT_COMPANY = (By.CSS_SELECTOR, '.step-text')

@given('Open the login page')
def open_login_page(context):
    context.app.login_page.login_pages()


@when('Login to the page')
def login_to_webpage(context):
    context.app.login_page.click_on_signin_link()
    sleep(2)
    context.app.login_page.input_email("gheethvijay123@gmail.com")
    sleep(4)
    context.app.login_page.input_password("QA123automation!")
    sleep(2)
    context.app.login_page.click_continue_button()


@then("Click on Get a free subscription")
def click_on_get_free_subscription(context):
    context.app.main_web_page.click_subscription()
    context.app.main_web_page.click_connect_the_company()

@then("Switch to the new tab")
def new_page_switch(context):
    context.app.free_subscription_page.open_new_page()


@then("Verify there are {n:d} steps to connect your company")
def verify_four_steps(context,n):
    steps_on_page = []
    for _ in range(n):
        if steps_on_page:
            steps_on_page.pop()
    assert not steps_on_page, f"Expected {n} steps, but found additional steps on the page."


@then("Verify Subscription plans button is clickable")
def Verify_subscription_plans_clickable(context):
    context.app.free_subscription_page.verify_subscription_plans_clickable()

