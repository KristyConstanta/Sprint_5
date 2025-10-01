import pytest
from data import locators
from data import email
from data import password
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class TestLogin:
    # Вход по кнопке «Войти в аккаунт» на главной
    def test_login_button_main_page(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*locators.login_button_main_page).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(locators.register_link))
        driver.find_element(*locators.email_field).send_keys(email)
        driver.find_element(*locators.password_field).send_keys(password)
        driver.find_element(*locators.login_button).click()
        WebDriverWait(driver, 8).until(expected_conditions.visibility_of_element_located(locators.make_an_order_button))
        assert driver.find_element(*locators.make_an_order_button).is_displayed()

    # Вход через кнопку «Личный кабинет»
    def test_login_button_personal_account(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*locators.personal_account_button).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(locators.register_link))
        driver.find_element(*locators.email_field).send_keys(email)
        driver.find_element(*locators.password_field).send_keys(password)
        driver.find_element(*locators.login_button).click()
        WebDriverWait(driver, 8).until(expected_conditions.visibility_of_element_located(locators.make_an_order_button))
        assert driver.find_element(*locators.make_an_order_button).is_displayed()

    # Вход через кнопку в форме регистрации
    def test_login_button_registration_form(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*locators.login_button_main_page).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(locators.register_link))
        driver.find_element(*locators.register_link).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(locators.login_button_in_registration_form))
        driver.find_element(*locators.login_button_in_registration_form).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(locators.register_link))
        driver.find_element(*locators.email_field).send_keys(email)
        driver.find_element(*locators.password_field).send_keys(password)
        driver.find_element(*locators.login_button).click()
        WebDriverWait(driver, 8).until(expected_conditions.visibility_of_element_located(locators.make_an_order_button))
        assert driver.find_element(*locators.make_an_order_button).is_displayed()

    # Вход через кнопку в форме восстановления пароля
    def test_login_button_recovery_password_form(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*locators.login_button_main_page).click()
        WebDriverWait(driver, 8).until(expected_conditions.visibility_of_element_located(locators.forgot_password_button))
        driver.find_element(*locators.forgot_password_button).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(locators.login_password_recovery_form_button))
        driver.find_element(*locators.login_password_recovery_form_button).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(locators.register_link))
        driver.find_element(*locators.email_field).send_keys(email)
        driver.find_element(*locators.password_field).send_keys(password)
        driver.find_element(*locators.login_button).click()
        WebDriverWait(driver, 8).until(expected_conditions.visibility_of_element_located(locators.make_an_order_button))
        assert driver.find_element(*locators.make_an_order_button).is_displayed()