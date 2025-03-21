import allure
from data import Urls
from locators import OrderFeedLocators, OrderCreatedLocators
from pages.base_page import BasePage


class OrderFeedPage(BasePage):

    @allure.step("Кликаем на кнопку Конструктор в шапке сайта")
    def click_constructor_button(self):
        self.click_element(OrderFeedLocators.GO_TO_CONSTRUCTOR_BUTTON)

    @allure.step("Ожидаем смены URL на страницу с лентой заказов")
    def wait_for_order_feed_url(self):
        self.wait_for_url_change(Urls.ORDER_FEED_PAGE)

    @allure.step("Ожидаем видимости заголовка Ленты заказов")
    def wait_for_order_feed_header(self):
        self.wait_for_element_visible(OrderFeedLocators.FEED_HEADER)

    @allure.step("Кликаем на заказ в ленте")
    def click_order(self):
        self.click_element(OrderFeedLocators.FIRST_ORDER)

    @allure.step("Получаем общее количество заказов")
    def get_completed_orders_count(self):
        completed_orders_element = self.wait_for_element_visible(OrderFeedLocators.TOTAL)
        return int(completed_orders_element.text)

    @allure.step("Получаем количество заказов за текущий день")
    def get_todays_orders_count(self):
        todays_orders_element = self.wait_for_element_visible(OrderFeedLocators.TODAY_TOTAL)
        return int(todays_orders_element.text)

    @allure.step("Прокручиваем до кнопки 'Заказать' внизу страницы")
    def scroll_to_todays_counter(self):
        button = self.find_element(OrderFeedLocators.TODAY_TOTAL)
        self.scroll_to_bottom(button)

    @allure.step("Проверяем, что конкретный заказ отображается")
    def is_specific_order_visible(self, order_id):
        specific_order_locator = (OrderFeedLocators.SPECIFIC_ORDER_LOCATOR[0], OrderFeedLocators.SPECIFIC_ORDER_LOCATOR[1].format(order_id))
        return self.is_element_displayed(specific_order_locator)

    @allure.step("Проверяем, что заказ в разделе 'В работе' отображается")
    def is_order_in_progress_visible(self, order_id):
        specific_locator = (OrderCreatedLocators.WAITING_FOR[0], OrderCreatedLocators.WAITING_FOR[1].format(order_id))
        return self.is_element_displayed(specific_locator)