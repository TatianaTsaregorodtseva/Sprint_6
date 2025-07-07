import allure
from .base_page import BasePage
from locators.locators_order_page import OrderPageLocators


class OrderPage(BasePage):

    @allure.step("Нажать на кнопку Заказать в начале страници")
    def click_order_button_top(self):
        self.click_on_element(OrderPageLocators.ORDER_BUTTON_TOP)

    @allure.step("Нажать на кнопку Заказать внизу страницы")
    def click_order_button_bottom(self):
        self.wait_for_element(OrderPageLocators.ORDER_BUTTON_BOTTOM)
        self.click_on_element(OrderPageLocators.ORDER_BUTTON_BOTTOM)

    @allure.step("Заполнить форму 'Для кого самокат")
    def fill_order_form(self, first_name, last_name, address, metro, phone):
        self.send_keys_to_input(OrderPageLocators.FIRST_NAME, first_name)
        self.send_keys_to_input(OrderPageLocators.LAST_NAME, last_name)
        self.send_keys_to_input(OrderPageLocators.ADDRESS, address)

        self.send_keys_to_input(OrderPageLocators.METRO, metro)
        self.wait_for_element(OrderPageLocators.METRO_LIST)
        self.click_on_element(OrderPageLocators.METRO_LIST)

        self.send_keys_to_input(OrderPageLocators.PHONE, phone)

    @allure.step("Клик по кнопке Далее")
    def click_next(self):
        self.click_on_element(OrderPageLocators.NEXT_BUTTON)

    @allure.step("Заполнить форму 'Про аренду'")
    def fill_second_order_form(self, date, period, color, comment):

        self.send_keys_to_input(OrderPageLocators.DATE_INPUT, date)
        self.click_on_element(OrderPageLocators.CALENDAR_DROPDOWN)

        self.click_on_element(OrderPageLocators.RENTAL_PERIOD)
        self.click_on_element(OrderPageLocators.RENTAL_OPTION)

        self.click_on_element(OrderPageLocators.COLOR_BLACK)
        self.click_on_element(OrderPageLocators.COLOR_GREY)

        self.send_keys_to_input(OrderPageLocators.COMMENT_INPUT, comment)

        self.click_on_element(OrderPageLocators.FINAL_ORDER_BUTTON)

    @allure.step("Подтверждение заказа")
    def confirm_order(self):
        self.click_on_element(OrderPageLocators.CONFIRM_BUTTON)


    @allure.step("Проверка отображения окна подтверждения заказа")
    def get_message(self):
        return self.find_element(OrderPageLocators.CONFIRMATION_MESSAGE).text