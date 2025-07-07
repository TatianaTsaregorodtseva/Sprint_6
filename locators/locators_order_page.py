from selenium.webdriver.common.by import By

class OrderPageLocators:
    ORDER_BUTTON_TOP = (By.CLASS_NAME, "Button_Button__ra12g")  # Кнопка заказать вверху
    ORDER_BUTTON_BOTTOM = (By.XPATH, "//button[contains(@class, 'Button_Button') and contains(text(), 'Заказать')]") # Кнопка заказать внизу

    FIRST_NAME = (By.XPATH, "//input[@placeholder='* Имя']") # Поле Имя
    LAST_NAME = (By.XPATH, "//input[@placeholder='* Фамилия']") # Поле Фамилия
    ADDRESS = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']") # Поле Адрес
    METRO = (By.XPATH, "//input[@placeholder='* Станция метро']") # Поле Метро

    METRO_LIST = (By.CLASS_NAME, "select-search__row")

    PHONE = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']") # Поле Телефон

    NEXT_BUTTON = (By.XPATH, '//div[@class="Order_NextButton__1_rCA"]/button[text() = "Далее"]') # Кнопка Далее на втором шаге

    DATE_INPUT = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']") # Поле Даты
    CALENDAR_DROPDOWN = (By.CLASS_NAME, "react-datepicker") # Выпадающий календарь

    RENTAL_PERIOD = (By.XPATH, "//div[contains(@class, 'Dropdown-placeholder') and .//text()='* Срок аренды']") # Поле выбора срока аренды
    RENTAL_OPTION = (By.XPATH, "//div[contains(@class, 'Dropdown-menu')]//div[contains(@class, 'Dropdown-option')]")
    #(By.XPATH, "//div[text()='сутки']") # Выпадающий список

    COLOR_BLACK = (By.XPATH, "//input[@id='black']") # Чекбокс черного цвета
    COLOR_GREY = (By.XPATH, "//input[@id='grey']") # Чекбокс серого цвета
    COMMENT_INPUT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']") # Поле Комментария

    FINAL_ORDER_BUTTON = (By.XPATH, "//div[contains(@class, 'Order_Buttons')]//button[text()='Заказать']") # Финальная кнопка Заказать
    CONFIRM_BUTTON = (By.XPATH, "//button[text()='Да']") # Кнопка подтверждения заказа
    SUCCESS_MESSAGE = (By.CLASS_NAME, "Order_ModalHeader") # Сообщение

    CONFIRMATION_MESSAGE = (By.XPATH, "//div[contains(text(),'Заказ оформлен')]")  # Сообщение об успешном заказе