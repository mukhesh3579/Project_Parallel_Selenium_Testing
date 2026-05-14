from pytest_bdd import scenarios, given, when, then, parsers

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

scenarios("../features/download.feature")

@given("user launches browser")
def launch_browser(driver):
    driver.maximize_window()
    driver.get("https://practice-automation.com/iframes/")

@when("user switches to selenium iframe")
def switch_iframe(driver):
    iframe = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "iframe-2")))
                                     
    #dynamic wait
    driver.switch_to.frame(iframe)

@when("user clicks Downloads link")
def click_downloads(driver):
    downloads = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Downloads")))
    downloads.click()

    driver.execute_script(
        "arguments[0].scrollIntoView({ block: 'center'});", 
        downloads
    )

@then("Downloads page should open")
def verify_downloads_page(driver):
    assert "downloads" in driver.current_url.lower()
    WebDriverWait(driver, 10).until(EC.url_contains("downloads"))