from appium.webdriver.common.appiumby import AppiumBy
from selene import have
from selene.support.shared import browser
# from allure import step
import allure


# def test_search():
#     with step('Type search'):
#         browser.element((AppiumBy.ACCESSIBILITY_ID, 'Search Wikipedia')).click()
#         browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/search_src_text')).type(
#             'BrowserStack'
#         )
#
#     with step('Verify content found'):
#         browser.all(
#             (AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title')
#         ).should(have.size_greater_than(0))


def test_search_browserstack():
    with allure.step('Search BrowserStack'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type("BrowserStack")

    with allure.step('Verify content found'):
        browser.all((AppiumBy.CLASS_NAME, "android.widget.TextView")).should(have.size_greater_than(0))


def test_search_python():
    with allure.step('Search Python'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type("Python")

    with allure.step('Verify content found'):
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/page_list_item_title")).click()
        browser.element((AppiumBy.CLASS_NAME, "android.widget.TextView")).should(have.text("An error occurred"))

