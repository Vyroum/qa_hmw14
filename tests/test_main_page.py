import time
import allure

from pages.main_page import MainPage
from resources.book import book

mainpage = MainPage()


def test_main_page():
    with allure.step("Открытие веб-страницы"):
        mainpage.open_browser()

    with allure.step("Поиск книги серии 'Гарри Поттер'"):
        mainpage.search_book(book)

    with allure.step("Проверка наличия книги в поисковой выдаче"):
        mainpage.check_book_availability(book)

    with allure.step("Добавить книгу в корзину"):
        mainpage.add_to_cart()
        time.sleep(2)

    with allure.step("Открываем корзину"):
        mainpage.open_cart()

    with allure.step("Проверка товара в корзине"):
        mainpage.check_cart(book)
