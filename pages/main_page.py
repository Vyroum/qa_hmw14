import time
from selene import browser, have, by, command, be
from resources.CPU import CPUs


class MainPage:

    def open_browser(self):
        browser.open("https://www.regard.ru/")
        time.sleep(1)

    def search_book(self, value: CPUs):
        browser.element('[#id=searchInput]').type(value.model).press_enter()
        time.sleep(5)

    def check_book_availability(self, value):
        browser.element('[class="rendererWrapper"]').should(have.text(value.model))

    def add_to_cart(self):
        browser.element(by.text("В корзину")).perform(command.js.scroll_into_view).click()

    def open_cart(self):
        browser.element(by.text("Корзина")).click()
        time.sleep(2)

    def check_cart(self, value):
        browser.element('[class="BasketItem_row__BI8uk"]').should(have.text(value.model))
        browser.element('[class="CountSwitcher_count__0gn_e"]').should(have.value(value.quantity))
