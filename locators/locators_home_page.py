from selenium.webdriver.common.by import By

class HomePageLocators:
    ORDER_BUTTON_TOP = (By.XPATH, '//div[@class="Header_Nav__AGCXC"]//button[text()= "Заказать"]') # Кнопка заказать вверху
    ORDER_BUTTON_BOTTOM = (By.XPATH, '//div[@class="Home_FinishButton__1_cWm"]//button[text()= "Заказать"]') # Кнопка заказать внизу
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