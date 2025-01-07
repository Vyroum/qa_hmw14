import time
import allure

from pages.main_page import MainPage
from resources.CPU import cpu

mainpage = MainPage()


def test_main_page(browser_set):
    with allure.step("Открытие веб-страницы"):
        mainpage.open_browser()

    with allure.step("Поиск процессора 'Intel Core i7'"):
        mainpage.search_book(cpu)

    with allure.step("Проверка наличия книги в поисковой выдаче"):
        mainpage.check_book_availability(cpu)

    with allure.step("Добавить процессор в корзину"):
        mainpage.add_to_cart()
        time.sleep(2)

    with allure.step("Открываем корзину"):
        mainpage.open_cart()

    with allure.step("Проверка товара в корзине"):
        mainpage.check_cart(cpu)
