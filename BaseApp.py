from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage(object):
    """Определяем базовые методы для работы c WebDriver"""

    def __init__(self, driver: object) -> None:
        self.driver = driver
        self.base_url = "https://b2c.passport.rt.ru/"

    def __repr__(self) -> str:
        return f"BaseUrl: {self.base_url}"

    def find_element(self, locator: object, time=10) -> object:
        "Метод поиска и возврата одного элемента"
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_element_located(locator), message=f"{locator} not found!"
        )

    def find_elements(self, locator: object, time=10) -> object:
        "Метод поиска и возврата множества элементов в виде списка"
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_all_elements_located(locator),
            message=f"{locator} not found!",
        )

    def return_site(self) -> object:
        "Переход на сайт"
        return self.driver.get(self.base_url)
