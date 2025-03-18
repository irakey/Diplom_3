import allure
from locators import OrderPopupFeedLocators
from pages.base_page import BasePage

class OrderPopupFeedPage(BasePage):

    @allure.step("Ожидаем видимости надписи Состав в попапе")
    def wait_until_contents_visible(self):
        self.wait_for_element_visible(OrderPopupFeedLocators.CONTENTS_HEADER)

    @allure.step("Проверяем, что заголовок содержимого попапа отображается")
    def is_contents_header_visible(self):
        return self.is_element_displayed(OrderPopupFeedLocators.CONTENTS_HEADER)