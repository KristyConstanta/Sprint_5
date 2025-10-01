import pytest
import random
from data import locators
from data import email
from data import password
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestRegistration:
    # Проверка успешной регистрации
    def test_registration_correct(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*locators.login_button_main_page).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(locators.register_link))
        driver.find_element(*locators.register_link).click()
        WebDriverWait(driver, 8).until(expected_conditions.visibility_of_element_located(locators.submit_button))
        driver.find_element(*locators.name_field).send_keys(f"UserKR_{random.randint(10, 9999)}")
        driver.find_element(*locators.email_field).send_keys(f"user_KR_{random.randint(10, 9999)}@ya.ru")
        driver.find_element(*locators.password_field).send_keys("qwerty123456")
        driver.find_element(*locators.submit_button).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(locators.login_button))
        assert driver.find_element(*locators.register_link).is_displayed()

    # Регистрация с невалидным паролем
    def test_registration_incorrect_password_message(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*locators.login_button_main_page).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(locators.register_link))
        driver.find_element(*locators.register_link).click()
        WebDriverWait(driver, 8).until(expected_conditions.visibility_of_element_located(locators.submit_button))
        driver.find_element(*locators.name_field).send_keys(f"UserKR_{random.randint(10, 9999)}")
        driver.find_element(*locators.email_field).send_keys(f"user_KR_{random.randint(10, 9999)}@ya.ru")
        driver.find_element(*locators.password_field).send_keys("qw123")
        driver.find_element(*locators.submit_button).click()
        assert driver.find_element(*locators.incorrect_password_message).text == 'Некорректный пароль'