# import pytest
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# url = ' https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/.'
#
#
# class TestMainPage:
#     @pytest.mark.regression
#     def test_page_contains_button_basket(self, browser, user_language):
#         browser.get(url)
#         browser.find_element(By.CSS_SELECTOR, "#add_to_basket_form > button")
import time

from selenium.webdriver.common.by import By


def test_find_add_to_card_btn(browser):
    browser.get('https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    time.sleep(5)
    assert browser.find_element(By.CLASS_NAME,
                                'btn-add-to-basket').is_displayed(), 'Кнопка добавления товара в корзину отсутсвует'
