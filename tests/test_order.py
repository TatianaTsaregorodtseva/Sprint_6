import pytest

from locators.locators_order_page import OrderPageLocators
from pages.order_page import OrderPage
import allure
import data

class TestOrder:
    @allure.title("Заказ самоката через верхнюю кнопку Заказать")
    @pytest.mark.parametrize("test_data", data.TEST_DATA)
    def test_order_top_button(self, driver, test_data):
        #Arrange
        order_page = OrderPage(driver)
        #Act
        order_page.click_order_button_top()
        order_page.fill_order_form(test_data["first_name"], test_data["last_name"], test_data["address"], test_data["metro"], test_data["phone"])
        order_page.click_next()
        order_page.fill_second_order_form(test_data["date"], test_data["period"], test_data["color"], test_data["comment"])
        order_page.confirm_order()
        success_message = order_page.get_message()
        #Assert
        assert "Заказ оформлен" in success_message


    @allure.title("Заказ самоката через нижнюю кнопку Заказать")
    @pytest.mark.parametrize("test_data", data.TEST_DATA2)
    def test_order_bottom_button(self, driver, test_data):
        #Arrange
        order_page = OrderPage(driver)
        #Act
        order_page.scroll_to_element(OrderPageLocators.ORDER_BUTTON_BOTTOM)
        order_page.click_order_button_bottom()
        order_page.fill_order_form(test_data["first_name"], test_data["last_name"], test_data["address"], test_data["metro"], test_data["phone"])
        order_page.click_next()
        order_page.fill_second_order_form(test_data["date"], test_data["period"], test_data["color"], test_data["comment"])
        order_page.confirm_order()
        success_message = order_page.get_message()
        #Assert
        assert "Заказ оформлен" in success_message
