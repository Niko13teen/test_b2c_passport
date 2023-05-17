from BaseApp import BasePage, RegisterPage
from selenium.webdriver.common.by import By


class PassportRTLocators:
    """Получение локаторов элементов страницы"""
    
    LOCATOR_RT_LOGIN_FIELD = (By.ID, "username")
    LOCATOR_RT_PASSWORD_FIELD = (By.ID, "password")
    LOCATOR_RT_SUBMIT_BUTTON = (By.ID, "kc-login")
    LOCATOR_RT_WARNING_MESSAGE = (By.ID, "form-error-message")
    LOCATOR_RT_LOGOUT_BUTTON = (By.ID, "logout-btn")
    LOCATOR_RT_FORGOT_PASSWORD = (By.ID, "forgot_password")
    LOCATOR_RT_NAME_FIELD = (By.NAME, 'fistName')


class AuthHelper(BasePage):
    """ Методы работы со страницей Авторизации """
    
    def enter_word_login(self, word: str) -> object:
        """ Поиск и ввод тестовых данных в поле 'Номер телефона' """
        login_field = self.find_element(PassportRTLocators.LOCATOR_RT_LOGIN_FIELD)
        login_field.click()
        login_field.send_keys(word)
        return login_field

    def enter_word_password(self, word: str) -> object:
        """ Поиск и ввод тестовых данных в поле 'Пароль' """
        password_field = self.find_element(PassportRTLocators.LOCATOR_RT_PASSWORD_FIELD)
        password_field.click()
        password_field.send_keys(word)
        return password_field

    def click_on_the_auth_button(self) -> None:
        """ Поиск и нажатие на кнопку 'Войти' """
        return self.find_element(
            PassportRTLocators.LOCATOR_RT_SUBMIT_BUTTON, time=5
        ).click()

    def check_error_message(self) -> str:
        """ Поиск сообщения об ошибке и получение его теста """
        return self.find_element(
            PassportRTLocators.LOCATOR_RT_WARNING_MESSAGE, time=5
        ).text

    def logout_button(self) -> None:
        """ Поиск кнопки 'Выход' и нажатие на нее """
        return self.find_element(
            PassportRTLocators.LOCATOR_RT_LOGOUT_BUTTON, time=5
        ).click()

    def get_color_forgot_password_button(self) -> str:
        """ Поиск кнопки 'Забыл Пароль' и получение его css-свойства 'color' в формате RGB """
        return self.find_element(
            PassportRTLocators.LOCATOR_RT_FORGOT_PASSWORD, time=5
        ).value_of_css_property("color")

class RegisterHelper(RegisterPage):
    """ Методы работы со страницей Регистрации """
    
    def enter_word_name(self, word: str) -> object:
        """ Поиск и ввод тестовых данных в поле 'Имя' """
        name_field = self.find_element(PassportRTLocators.LOCATOR_RT_NAME_FIELD)
        name_field.click()
        name_field.send_keys(word)
        return name_field
