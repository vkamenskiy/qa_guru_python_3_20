from appium.webdriver.common.appiumby import AppiumBy
from selene import have
from selene.support.shared import browser
from allure import step

from mobile_tests_lesson_13.model import app


def test_search_browserstack():
    app.given_opened()

    with step("Search BrowserStack"):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type(
            "BrowserStack"
        )

    with step("Verify content found"):
        browser.all((AppiumBy.CLASS_NAME, "android.widget.TextView")).should(
            have.size_greater_than(0)
        )


def test_search_python():
    app.given_opened()

    with step("Search Python"):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type(
            "Python"
        )

    with step("Verify content found"):
        browser.element(
            (AppiumBy.ID, "org.wikipedia.alpha:id/page_list_item_description")
        ).should(have.text("Topics referred to by the same term"))


def test_headers_on_onboarding_screen():
    with step("First page header"):
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/primaryTextView")).should(
            have.text("The Free Encyclopedia\n…in over 300 languages")
        )
        browser.element(
            (AppiumBy.ID, "org.wikipedia.alpha:id/fragment_onboarding_forward_button")
        ).click()

    with step("Second page header"):
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/primaryTextView")).should(
            have.text("New ways to explore")
        )
        browser.element(
            (AppiumBy.ID, "org.wikipedia.alpha:id/fragment_onboarding_forward_button")
        ).click()

    with step("Third page header"):
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/primaryTextView")).should(
            have.text("Reading lists with sync")
        )
        browser.element(
            (AppiumBy.ID, "org.wikipedia.alpha:id/fragment_onboarding_forward_button")
        ).click()

    with step("Fourth page header"):
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/primaryTextView")).should(
            have.text("Send anonymous data")
        )
