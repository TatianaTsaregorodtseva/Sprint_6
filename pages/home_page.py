import allure
from pages.base_page import BasePage
from locators.locators_home_page import HomePageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage(BasePage):
    @allure.step("Клик по верхней кнопки Заказать")
    def click_order_button_top(self):
        self.click_on_element(HomePageLocators.ORDER_BUTTON_TOP)

    @allure.step("Клик по нижней кнопке Заказать")
    def click_order_button_bottom(self):
        self.click_on_element(HomePageLocators.ORDER_BUTTON_BOTTOM)

    @allure.step("Клик по логотипу Самоката")
    def click_scooter_logo(self):
        self.click_on_element(HomePageLocators.LOGO_SAMOKAT)

    @allure.step("Клик по логотипу Яндекса")
    def click_yandex_logo(self):
        self.click_on_element(HomePageLocators.LOGO_YANDEX)
        self.switch_to_next_tab()

    @allure.step("Подождать загрузки списка вопросов")
    def wait_for_question_list(self):
        self.scroll_to_element(HomePageLocators.FAQ_SECTION)
        self.wait_for_element(HomePageLocators.FAQ_SECTION)

    @allure.step("Открыть вопрос")
    def click_on_question(self, question_number):
        question_locator = HomePageLocators.question_number(question_number)
        self.scroll_to_element(question_locator)
        self.wait_for_element(question_locator)
        self.click_on_element(question_locator)

    @allure.step("Ответы на вопрос")
    def check_question_answers(self, question_number, expected_text):
        answer_locator = HomePageLocators.answer_number(question_number)
        self.wait_for_element(answer_locator)
        actual_text = self.get_text_on_element(answer_locator)
        return actual_text == expected_text