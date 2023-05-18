from configuration.BaseApp import BasePage
from selenium.webdriver.common.by import By


class PassportRTLocators:
    """Получение локаторов элементов страницы"""
    
    LOCATOR_RT_LOGIN_FIELD = (By.ID, "username")
    LOCATOR_RT_PASSWORD_FIELD = (By.ID, "password")
    LOCATOR_RT_SUBMIT_BUTTON = (By.ID, "kc-login")
    LOCATOR_RT_WARNING_MESSAGE_AUTHORIZATION = (By.ID, "form-error-message")
    LOCATOR_RT_LOGOUT_BUTTON = (By.ID, "logout-btn")
    LOCATOR_RT_FORGOT_PASSWORD = (By.ID, "forgot_password")
    LOCATOR_RT_REGISTER_BUTTON = (By.ID, 'kc-register')
    LOCATOR_RT_FIRST_NAME_FIELD = (By.NAME, 'firstName')
    LOCATOR_RT_LAST_NAME_FIELD = (By.NAME, 'lastName')
    LOCATOR_RT_REGISTER_SUMBMIT = (By.NAME, 'register')
    LOCATOR_RT_ADDRESS_FIELD = (By.ID, 'address')
    LOCATOR_RT_PASSWORD_CONFIRM_FIELD = (By.ID, 'password-confirm')
    LOCATOR_RT_REGISTER_CONFIRIM = (By.CLASS_NAME, 'register-confirm-form-container__desc')
    LOCATOR_RT_BACK_STEP_REGISTRATION_BUTTON = (By.NAME, 'otp_back_phone')
    LOCATOR_RT_WARNING_MESSAGE_FOR_REGISTRATION = (By.CSS_SELECTOR, '.rt-input-container__meta--error')


class AuthHelper(BasePage):

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
            PassportRTLocators.LOCATOR_RT_WARNING_MESSAGE_AUTHORIZATION, time=5
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
        
    def register_button(self) -> None:
        """ Поиск и нажатие на кнопку 'Регистрация' """
        return self.find_element(
            PassportRTLocators.LOCATOR_RT_REGISTER_BUTTON, time=5
        ).click()
   
    def enter_word_first_name(self, word: str) -> object:
        """ Поиск и ввод тестовых данных в поле 'Имя' """
        first_name_field = self.find_element(PassportRTLocators.LOCATOR_RT_FIRST_NAME_FIELD, time=5)
        first_name_field.click()
        first_name_field.send_keys(word)
        return first_name_field
    
    def enter_word_last_name(self, word: str) -> object:
        """ Поиск и ввод тестовых данных в поле 'Фамилия' """
        last_name_field = self.find_element(PassportRTLocators.LOCATOR_RT_LAST_NAME_FIELD, time=5)
        last_name_field.click()
        last_name_field.send_keys(word)
        return last_name_field
    
    def enter_word_address(self, word: str) -> object:
        """ Поиск и ввод тестовых данных в поле 'E-mail или мобильный телефон' """
        address_field = self.find_element(PassportRTLocators.LOCATOR_RT_ADDRESS_FIELD)
        address_field.click()
        address_field.send_keys(word)
        return address_field
    
    def enter_word_password_confirim(self, word: str) -> object:
        """ Поиск и ввод тестовых данных в поле 'Подтверждение пароля' """
        password_confirim_field = self.find_element(PassportRTLocators.LOCATOR_RT_PASSWORD_CONFIRM_FIELD)
        password_confirim_field.click()
        password_confirim_field.send_keys(word)
        return password_confirim_field
    
    def get_text_for_register_confirim(self) -> str:
        return self.find_element(
            PassportRTLocators.LOCATOR_RT_REGISTER_CONFIRIM, time=5
        ).text
    
    def register_submit(self) -> None:
        """ Поиск кнопки 'Зарегистрироваться' и нажатие на нее """ 
        return self.find_element(
            PassportRTLocators.LOCATOR_RT_REGISTER_SUMBMIT, time=5
        ).click()
    
    def register_back_step(self) -> None:
        """ Поиск кнопки 'Изменить email' и нажатие на нее """ 
        return self.find_element(
            PassportRTLocators.LOCATOR_RT_BACK_STEP_REGISTRATION_BUTTON, time=5
        ).click()  
    
    def get_text_warning_message_for_registration(self) -> str:
        """ Поиск сообщения об ошибке и получение его теста """
        return self.find_element(
            PassportRTLocators.LOCATOR_RT_WARNING_MESSAGE_FOR_REGISTRATION, time=5
        ).text

