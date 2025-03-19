import allure
from locators import IngredientPopupLocators
from pages.base_page import BasePage


class IngredientPopupPage(BasePage):

    @allure.step("Проверяем видимость заголовка попапа с деталями ингредиента")
    def wait_until_popup_header_visible(self):
        self.wait_for_element_visible(IngredientPopupLocators.INGREDIENT_HEADER)

    @allure.step("Кликаем на кнопку в виде крестика для закрытия попапа")
    def close_popup(self):
        self.click_element(IngredientPopupLocators.POPUP_CLOSE_BUTTON)

    @allure.step("Дожидаемся скрытия попапа")
    def wait_until_popup_invisible(self):
        self.wait_until_element_invisible(IngredientPopupLocators.INGREDIENT_HEADER)

    @allure.step("Проверяем, что попап с информацией об ингредиенте закрыт")
    def is_popup_closed(self):
        return not self.is_element_displayed(IngredientPopupLocators.INGREDIENT_HEADER)