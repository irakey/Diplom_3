from data import Urls
import allure
from pages.login_page import LoginPage
from pages.forgot_password_page import ForgotPasswordPage
from pages.reset_password_page import ResetPasswordPage


class TestResetPassword:

    @allure.title("Проверка навигации на страницу восстановления пароля после клика на 'Восстановить пароль'")
    def test_click_reset_password_on_login_page(self, driver):
        login_page = LoginPage(driver)
        login_page.navigate(Urls.LOGIN_PAGE)
        login_page.click_reset_password()
        forgot_page = ForgotPasswordPage(driver)
        forgot_page.wait_for_remember_password_visible()
        assert forgot_page.is_on_recovery_page()

    @allure.title("Проверка ввода email и перехода к восстановлению пароля")
    def test_enter_email_and_go_to_reset_password(self, driver):
        forgot_page = ForgotPasswordPage(driver)
        forgot_page.navigate(Urls.RECOVERY_PAGE)
        forgot_page.wait_for_email_field_to_be_clickable()
        forgot_page.click_email_field()
        forgot_page.fill_in_email_field()
        forgot_page.click_reset_button()
        reset_page = ResetPasswordPage(driver)
        reset_page.wait_until_email_code_field_is_visible()
        assert reset_page.is_on_reset_page()

    @allure.title("Проверка видимости пароля по клику на иконку глазика")
    def test_draft_2(self, driver):
        forgot_page = ForgotPasswordPage(driver)
        forgot_page.navigate(Urls.RECOVERY_PAGE)
        forgot_page.wait_for_email_field_to_be_clickable()
        forgot_page.click_reset_button()
        reset_page = ResetPasswordPage(driver)
        reset_page.wait_until_password_field_visible()
        assert reset_page.is_on_reset_page()
        reset_page.click_password_field()
        reset_page.find_password_field_type_text()
        reset_page.click_eye_button()
        assert reset_page.is_password_visible()
