import allure
from data import Urls
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage
from pages.order_history_page import OrderHistoryPage
from pages.order_popup_feed_page import OrderPopupFeedPage
from pages.order_created_popup_page import OrderCreatedPage
from pages.profile_page import ProfilePage


class TestOrderFeed:

    @allure.title("Проверка открытия попапа с деталями заказа")
    def test_open_order_info_popup_opens(self, driver):
        order_feed = OrderFeedPage(driver)
        order_feed.navigate(Urls.ORDER_FEED_PAGE)
        order_feed.wait_for_order_feed_header()
        order_feed.click_order()
        popup = OrderPopupFeedPage(driver)
        popup.wait_until_contents_visible()
        assert popup.is_contents_header_visible()

    @allure.title("Проверка отображения заказов пользователя из раздела 'История заказов'")
    def test_users_orders_displayed_in_feed(self, driver, registration):
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
        popup.incorrect_number_invisible()
        popup.close_order_created_popup()
        main = MainPage(driver)
        main.click_profile_button()
        profile = ProfilePage(driver)
        profile.personal_data_informer_visible()
        profile.click_order_history()
        history_page = OrderHistoryPage(driver)
        history_page.wait_until_url_is_order_history()
        order_id = history_page.get_order_id()
        orders_feed = OrderFeedPage(driver)
        orders_feed.navigate(Urls.ORDER_FEED_PAGE)
        assert orders_feed.is_specific_order_visible(order_id)

    @allure.title("Проверка работы счетчика 'Выполнено за всё время' при создании заказа")
    def test_alltime_orders_increased(self, driver, registration):
        login_page = LoginPage(driver)
        login_page.navigate(Urls.LOGIN_PAGE)
        login_page.fill_in_email(registration['email'])
        login_page.fill_in_password(registration['password'])
        login_page.click_login_button()
        main_page = MainPage(driver)
        main_page.wait_order_button_visible()
        assert main_page.get_current_url() == Urls.MAIN_PAGE
        main_page.click_order_feed_button()
        order_feed = OrderFeedPage(driver)
        order_feed.wait_for_order_feed_header()
        result = order_feed.get_completed_orders_count()
        order_feed.click_constructor_button()
        main = MainPage(driver)
        main.wait_order_button_visible()
        main.ingredient_drag_and_drop()
        main.click_order_button()
        popup = OrderCreatedPage(driver)
        popup.incorrect_number_invisible()
        popup.close_order_created_popup()
        main_return = MainPage(driver)
        main_return.click_order_feed_button()
        order_feed_return = OrderFeedPage(driver)
        new_result = order_feed_return.get_completed_orders_count()
        assert new_result == result + 1

    @allure.title("Проверка работы счетчика 'Выполнено за сегодня' при создании заказа")
    def test_today_orders_increased(self, driver, registration):
        login_page = LoginPage(driver)
        login_page.navigate(Urls.LOGIN_PAGE)
        login_page.fill_in_email(registration['email'])
        login_page.fill_in_password(registration['password'])
        login_page.click_login_button()
        main_page = MainPage(driver)
        main_page.wait_order_button_visible()
        assert main_page.get_current_url() == Urls.MAIN_PAGE
        main_page.click_order_feed_button()
        order_feed = OrderFeedPage(driver)
        order_feed.wait_for_order_feed_header()
        order_feed.scroll_to_todays_counter()
        result = order_feed.get_todays_orders_count()
        order_feed.click_constructor_button()
        main = MainPage(driver)
        main.wait_order_button_visible()
        main.ingredient_drag_and_drop()
        main.click_order_button()
        popup = OrderCreatedPage(driver)
        popup.incorrect_number_invisible()
        popup.close_order_created_popup()
        main_return = MainPage(driver)
        main_return.click_order_feed_button()
        order_feed_return = OrderFeedPage(driver)
        order_feed_return.scroll_to_todays_counter()
        new_result = order_feed_return.get_todays_orders_count()
        assert new_result == result + 1

    @allure.title("Проверка отображения созданного заказа в разделе В работе")
    def test_created_order_in_work(self, driver, registration):
        login_page = LoginPage(driver)
        login_page.navigate(Urls.LOGIN_PAGE)
        login_page.fill_in_email(registration['email'])
        login_page.fill_in_password(registration['password'])
        login_page.click_login_button()
        main_page = MainPage(driver)
        main_page.wait_order_button_visible()
        assert main_page.get_current_url() == Urls.MAIN_PAGE
        main_page.ingredient_drag_and_drop()
        main_page.click_order_button()
        popup = OrderCreatedPage(driver)
        popup.incorrect_number_invisible()
        result = popup.get_just_created_orders_count()
        popup.close_order_created_popup()
        main_return = MainPage(driver)
        main_return.click_order_feed_button()
        order_feed = OrderFeedPage(driver)
        order_feed.wait_for_order_feed_header()
        assert order_feed.is_order_in_progress_visible(result)
