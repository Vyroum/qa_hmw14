import time
from selene import browser, have, by, command, be
from resources.book import Books


class MainPage:

    def open_browser(self):
        browser.open("https://chitai-gorod.ru")
        browser.element('[class="button change-city__button change-city__button--accept blue"]').click()
        time.sleep(1)
        if browser.element('[class="popmechanic-close"]').should(be.visible):
            browser.element('[class="popmechanic-close"]').click()
        browser.element('[class="button cookie-notice__button white"]').click()

    def search_book(self, value: Books):
        browser.element('[class="header-search__input"]').clear().type(value.name).press_enter()
        time.sleep(5)

    def check_book_availability(self, value):
        browser.element('[class="products-list"]').should(have.text(value.name))

    def add_to_cart(self):
        if browser.element('[class="popmechanic-close"]').should(be.visible):
            browser.element('[class="popmechanic-close"]').click()
        else:
            pass
        browser.element(by.text("Купить")).perform(command.js.scroll_into_view).click()

    def open_cart(self):
        browser.element("[href='/cart']").click()
        time.sleep(2)

    def check_cart(self, value):
        browser.element('[class="cart-page"]').should(have.text(value.name))
        browser.element('[class="cart-page"]').should(have.text(value.author))
        browser.element('[class="product-quantity__counter"]').should(have.value(value.quantity))
