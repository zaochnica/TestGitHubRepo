import time

from selenium.webdriver.common.by import By


def test_find_add_to_card_btn(browser):
    browser.get('https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    time.sleep(5)
    assert browser.find_element(
        By.CLASS_NAME,
        'btn-add-to-basket'
    ).is_displayed(), 'Кнопка добавления товара в корзину отсутсвует'
