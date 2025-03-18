import allure
from data import Urls
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.order_history_page import OrderHistoryPage
from pages.profile_page import ProfilePage


class TestProfile:

    @allure.title("Проверка перехода с главной страницы в личный кабинет для авторизованного пользователя")
    def test_go_to_profile(self, driver, registration):
        login_page = LoginPage(driver)
        login_page.navigate(Urls.LOGIN_PAGE)
        login_page.fill_in_email(registration['email'])
        login_page.fill_in_password(registration['password'])
        login_page.click_login_button()
        main_page = MainPage(driver)
        main_page.wait_order_button_visible()
        assert main_page.is_on_main_page()
        main_page.click_profile_button()
        profile_page = ProfilePage(driver)
        profile_page.personal_data_informer_visible()
        assert profile_page.is_on_profile_page()

    @allure.title("Проверка возможности перехода в Историю заказов из Личного кабинета")
    def test_go_to_order_history(self, driver, registration):
        login_page = LoginPage(driver)
        login_page.navigate(Urls.LOGIN_PAGE)
        login_page.fill_in_email(registration['email'])
        login_page.fill_in_password(registration['password'])
        login_page.click_login_button()
        main_page = MainPage(driver)
        main_page.wait_order_button_visible()
        assert main_page.is_on_main_page()
        main_page.click_profile_button()
        profile_page = ProfilePage(driver)
        profile_page.personal_data_informer_visible()
        assert profile_page.is_on_profile_page()
        profile_page.click_order_history()
        history_page = OrderHistoryPage(driver)
        history_page.wait_until_url_is_order_history()
        assert history_page.is_on_order_history_page()

    @allure.title("Проверка успешного логаута")
    def test_logout(self, driver, registration):
        login_page = LoginPage(driver)
        login_page.navigate(Urls.LOGIN_PAGE)
        login_page.fill_in_email(registration['email'])
        login_page.fill_in_password(registration['password'])
        login_page.click_login_button()
        main_page = MainPage(driver)
        main_page.wait_order_button_visible()
        assert main_page.is_on_main_page()
        main_page.click_profile_button()
        profile_page = ProfilePage(driver)
        profile_page.personal_data_informer_visible()
        assert profile_page.is_on_profile_page()
        profile_page.click_logout()
        profile_page.wait_for_login_url()
        assert profile_page.is_on_login_page()
