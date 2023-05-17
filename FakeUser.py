from typing import Literal


# Обьект данных пользователя для генерации тестовых случаев
LITERAL_FAKE_DATA = {
    "positive_user_phone": "9136756313",
    "positive_user_password": "Rufus666!",
    "negative_user_phone": "9146756313",
    "negative_user_password": "Qwerty123!",
    "positive_user_email": "sergey.devops.link@gmail.com",
    "negative_user_email": "sergeydevops@gmail.com",
    "positive_user_name": "Сергей",
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
    
    def return_positive_name(self) -> dict[Literal["positive_user_name"], str]:
        """ Вовзрат верного имени """
        positive_user_name = self.fake_user.get("positive_user_name")
        return (
            positive_user_name
            if positive_user_name is not None
            else exec("raise Exception('Missing value!')")
        )
