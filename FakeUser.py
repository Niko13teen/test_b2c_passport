from typing import Literal


# Обьект данных пользователя для генерации тестовых случаев
LITERAL_FAKE_DATA = {
    "positive_user_phone": "9136756313",
    "positive_user_password": "Rufus666!",
    "negative_user_phone": "9146756313",
    "negative_user_password": "Qwerty123!",                   
    "positive_user_email": "sergey.devops.link@gmail.com",    
    "negative_user_email": "sergeydevops@gmail.com",          
    "positive_user_first_name_for_register": "Тестовыйслучай",             # 14 characters for equivalence classes (middle)
    "positive_user_last_name_for_register": "Тестовыйслучай",              # 14 characters for equivalence classes (middle)
    "positive_user_email_address_for_register": "testuser@fakemail.com",   
    "positive_user_password_for_register": "P4s6w0rd",                     # 8 characters
    "positive_user_password_for_register_confirim": "P4s6w0rd",            # 8 characters
}


class FakeUserData:
    """Обьект методов пользователя"""

    def __init__(self) -> None:
        """Инициализация пользователя"""
        self.fake_user = LITERAL_FAKE_DATA

    def return_positive_phone(self) -> dict[Literal["positive_user_phone"], str]:
        """Возврат верного номера"""
        positive_user_phone = self.fake_user.get("positive_user_phone")
        return (
            positive_user_phone
            if positive_user_phone is not None
            else exec("raise Exception('Missing value!')")
        )

    def return_positive_password(self) -> dict[Literal["positive_user_password"], str]:
        """Возврат верного пароля"""
        positive_user_password = self.fake_user.get("positive_user_password")
        return (
            positive_user_password
            if positive_user_password is not None
            else exec("raise Exception('Missing value!')")
        )

    def return_negative_phone(self) -> dict[Literal["negative_user_phone"], str]:
        """Возврат неверного номера"""
        negative_user_phone = self.fake_user.get("negative_user_phone")
        return (
            negative_user_phone
            if negative_user_phone is not None
            else exec("raise Exception('Missing value!')")
        )

    def return_negative_password(self) -> dict[Literal["negative_user_password"], str]:
        """Возврат неверного пароля"""
        negative_user_password = self.fake_user.get("negative_user_password")
        return (
            negative_user_password
            if negative_user_password is not None
            else exec("raise Exception('Missing value!')")
        )

    def return_positive_email(self) -> dict[Literal["positive_user_email"], str]:
        """Возврат верного email"""
        positive_user_email = self.fake_user.get("positive_user_email")
        return (
            positive_user_email
            if positive_user_email is not None
            else exec("raise Exception('Missing value!')")
        )

    def return_negative_email(self) -> dict[Literal["negative_user_email"], str]:
        """Возврат неверного email"""
        negative_user_email = self.fake_user.get("negative_user_email")
        return (
            negative_user_email
            if negative_user_email is not None
            else exec("raise Exception('Missing value!')")
        )
    
    def return_positive_first_name(self) -> dict[Literal["positive_user_first_name_for_register"], str]:
        """ Вовзрат верного имени """
        positive_user_first_name = self.fake_user.get("positive_user_first_name_for_register")
        return (
            positive_user_first_name
            if positive_user_first_name is not None
            else exec("raise Exception('Missing value!')")
        )
    
    def return_positive_last_name(self) -> dict[Literal["positive_user_last_name_for_register"], str]:
        """ Вовзрат верной фамилии """
        positive_user_last_name = self.fake_user.get("positive_user_last_name_for_register")
        return (
            positive_user_last_name
            if positive_user_last_name is not None
            else exec("raise Exception('Missing value!')")
        )
    
    def return_positive_password_for_register(self) -> dict[Literal["positive_user_password_for_register"], str]:
        """ Вовзрат верного пароля для регистрации """
        positive_password_for_register = self.fake_user.get("positive_user_password_for_register")
        return (
            positive_password_for_register
            if positive_password_for_register is not None
            else exec("raise Exception('Missing value!')")
        )
    
    def return_positive_password_for_register_confirim(self) -> dict[Literal["positive_user_password_for_register_confirim"], str]:
        """ Вовзрат верного пароля для регистрации (подтверждение) """
        positive_password_for_register_confirim = self.fake_user.get("positive_user_password_for_register_confirim")
        return (
            positive_password_for_register_confirim
            if positive_password_for_register_confirim is not None
            else exec("raise Exception('Missing value!')")
        )
    
    def return_positive_email_for_register(self) -> dict[Literal["positive_user_email_address_for_register"], str]:
        """ Вовзрат верного пароля для регистрации (подтверждение) """
        positive_email_for_register = self.fake_user.get("positive_user_email_address_for_register")
        return (
            positive_email_for_register
            if positive_email_for_register is not None
            else exec("raise Exception('Missing value!')")
        )
