class Urls:
    MAIN_PAGE = 'https://stellarburgers.nomoreparties.site/'
    RECOVERY_PAGE = f"{MAIN_PAGE}forgot-password"
    PROFILE_PAGE = f"{MAIN_PAGE}account/profile"
    RESET_PAGE = f"{MAIN_PAGE}reset-password"
    ORDER_HISTORY_PAGE = f"{MAIN_PAGE}account/order-history"
    ORDER_FEED_PAGE = f"{MAIN_PAGE}feed"
    LOGIN_PAGE = f"{MAIN_PAGE}login"

    CREATE_USER = f"{MAIN_PAGE}api/auth/register"
    AUTH_USER = f"{MAIN_PAGE}api/auth/user"


class Buttons:
    PROFILE_BUTTON_TEXT = 'Профиль'
    ENTER_BUTTON_TEXT = 'Войти'
    ORDER_DETAILS = 'Детали ингредиента'
    ORDER_IS_CREATING = 'Ваш заказ начали готовить'
    COMPOUND_TEXT = 'Cостав'


class TestData:
    test_email = 'kurbanova_19@gmail.com'
    test_password = '@12345'
