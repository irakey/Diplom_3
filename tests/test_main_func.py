import allure
from data import Urls
from pages.ingredient_popup_page import IngredientPopupPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage
from pages.order_created_popup_page import OrderCreatedPage


class TestMainFunctions:

    @allure.title("Проверка перехода на главную по клику на 'Конструктор'")
    def test_go_to_constructor_page(self, driver):
        order_feed = OrderFeedPage(driver)
        order_feed.navigate(Urls.ORDER_FEED_PAGE)
        order_feed.click_constructor_button()
        main = MainPage(driver)
        main.wait_until_url_main()
        assert main.get_current_url() == Urls.MAIN_PAGE

    @allure.title("Проверка перехода на ленту заказов по клику на 'Лента заказов'")
    def test_go_to_order_feed_page(self, driver):
        main = MainPage(driver)
        main.navigate(Urls.MAIN_PAGE)
        main.click_order_feed_button()
        order_feed = OrderFeedPage(driver)
        order_feed.wait_for_order_feed_url()
        assert order_feed.get_current_url() == Urls.ORDER_FEED_PAGE

    @allure.title("Проверка открытия и закрытия попапа с информацией об ингредиенте")
    def test_open_ingredient_info(self, driver):
        main = MainPage(driver)
        main.navigate(Urls.MAIN_PAGE)
        main.wait_for_bun()
        main.click_bun()
        popup = IngredientPopupPage(driver)
        popup.wait_until_popup_header_visible()
        assert "ingredient" in popup.get_current_url()
        popup.close_popup()
        popup.wait_until_popup_invisible()
        assert popup.is_popup_closed()

    @allure.title("Проверка добавления ингредиента в заказ и изменение каунтера")
    def test_add_ingredient(self, driver):
        main = MainPage(driver)
        main.navigate(Urls.MAIN_PAGE)
        main.ingredient_drag_and_drop()
        main.wait_for_counter_visible()
        assert main.is_counter_visible()

    @allure.title("Проверка оформления заказа авторизованным пользователем")
    def test_authorized_order_flow(self, driver, registration):
        login_page = LoginPage(driver)
        login_page.navigate(Urls.LOGIN_PAGE)
        login_page.fill_in_email(registration['email'])
        login_page.fill_in_password(registration['password'])
        login_page.click_login_button()
        main_page = MainPage(driver)
        main_page.wait_order_button_visible()
        assert main_page.get_current_url() == Urls.MAIN_PAGE
        main_page.ingredient_drag_and_drop()
        main_page.wait_for_counter_visible()
        main_page.click_order_button()
        popup = OrderCreatedPage(driver)
        popup.wait_until_popup_text_visible()
        assert popup.is_popup_text_visible()
