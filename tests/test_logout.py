import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import Locators
locators = Locators()
email = 'kristy_rassudova_31@yandex.ru'
password = '510547'

# Вход по кнопке «Войти в аккаунт» на главной
def test_login_button_main_page(driver):
    driver.get("https://stellarburgers.nomoreparties.site/")

    driver.find_element(*locators.login_button_main_page).click()
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(locators.register_link))
    driver.find_element(*locators.email_field).send_keys(email)
    driver.find_element(*locators.password_field).send_keys(password)
    driver.find_element(*locators.login_button).click()
    WebDriverWait(driver, 8).until(expected_conditions.visibility_of_element_located(locators.make_an_order_button))
    driver.find_element(*locators.personal_account_button).click()
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(locators.logout_button))
    driver.find_element(*locators.logout_button).click()
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(locators.login_button))
    assert driver.find_element(*locators.login_button).is_displayed()