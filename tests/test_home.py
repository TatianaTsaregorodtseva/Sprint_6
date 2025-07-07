from urls import *
import allure
import pytest
from data import Data
from pages.home_page import HomePage

class TestLogo:
    @allure.title("Проверяем редирект по логотипу Самоката")
    def test_logo_scooter(self, driver):
        # Arrange
        home_page = HomePage(driver)
        # Act
        home_page.click_order_button_top()
        home_page.click_scooter_logo()
        #Assert
        assert home_page.get_current_url == main_site

    @allure.title("Проверяем редирект по логотипу Яндекса")
    def test_logo_yandex(self, driver):
        #Arrenge
        home_page = HomePage(driver)
        #Act
        home_page.click_yandex_logo()
        home_page.switch_to_next_tab()
        home_page.wait_url()
        #Assert
        assert dzen in home_page.get_current_url


class TestQuestions:
       @allure.title("Тест вопросы о важном и ответы")
       @pytest.mark.parametrize('question_number, expected_text', Data.questions)
       def test_questions_answers(self, driver, question_number, expected_text):
           # Arrange
           home_page = HomePage(driver)
           home_page.wait_for_question_list()
           # Act
           home_page.click_on_question(question_number)
           #Assert
           assert home_page.check_question_answers(question_number, expected_text)