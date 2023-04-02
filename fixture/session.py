# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.by import By


class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, user_name, password):
        driver = self.app.driver
        self.app.open_home_page()
        driver.find_element(By.NAME, "user").click()
        driver.find_element(By.NAME, "user").send_keys(user_name)
        driver.find_element(By.NAME, "pass").click()
        driver.find_element(By.NAME, "pass").send_keys(password)
        driver.find_element(By.CSS_SELECTOR, "input:nth-child(7)").click()

    def logout(self):
        driver = self.app.driver
        driver.find_element(By.LINK_TEXT, "Logout").click()

    def ensure_logout(self):
         if self.is_logged_in():
            self.logout()

    def is_logged_in(self):
        driver = self.app.driver
        return len(driver.find_elements(By.LINK_TEXT, "Logout")) > 0

    def is_logged_in_as(self, user_name):
        driver = self.app.driver
        return driver.find_element(By.CSS_SELECTOR, "form[name='logout'] b").text == "("+user_name+")"
    
    def ensure_login(self, user_name, password):
        if self.is_logged_in():
            if self.is_logged_in_as(user_name):
                return
            else:
                self.logout()
        self.login(user_name, password)
