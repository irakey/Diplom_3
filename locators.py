from selenium.webdriver.common.by import By

#Страница "Восстановить пароль"
class ForgotPasswordLocators:
    EMAIL_FIELD = By.CSS_SELECTOR, ".input" #Поле "Email"
    EMAIL_FIELD_ACTIVE = (By.XPATH, "//input[@class='text input__textfield text_type_main-default']") #Поле Email в активном состоянии
    RESET_PASSWORD_BUTTON = (By.XPATH, "//button[contains(.,'Восстановить')]") #Кнопка "Восстановить"
    REMEMBER_PASSWORD_BUTTON = (By.XPATH, "//p[contains(.,'Вспомнили пароль? Войти')]") #Надпись "Вспомнили пароль?"

#Страница восстановления пароля с полем для ввода нового
class ResetPasswordLocators:
    NEW_PASSWORD_FIELD = (By.XPATH, "//label[contains(.,'Пароль')]") #Поле "Пароль"
    VIEW_PASSWORD_BUTTON = (By.XPATH, '//div[@class="input__icon input__icon-action"]') #Иконка видимости пароля в виде глаза - открытый глаз, пароль закрыт точками
    EMAIL_CODE_FIELD = (By.XPATH, "//label[contains(.,'Введите код из письма')]") #Поле ввода кода из письма
    PASSWORD_FIELD2 = (By.XPATH, "//input[contains(@type,'text')]") #Поле "Пароль" с типом изменившимся на text

#Страница логина
class LoginPageLocators:
    FORGOT_PASSWORD_BUTTON = (By.XPATH, "//a[contains(.,'Восстановить пароль')]") #Кнопка "Восстановить пароль"
    EMAIL_FIELD_INACTIVE = (By.XPATH, "(//div[contains(.,'Email')])[5]") #Поле "Email" в неактивном состоянии
    EMAIL_FIELD_ACTIVE = (By.XPATH, "(//input[@class='text input__textfield text_type_main-default'])[1]") #Поле Email в активном состоянии
    PASSWORD_FIELD_INACTIVE = (By.XPATH, "//label[contains(.,'Пароль')]") #Поле "Пароль" в неактивном состоянии
    PASSWORD_FIELD_ACTIVE = (By.XPATH, "//input[contains(@name,'Пароль')]") #Поле "Пароль" в активном состоянии
    LOGIN_BUTTON = (By.XPATH, "//button[contains(.,'Войти')]") #Кнопка "Войти"

#Главная страница
class MainPageLocators:
    GO_TO_PROFILE_BUTTON = (By.XPATH, "//p[contains(.,'Личный Кабинет')]") #Кнопка "Личный кабинет"
    GO_TO_ORDER_FEED_BUTTON = (By.XPATH, "//p[contains(.,'Лента Заказов')]") #Кнопка "Лента заказов"
    ORDER_BUTTON = (By.XPATH, "//button[contains(.,'Оформить заказ')]") #Кнопка "Оформить заказ"
    FLUO_BUN = (By.XPATH, "//a[1]/p[text()='Флюоресцентная булка R2-D3']") #Ингредиент Флюоресцентная булка
    INGREDIENT_PLACE = (By.XPATH, "//div[@class='constructor-element constructor-element_pos_top']") #Место для перетаскивания ингредиента
    FLUO_BUN_COUNTER = (By.XPATH, "//div[1]/p[@class='counter_counter__num__3nue1' and text()='2']") #Каунтер Флюоресцентной булки

#Личный кабинет
class ProfileLocators:
    ORDER_HISTORY_BUTTON = (By.XPATH, "//a[contains(.,'История заказов')]") #Кнопка для перехода в "История заказов"
    LOGOUT_BUTTON = (By.XPATH, "//button[@type='button'][contains(.,'Выход')]") #Кнопка "Выход"
    PERSONAL_DATA_INFORMER = (By.XPATH, "//p[contains(.,'персональные данные')]") #Надпись о персон данных

#Страница ленты заказов
class OrderFeedLocators:
    GO_TO_CONSTRUCTOR_BUTTON = (By.XPATH, "//p[contains(.,'Конструктор')]") #Кнопка для перехода в "Конструктор"
    FEED_HEADER = (By.XPATH, "//h1[contains(.,'Лента заказов')]") #Заголовок страницы
    FIRST_ORDER = (By.XPATH, "(//h2[contains(@class,'main-medium mb-2')])[1]") #Первый зааказ в списке
    SPECIFIC_ORDER_LOCATOR = (By.XPATH, "//p[@class='text text_type_digits-default'][contains(.,'#{}')]") #Конкретный заказ
    TOTAL = (By.XPATH, "(// p[contains( @class ,'digits-large')])[1]") #Общее количество заказов
    TODAY_TOTAL = (By.XPATH, "(//p[contains(@class,'digits-large')])[2]") #Количество заказов за текущий день

#Попап заказа в Ленте
class OrderPopupFeedLocators:
    CONTENTS_HEADER = (By.XPATH, "//p[contains(.,'Cостав')]") #Заголовок "Состав" в попапе

#Попап с деталями ингредиента
class IngredientPopupLocators:
    INGREDIENT_HEADER = (By.XPATH, "//h2[contains(.,'Детали ингредиента')]") #Заголовок попапа
    POPUP_CLOSE_BUTTON = (By.XPATH, "(//button[contains(@type,'button')])[1]") #Иконка "Крестик"

#Попап с номером заказа
class OrderCreatedLocators:
    POPUP_TEXT = (By.XPATH, "//p[contains(.,'идентификатор заказа')]") #Текст в попапе
    CLOSE_BUTTON = (By.XPATH, "//button[contains(@type,'button')]") #Кнопка Крестик
    INCORRECT_NUMBER = (By.XPATH, "//h2[contains(.,'9999')]") #Неправильный номер
    JUST_CREATED_ORDER = (By.XPATH, "//h2[contains(@class,'digits-large mb-8')]") #Номер только что созданного заказа
    WAITING_FOR = (By.XPATH, "//li[@class='text text_type_digits-default mb-2'][contains(.,'{}')]") #Локатор для ожидания

#История заказов в профиле
class OrderHistoryLocators:
    ORDER_NUMBER = (By.XPATH, "//p[@class='text text_type_digits-default'][contains(.,'#')]") #Номер заказа пользователя