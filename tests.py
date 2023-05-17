from PassportRTPages import AuthHelper, RegisterHelper
from FakeUser import FakeUserData


user_object = FakeUserData()


def test_positive_registration(browser: object) -> None:
    """ soon """
    pass


def test_positive_auth_for_phone_and_password(browser: object) -> None:
    """ Авторизация по номеру с верным номером и паролем """
    passport_main_page = AuthHelper(browser)
    passport_main_page.return_site()
    passport_main_page.enter_word_login(user_object.return_positive_phone())
    passport_main_page.enter_word_password(user_object.return_positive_password())
    passport_main_page.click_on_the_auth_button()
    redirect_url = browser.current_url
    assert redirect_url[:50] == "https://b2c.passport.rt.ru/account_b2c/page?state="
    passport_main_page.logout_button()


def test_positive_auth_for_email_and_password(browser: object) -> None:
    """ Авторизация по email с верным email и верным паролем """
    passport_main_page = AuthHelper(browser)
    passport_main_page.return_site()
    passport_main_page.enter_word_login(user_object.return_positive_email())
    passport_main_page.enter_word_password(user_object.return_positive_password())
    passport_main_page.click_on_the_auth_button()
    redirect_url = browser.current_url
    assert redirect_url[:50] == "https://b2c.passport.rt.ru/account_b2c/page?state="
    passport_main_page.logout_button()


 def test_negative_auth_for_valid_phone_and_novalid_password(browser: object) -> None:
    """ Авторизация по номеру с верным номером, но неверным паролем """
    passport_main_page = AuthHelper(browser)
    passport_main_page.return_site()
    passport_main_page.enter_word_login(user_object.return_positive_phone())
    passport_main_page.enter_word_password(user_object.return_negative_password())
    passport_main_page.click_on_the_auth_button()
    warning_message = passport_main_page.check_error_message()
    color_forgot_password = passport_main_page.get_color_forgot_password_button()
    assert warning_message == 'Неверный логин или пароль'
    assert color_forgot_password == 'rgba(255, 79, 18, 1)'

 def test_negative_auth_for_novalid_phone_and_novalid_password(browser: object) -> None:
    """ Авторизация по номеру с неверным номером и неверным паролем """     
    passport_main_page = AuthHelper(browser)
    passport_main_page.return_site()
    passport_main_page.enter_word_login(user_object.return_negative_phone())
    passport_main_page.enter_word_password(user_object.return_negative_password())
    passport_main_page.click_on_the_auth_button()
    warning_message = passport_main_page.check_error_message()
    color_forgot_password = passport_main_page.get_color_forgot_password_button()
    assert warning_message == 'Неверный логин или пароль'
    assert color_forgot_password == 'rgba(255, 79, 18, 1)'

 def test_negative_auth_for_valid_email_and_novalid_password(browser: object) -> None:
    """ Авторизация по номеру с верным email, но неверным паролем """
    passport_main_page = AuthHelper(browser)
    passport_main_page.return_site()
    passport_main_page.enter_word_login(user_object.return_positive_email())
    passport_main_page.enter_word_password(user_object.return_negative_password())
    passport_main_page.click_on_the_auth_button()
    warning_message = passport_main_page.check_error_message()
    color_forgot_password = passport_main_page.get_color_forgot_password_button()
    assert warning_message == 'Неверный логин или пароль'
    assert color_forgot_password == 'rgba(255, 79, 18, 1)'

 def test_negative_auth_for_novalid_email_and_novalid_password(browser: object) -> None:
    """ Авторизация по номеру с неверным email и неверным паролем """
    passport_main_page = AuthHelper(browser)
    passport_main_page.return_site()
    passport_main_page.enter_word_login(user_object.return_negative_email())
    passport_main_page.enter_word_password(user_object.return_negative_password())
    passport_main_page.click_on_the_auth_button()
    warning_message = passport_main_page.check_error_message()
    color_forgot_password = passport_main_page.get_color_forgot_password_button()
    assert warning_message == 'Неверный логин или пароль'
    assert color_forgot_password == 'rgba(255, 79, 18, 1)'
