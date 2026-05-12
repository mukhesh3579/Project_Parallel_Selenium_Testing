#code behind file

from pytest_bdd import scenarios, given, when, then, parsers

from pages.login_page import LoginPage
from openpyxl import load_workbook
import time
scenarios("../features/login.feature")

@given("user launches saucedemo site")
def launch_site(driver):
    page = LoginPage(driver)
    page.open()

@when(parsers.parse('user enters username "{username}"'))
def enter_username(driver, username):
    page = LoginPage(driver)
    wb=load_workbook("sample.xlsx")
    sheet=wb.active

    username=sheet["a2"].value
    page.enter_username(username)

@when(parsers.parse('user enters password "{password}"'))
def enter_password(driver, password):
    page = LoginPage(driver)
    page.enter_password(password)

@when("user clicks login button")
def click_login(driver):
    page = LoginPage(driver)
    time.sleep(15)
    page.click_login()

@then("user should see products page")
def verify_products_page(driver):
    page = LoginPage(driver)
    time.sleep(15)
    assert "inventory" in driver.current_url