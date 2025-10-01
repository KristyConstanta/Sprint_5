import pytest
from data import locators
from data import email
from data import password
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestMoveAccount:
    def test_move_personal_account(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*locators.login_button_main_page).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(locators.register_link))
        driver.find_element(*locators.email_field).send_keys(email)
        driver.find_element(*locators.password_field).send_keys(password)
        driver.find_element(*locators.login_button).click()
        WebDriverWait(driver, 8).until(expected_conditions.visibility_of_element_located(locators.personal_account_button))
        driver.find_element(*locators.personal_account_button).click()
        WebDriverWait(driver, 8).until(expected_conditions.visibility_of_element_located(locators.logout_button))
        assert driver.find_element(*locators.logout_button).is_displayed()