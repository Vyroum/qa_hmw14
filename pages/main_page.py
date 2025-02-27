import time
from selene import browser, have, by, command, be
from resources.cpu import CPUs


class MainPage:

    def open_browser(self):
        browser.open("https://www.regard.ru/")
        time.sleep(1)

    def search_book(self, value: CPUs):
        browser.element('[id="searchInput"]').click().type(value.model).press_enter()
        time.sleep(3)

    def check_book_availability(self, value):
        browser.element('[class="rendererWrapper"]').should(have.text(value.model))

    def add_to_cart(self):
        browser.element(by.text("В корзину")).click()

    def open_cart(self):
        browser.element(by.text("В корзине")).click()
        time.sleep(2)

    def check_cart(self, value):
        browser.element('[class="BasketItem_row__BI8uk"]').should(have.text(value.model))
        browser.element('[class="SelectableList_title__BQ9Zk"]').should(have.text(value.quantity))
