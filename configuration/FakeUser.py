from typing import Literal


# Обьект данных пользователя для генерации тестовых случаев
LITERAL_FAKE_DATA = {
    "positive_user_phone": "9136756313",
    "positive_user_password": "Rufus666!",
    "negative_user_phone": "9146756313",
    "negative_user_password": "Qwerty123!",                   
    "positive_user_email": "sergey.devops.link@gmail.com",    
    "negative_user_email": "sergeydevops@gmail.com",          
    "positive_user_first_name_for_register_middle": "ТестовыйСлучай",                   # 14 characters for equivalence classes (middle)
    "positive_user_last_name_for_register_middle": "ТестовыйСлучай",                    # 14 characters for equivalence classes (middle)
    "positive_user_email_address_for_register": "testuser@fakemail.com",   
    "positive_user_password_for_register": "P4s6w0rd",                                  # 8 characters
    "positive_user_password_for_register_confirim": "P4s6w0rd",                         # 8 characters
    "positive_user_phone_for_register": "+79136756314",
    "negative_user_first_name_for_register": "Тестовыйслучайтестовыйслучайтес",         # 31 characters for going beyond the limit values
    "negative_user_last_name_for_register": "Тестовыйслучайтестовыйслучайтес",          # 31 characters for going beyond the limit values
    "negative_user_email_address_for_register": "@mail.com",                            # Incorrected email
    "negative_user_phone_for_register": "+712312312312",                                # Incorrected phone
    "negative_user_password_for_register": "P4s6w0r",                                   # 7 characters for going beyond the limit values
    "negative_user_password_for_register_no_latin": "ПароЛь!123",                       # Incorrected password (no latin)
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
    
    def return_positive_first_name_middle(self) -> dict[Literal["positive_user_first_name_for_register_middle"], str]:
        """ Возврат верного имени """
        positive_user_first_name_middle = self.fake_user.get("positive_user_first_name_for_register_middle")
        return (
            positive_user_first_name_middle
            if positive_user_first_name_middle is not None
            else exec("raise Exception('Missing value!')")
        )
    
    def return_positive_last_name_middle(self) -> dict[Literal["positive_user_last_name_for_register_middle"], str]:
        """ Возврат верной фамилии """
        positive_user_last_name_middle = self.fake_user.get("positive_user_last_name_for_register_middle")
        return (
            positive_user_last_name_middle
            if positive_user_last_name_middle is not None
            else exec("raise Exception('Missing value!')")
        )
    
    def return_positive_password_for_register(self) -> dict[Literal["positive_user_password_for_register"], str]:
        """ Возврат верного пароля для регистрации """
        positive_password_for_register = self.fake_user.get("positive_user_password_for_register")
        return (
            positive_password_for_register
            if positive_password_for_register is not None
            else exec("raise Exception('Missing value!')")
        )
    
    def return_positive_password_for_register_confirim(self) -> dict[Literal["positive_user_password_for_register_confirim"], str]:
        """ Возврат верного пароля для регистрации (подтверждение) """
        positive_password_for_register_confirim = self.fake_user.get("positive_user_password_for_register_confirim")
        return (
            positive_password_for_register_confirim
            if positive_password_for_register_confirim is not None
            else exec("raise Exception('Missing value!')")
        )
    
    def return_positive_email_for_register(self) -> dict[Literal["positive_user_email_address_for_register"], str]:
        """ Возврат верного email для регистрации """
        positive_email_for_register = self.fake_user.get("positive_user_email_address_for_register")
        return (
            positive_email_for_register
            if positive_email_for_register is not None
            else exec("raise Exception('Missing value!')")
        )
    
    def return_positive_phone_for_register(self) -> dict[Literal["positive_user_phone_for_register"], str]:
        """ Возврат верного номера для регистрации """
        positive_email_for_register = self.fake_user.get("positive_user_phone_for_register")
        return (
            positive_email_for_register
            if positive_email_for_register is not None
            else exec("raise Exception('Missing value!')")
        )
    
    @staticmethod
    def return_positive_phone_for_register_convert(number: str) -> str:
        """ Возврат верного номера для регистрации (конвертация) """
        phone_number_convert = f"+{number[1]} {number[2:5]} {number[5:8]}-{number[8:10]}-{number[10:12]}"
        return phone_number_convert
    
    @staticmethod
    def return_negative_password_for_doesnt_match(password: str) -> str:
        """ Вовзрат перевернутого пароля """
        return password[::-1]
    
    @staticmethod
    def return_negative_password_all_lower_characters(password: str) -> str:
        """ Вовзрат пароля (нет заглавных букв)"""
        return password.lower()
    
    
    def return_negative_first_name(self) -> dict[Literal["negative_user_first_name_for_register"], str]:
        """ Возврат неверного имени (выход за Граничные Значения) """
        negative_first_name = self.fake_user.get("negative_user_first_name_for_register")
        return (
            negative_first_name
            if negative_first_name is not None
            else exec("raise Exception('Missing value!')")
        )
    
    def return_negative_last_name(self) -> dict[Literal["negative_user_last_name_for_register"], str]:
        """ Возврат неверной фамилии (выход за Граничные Значения) """
        negative_last_name = self.fake_user.get("negative_user_last_name_for_register")
        return (
            negative_last_name
            if negative_last_name is not None
            else exec("raise Exception('Missing value!')")
        )
    
    def return_negative_email_for_register(self) -> dict[Literal["negative_user_email_address_for_register"], str]:
        """ Возврат некорретного email """
        nagative_email_for_registration = self.fake_user.get("negative_user_email_address_for_register")
        return (
            nagative_email_for_registration
            if nagative_email_for_registration is not None
            else exec("raise Exception('Missing value!')")
        )
    
    def return_negative_password_for_register(self) -> dict[Literal["negative_user_password_for_register"], str]:
        """ Возврат некорретного email """
        nagative_email_for_registration = self.fake_user.get("negative_user_password_for_register")
        return (
            nagative_email_for_registration
            if nagative_email_for_registration is not None
            else exec("raise Exception('Missing value!')")
        )
    
    def return_negative_phone_for_register(self) -> dict[Literal["negative_user_phone_for_register"], str]:
        """ Возврат верного номера для регистрации """
        negative_phone_for_register = self.fake_user.get("negative_user_phone_for_register")
        return (
            negative_phone_for_register
            if negative_phone_for_register is not None
            else exec("raise Exception('Missing value!')")
        )
    
    def return_negative_password_no_latin(self) -> dict[Literal["negative_user_password_for_register_no_latin"], str]:
        """ Возврат некорректного пароля (не латинские буквы) """
        negative_password_no_latin = self.fake_user.get("negative_user_password_for_register_no_latin")
        return (
            negative_password_no_latin
            if negative_password_no_latin is not None
            else exec("raise Exception('Missing value!')")
        )