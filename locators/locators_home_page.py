from selenium.webdriver.common.by import By

class HomePageLocators:
    ORDER_BUTTON_TOP = (By.XPATH, "//button[text()='Заказать' and contains(@class, 'Button_Button')]") # Кнопка заказать вверху
    ORDER_BUTTON_BOTTOM = (By.XPATH, "//button[text()='Заказать'][@class='Order_Button_Black']") # Кнопка заказать внизу
    LOGO_SAMOKAT = (By.XPATH, "//img[@alt='Scooter']")  # Логотип Самоката
    LOGO_YANDEX = (By.XPATH, "//a[@class='Header_LogoYandex__3TSOI']") # Логотип Яндекса


    FAQ_SECTION = (By.CLASS_NAME, "Home_FAQ__3uVm4") # Список со всеми вопросами
    FAQ_QUESTION = (By.XPATH, "//div[@data-accordion-component='AccordionItemButton']") # Вопрос (кнопка)
    FAQ_ANSWER = (By.XPATH, "//div[@data-accordion-component='AccordionItemPanel']") # Ответ (раскрывающийся контент)


    @staticmethod
    def question_number(number):
        return (By.XPATH, f"(//div[@class='accordion__button'])[{number}]")

    @staticmethod
    def answer_number(number):
        return (By.XPATH, f"(//div[@class='accordion__panel'])[{number}]")